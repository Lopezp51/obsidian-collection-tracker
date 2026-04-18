---
Processado em: 2025-11-24
Situação: Completo
Data de Entrega: 2025-12-16
Chegou: true
Status de Leitura: Lido
Vezes que Li: 1
Páginas: 416
valor: 57.9
Favorito: true
Avaliação: 5
imagem: Banco de Imagens/HQ's/Watchmen (DC de Bolso).jpg
Tipo: Quadrinho
Última Leitura: 2025-12-10
Data de Publicação: 2024-09-01
Universo: DC
Nexo:
  - Quadrinho
  - DC de Bolso
  - Panini
  - Watchmen
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
> - [data:: 2025-12-05] | [pagina:: 74] | [obs:: Pô ta abordando alguns temas mais pesados mesmos, li por enquanto só as duas primeiras partes, estranho pensar que isso foi publicado quando não tinha esse estilo de história, parece algo mais comum que eu veria hoje em dia. E eu lembro que do filme eu gostava muito do Rorschach, lendo aqui eu to odiando ele, pelo jeito que ele se porta.]
> - [data:: 2025-12-06] | [pagina:: 96] | [obs:: ]
> - [data:: 2025-12-07] | [pagina:: 142] | [obs:: ]
> - [data:: 2025-12-08] | [pagina:: 210] | [obs:: Caraca os ultimos caítulos foram inscríveis velho, até então eu tava intrigado só lendo, mas agora me fisco de jeito.]
> - [data:: 2025-12-09] | [pagina:: 244] | [obs:: ]
> - [data:: 2025-12-10] | [pagina:: 416] | [obs:: Fiquei em choque com o final da parte 11, foi muito forte aquela imagem e o peso dos dos personagens que acompanhamos o quadrinho inteiro vivendo suas vidas foi me pegou muito. O plano do Ozymandias achei sensanioal e o final e a obra como um todo foi incrível.]