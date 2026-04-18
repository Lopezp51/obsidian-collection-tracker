# Obsidian Collection Tracker 📚

Bem-vindo ao **Obsidian Collection Tracker**! Este repositório guarda a estrutura completa de um `Vault` de Obsidian focado no acompanhamento, gerenciamento e controle de Mangás e Histórias em Quadrinhos (HQs), integrado a um Dashboard Web (FastAPI)  desenvolvido para raspar (scrape) e organizar novas capas e metadados diretamente da Panini.

## 🌟 Principais Funcionalidades

- **Gerenciamento Via Markdown:** Cada item da sua coleção é uma nota `.md` salva localmente no Obsidian com um frontmatter riquíssimo (Situação, Data de Entrega, Avaliação, etc).
- **Web Dashboard Local:** Uma interface interativa acessada pelo navegador que lê em tempo real os itens do seu Vault Obsidian.
- **Scraping Integrado:** Através do painel, você pesquisa um título diretamente na base de dados da Panini. Com a ajuda do *Playwright*, o painel baixa as capas em alta resolução e cria instantaneamente os arquivos Markdown corretos, já configurados!
- **Organização por Metadados:** Seletor nativo no app para jogar aquisições para `Faturado`, `Pendente`, `Desejado`, `Pré Venda` ou `Finalizado`.

## 📁 Estrutura do Projeto

A raiz desse repositório serve simultaneamente como o seu **Obsidian Vault** e abriga a pasta do código da aplicação (`painel-app`).

```text
├── 📂 Acervo (ou Gestão de Compras)/  <- Suas notas .md com a coleção.
├── 📂 Banco de Imagens/               <- Capas (Mangas e HQ's) armazenadas localmente.
├── 📂 Bases/                          <- Tabelas e visões configuradas do Obsidian.
├── 📂 Templates/                      <- Templates MD de Mangá e HQ.
└── 📂 painel-app/                     <- A Aplicação Backend & Frontend.
    ├── 📂 static/                     <- JS e CSS do Dashboard (Estilização Premium).
    ├── 📂 templates/                  <- O HTML local.
    ├── app.py                         <- Servidor FastAPI (Rotas, Lógicas, Playwright).
    └── requirements.txt               <- Dependências do Python Python.
```

## 🚀 Como Executar o Web Dashboard

1. **Abra o terminal** na pasta do projeto e navegue até o aplicativo web:
   ```bash
   cd painel-app
   ```

2. **Crie/Ative um ambiente virtual (Recomendado)**
   ```powershell
   # Windows
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```

4. **Inicie o servidor localmente**
   ```bash
   python app.py
   ```
   *Alternativamente:* `uvicorn app:app --host 127.0.0.1 --port 8000 --reload`

5. Acesse [http://127.0.0.1:8000](http://127.0.0.1:8000) pelo navegador para visualizar a sua Estante!

## 🤝 Uso no Dia a Dia
- Como a aplicação acessa o Vault diretamente (uma camada acima: `../`), ao abrir o painel web e adicionar uma nova encomenda num status (como *Desejado*), o arquivo será salvo na mágica e na hora na pasta correspondente.
- Assim que você abrir as "Bases" e visualizações através do **aplicativo nativo do Obsidian**, tudo já estará perfeitamente sincronizado com as tags arrumadas!

---
Desenvolvido incansavelmente para transformar uma simples planilha de compras na estante virtual mais incrível de todas! 🦇✨
