---
Situação: Finalizado
Favorito: false
Avaliação: 2
Última Leitura: 2026-06-10
Status de Leitura: Lido
Processado em: 2026-04-24
Data de Entrega: 2026-05-27
Chegou: true
Data de Publicação: 2026-04-24
Coleção:
  - X-Men
Formato:
  - Grampo
Editora:
  - Marvel
  - Panini
valor: 11.94
Páginas: 48
Vezes que Li: 1
Roteiro: []
Arte: []
Cores: []
imagem: Banco de Imagens/HQ's/Excepcionais X-Men 06.webp
tags:
  - Quadrinho
Colocado no saquinho: 2026-06-10
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
> - [data:: 2026-06-10] | [pagina:: 48] | [obs:: Dessa vez X factor levou a melhor,  po a frenesi é daora demais, mas ela teve pouca aparição nesse. Excepcionais ta meia boca ainda, parece que vai ser um plot de traição que já vimos tantas vezes já, não tem surpresa]