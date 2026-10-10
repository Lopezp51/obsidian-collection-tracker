---
Título: Assinatura A Saga Da Mulher Maravilha - 6 Meses + 10% Desc.
Editora:
  - Panini
Status: Concluída
Envio: Bimestral
Parcelas: 3
Valor Original: 137.70
Desconto: 19%
Valor Total: 111.54
Valor Mensal: 37.18
Início: 2026-01-07
Término: 2026-05-13
Volume Inicial: 10
Volume Final Contratado: 12
Volume Atual Recebido: 12
imagem: Banco de Imagens/HQ's/A Saga da Mulher-Maravilha Vol. 10.webp
tags:
  - Assinatura
---

> [!bookbox]
> ```meta-bind
> INPUT[imageSuggester(optionQuery("")):imagem]
> ```
> <div class="book-metadata">
>
> **Status:** `$= dv.current()?.Status || "Concluída"` &nbsp;|&nbsp; **Editora:** `$= (Array.isArray(dv.current()?.Editora) ? dv.current()?.Editora.join(", ") : dv.current()?.Editora) || "Panini"`
>
> ```dataviewjs
> const ini = dv.current()?.["Volume Inicial"] || 1;
> const fim = dv.current()?.["Volume Final Contratado"] || 1;
> const atual = dv.current()?.["Volume Atual Recebido"] || 0;
> const total = (fim - ini + 1) || 1;
> const recebidos = atual === 0 ? 0 : Math.min(total, Math.max(0, atual - ini + 1));
> const pct = Math.min(100, Math.round((recebidos / total) * 100));
> const corGradiente = dv.current()?.Status === "Concluída" ? "linear-gradient(90deg, #3b82f6, #1d4ed8)" : "linear-gradient(90deg, #10b981, #059669)";
> 
> const htmlBar = `
> <div style="width: 100%; background-color: var(--background-modifier-border); border-radius: 10px; height: 18px; margin-top: 6px; overflow: hidden; position: relative; border: 1px solid rgba(0,0,0,0.1);">
>     <div style="width: ${pct}%; background: ${corGradiente}; height: 100%; transition: width 0.5s ease;"></div>
>     <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: bold; color: white; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">
>         ${pct}% (Concluída)
>     </div>
> </div>
> <div style="text-align: center; font-size: 0.85em; margin-top: 4px; color: var(--text-muted);">
>     Recebidos todos os <b>${total}</b> volumes contratados (Vol. ${ini} ao ${fim})
> </div>
> `;
> 
> dv.span(htmlBar);
> ```
> 
> </div>

### 💳 Dados Financeiros e Envio

| Informação | Detalhe |
| :--- | :--- |
| **Valor Base por Volume** | **R$ 41,31** *(com 10% de desc. sobre tabela)* |
| **Valor Final Pago por Edição** | **R$ 37,18** *(com desconto adicional no checkout)* |
| **Valor Total Pago** | **R$ 111,54** *(Preço do pacote: R$ 123,93)* |
| **Frequência de Envio** | Bimestral (Plano de 6 Meses) |
| **Período de Envio** | 07/01/2026 a 13/05/2026 |
| **Volumes Contratados** | Vol. 10 ao 12 (3 volumes no total) |

---

### 📝 Observações
- Pedido Panini #2851083 / #009024133 de 07/12/2025.
- Contrato de 3 volumes bimestrais finalizado com 100% das entregas concluídas.
