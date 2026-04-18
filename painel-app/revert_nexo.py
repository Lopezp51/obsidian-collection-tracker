import os
import glob
import re
import yaml

TARGET_VAULT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REPORTS_FOLDER = os.path.join(TARGET_VAULT, "Relatórios Linter")

def run_revert():
    reports = glob.glob(os.path.join(REPORTS_FOLDER, "*.md"))
    if not reports:
        print("Nenhum relatório encontrado.")
        return
        
    latest_report = max(reports, key=os.path.getctime)
    print(f"Lendo relatório: {latest_report}")
    
    with open(latest_report, "r", encoding="utf-8") as f:
        content = f.read()
        
    to_revert = []
    # format: | [[Filename]] | Nexo inferido e criado para 'Manga' |
    for match in re.finditer(r'\|\s*\[\[(.*?)\]\]\s*\|\s*(.*Nexo inferido e criado.*)\s*\|', content):
        to_revert.append(match.group(1).strip())
        
    print(f"Total de notas a reverter (apenas 'Nexo'): {len(to_revert)}")
    
    # Map all files
    all_files = glob.glob(os.path.join(TARGET_VAULT, "**", "*.md"), recursive=True)
    file_map = {os.path.basename(f).replace('.md', ''): f for f in all_files}
    
    reverted_count = 0
    for name in to_revert:
        if name in file_map:
            fpath = file_map[name]
            with open(fpath, "r", encoding="utf-8") as f:
                file_content = f.read()
                
            if "---" in file_content:
                parts = file_content.split("---")
                if len(parts) >= 3:
                    fm_str = parts[1]
                    body = "---".join(parts[2:])
                    try:
                        fm = yaml.safe_load(fm_str)
                        if isinstance(fm, dict) and "Nexo" in fm:
                            del fm["Nexo"]
                            
                            import io
                            stream = io.StringIO()
                            yaml.dump(fm, stream, sort_keys=False, allow_unicode=True, default_flow_style=False)
                            new_fm_str = stream.getvalue()
                            
                            new_content = "---\n" + new_fm_str + "---" + body
                            with open(fpath, "w", encoding="utf-8") as f:
                                f.write(new_content)
                                
                            reverted_count += 1
                    except:
                        pass
                        
    print(f"Reversão completa. {reverted_count} notas limpas do Nexo provisório.")

if __name__ == "__main__":
    run_revert()
