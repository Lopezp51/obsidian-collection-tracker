from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from playwright.sync_api import sync_playwright
import bs4
import asyncio
import re
import os
import datetime
import urllib.request
import glob
import yaml

if os.name == 'nt':
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

app = FastAPI()

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ANTIGRAVITY_DIR = os.path.dirname(__file__)
TARGET_VAULT = BASE_DIR
collection_cache = []

# Make sure directories exist
os.makedirs(os.path.join(ANTIGRAVITY_DIR, "templates"), exist_ok=True)
os.makedirs(os.path.join(ANTIGRAVITY_DIR, "static"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "Banco de Imagens", "Mangas"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "Banco de Imagens", "HQ's"), exist_ok=True)
os.makedirs(os.path.join(ANTIGRAVITY_DIR, "obsidian-skills", "Notas"), exist_ok=True)

app.mount("/static", StaticFiles(directory=os.path.join(ANTIGRAVITY_DIR, "static")), name="static")
app.mount("/images", StaticFiles(directory=os.path.join(BASE_DIR, "Banco de Imagens")), name="images")

# We will serve a simple HTML string to avoid Jinja setup complexity, or put it in templates/index.html
# Let's read from templates/index.html

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open(os.path.join(ANTIGRAVITY_DIR, "templates", "index.html"), "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read(), status_code=200)

def search_panini(query: str):
    import urllib.request
    import urllib.parse
    import json
    
    url = f"https://panini.com.br/search/ajax/suggest/?q={urllib.parse.quote(query)}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
    except Exception as e:
        print("Search error:", e)
        return []
        
    results = []
    for item in data:
        if item.get("type") == "product":
            # Extract price text from HTML snippet
            price_html = item.get("price", "").replace("&nbsp;", " ").replace("\xa0", " ")
            m = re.search(r'> *(R\$.*?) *<', price_html)
            price_text = m.group(1).strip() if m else ""
            
            # Optionally extract img_url but UI no longer needs it.
            
            results.append({
                "title": item.get("title", ""),
                "url": item.get("url", ""),
                "price": price_text
            })
            
    return results

@app.get("/api/search")
def api_search(q: str):
    results = search_panini(q)
    return JSONResponse(content=results)

def get_product_details(url: str, title: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--no-sandbox", "--disable-blink-features=AutomationControlled"], headless=True)
        context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        page = context.new_page()
        page.goto(url, wait_until="domcontentloaded")
        
        try:
            # Wait for main product image loaded by fotorama
            page.wait_for_selector(".fotorama__img", timeout=8000)
            page.wait_for_timeout(1000)
        except:
            pass
            
        html = page.content()
        soup = bs4.BeautifulSoup(html, "html.parser")
        
        # High res image inside active fotorama frame
        img_el = soup.select_one(".fotorama__active .fotorama__img")
        if not img_el:
            img_el = soup.select_one(".fotorama__img")
            
        img_url = img_el["src"] if img_el else ""
        
        # Release date from Panini's specs table (if available)
        release_date = ""
        th_el = soup.find("th", string=re.compile(r"Data de Publicação|Lançamento", re.I))
        if th_el:
            td_el = th_el.find_next_sibling("td")
            if td_el:
                release_date = td_el.text.strip()
                
        release_date_iso = ""
        if release_date:
            m = re.search(r"(\d{2})/(\d{2})/(\d{4})", release_date)
            if m:
                release_date_iso = f"{m.group(3)}-{m.group(2)}-{m.group(1)}"
                
        # Pages quantity
        pages = 0
        pages_td = soup.select_one('td.data[data-th="Quantidade de páginas"]')
        if pages_td:
            try:
                pages = int(re.sub(r"\D", "", pages_td.text.strip()))
            except:
                pass
                
        return {"high_res_img": img_url, "release_date_iso": release_date_iso, "paginas": pages}

def create_obsidian_note(product_data, details_data):
    title = product_data["title"]
    price = product_data["price"]
    url = product_data["url"]
    high_res_img = details_data["high_res_img"]
    release_date_iso = details_data["release_date_iso"]
    paginas = details_data["paginas"]
    
    # Identify type by checking title structure or assuming Manga/Quadrinho
    # Let's create some naive rules:
    is_manga = "manga" in title.lower() or "vol" in title.lower()
    tipo = "Manga" if is_manga else "Quadrinho"
    
    # Download Image
    safe_title = re.sub(r'[\\/*?:"<>|]', "", title).strip()
    img_ext = high_res_img.split(".")[-1]
    if len(img_ext) > 4 or "?" in img_ext:
        img_ext = "jpg" # fallback
        
    img_filename = f"{safe_title}.{img_ext}"
    
    # Decide saving path
    target_img_dir = os.path.join(BASE_DIR, "Banco de Imagens", "Mangas") if tipo == "Manga" else os.path.join(BASE_DIR, "Banco de Imagens", "HQ's")
    img_path = os.path.join(target_img_dir, img_filename)
    
    # Actually download image
    if high_res_img:
        try:
            req = urllib.request.Request(high_res_img, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response, open(img_path, 'wb') as out_file:
                out_file.write(response.read())
        except Exception as e:
            print("Failed to download image:", e)
            
    # Release date already ISO from Guia dos Quadrinhos
    
    # Try to parse price to float
    clean_price = re.sub(r"[^\d,.-]", "", price).replace(",", ".")
    try:
        val_price = float(clean_price)
    except:
        val_price = 0.0
        
    # Generate Nexo string
    nexo_items = []
    if tipo == "Quadrinho":
        nexo_items.append("Quadrinho")
        if "absolute" in title.lower(): nexo_items.append("Absolute")
        if "batman" in title.lower(): nexo_items.append("Batman")
        if "mulher-maravilha" in title.lower(): nexo_items.append("Mulher-Maravilha")
        if "vertigo" in title.lower(): nexo_items.append("Vertigo")
        nexo_items.append("Panini")
    else:
        nexo_items.append("Manga")
        nexo_items.append("Panini")
        # Try to guess series
        # E.g. "One Piece Vol. 105" -> "One Piece"
        series = re.split(r"Vol\.", title, flags=re.I)[0].strip()
        if series: nexo_items.append(series)

    nexo_yaml = "\n  - ".join(nexo_items)
    nexo_str = "Nexo:\n  - " + nexo_yaml
    
    # Get Templates
    template_name = "Novo Manga.md" if tipo == "Manga" else "Novo Quadrinho.md"
    template_file = os.path.join(BASE_DIR, "Templates", template_name)
    try:
        with open(template_file, "r", encoding="utf-8") as f:
            template_content = f.read()
    except Exception as e:
        template_content = "Template not found."
        
    # Set proper image string for frontmatter
    folder_prefix = "Banco de Imagens/Mangas/" if tipo == "Manga" else "Banco de Imagens/HQ's/"
    full_img_str = f"{folder_prefix}{img_filename}"
        
    # Modify template dynamically replacing frontmatter
    # Split by the second ---
    parts = template_content.split("---")
    
    today_iso = datetime.datetime.now().strftime("%Y-%m-%d")
    
    new_yaml = f"""---
Processado em: {today_iso}
Situação: Finalizado
Data de Entrega: 
Chegou: true
Status de Leitura: Não Iniciado
Vezes que Li: 0
Páginas: {paginas}
valor: {val_price}
Favorito: false
Avaliação: 0
imagem: {full_img_str}
Última Leitura: 
Data de Publicação: {release_date_iso}
{nexo_str}
---"""
    
    if len(parts) >= 3:
        body = "---".join(parts[2:])
        final_note = new_yaml + "\n" + body
    else:
        final_note = new_yaml + "\n\n" + template_content

    note_path = os.path.join(ANTIGRAVITY_DIR, "obsidian-skills", "Notas", f"{safe_title}.md")
    
    with open(note_path, "w", encoding="utf-8") as f:
        f.write(final_note)
        
    return {"status": "success", "note": safe_title, "nexo": nexo_items}

from pydantic import BaseModel

class AddItemRequest(BaseModel):
    title: str
    url: str
    price: str

@app.post("/api/add_item")
def api_add_item(req: AddItemRequest):
    global collection_cache
    collection_cache = [] # Invalidate cache
    
    item = {"title": req.title, "url": req.url, "price": req.price}
    details = get_product_details(req.url, req.title)
    res = create_obsidian_note(item, details)
    return JSONResponse(content=res)

@app.get("/api/collection")
def api_collection():
    global collection_cache
    if collection_cache:
        return JSONResponse(content={"status": "success", "items": collection_cache})
        
    try:
        files = glob.glob(os.path.join(TARGET_VAULT, "**", "*.md"), recursive=True)
    except:
        return JSONResponse(content={"status": "error", "items": []})
        
    items = []
    for fpath in files:
        if ".agents" in fpath or ".obsidian" in fpath or "Templates" in fpath:
            continue
            
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            
            if "---" in content:
                parts = content.split("---")
                if len(parts) >= 3:
                    frontmatter_str = parts[1]
                    try:
                        fm = yaml.safe_load(frontmatter_str)
                        if not isinstance(fm, dict):
                            continue
                    except:
                        continue
                        
                    # Filtering rules: we want to only collect comics
                    nexo = fm.get("Nexo", [])
                    is_book = False
                    if isinstance(nexo, list) and any(n in [x.title() if isinstance(x, str) else "" for x in nexo] for n in ["Quadrinho", "Manga", "Livro", "Graphic Novel"]):
                        is_book = True
                        
                    if not is_book and "imagem" not in fm:
                        continue
                        
                    img_val = fm.get("imagem", "")
                    img_url = ""
                    if img_val:
                        # Normalize path
                        if img_val.startswith("Banco de Imagens/"):
                            img_path = img_val.replace("Banco de Imagens/", "", 1)
                            img_url = f"/images/{img_path}"
                        else:
                            img_url = f"/images/{img_val}"
                            
                    items.append({
                        "title": os.path.basename(fpath).replace(".md", ""),
                        "folder": os.path.dirname(fpath).replace(TARGET_VAULT, "").strip("\\/"),
                        "chegou": fm.get("Chegou", False),
                        "situacao": fm.get("Situação", ""),
                        "status_leitura": fm.get("Status de Leitura", ""),
                        "processado_em": str(fm.get("Processado em", "")),
                        "data_publi": str(fm.get("Data de Publicação", "")),
                        "imagem_url": str(img_url),
                        "valor": fm.get("valor", 0.0),
                        "paginas": fm.get("Páginas", 0),
                        "avaliacao": fm.get("Avaliação", 0)
                    })
        except Exception as e:
            pass
            
    collection_cache = items
    return JSONResponse(content={"status": "success", "items": items})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
