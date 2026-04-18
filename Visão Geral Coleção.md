
### Gastos por Mês
```dataview
TABLE WITHOUT ID
    dateformat(rows[0]["Processado em"], "MM/yyyy") as "Mês",
    "R$ " + round(sum(rows.valor), 2) as "Total Gasto", 
    length(rows) as "Qtd Itens"
WHERE valor != null
GROUP BY dateformat(row["Processado em"], "yyyy-MM")
SORT key desc
```

