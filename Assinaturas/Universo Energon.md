---
Título: Assinatura Universo Energon - 14 Volumes + 30% Desc.
Editora:
  - Panini
Status: Ativa
Envio: Mensal
Parcelas: 12
Valor Original: 553.60
Desconto: 37%
Valor Total: 348.77
Valor Mensal: 29.06
Início: 2025-12-07
Início Pagamento: 2026-01
Fim Pagamento: 2026-12
Status Pagamento: Em Pagamento
Volume Inicial: 1
Volume Final Contratado: 14
Volume Atual Recebido: 7
imagem: Banco de Imagens/HQ's/Universo Energon 01 ∣ Transformers Vol. 01 - Robôs Disfarçados.webp
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
| **Parcelamento** | 12x de **R$ 29,06** *(01/2026 a 12/2026)* |
| **Valor Total Pago** | **R$ 348,77** *(desconto promocional de 30% + cupom)* |
| **Valor Médio / Volume** | **R$ 24,91** *(14 volumes)* |
| **Frequência de Envio** | Mensal |
| **Data do Pedido** | 07/12/2025 *(Corte cartão dia 06 -> 1ª parcela em 01/2026)* |
| **Volumes Contratados** | Vol. 01 ao 14 (14 volumes no total) |

---

### 📝 Observações
- Pedido Panini #2850914 realizado em 07/12/2025.
- Parcelamento em 12x de R$ 29,06 no cartão (Janeiro a Dezembro de 2026).
- ⚠️ **Ciclo Financeiro:** Quitado em Dezembro de 2026. A partir de Janeiro de 2027 a assinatura não terá mais custo mensal, permanecendo ativa no acervo apenas para o recebimento dos volumes pendentes.
- Contratados 14 volumes no total. Atualmente com 7 volumes entregues (Vol. 01 ao 07) e o **Volume 08 (Destro)** com envio pendente.
