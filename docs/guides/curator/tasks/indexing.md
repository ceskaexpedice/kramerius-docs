[Úvod](../../../index.md) > [Návody](../../../guides/index.md) / [Kurátor](../../curator/index.md) / [Úlohy](index.md)

# Spuštění indexace

Indexace převádí importovaná data do vyhledávací vrstvy systému Kramerius.

Indexace je buď:

- spuštěna automaticky po importu
- nebo spuštěna ručně

---

## Předpoklady

- data byla úspěšně importována
- existuje běžící nebo dokončený importní proces

---

## Postup spuštění

1. Otevřete **Admin klienta**
2. Přejděte do sekce **Procesy**

   ![Processes menu](../../images/processes-menu.png)

3. Vyberte importní proces

4. Klikněte na **Spustit indexaci**

---

## Typy indexace

### Kompletní indexace
- indexuje všechny kořenové dokumenty

### Částečná indexace
- indexuje pouze nové dokumenty
- doplňuje předky dle struktury

---

## Co se děje po spuštění

- indexace běží asynchronně
- lze sledovat stav v seznamu procesů
- výsledky se projeví ve vyhledávání

---

## Ověření výsledku

- dokument je viditelný ve vyhledávání
- proces indexace je ve stavu `DONE`

---

## Související

