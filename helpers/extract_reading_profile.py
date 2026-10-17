import os
import re
import json
from collections import Counter, defaultdict

def parse_simple_yaml_and_obs(text):
    data = {}
    obs_list = []
    
    # 1. Extrair YAML
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            yaml_text = parts[1]
            body_text = parts[2]
            
            current_key = None
            for line in yaml_text.splitlines():
                line = line.rstrip()
                if not line or line.startswith("#"):
                    continue
                
                list_match = re.match(r"^(\s*)-\s+(.*)$", line)
                if list_match and current_key:
                    val = list_match.group(2).strip()
                    if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                        val = val[1:-1]
                    if not isinstance(data.get(current_key), list):
                        data[current_key] = []
                    data[current_key].append(val)
                    continue
                    
                key_val_match = re.match(r"^([\w\s\u00C0-\u017F\-\/]+):\s*(.*)$", line)
                if key_val_match:
                    k = key_val_match.group(1).strip()
                    v = key_val_match.group(2).strip()
                    current_key = k
                    
                    if v == "" or v == "[]":
                        data[k] = []
                    elif v.startswith("[") and v.endswith("]"):
                        items = [x.strip().strip("'\"") for x in v[1:-1].split(",") if x.strip()]
                        data[k] = items
                    elif v.lower() == "true":
                        data[k] = True
                    elif v.lower() == "false":
                        data[k] = False
                    elif v.lower() in ("null", "~"):
                        data[k] = None
                    else:
                        try:
                            if "." in v:
                                data[k] = float(v)
                            else:
                                data[k] = int(v)
                        except ValueError:
                            if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
                                v = v[1:-1]
                            data[k] = v
                    continue
        else:
            body_text = text
    else:
        body_text = text

    # 2. Extrair observações de leitura inline: [obs:: ...]
    # Exemplos: [obs:: Texto da observação]
    matches = re.findall(r"\[obs::\s*([^\]]+)\]", body_text, re.IGNORECASE)
    for m in matches:
        clean = m.strip()
        if clean:
            obs_list.append(clean)

    return data, obs_list

