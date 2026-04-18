import os
import glob
import yaml
import re
import datetime

TARGET_VAULT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def run_linter():
    print("Iniciando YAML Linter...")
    files = glob.glob(os.path.join(TARGET_VAULT, "**", "*.md"), recursive=True)
    
    total_audited = 0
    modifications_log = []
    orphaned_images = []
    
    for fpath in files:
        if ".agents" in fpath or ".obsidian" in fpath or "Templates" in fpath or ".git" in fpath or ".trash" in fpath or ".venv" in fpath:
            continue
            
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
                
            if "---" not in content:
                continue
                
            parts = content.split("---")
            if len(parts) >= 3:
                frontmatter_str = parts[1]
                body = "---".join(parts[2:])
                
                try:
                    fm = yaml.safe_load(frontmatter_str)
                    if not isinstance(fm, dict):
                        continue
                except:
                    continue
                    
                total_audited += 1
                modified = False
                reasons = []
                
                # 1. Caçador de Strings em Booleans
                for key in ["Chegou", "Favorito"]:
                    if key in fm:
                        val = fm[key]
                        if not isinstance(val, bool):
                            new_val = False
                            if isinstance(val, str) and val.strip().lower() in ['sim', 'true', '1']:
                                new_val = True
                            fm[key] = new_val
                            modified = True
                            reasons.append(f"Corrigido boolean em '{key}'")
                            
                # 2. Corrigir "Valor" Quebrado
                if "valor" in fm:
                    val = fm["valor"]
                    if not isinstance(val, (int, float)):
                        clean_price = re.sub(r"[^\d,.-]", "", str(val)).replace(",", ".")
                        try:
                            f_val = float(clean_price)
                        except:
                            f_val = 0.0
                        fm["valor"] = f_val
                        modified = True
                        reasons.append(f"Limpo 'valor': de '{val}' para '{f_val}'")

                # 3. Padronização de Nexo Inteligente
                nexo = fm.get("Nexo")
                
                folder = os.path.dirname(fpath).lower()
                title_orig = os.path.basename(fpath).replace(".md", "")
                title_lower = title_orig.lower()

                def extract_manga_series(t):
                    cutoffs = [" - parte", " – parte", " vol.", " - vol", " (", " - 0", " - 1", " - 2", " - 3"]
                    res = t
                    for c in cutoffs:
                        if c in res.lower():
                            idx = res.lower().find(c)
                            res = res[:idx]
                    return res.strip()

                inferred_tags = []
                
                is_hq = any(k in folder for k in ["hq", "quadrinho", "comic"])
                is_manga = any(k in folder for k in ["manga", "mangas", "mangá"])
                is_livro = "livro" in folder
                
                # Title heuristics for HQ
                hq_keywords = ["absolute ", "dc de bolso", "marvel de bolso", "grandes heróis", "(2025)", "(2026)", "batman", "superman", "mulher-maravilha", "homem-aranha", "x-men", "liga da justiça", "lanterna verde", "flash", "demolidor", "wolverine", "quarteto fantástico", "vingadores", "pantera negra", "os supremos", "tomb raider", "godzilla"]
                if not is_hq and any(k in title_lower for k in hq_keywords):
                    is_hq = True
                    is_manga = False
                    
                # If neither HQ nor Livro, and has Volume, assume Manga
                if not is_hq and not is_manga and not is_livro:
                    if "vol." in title_lower or "vol " in title_lower or "- vol" in title_lower or "parte" in title_lower:
                        is_manga = True
                        
                if is_manga and "frankenstein" in title_lower:
                    is_manga = False
                    is_hq = True
                
                if is_manga:
                    serie = extract_manga_series(title_orig)
                    inferred_tags = ["Manga", serie, "Panini"]
                elif is_hq:
                    tags = ["Quadrinho"]
                    if "absolute" in title_lower: tags.append("Absolute")
                    if "dc de bolso" in title_lower: tags.append("DC de Bolso")
                    if "marvel de bolso" in title_lower: tags.append("Marvel de Bolso")
                    if "grandes heróis dc" in title_lower: tags.append("Grandes Heróis DC")
                    if "(2025)" in title_lower or "(2026)" in title_lower: tags.append("Sem Limites")
                    
                    chars = ["Batman", "Superman", "Mulher-Maravilha", "Homem-Aranha", "X-Men", "Liga da Justiça", "Lanterna Verde", "Flash", "Demolidor", "Wolverine", "Quarteto Fantástico", "Vingadores", "Pantera Negra", "Os Supremos", "Tomb Raider", "Godzilla"]
                    for c in chars:
                        if c.lower() in title_lower:
                            tags.append(c)
                            break
                    tags.append("Panini")
                    inferred_tags = tags
                elif is_livro:
                    inferred_tags = ["Livro"]
                    
                if nexo is None or not isinstance(nexo, list) or len(nexo) == 0:
                    if inferred_tags:
                        fm["Nexo"] = inferred_tags
                        modified = True
                        reasons.append(f"Nexo avançado criado")
                elif isinstance(nexo, list):
                    new_nexo = []
                    nexo_mod_flag = False
                    for item in nexo:
                        item_str = str(item)
                        if item_str.lower() == "mangá":
                            new_nexo.append("Manga")
                            nexo_mod_flag = True
                        else:
                            new_nexo.append(item_str)
                    
                    has_primary = any(str(n).title() in ["Quadrinho", "Manga", "Livro", "Graphic Novel"] for n in new_nexo)
                    if not has_primary and inferred_tags:
                        # Append new inferred tags if missing from current list
                        for tg in inferred_tags:
                            if tg not in new_nexo:
                                new_nexo.append(tg)
                        nexo_mod_flag = True
                        
                    if nexo_mod_flag:
                        fm["Nexo"] = new_nexo
                        modified = True
                        reasons.append(f"Nexo padronizado")
                        
                elif isinstance(nexo, str):
                    fm["Nexo"] = inferred_tags if inferred_tags else [nexo.title()]
                    modified = True
                    reasons.append(f"Nexo corrigido de string para lista rica")

                # 4. Auditoria de Imagens Orfãs
                img_val = fm.get("imagem", "")
                if img_val:
                    if str(img_val).startswith("http"):
                        orphaned_images.append((os.path.basename(fpath), img_val, "Imagem usando link HTTP (Internet)"))
                    else:
                        img_path = os.path.join(TARGET_VAULT, img_val)
                        if not os.path.exists(img_path):
                            orphaned_images.append((os.path.basename(fpath), img_val, "Arquivo de imagem ausente no disco local"))

                # Write changes back if modified
                if modified:
                    import io
                    stream = io.StringIO()
                    yaml.dump(fm, stream, sort_keys=False, allow_unicode=True, default_flow_style=False)
                    new_fm_str = stream.getvalue()
                    
                    new_content = "---\n" + new_fm_str + "---" + body
                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                        
                    modifications_log.append({
                        "nota": os.path.basename(fpath),
                        "motivos": "; ".join(reasons)
                    })

        except Exception as e:
            print(f"Erro processando {fpath}: {e}")
            
    generate_report(total_audited, modifications_log, orphaned_images)

