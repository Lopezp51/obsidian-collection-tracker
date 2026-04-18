---
description: Fazer pesquisa automática em 10 itens sem autor e preencher Roteiro, Desenho e Criação
---

# Skill: Preencher Autores de Quadrinhos/Mangás

Quando o usuário invocar esta skill (`/fill-authors` ou `execute a preenchedora de autores`), siga este fluxo exato:

## 1. Identificar Registros Sem Autor
Utilize um script Python nativo no ambiente (ou sua varredura interna) para encontrar arquivos no Obsidian nas pastas "Gestão de Compras" ou "Acervo" cuja chave property do YAML `Autore(s)` não existe, está vazia (`null`), ou é uma lista vazia (`[]`).
- DESSA lista vazia, selecione um **Lote (Batch)** de até **10 arquivos aleatórios**.

## 2. Pesquisar Metadados (Web Search)
Use sua ferramenta de `search_web` para buscar informações factuais de autoria de cada um dos 10 arquivos listados. Exemplo de *query*: `"{Titulo do Livro/Quadrinho}" quadrinho roteirista desenhista`.

Gere o "pacote de autores" baseado no cenário:

### Para Mangás & Livros Clássicos
Aglomerar em uma única tag, indicando autoria principal.
- **Formato esperado YAML List:** `- Nome do Autor (Criador)` ou `- Nome do Autor (Autor)`

### Para Quadrinhos (Comics / HQ)
Identifique e separe o responsável pela história e o responsável pela arte. Se houver mais de um ilustrador na mesma obra, deve-se gerar uma linha com a tag para cada um, adotando o mesmo padrão de parenteses.
- **Formato esperado YAML List:**
  - `- Fulano de Tal (Roteiro)`
  - `- Ciclano de Tal (Arte)`
  - `- Beltrano de Tal (Arte)`

## 3. Preenchimento via Edição de Arquivo (Injeção YAML Segura)
Processe os arquivos usando o módulo `yaml` de Python manipulando especificamente o Header de forma segura (preservando o resto da nota). Atualize as respectivas 10 notas injetando o pacote preparado dentro de `Autore(s)`.

## 4. Relatar
Ao final, entregue ao usuário no chat uma tabela rápida com as 10 obras processadas e quem você inseriu. (Não é preciso salvar o log no disco fisicamente se não for solicitado, o relatório verbal e a própria atualização das tags satisfazem a auditoria da base `Sem Autores`).
