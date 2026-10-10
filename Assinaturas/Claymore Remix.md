---
Editora:
  - Panini
Status: Ativa
Envio: Bimestral
Parcelas: 12
Valor Original: 479.52
Desconto: 46%
Valor Total: 432.12
Valor Mensal: 36.01
Início: 2026-08-31
Início Pagamento: 2026-09
Fim Pagamento: 2027-08
Status Pagamento: Em Pagamento
Volume Inicial: 1
Volume Final Contratado: 8
Volume Atual Recebido: 1
imagem: Banco de Imagens/Mangas/Claymore Remix 01.webp
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
> const pct = Math.min(100, Math.round((atual / total) * 100));
> 
> const htmlBar = `
> <div style="width: 100%; background-color: var(--background-modifier-border); border-radius: 10px; height: 18px; margin-top: 6px; overflow: hidden; position: relative; border: 1px solid rgba(0,0,0,0.1);">
>     <div style="width: ${pct}%; background: linear-gradient(90deg, #10b981, #059669); height: 100%; transition: width 0.5s ease;"></div>
>     <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: bold; color: white; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">
>         ${pct}%
>     </div>
> </div>
> <div style="text-align: center; font-size: 0.85em; margin-top: 4px; color: var(--text-muted);">
>     Recebidos <b>${atual}</b> de <b>${total}</b> volumes contratados (Vol. ${ini} ao ${fim})
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
| **Parcelamento** | 12x de **R$ 36,01** |
| **Valor Total** | **R$ 432,12** *(desconto sobre R$ 799,20)* |
| **Frequência de Envio** | Bimestral |
| **Início dos Envios** | 31/10/2026 |
| **Volumes Contratados** | 8 volumes (Coleção Completa) |

---

### 📝 Observações
- Assinatura promocional com ~46% de desconto no pacote completo.