def generate_report(total, mods, orphans):
    reports_folder = os.path.join(TARGET_VAULT, "Relatórios Linter")
    os.makedirs(reports_folder, exist_ok=True)
    
    date_str = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    report_name = f"Relatório Linter {date_str}.md"
    report_path = os.path.join(reports_folder, report_name)
    
    lines = []
    lines.append(f"# Relatório YAML Linter ({date_str})")
    lines.append("")
    lines.append(f"**Total de notas auditadas:** {total}")
    lines.append(f"**Notas corrigidas:** {len(mods)}")
    lines.append(f"**Avisos de Imagem:** {len(orphans)}")
    lines.append("")
    
    if mods:
        lines.append("## 🔧 Correções Realizadas")
        lines.append("| Nota | Motivo(s) |")
        lines.append("|---|---|")
        for m in mods:
            lines.append(f"| [[{m['nota'].replace('.md', '')}]] | {m['motivos']} |")
        lines.append("")
        
    if orphans:
        lines.append("## 🖼️ Imagens com Anomalia (Ação Manual Recomendada)")
        lines.append("| Nota | Valor da Imagem | Causa |")
        lines.append("|---|---|---|")
        for o in orphans:
            lines.append(f"| [[{o[0].replace('.md', '')}]] | `{o[1]}` | {o[2]} |")
        lines.append("")
        
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
        
    print(f"Linter finalizado. Relatório gerado em: {report_path}")

if __name__ == "__main__":
    run_linter()
