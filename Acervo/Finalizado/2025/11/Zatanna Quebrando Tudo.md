---
Processado em: 2025-11-12
Situação: Completo
Data de Entrega: 2025-12-16
Chegou: true
Status de Leitura: Lido
Vezes que Li: 1
Páginas: 176
valor: 57.9
Favorito: false
Avaliação: 4
imagem: Banco de Imagens/HQ's/Zatanna Quebrando Tudo.jpg
Tipo: Quadrinho
Última Leitura: 2025-12-13
Data de Publicação: 2025-10-01
Universo: Marvel
---

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

```dataviewjs
// Busca o total de páginas da propriedade "Páginas" do YAML
const total = dv.current()["Páginas"] || 1;

// Busca todos os itens de lista na nota que possuem o campo "pagina"
const listaItens = dv.current().file.lists;
const progresso = listaItens
    .where(i => i.pagina != null)
    .map(i => Number(i.pagina));

// Define a página atual como a maior encontrada na lista
let atual = 0;
if (progresso.length > 0) {
    atual = Math.max(...progresso);
}

// Calcula a porcentagem
const pct = Math.min(100, Math.round((atual / total) * 100));

// Renderização da Barra (Mantive o seu CSS original)
const htmlBar = `
<div style="width: 100%; background-color: var(--background-modifier-border); border-radius: 10px; height: 20px; margin-top: 5px; overflow: hidden; position: relative;">
    <div style="width: ${pct}%; background-color: var(--interactive-accent); height: 100%; border-radius: 0px; transition: width 0.5s ease;"></div>
    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: bold; color: var(--text-on-accent); text-shadow: 0px 0px 3px rgba(0,0,0,0.5);">
        ${pct}%
    </div>
</div>
<div style="text-align: center; font-size: 0.9em; margin-top: 4px; color: var(--text-muted);">
    Lidos <b>${atual}</b> de <b>${total}</b> páginas
</div>
`;

dv.span(htmlBar);
```


### Páginas lidas
> - [data:: 2025-12-12] | [pagina:: 74] | [obs::]
> - [data:: 2025-12-13] | [pagina:: 176] | [obs:: Bem divertido, queria ver mais desse mundo que a história se passou. ]

