---
Processado em: 2025-11-27
Situação: Finalizado
Data de Entrega:
Chegou: true
Status de Leitura: Lido
Vezes que Li: 1
Páginas: 640
valor: 206.2
Favorito: true
Avaliação: 5
imagem: Banco de Imagens/HQ's/Mulher-Maravilha por George Pérez Vol. 1.jpg
Tipo: Quadrinho
Última Leitura: 2026-03-03
Data de Publicação: 2023-09-01
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
> - [data:: 2026-02-06] | [pagina:: 46] | [obs:: Cara que incrível esse começo, li só a primeira história, mas foi tudo tão incrível, eu chorei no nascimento da Diana, e todo o background as amazonas, em especial da hipolita foi incrível, da pra ver que estou lendo algo especial.]
> - [data:: 2026-02-09] | [pagina:: 70] | [obs:: Segue incrível, é estranho estar lendo algo de origem assim, parece realmente que estou lendo algo épico]
> - [data:: 2026-02-10] | [pagina:: 116] | [obs:: Sensação de algo épico continua, parece que estou lendo algo de um começo que vai expandir em muito ainda.]
> - [data:: 2026-02-14] | [pagina:: 184] | [obs:: Finalizou o arco de Ares, achei daora como terminol e curioso pro futuro, mas o arco foi perfeito incrível demais.]
> - [data:: 2026-02-15] | [pagina:: 209] | [obs:: Esse foi mais cansativo, que foi tipo mais logs de pessoas falando sobre a diana, mas o final da Barbara Minerva me deixou intrigado, do outro cinturão de gaia.]
> - [data:: 2026-02-16] | [pagina:: 254] | [obs:: Meu pesou o clima igual na primeira história, tamo indo pra uma missão de provação perante aos deuses]
> - [data:: 2026-02-17] | [pagina:: 276] | [obs:: Plot continua muito bom, to curioso pra descobrir mais da Diana, a mulher que o nome foi homenagem a princesa. ]
> - [data:: 2026-02-18] | [pagina:: 322] | [obs:: Pelo jeito ta finalizando o arco dos desafios dos deuses ou tamo no encerramento, irado o final]
> - [data:: 2026-02-22] | [pagina:: 392] | [obs:: Terminamos a parte dos deuses e fomos pra algumas histórias focadas no mundo do patriarcado, mas parece que pelo final que vai ter algo relacionado aos deuses de novo.]
> - [data:: 2026-02-23] | [pagina:: 416] | [obs:: Estamos começando um novo arco, um deslocamento dos deuses do Olimpo para outro local e a viagem de Diana para a Grécia.]
> - [data:: 2026-02-25] | [pagina:: 438] | [obs:: Caraca Circe apareceu, vai ser legal ver a contraparte dela aqui, sendo que a única que conheço é do universo absolute.]
> - [data:: 2026-02-28] | [pagina:: 508] | [obs:: Pelo jeito chegamos no fim dos deseus como conhecemos, curioso para ver o que de novo vai se formar.]
> - [data:: 2026-03-02] | [pagina:: 553] | [obs:: Parei no meio do anual, deu pra ver na hora que não era mais o Perez desenhando, achei que ia acontecer algo de ruim na visita da Vanessa e da Julia a ilha paraíso, mas tudo segue bem, foi legal de ver a animação da Diana em trazer as duas para a ilha.]
> - [data:: 2026-03-03] | [pagina:: 640] | [obs:: Termineu, leitura fenomenal, como um todo, ver a origem da Diana foi incrível demais, animado para ver como vai continuar a história do George Perez, fico de cara com tanta história ele contou em 24 edições, fenomenal.]