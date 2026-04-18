---
Processado em: 2026-01-19
Situação: Finalizado
Data de Entrega: 2026-01-23
Chegou: true
Status de Leitura: Não Iniciado
Vezes que Li: 0
Páginas: 184
valor: 54.47
Favorito: false
Avaliação: 0
imagem: Banco de Imagens/HQ's/Homem De Ferro - O Demônio Na Garrafa (Marvel Essenciais).webp
Tipo: Quadrinho
Última Leitura:
Data de Publicação: 2025-10-15
Universo: Marvel
---

> [!bookbox]
> ```meta-bind
>INPUT[imageSuggester(optionQuery("")):imagem]
>```
> <div class="book-metadata">
>
> **Status:** `$= dv.current()["Status de Leitura"]`
> **Páginas:** `$= dv.current()["Páginas"]`
> **Universo:** `$= dv.current()["Universo"]`
> **Avaliação:** ⭐ `$= dv.current()["Avaliação"]`/5
> **Progresso:**
> ```dataviewjs
> const total = dv.current()["Páginas"] || 1;
> const listaItens = dv.current().file.lists;
> const progresso = listaItens.where(i => i.pagina != null).map(i => Number(i.pagina));
> let atual = 0;
> if (progresso.length > 0) { atual = Math.max(...progresso); }
> const pct = Math.min(100, Math.round((atual / total) * 100));
> 
> const htmlBar = `
> <div style="width: 100%; background-color: var(--background-modifier-border); border-radius: 10px; height: 20px; margin-top: 5px; overflow: hidden; position: relative;">
>     <div style="width: ${pct}%; background-color: var(--interactive-accent); height: 100%; border-radius: 0px; transition: width 0.5s ease;"></div>
>     <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: bold; color: var(--text-on-accent); text-shadow: 0px 0px 3px rgba(0,0,0,0.5);">
>         ${pct}%
>     </div>
> </div>
> <div style="text-align: center; font-size: 0.9em; margin-top: 4px; color: var(--text-muted);">
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
