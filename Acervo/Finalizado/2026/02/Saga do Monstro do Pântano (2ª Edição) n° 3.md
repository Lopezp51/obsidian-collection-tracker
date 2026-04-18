---
Processado em: 2026-02-01
Situação: Finalizado
Data de Entrega: 2026-01-30
Chegou: true
Status de Leitura: Lido
Vezes que Li: 1
Páginas: 210
valor: 50.33
Favorito: true
Avaliação: 5
imagem: Banco de Imagens/HQ's/Saga do Monstro do Pântano (2ª Edição) n° 3.jpeg
Nexo:
  - Quadrinho
  - Vertigo
  - DC
Última Leitura: 2026-03-28
Data de Publicação: 2018-08-11
Universo: Vertigo
---

> [!bookbox]
> ```meta-bind
> INPUT[imageSuggester(optionQuery("")):imagem]
> ```
> <div class="book-metadata">
>
> **Avaliação:** `$= const r = dv.current().Avaliação || 0; let s = "<div class='rating-wrapper'>"; for (let i = 1; i <= 5; i++) { if (i <= Math.floor(r)) { s += "<span class='rating-star star-full'>" + obsidian.getIcon("star").outerHTML + "</span>"; } else if (i === Math.ceil(r) && r % 1 >= 0.5) { s += "<span class='rating-star star-half'>" + obsidian.getIcon("star-half").outerHTML + "</span>"; } else { s += "<span class='rating-star star-empty'>" + obsidian.getIcon("star").outerHTML + "</span>"; } } s += "</div>"; dv.span(s)`
> ```dataviewjs
> const total = dv.current()["Páginas"] || 1;
> const listaItens = dv.current().file.lists;
> const progresso = listaItens.where(i => i.pagina != null).map(i => Number(i.pagina));
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
> - [data:: 2026-03-25] | [pagina:: 109] | [obs:: Ele se deslocar foi muito daora e esse design do Constantine é o mais daora que já vi]> 
> - [data:: 2026-03-24] | [pagina:: 62] | [obs:: Caramba, curti essa crítica ao lixo radioativo e po, muito visceral as duas primeiras história, deu um dó do monstro.]=
> - [data:: 2026-03-26] | [pagina:: 158] | [obs:: Cara esse arco dos monstros ta irado, entre os de vampiro e lobisomem, apesar da de lobisomem ter sido uma história só, acho que preferi ela]
> - [data:: 2026-03-28] | [pagina:: 210] | [obs:: Po os capitulos de zumbi foram demais velho, pesados e interessantes, mal posso esperar para ver o desenrolar desse arco de monstros inteiro]