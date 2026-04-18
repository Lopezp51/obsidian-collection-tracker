import urllib.request

url = 'https://d14d9vp3wdof84.cloudfront.net/image/589816272436/image_frm4bma1mt7tnfhpfa7ish4g3a/-S897-FWEBP'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    save_path = r"h:\Meu Drive\Obsidian\Painel de Controle de Encomendas\Banco de Imagens\HQ's\Superman Por Geoff Johns Vol. 01 - Origem Secreta.jpg"
    print(f"Downloading to {save_path}...")
    with urllib.request.urlopen(req) as response, open(save_path, 'wb') as out_file:
        data = response.read()
        out_file.write(data)
        print(f"Success! Downloaded {len(data)} bytes.")
except Exception as e:
    print(f"Error: {e}")
