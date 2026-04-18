import pandas as pd
import os
import datetime
import re
import calendar

# ================= CONFIGURAÇÕES =================
# Caminho para o seu CSV
ARQUIVO_CSV = 'Controles Livros - Página5.csv'

# Caminho para o arquivo de modelo (para pegar a parte do Dataview)
ARQUIVO_MODELO = 'A Saga da Mulher-Maravilha Vol. 1.md'

# Pasta ONDE os arquivos serão salvos
PASTA_SAIDA = 'Gestão de Compras/Finalizado'
# =================================================

def limpar_valor_monetario(valor_str):
    """Converte 'R$ 56,99' para 56.99 (float)"""
    if pd.isna(valor_str):
        return 0.0
    if isinstance(valor_str, (int, float)):
        return valor_str
    clean = str(valor_str).replace('R$', '').replace('.', '').replace(',', '.').strip()
    try:
        return float(clean)
    except ValueError:
        return 0.0

def formatar_data_iso(data_str):
    """Converte '01/12/2025' para '2025-12-01'"""
    if pd.isna(data_str):
        return ""
    try:
        dt = datetime.datetime.strptime(str(data_str), "%d/%m/%Y")
        return dt.strftime("%Y-%m-%d")
    except ValueError:
        return ""

def calcular_ultima_leitura(data_str):
    """Calcula 1 mês após a data informada e retorna ISO."""
    if pd.isna(data_str):
        return ""
    try:
        dt = datetime.datetime.strptime(str(data_str), "%d/%m/%Y")
        
        # Adiciona 1 mês
        new_year = dt.year
        new_month = dt.month + 1
        
        # Vira o ano se passar de dezembro
        if new_month > 12:
            new_month = 1
            new_year += 1
            
        # Lida com dias (ex: evita erro de 31 de fevereiro)
        last_day = calendar.monthrange(new_year, new_month)[1]
        new_day = min(dt.day, last_day)
        
        new_dt = dt.replace(year=new_year, month=new_month, day=new_day)
        return new_dt.strftime("%Y-%m-%d")
    except ValueError:
        return ""

def obter_ano_mes(data_str):
    """Retorna (2025, '12') a partir de '01/12/2025' para criar pastas"""
    if pd.isna(data_str):
        return "SemData", "Geral"
    try:
        dt = datetime.datetime.strptime(str(data_str), "%d/%m/%Y")
        return str(dt.year), str(dt.month).zfill(2)
    except ValueError:
        return "SemData", "Geral"

def limpar_nome_arquivo(titulo):
    """Remove caracteres proibidos em nomes de arquivos"""
    limpo = str(titulo).replace(':', ' -').replace('/', '-')
    return re.sub(r'[\\/*?<>|]', '', limpo).strip()

def carregar_corpo_modelo(caminho_modelo):
    """Lê o arquivo MD modelo e retorna apenas o conteúdo após o YAML"""
    if not os.path.exists(caminho_modelo):
        print(f"Aviso: Modelo {caminho_modelo} não encontrado.")
        return ""
    
    with open(caminho_modelo, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    
    # Separa o Frontmatter (YAML) do resto do conteúdo
    partes = conteudo.split('---')
    if len(partes) >= 3:
        return '---'.join(partes[2:]).strip()
    else:
        return conteudo

def main():
    print(f"Iniciando importação para a pasta '{PASTA_SAIDA}'...")
    
    if not os.path.exists(ARQUIVO_CSV):
        print(f"Erro Crítico: Arquivo CSV '{ARQUIVO_CSV}' não encontrado.")
        return

    try:
        df = pd.read_csv(ARQUIVO_CSV)
    except Exception as e:
        print(f"Erro ao ler CSV: {e}")
        return

    corpo_dataview = carregar_corpo_modelo(ARQUIVO_MODELO)
    count_sucesso = 0
    
    # Cria a pasta 'Finalizado' se ela não existir
    if not os.path.exists(PASTA_SAIDA):
        os.makedirs(PASTA_SAIDA)

    for index, row in df.iterrows():
        titulo = row.get('Título', 'Sem Titulo')
        if pd.isna(titulo): continue

        # Preparar dados
        valor = limpar_valor_monetario(row.get('valor'))
        paginas = int(row.get('Páginas', 0)) if not pd.isna(row.get('Páginas')) else 0
        data_proc_original = row.get('Processado em')
        data_proc_iso = formatar_data_iso(data_proc_original)
        data_pub_iso = formatar_data_iso(row.get('Data de Publicação'))
        
        # Cálculo de Data (1 mês depois)
        ultima_leitura_iso = calcular_ultima_leitura(data_proc_original)
        
        tipo = row.get('Tipo', 'Quadrinho')
        universo = row.get('Universo', '')

        # Definir pastas (Finalizado/2025/12)
        ano, mes = obter_ano_mes(data_proc_original)
        caminho_pasta = os.path.join(PASTA_SAIDA, ano, mes)
        os.makedirs(caminho_pasta, exist_ok=True)

        nome_arquivo = f"{limpar_nome_arquivo(titulo)}.md"
        caminho_final = os.path.join(caminho_pasta, nome_arquivo)

        # Montar o Conteúdo
        conteudo_arquivo = f"""---
Processado em: {data_proc_iso}
Situação: Finalizado
Data de Entrega:
Chegou: true
Status de Leitura: Lido
Vezes que Li: 1
Páginas: {paginas}
valor: {valor}
Favorito: false
Avaliação:
imagem:
Tipo: {tipo}
Última Leitura: {ultima_leitura_iso}
Data de Publicação: {data_pub_iso}
Universo: {universo}
---

{corpo_dataview}
"""

        with open(caminho_final, 'w', encoding='utf-8') as f:
            f.write(conteudo_arquivo)
        
        count_sucesso += 1

    print(f"Concluído! {count_sucesso} arquivos gerados dentro de '{PASTA_SAIDA}'.")

if __name__ == "__main__":
    main()