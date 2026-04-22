# Guia de Estrutura da Vault

Esta skill fornece conhecimento abrangente sobre a estrutura, organização e padrões de metadados da vault Obsidian "Painel de Controle de Encomendas & Acervo". Use estas informações para garantir consistência ao criar ou modificar notas, mover arquivos ou atualizar propriedades.

## 🏗️ 1. Arquitetura de Pastas

A Vault é organizada seguindo o fluxo de aquisição e processamento de dados:

- **`Acervo/`**: O coração da vault. Contém as notas de cada obra individual.
    - `Desejado/`: Wishlist ativa.
    - `Pré Venda/`: Itens comprados mas ainda não lançados.
    - `Faturado/`: Itens em trânsito ou com pagamento confirmado.
    - `Pendente/`: Itens recebidos mas que ainda precisam de processamento de dados ou leitura.
    - `Finalizado/`: Arquivo histórico organizado por ano (`2024/`, `2025/`, etc).
- **`Bases/`**: Contém arquivos `.base` que funcionam como configurações para o plugin *Dynamic Views* ou consultas complexas do *Dataview*. São os "Dashboards" da vault.
- **`Banco de Imagens/`**: Armazenamento centralizado de capas e mídias, categorizado por tipo (`HQ's/`, `Livros/`).
- **`painel-app/`**: Um backend externo em Python (Flask) que fornece ferramentas de manipulação de dados fora das limitações do Obsidian.
- **`.agents/`**: Repositório de inteligência. Contém instruções de workflows para IAs e scripts de automação de metadados.

---

## 🛠️ 2. Propriedades e Metadados (YAML)

Cada nota de obra deve seguir o padrão rigoroso de metadados definido em `PROPOSTA_PROPRIEDADES.md`. Os campos incluem:

| Propriedade | Tipo | Descrição |
| :--- | :--- | :--- |
| `Situação` | Texto | Localização no ciclo de vida (Desejado, Faturado, Pendente, Finalizado). |
| `Favorito` | Booleano | Se o item é um favorito. |
| `Avaliação` | Número | Nota de 0 a 5. |
| `Última Leitura` | Data | Data da última leitura realizada. |
| `Status de Leitura` | Texto | Status do progresso de leitura. |
| `Processado em` | Data | Data em que os metadados foram processados pela última vez. |
| `Data de Entrega` | Data | Data prevista ou real de entrega. |
| `Chegou` | Booleano | Se o item já foi recebido fisicamente. |
| `Data de Publicação` | Data | Data de lançamento oficial da obra. |
| `Coleção` | Lista | Nome da série ou coleção principal. |
| `Formato` | Texto | Formato físico (ex: Capa Dura, Brochura). |
| `Editora` | Lista | Editoras responsáveis pela publicação. |
| `valor` | Número | Valor de aquisição do item. |
| `Páginas` | Número | Quantidade de páginas da edição. |
| `Vezes que Li` | Número | Contador de leituras completas. |
| `Roteiro` | Texto/Lista | Responsável(is) pelo roteiro/escrita. |
| `Arte` | Texto/Lista | Responsável(is) pela arte/desenho. |
| `Cores` | Texto/Lista | Responsável(is) pelas cores. |
| `imagem` | Link | Caminho para a imagem dentro de `Banco de Imagens/`. |
| `tags` | Lista | Categorização por gênero ou formato (ex: #Quadrinho, #Manga). |

---

## ⚙️ 3. O Ecossistema de Automação

A Vault depende de três pilares tecnológicos:

1.  **Python Backend (`painel-app`)**: Utilizado para tarefas pesadas como `revert_nexo.py` e `yaml_linter.py`. O Linter garante que nenhuma nota quebre o sistema por falta de campos obrigatórios.
2.  **Helpers JS (`helpers/`)**: Scripts como `path_logic.js` que automatizam a movimentação de arquivos entre as pastas do `Acervo/` com base na mudança de status.
3.  **Workflows de IA (`.agents/workflows/`)**: Conjunto de instruções para agentes processarem dados em lote, como buscar metadados de mangás ou preencher autores automaticamente.

---

## 🎨 4. Interface e Visual (UX)

A Vault utiliza **Snippets CSS customizados** para transformar notas de texto em objetos visuais:
- `bookbox.css` / `book_effect.css`: Renderiza as notas com aparência de capas de livros/HQs.
- `rating.css`: Sistema visual de estrelas para avaliação de leitura.
- **Plugins Chave**: *Meta Bind* (para botões interativos de mudança de status) e *Dataview* (para tabelas automáticas).

---

## 📜 5. Instruções para Agentes de IA

Ao interagir com esta Vault, o agente deve:
1.  **Respeitar o Schema**: Nunca criar propriedades YAML fora do padrão estabelecido em `PROPOSTA_PROPRIEDADES.md`.
2.  **Seguir a Lógica de Pastas**: Se um item mudar de "Situação", ele deve ser movido fisicamente para a pasta correspondente no `Acervo/`.
3.  **Priorizar o Linter**: Antes de finalizar alterações em massa, considerar a conformidade com o `yaml_linter.py`.
4.  **Cuidado com Imagens**: Referências de imagem devem apontar sempre para a estrutura dentro de `Banco de Imagens/`.

---
*Última atualização: 21 de abril de 2026*
