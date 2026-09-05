---
Processado em: 2026-03-24
Situação: Finalizado
Data de Entrega: 2026-03-26
Chegou: true
Status de Leitura: Lido
Vezes que Li: 0
Páginas: 528
valor: 305.93
Favorito: true
Avaliação: 5
imagem: Banco de Imagens/HQ's/DC -  A Nova Fronteira (Edição Absoluta).webp
Tipo: Quadrinho
Última Leitura: 2026-06-23
Data de Publicação: 2026-03-19
Universo: DC
Planejo pegar em: 2026-07-01
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
> - [data:: 2026-06-21] | [pagina:: 87] | [obs:: Devo dizer que não foi o que eu esperava até então, por enquanto teve mais 3 aparições dos personagens da Liga só, achei que ia ter mais coisa. A arte em si é fenomenal, e adorei o design da Diana]
> - [data:: 2026-06-22] | [pagina:: 214] | [obs:: Okay nova fronteira ganhou meu interesse kkkk eu tava achando que tudo seria só um antologia de histórias que não se amarram muito, mas nessas páginas tudo ta se conectando com todas as histórias que estão aparecendo. To curtindo ver muito a galera da liga, ver o Flash quebrando a barreira do som foi irado, o Hal ta com um desenvolvimento lento e to amando, aparições do Batman foram poucas até agora mas muito boa, e o caçador de marte ta daora também, tudo ta muito bom. E pelo jeito a Diana vai se desapontar com o jeito americano, pelo andar das coisas]
> - [data:: 2026-06-23] | [pagina:: 528] | [obs:: Absolute cinema, cara amei de mais isso, toda a história ficando amarradinha, cada personagem pareceu significar de mais pra tudo, pra mim no final mulher maravilha, flash e lanterna verde foram os melhores personagens, mas personagem como o Faraday e Rick Flag me ganharam também, eles tinham bons motivos para fazer oq fizeram. Os extras também amei, cada capa linda, e a ideia do epilogo com o Aquaman e Superman ter ficado de fora pq parecia gay demais rachei com o comentário do autor. História perfeita.]