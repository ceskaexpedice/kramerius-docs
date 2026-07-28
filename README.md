# Kramerius – dokumentace

Zdrojové texty produktové a technické dokumentace systému Kramerius. Stránky jsou napsané v Markdownu, MkDocs je sestavuje do statického webu a téma MkDocs Material zajišťuje vzhled, navigaci, vyhledávání a světlý/tmavý režim.

## Struktura projektu

- `mkdocs.yml` obsahuje konfiguraci webu a hlavní navigaci.
- `docs/` obsahuje zdrojové Markdown stránky a statické soubory.
- `requirements.txt` připíná verzi MkDocs Material pro lokální i automatické sestavení.
- `.github/workflows/publish-pages.yml` publikuje web do větve `gh-pages`.

Navigace je definovaná v sekci `nav` souboru `mkdocs.yml`. Detailní stránky jsou dostupné z rozcestníků jednotlivých hlavních sekcí.

## Lokální spuštění ve Windows 11

Požadavkem je nainstalovaný Python 3. V PowerShellu spusťte z kořenové složky repozitáře:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install --requirement requirements.txt
python -m mkdocs serve
```

Vývojový server bude dostupný na adrese [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Při změně konfigurace nebo souborů v `docs/` MkDocs web automaticky znovu sestaví. Server ukončíte klávesami `Ctrl+C`.

Při dalších spuštěních stačí virtuální prostředí aktivovat a spustit server:

```powershell
.\.venv\Scripts\Activate.ps1
python -m mkdocs serve
```

Pokud PowerShell nepovolí aktivační skript, lze příkazy spouštět přímo přes Python ve virtuálním prostředí:

```powershell
.\.venv\Scripts\python.exe -m pip install --requirement requirements.txt
.\.venv\Scripts\python.exe -m mkdocs serve
```

## Kontrola sestavení

Produkční web lze lokálně sestavit příkazem:

```powershell
python -m mkdocs build
```

Výstup vznikne ve složce `site/`.

## Přidání stránky

1. Vytvořte Markdown soubor ve složce `docs/`.
2. Přidejte na něj odkaz do odpovídajícího rozcestníku.
3. Pokud má být dostupný přímo z hlavního menu, přidejte ho také do sekce `nav` v `mkdocs.yml`.
4. Spusťte `python -m mkdocs serve` a stránku zkontrolujte.

## Publikování na GitHub Pages

Workflow se spustí automaticky po pushi do větve `main`. Ručně ho lze spustit také na kartě **Actions** výběrem workflow **Publish documentation to GitHub Pages**.

Před prvním publikováním nastavte v repozitáři **Settings → Pages → Build and deployment → Deploy from a branch**, vyberte větev `gh-pages` a složku `/(root)`. Větev `gh-pages` vytvoří workflow při prvním úspěšném běhu.

Zdrojové soubory upravujte pouze ve větvi `main`; obsah větve `gh-pages` je automaticky generovaný a nemá se editovat ručně.
