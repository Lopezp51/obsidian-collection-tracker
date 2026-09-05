---
Processado em: 2026-03-12
Situação: Finalizado
Data de Entrega: 2026-03-16
Chegou: true
Status de Leitura: Lido
Vezes que Li: 1
Páginas: 388
valor: 110.2
Favorito: true
Avaliação: 5
imagem: Banco de Imagens/HQ's/O Quarto Poder e a Conspiração Starr.jpg
Tipo: Quadrinho
Última Leitura: 2026-06-16
Data de Publicação: 2025-02-21
Universo: Indie
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
> - [data:: 2026-06-10] | [pagina:: 72] | [obs:: Po eu to de cara que o motivo de eu ter comprado a HQ foi a personagem da capa, e ela morre na primeira história, topzeira hein, segunda vez que meio que quebro a cara por capa do pipoca, próximas vezes vou mais a fundo. Mas vamos ver qualé que é das outras histórias]
> - [data:: 2026-06-11] | [pagina:: 200] | [obs:: Po....quebrei a cara agora de novo kkkkkk li o tomo 2 e 3 e foram muito bons kkkk não esperava, curti muito a Gal e a J.A.K, me senti traído na primeira história por conta da Mega, achei q ia ser o fim dela ou da QB4, mas eu errei, leitura foi muito boa desses dois tomo de hoje]
> - [data:: 2026-06-14] | [pagina:: 258] | [obs:: Muito legal a última história, apesar de eu querer ter visto mais da Gal e da J.A.K juntas, focou muito mais num conflito onde Gal foi se esconder, mas achei interessante a torre e fiquei meio triste ao ver que a história da Gal finaliza naquele planeta, por conta que não teve histórias dela a seguir, mas foi um legal final em aberto pro futuro dela.]
> - [data:: 2026-06-15] | [pagina:: 314] | [obs:: Cospiração Starr foi divertido kkkkk é totalmente comédia e uma aventura no espaço, mas as situações foram interessantes, Leo e Meke formam uma boa dupla]
> - [data:: 2026-06-16] | [pagina:: 388] | [obs:: Caramba que doideira o último, curti o plot do Leo e do Meke, o Leo eu tinha já gostado na primeira história mas o Meke foi interessante nessa, e a arte durante tudo taba belissima, um dos quadrinhos mais lindos que já li, quero mais do autor.]