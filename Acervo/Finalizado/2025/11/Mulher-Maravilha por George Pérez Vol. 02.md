---
Processado em: 2025-11-27
Situação: Finalizado
Data de Entrega:
Chegou: true
Status de Leitura: Próximo
Vezes que Li: 0
Páginas: 552
valor: 206.2
Favorito: false
Avaliação:
imagem: Banco de Imagens/HQ's/Mulher-Maravilha por George Pérez Vol. 2.webp
Nexo:
  - Quadrinho
  - Mulher-Maravilha
  - Omnibus
  - Panini
  - DC
Última Leitura: 2026-04-19
Data de Publicação: 2024-05-01
Universo: DC
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
> - [data:: 2026-04-06] | [pagina:: 34] | [obs:: Esse omnibus começa na edição 24, ta tipo num crossover com a liga, mas comecinho ta mais ou menos, e uma galera falando mal da diana ou dando em cima dela não pegou muito bem]
> - [data:: 2026-04-09] | [pagina:: 80] | [obs:: Pelo jeito vamos adentrar mais na história da mulher leopardo, ainda bem, pq ela apareceu no começo em umas duas histórias e nada mais, tomara que o foco seja mais Diana e o universo dela, do que os outros da liga.]
> - [data:: 2026-04-10] | [pagina:: 126] | [obs:: Po finalmente ficou legal, duas edições focadas na orgem da mulher leopardo, fui irado de ver a cultura por cima, os cara podiam sei lá, ter feito em umas 3 páginas tudo, mas foram muito a fundo, parte mais legal desse volume até agora]
> - [data:: 2026-04-11] | [pagina:: 172] | [obs:: Cara essa parte inteira da Barbara, das amazonas do egito e a Diana sendo forçada a ser mais violenta foi irado demais, me empolguei muito igual no Ares.]
> - [data:: 2026-04-14] | [pagina:: 195] | [obs:: Dam, começou meio morno mas parece que o próximo foco vai ser as amazonas do egito, hype demais]
> - [data:: 2026-04-15] | [pagina:: 218] | [obs:: Caramba plot ta daora ainda, espero que leve um tempo esse arco dessas amazonas ]
> - [data:: 2026-04-19] | [pagina:: 263] | [obs:: Finalizamos o arco das amazonas do egito, gostei muito no geral, foi muito bom, estou curioso se vamos ver mais da Shim'tar, porque ela pareceu ser identica a Diana, então talvez seja um clone ou algo do tipo, mas deve aparecer mais pra frente ainda.]
> - [data:: 2026-04-21] | [pagina:: 316] | [obs:: O anual foi muito melhor que o último, focar em como o mundo reagia a Diana foi bem legal, mas em espefico o mundo do marketing que a Mynde criou]