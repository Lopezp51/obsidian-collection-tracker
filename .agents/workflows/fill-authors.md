---
description: Fazer pesquisa automática em 10 itens sem autor e preencher Roteiro, Desenhos e Autoria
---

# Skill: Preencher Autores de Quadrinhos/Mangás

Quando o usuário invocar esta skill (`/fill-authors` ou `execute a preenchedora de autores`), siga este fluxo exato:

## 1. Identificar Registros Sem Autor
Utilize um script Python nativo no ambiente (ou sua varredura interna) para encontrar arquivos no Obsidian nas pastas "Gestão de Compras" ou "Acervo" onde os campos `Roteiro`, `Desenhos` ou `Autoria` (dependendo do tipo) não existem, estão vazios (`null`), ou são listas vazias (`[]`).
- DESSA lista, selecione um **Lote (Batch)** de até **10 arquivos aleatórios**.

## 2. Pesquisar Metadados (Web Search)
Use sua ferramenta de `search_web` para buscar informações factuais de autoria de cada um dos 10 arquivos listados. Exemplo de *query*: `"{Titulo do Livro/Quadrinho}" quadrinho roteirista desenhista`.

Gere o "pacote de autores" baseado no cenário:

### Para Mangás & Livros Clássicos
Preencher o campo `Autoria`.
- **Formato esperado YAML List:** `["Nome do Autor"]`

### Para Quadrinhos (Comics / HQ)
Identifique e separe o responsável pela história e o responsável pela arte para preencher `Roteiro` e `Desenhos`.
- **Campo Roteiro:** `["Nome do Roteirista"]`
- **Campo Desenhos:** `["Nome do Desenhista", "Nome do Colorista"]`

## 3. Preenchimento via Edição de Arquivo (Injeção YAML Segura)
Atualize as notas injetando os valores nos campos corretos (`Roteiro`, `Desenhos`, `Autoria`). Certifique-se de manter os outros campos do YAML intactos.

## 4. Relatar
Ao final, entregue ao usuário no chat uma tabela rápida com as 10 obras processadas e os autores inseridos em cada campo.
