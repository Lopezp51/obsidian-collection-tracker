---
Título: "Assinatura Absolute Caçador De Marte - 12 Meses + 20% Desc."
Editora:
  - Panini
Status: Ativa
Envio: Bimestral
Parcelas: 12
Valor Original: 144.40
Desconto: 28%
Valor Total: 103.97
Valor Mensal: 8.66
Início: 2026-01-13
Início Pagamento: 2026-02
Fim Pagamento: 2027-01
Status Pagamento: Em Pagamento
Volume Inicial: 1
Volume Final Contratado: 6
Volume Atual Recebido: 5
imagem: Banco de Imagens/HQ's/Absolute Caçador De Marte 01.webp
tags:
  - Assinatura
---

> [!bookbox]
> ```meta-bind
> INPUT[imageSuggester(optionQuery("")):imagem]
> ```
> <div class="book-metadata">
>
> **Status:** `$= dv.current()?.Status || "Ativa"` &nbsp;|&nbsp; **Editora:** `$= (Array.isArray(dv.current()?.Editora) ? dv.current()?.Editora.join(", ") : dv.current()?.Editora) || "Panini"`
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
>         ${pct}%
>     </div>
> </div>
> <div style="text-align: center; font-size: 0.85em; margin-top: 4px; color: var(--text-muted);">
>     Recebidos <b>${recebidos}</b> de <b>${total}</b> volumes contratados (Vol. ${ini} ao ${fim})
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
| **Parcelamento** | 12x de **R$ 8,66** |
| **Valor Total** | **R$ 103,97** *(desconto sobre R$ 144,40 - Pedido #2895413)* |
| **Frequência de Envio** | Bimestral |
| **Início dos Envios** | 13/01/2026 |
| **Volumes Contratados** | Vol. 01 ao 06 (6 volumes no total) |

---

### 📝 Observações
- Pedido Panini #2895413 realizado em 13/01/2026.
- Assinatura de 12 meses com periodicidade bimestral contemplando os volumes 01 ao 06.
- ⚠️ **Edição 06 pendente de envio / entrega.** Volumes 01 ao 05 recebidos com sucesso.
