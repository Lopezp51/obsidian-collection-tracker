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

## 🤖 Gemini CLI & Agent Skills

Este projeto conta com o **Gemini CLI**, um agente de IA integrado que ajuda na manutenção e automação do seu Vault. Criamos uma Skill personalizada para manter seus metadados sempre limpos e atualizados.

### 🛠️ Skill: `update-properties-search`
Esta skill automatiza a padronização das notas. Ela:
1. Reorganiza as propriedades do YAML seguindo o modelo em `Templates/PROPOSTA_PROPRIEDADES.md`.
2. Mantém seus valores atuais (preço, páginas, etc).
3. Pesquisa automaticamente no Google o **Roteiro, Arte e Cores** caso estejam vazios e preenche como listas YAML.

### 📖 Como usar (Passo a Passo)

Sempre que iniciar uma nova sessão no Gemini CLI:

1. **Recarregue as Skills:**
   ```bash
   /skills reload
   ```
2. **Peça uma atualização:**
   Você pode pedir para o agente atualizar um arquivo específico ou um lote de arquivos. Exemplos:
   - *"Padronize o arquivo 'Acervo/Faturado/Batman 01.md' usando minha skill."*
   - *"Aplique a skill de propriedades em todos os volumes de 'Mulher-Maravilha' do 01 ao 13."*
   - *"Atualize o título [Nome], use o formato [Grampo] e a coleção [Batman]."*

> **Dica:** O modelo de ordem das propriedades pode ser editado em `Templates/PROPOSTA_PROPRIEDADES.md`. O agente sempre consultará esse arquivo para saber a ordem correta.

---
Desenvolvido incansavelmente para transformar uma simples planilha de compras na estante virtual mais incrível de todas! 🦇✨
