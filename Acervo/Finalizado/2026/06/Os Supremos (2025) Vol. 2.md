---
Processado em: 2026-06-11
Situação: Finalizado
Data de Entrega: 2026-06-22
Chegou: true
Status de Leitura: Lido
Vezes que Li: 1
Páginas: 176
valor: 48.52
Favorito: false
Avaliação: 1.5
imagem: Banco de Imagens/HQ's/Os Supremos (2025) Vol. 2.webp
Nexo:
  - Quadrinho
  - Ultimate
  - Marvel
  - Panini
Última Leitura: 2026-07-17
Data de Publicação: 2026-05-25
Universo: Marvel
Planejo pegar em: 2026-06-01
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
> - [data:: 2026-07-17] | [pagina:: 176] | [obs:: Nossa que merda ta sendo esse volume, história da américa chaves foi paia, tipo só mostrou coisas que ela fez no passado, só expos pra caramba. A morte do garoto de ferro foi desfeita, na verdade ele ta vivo. A história do Nick Fury sendo um clona e sempre tentando matar o conselho e sempre falhando, péssimo pra fazer tudo numa história só. Luke Cage a lá Alan Moore, tanto painel maluco pra que, mas foi a melhorzinha até agora. Do caveira achei uma porcaria a condução de tudo, não gosto nenhum pouco dos Supremos só matando seus inimigos. História do Thor e da Sif sendo só uma arte por página e só um narrador explicando oq ta acontecendo, quase me dá saudade do Tom King (que não gosto), de longe a pior história desse volume. A última foi melhorzinha, então o Tony realmente morreu, mas o Destino voltou no tempo, pouco antes de ele morrer e os outros morrerem, no caso eles morreram mesmo, mas naquele momento que o Tony está a beira da morte foi quando o destino puxou eles, e vão começar os supremos 3.0, ver que q vai dar, e po sério que a Vespa ta sendo uma espia pro Fury? Que merda mesmo]