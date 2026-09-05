---
Processado em: 2026-07-04
Situação: Finalizado
Data de Entrega: 2026-07-13
Chegou: true
Status de Leitura: Lido
Vezes que Li: 1
Páginas: 152
valor: 38.8
Favorito: false
Avaliação: 3
imagem: Banco de Imagens/Mangas/Ultimate Homem-Aranha (2024) Vol. 3.jpg
Última Leitura: 2026-07-29
Data de Publicação: 2026-06-26
Nexo:
  - Panini
  - Quadrinho
  - Homem-Aranha
  - Universo Ultimate
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
> - [data:: 2026-07-29] | [pagina:: 152] | [obs:: O Vini tinha falado que era muito bom esse volume 3, mas achei bem mais ou menos, confronto com o Kraven achei muito rápido, não achei bem desenvolvido. Uma parte que gostei foi da Gwen ser o mistério, mas que provavelmente vão ter que parar ela. Tempo de familia com o miranha ele ficou mais com o Richard que foi legalzin de ver, teve o homem areia que parece que foi colocado por quase nada. Tipo tem um arco grande que vai culminar no rei do crime no final, mas podia ser uma HQ muito mais longa e ir com calma, enorme pontecial perdido. E Felicia ser um X9 eu odiei, espero que ela esteja só fingindo, mas daqui uns 6 meses decobrimos.]