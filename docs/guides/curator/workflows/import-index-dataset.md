[Úvod](../../../index.md) > [Návody](../../../guides/index.md) / [Kurátor](../../curator/index.md) / [Pracovní postupy](../../curator/workflows/index.md) 

# Zpracování nové dávky (Import + indexace)

Tento workflow popisuje kompletní zpracování nové digitální dávky od jejího importu až po indexaci v systému Kramerius.

Workflow se skládá ze dvou navazujících kroků:

1. Import dat
2. Indexace dat

Oba kroky jsou spouštěny v Admin klientu a běží asynchronně.

---

## Přehled procesu

![Diagram](assets/import-index-dataset.png)


---

## 1. [Import](../tasks/import.md)

Import je vstupní krok, který načte data z importního adresáře definovaného v konfiguraci systému.

## 2. [Indexace](../tasks/indexing.md)

Po úspěšném importu následuje indexace dat do vyhledávacího systému.

---

## Jak poznám, že workflow proběhlo správně?

- importní proces skončí bez chyby
- indexace dokončena
- dokument je dostupný ve vyhledávání

---

## Co dělat při problému

- import selhal → viz Troubleshooting
- indexace neběží → viz Troubleshooting
- dokument se nezobrazuje → viz Troubleshooting

➡️ [Řešení problémů](../troubleshooting/index.md)

---

## Související dokumentace

- ➡️ ...
- ➡️ 
