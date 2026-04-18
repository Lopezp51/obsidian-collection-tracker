---
description: Busca metadados de mangás na internet, faz download da capa HQ e preenche YAML + Templates do Dashboard.
---

# Workflow: Manga Metadata Sync (`manga-metadata-sync`)

Quando o usuário solicitar `/manga-metadata-sync <Nome da Obra e Volume>`, o assistente (você) DEVE seguir rigorosamente estes passos, sem pular nenhum.

## Passo 1: Caça aos Dados 🕵️
1. Use ferramentas de busca web (`search_web`) para encontrar o preço, páginas e data de lançamento.

## Passo 2: Captura da Capa em Alta Resolução (Via Browser) 🖼️
Como as APIs fornecem miniaturas de péssima qualidade:
1. Use o `browser_subagent` para navegar no Google/Amazon/Panini buscando a obra.
2. Acesse a página do produto, **aguarde o carregamento completo da imagem** de alta resolução e salve/faça download na pasta correta (`Banco de Imagens/Mangas/` ou `Banco de Imagens/HQ's/`).
3. **MUITO IMPORTANTE:** O nome do arquivo da imagem (.jpg) deve ser **exatamente idêntico** ao nome da nota (.md). Exemplo: Se a nota é `Demon Slayer Vol. 1.md`, a imagem DEVE se chamar `Demon Slayer Vol. 1.jpg`.

## Passo 3: Limpeza Estrita de Variáveis 🧹
Como o dashboard (em `app.py`) processa os dados, o rigor de tipo é absoluto:
*   **Valor:** Apenas float. Sem "R$". Ex: `36.90`.
*   **Data_ISO:** Padrão `YYYY-MM-DD`.

## Passo 4: Atualização do Frontmatter YAML e Injeção do Template 📝
Substitua ou crie a nota `.md` da obra, garantindo esse YAML exato:

```yaml
---
Processado em: [Data local de hoje, ex: 2026-04-18]
Situação: Desejado
Data de Entrega: 
Chegou: false
Status de Leitura: Não Iniciado
Vezes que Li: 0
Páginas: [Número de páginas]
valor: [Preço em Float]
Favorito: false
Avaliação: 0
imagem: "Banco de Imagens/[Mangas ou HQ's]/[Nome exato da nota.jpg]"
Tipo: [Quadrinho ou Manga]
Última Leitura: 
Data de Publicação: [Data ISO]
Nexo:
  - Manga ou Quadrinho
  - Panini
  - [Nome da Obra]
---
```

**MUITO IMPORTANTE:** Após o YAML estar completo, você DEVE pular uma linha e **copiar todo o corpo de texto (Body)** do arquivo `Templates/Novo Manga.md` (ou `Novo Quadrinho.md`), que contém os scripts "meta-bind" e "dataviewjs" (o `> [!bookbox]`), e colar embaixo desse frontmatter. NUNCA crie uma nota vazia.

## Passo 5: Confirmação e Log Final ✅
Exiba os dados processados e confirme que a nota foi completa.
