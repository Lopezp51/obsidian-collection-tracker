---
Situação: Finalizado
Favorito: true
Avaliação: 5
Última Leitura: 2026-08-24
Status de Leitura: Lido
Processado em: 2026-01-07
Data de Entrega: 2026-02-12
Chegou: true
Data de Publicação: 2026-01-01
Coleção:
  - Mulher-Maravilha
  - Sagas Panini
Formato:
  - Capa Cartão
Editora:
  - Panini
  - DC
valor: 41.31
Páginas: 144
Vezes que Li: 1
Roteiro:
  - Greg Rucka
Arte:
  - Drew Johnson
  - James Raiz
  - Sean Phillips
Cores:
  - Richard Horie
  - Tanya Horie
imagem: Banco de Imagens/HQ's/A Saga da Mulher-Maravilha Vol. 10.webp
tags:
  - Quadrinho
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
> - [data:: 2026-08-23] | [pagina:: 52] | [obs:: Dam começou legal, Medusa pelo jeito vai ser uma ameaça tensa, curioso com o jogo que o doutor psycho ta fazendo, toda vez q ele aparece, é um desgraçado mesmo ]
> - [data:: 2026-08-24] | [pagina:: 144] | [obs:: Irado demais, a luta entre Diana e Medusa foi muito boa, e com consequencias a principio, teve a petrificação do garoto e a Diana ficando cega. Os deuses também só ficam fazendo seus joguinhos, odiei a resposta que Atena deu a diana, dizendo que a morte do garoto foi um pequeno preço a pagar e agora Diana deveria dar essa respota ao pai do garoto. Ela lutando contra a liga foi daora também, pra se provar que ela ainda dá conta do recado.]