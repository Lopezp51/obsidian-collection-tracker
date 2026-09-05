---
Situação: Finalizado
Favorito: false
Avaliação: 2.5
Última Leitura: 2026-08-27
Status de Leitura: Lido
Processado em: 2026-08-11
Data de Entrega: 2026-08-15
Chegou: true
Data de Publicação: 2023-12-15
Coleção:
Formato:
  - Capa Cartão
Editora:
  - "Devir Livraria\r"
valor: 54.87
Páginas: 152
Vezes que Li: 0
Roteiro: []
Arte: []
Cores: []
imagem: Banco de Imagens/HQ's/Rain.jpg
tags:
  - Quadrinho
---

> [!bookbox]
> ```meta-bind
> INPUT[imageSuggester(optionQuery("")):imagem]
> ```
> <div class="book-metadata">
>
> **Avaliação:** `$= const r = dv.current()?.Avaliação || 0; let s = "<div class='rating-wrapper'>"; for (let i = 1; i <= 5; i++) { if (i <= Math.floor(r)) { s += "<span class='rating-star star-full'>" + obsidian.getIcon("star").outerHTML + "</span>"; } else if (i === Math.ceil(r) && r % 1 >= 0.5) { s += "<span class='rating-star star-half'>" + obsidian.getIcon("star-half").outerHTML + "</span>"; } else { s += "<span class='rating-star star-empty'>" + obsidian.getIcon("star").outerHTML + "</span>"; } } s += "</div>"; dv.span(s)`
> ```dataviewjs
> const total = dv.current()?.["Páginas"] || 1;
> const listas = dv.current()?.file?.lists || [];
> const progresso = listas.where ? listas.where(i => i.pagina != null).map(i => Number(i.pagina)) : [];
> let atual = 0;
> if (progresso.length > 0) { atual = Math.max(...progresso); }
> const pct = Math.min(100, Math.round((atual / total) * 100));
> 
> const htmlBar = `
> <div style="width: 100%; background-color: var(--background-modifier-border); border-radius: 10px; height: 18px; margin-top: 5px; overflow: hidden; position: relative; border: 1px solid rgba(0,0,0,0.1);">
>     <div style="width: ${pct}%; background: linear-gradient(90deg, #8e44ad, #a29bfe); height: 100%; transition: width 0.5s ease;"></div>
>     <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: bold; color: white; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">
>         ${pct}%
>     </div>
> </div>
> <div style="text-align: center; font-size: 0.85em; margin-top: 4px; color: var(--text-muted);">
>     Lidos <b>${atual}</b> de <b>${total}</b> páginas
> </div>
> `;
> 
> dv.span(htmlBar);
> ```
> 
> </div>

### **🗓️ Histórico de leitura**

```dataview
TABLE WITHOUT ID 
    item.data AS "Data", 
    item.pagina AS "Página", 
    item.obs AS "Observação"
FROM ""
FLATTEN file.lists AS item
WHERE file.path = this.file.path 
  AND item.data != null
SORT item.data DESC
```

### Páginas lidas

> [!quote]- Dados de Leitura (Clique para expandir)
> - [data:: 2026-08-27] | [pagina:: 152] | [obs:: Se eu tivesse pesquisado um pouco mais não teria comprado eu acho, o que me vendeu foi a capa, achei que seria tipo o amor se mantendo numa terra meio devastada. Achei a história triste até demais, realmente como o autor diz, essa não é uma história de lição de moral, é para voce ver um outro mundo na pele de um personagem, um mundo nada justo e talvez perto do nosso de certa forma, os personagens não estão nem um pouco seguros, o que me deixa triste. Não foi uma história pra mim, mas a arte em si é linda demais]