def extract_profile_data(vault_dir):
    acervo_dir = os.path.join(vault_dir, "Acervo")
    assinaturas_dir = os.path.join(vault_dir, "Assinaturas")
    
    read_items = []
    
    if os.path.exists(acervo_dir):
        for root, _, files in os.walk(acervo_dir):
            for file in files:
                if not file.endswith(".md"):
                    continue
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                    data, obs = parse_simple_yaml_and_obs(content)
                    
                    status_leitura = str(data.get("Status de Leitura", "")).strip().lower()
                    if "lido" in status_leitura or data.get("Última Leitura") or obs:
                        data["_filename"] = file[:-3]
                        data["_path"] = path
                        data["_obs"] = obs
                        read_items.append(data)
                except Exception:
                    pass

    subscriptions = []
    if os.path.exists(assinaturas_dir):
        for file in os.listdir(assinaturas_dir):
            if file.endswith(".md"):
                path = os.path.join(assinaturas_dir, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                    data, _ = parse_simple_yaml_and_obs(content)
                    data["_title"] = file[:-3]
                    subscriptions.append(data)
                except Exception:
                    pass

    return read_items, subscriptions

def summarize_profile(read_items, subscriptions):
    total_lidos = len(read_items)
    formatos = Counter()
    editoras = Counter()
    avaliacoes = Counter()
    
    favoritos = []
    releituras = []
    alta_nota = [] # >= 4.0
    baixa_nota = [] # > 0 and <= 2.5
    com_observacoes = []
    
    roteiristas_alta_nota = Counter()
    artistas_alta_nota = Counter()
    colecoes = Counter()
    
    for item in read_items:
        fmt = item.get("Formato") or "Não especificado"
        if isinstance(fmt, list):
            fmt = ", ".join(fmt)
        formatos[str(fmt)] += 1
        
        # Editora
        ed = item.get("Editora")
        if isinstance(ed, list):
            for e in ed:
                if e: editoras[e.strip()] += 1
        elif ed:
            editoras[str(ed).strip()] += 1
            
        # Coleção
        col = item.get("Coleção")
        col_list = []
        if isinstance(col, list):
            for c in col:
                if c: 
                    colecoes[c.strip()] += 1
                    col_list.append(c.strip())
        elif col:
            colecoes[str(col).strip()] += 1
            col_list.append(str(col).strip())
            
        # Avaliação
        aval = item.get("Avaliação")
        try:
            aval_num = float(aval) if aval is not None else 0.0
        except (ValueError, TypeError):
            aval_num = 0.0
            
        avaliacoes[round(aval_num, 1)] += 1
        
        title = item.get("_filename")
        is_fav = bool(item.get("Favorito"))
        vezes = item.get("Vezes que Li") or 0
        try:
            vezes_num = int(vezes)
        except (ValueError, TypeError):
            vezes_num = 0
            
        roteiro = item.get("Roteiro") or item.get("Autoria") or []
        if isinstance(roteiro, str):
            roteiro = [roteiro]
        arte = item.get("Arte") or item.get("Desenhos") or []
        if isinstance(arte, str):
            arte = [arte]
            
        obs = item.get("_obs", [])
        
        info = {
            "titulo": title,
            "colecoes": col_list,
            "formato": fmt,
            "avaliacao": aval_num,
            "favorito": is_fav,
            "releituras": vezes_num,
            "roteiro": [r.strip() for r in roteiro if r and isinstance(r, str)],
            "arte": [a.strip() for a in arte if a and isinstance(a, str)],
            "observacoes": obs
        }
        
        if obs:
            com_observacoes.append(info)
            
        if is_fav:
            favoritos.append(info)
            
        if vezes_num > 1:
            releituras.append(info)
            
        if aval_num >= 4.0:
            alta_nota.append(info)
            for r in info["roteiro"]:
                roteiristas_alta_nota[r] += 1
            for a in info["arte"]:
                artistas_alta_nota[a] += 1
        elif 0 < aval_num <= 2.5:
            baixa_nota.append(info)
            
    favoritos.sort(key=lambda x: (x["avaliacao"], len(x["observacoes"])), reverse=True)
    alta_nota.sort(key=lambda x: (x["avaliacao"], x["favorito"], len(x["observacoes"])), reverse=True)
    baixa_nota.sort(key=lambda x: (x["avaliacao"], len(x["observacoes"])))
    
    sub_titles = [s.get("_title") for s in subscriptions]
    
    return {
        "total_lidos": total_lidos,
        "formatos": dict(formatos.most_common()),
        "editoras": dict(editoras.most_common(10)),
        "distribuicao_notas": {str(k): v for k, v in sorted(avaliacoes.items(), reverse=True)},
        "top_colecoes_lidas": dict(colecoes.most_common(20)),
        "roteiristas_destaque": dict(roteiristas_alta_nota.most_common(20)),
        "artistas_destaque": dict(artistas_alta_nota.most_common(20)),
        "favoritos": favoritos,
        "releituras": releituras,
        "amostra_alta_nota": alta_nota[:40],
        "baixa_nota_ou_criticas": baixa_nota[:25],
        "com_observacoes": com_observacoes,
        "assinaturas_ativas_e_recentes": sub_titles
    }

def generate_markdown_summary(summary):
    md = []
    md.append("# Resumo Consolidado do Acervo de Leitura")
    md.append(f"- **Total de Obras Lidas:** {summary['total_lidos']}")
    md.append(f"- **Total de Favoritos Declarados:** {len(summary['favoritos'])}")
    md.append(f"- **Total de Obras com Notas Altas (4.0 a 5.0+):** {sum(v for k, v in summary['distribuicao_notas'].items() if float(k) >= 4.0)}")
    md.append(f"- **Total de Obras com Notas Críticas (<= 2.5):** {sum(v for k, v in summary['distribuicao_notas'].items() if 0 < float(k) <= 2.5)}")
    md.append("")
    
    md.append("## Distribuição de Notas")
    for nota, qtd in summary['distribuicao_notas'].items():
        if qtd > 0:
            md.append(f"- **Nota {nota}:** {qtd} edições")
    md.append("")
    
    md.append("## Top Coleções Mais Consumidas")
    for col, count in list(summary['top_colecoes_lidas'].items())[:12]:
        md.append(f"- **{col}:** {count} volumes lidos")
    md.append("")
    
    md.append("## Criadores com Maior Frequência nas Notas 4-5")
    md.append("- **Roteiristas:** " + ", ".join([f"{k} ({v}x)" for k, v in list(summary['roteiristas_destaque'].items())[:12]]))
    md.append("- **Artistas/Desenhistas:** " + ", ".join([f"{k} ({v}x)" for k, v in list(summary['artistas_destaque'].items())[:12]]))
    md.append("")
    
    md.append("## Assinaturas Atuais (Compromisso Ativo)")
    for sub in summary['assinaturas_ativas_e_recentes']:
        md.append(f"- {sub}")
    md.append("")
    
    md.append("## Amostra de Obras Favoritas & Altas Avaliações (Com Notas Pessoais)")
    for item in summary['favoritos'][:15]:
        obs_text = " | ".join(item['observacoes']) if item['observacoes'] else "Sem anotação de texto"
        autores = ", ".join(item['roteiro'] + item['arte']) if (item['roteiro'] or item['arte']) else "N/A"
        md.append(f"### ⭐ {item['titulo']} (Nota: {item['avaliacao']} | Favorito: Sim)")
        md.append(f"- **Autoria/Arte:** {autores}")
        md.append(f"- **Impressão Real:** *\"{obs_text}\"*")
        md.append("")
        
    md.append("## Amostra de Obras com Baixa Avaliação ou Frustrações (Para Entender Dealbreakers)")
    for item in summary['baixa_nota_ou_criticas'][:15]:
        obs_text = " | ".join(item['observacoes']) if item['observacoes'] else "Sem anotação de texto"
        autores = ", ".join(item['roteiro'] + item['arte']) if (item['roteiro'] or item['arte']) else "N/A"
        md.append(f"### ❌ {item['titulo']} (Nota: {item['avaliacao']})")
        md.append(f"- **Autoria/Arte:** {autores}")
        md.append(f"- **Impressão Real / Motivo do Descontentamento:** *\"{obs_text}\"*")
        md.append("")

    md.append("## Observações Marcantes Adicionais do Leitor")
    # Pega itens que tem observações longas ou expressivas que não entraram no top
    extras = [i for i in summary['com_observacoes'] if i not in summary['favoritos'][:15] and i not in summary['baixa_nota_ou_criticas'][:15]]
    for item in extras[:15]:
        obs_text = " | ".join(item['observacoes'])
        md.append(f"- **{item['titulo']}** (Nota {item['avaliacao']}): *\"{obs_text}\"*")
        
    return "\n".join(md)

if __name__ == "__main__":
    vault_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    read_items, subs = extract_profile_data(vault_dir)
    summary = summarize_profile(read_items, subs)
    
    json_path = os.path.join(vault_dir, "helpers", "dados_perfil_leitor.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
        
    md_summary = generate_markdown_summary(summary)
    md_path = os.path.join(vault_dir, "helpers", "resumo_perfil_leitor.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_summary)
        
    print(f"Sucesso! Gerados {json_path} e {md_path}")
