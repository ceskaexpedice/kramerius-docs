# DevOps – build, CI/CD a vývojové nástroje

Tato stránka popisuje technické nástroje a automatizace používané při vývoji, buildu a dodávce systému Kramerius a souvisejících komponent
(process platform, workery, backend služby).

---

## Build systém

Pro build systému používáme **Gradle**.

Gradle zajišťuje:

- sestavení backend modulů (JAR/WAR aplikace)
- spuštění testů
- generování artefaktů pro release
- build workerů pro process platform
- správu multi-module struktury projektu

Build je rozdělen do více modulů podle komponent systému (core, API, workers).

---

## CI/CD

CI/CD je realizováno pomocí GitHub Actions.

Typické kroky pipeline:

- build projektu při pushi a pull requestech
- spuštění unit a integračních testů
- statická analýza kódu
- generování artefaktů
- publikace release buildů

Pipeline jsou definovány v repozitáři v adresáři `.github/workflows`.

---

## Build process platform workerů

Součástí systému Kramerius je **process platform**, která využívá samostatné worker aplikace.

Charakteristika:

- každý worker reprezentuje jeden typ procesu
- workery jsou buildovány jako samostatné JVM aplikace
- build je řízen přes Gradle pluginy
- výsledkem je distribuovatelný JAR balíček

Tato část popisuje pouze build pohled, nikoliv runtime architekturu.

---

## REST API

Backend služby poskytují REST API dokumentované pomocí OpenAPI (Swagger).

Používáme Swagger pro:

- generování API dokumentace
- definici kontraktů mezi backendem a klienty
- validaci API specifikace

Dostupné výstupy:

- Swagger UI
- OpenAPI JSON/YAML specifikace
- případně generované klientské knihovny

---

## Vyhledávání (Solr)

Vyhledávací vrstva systému je postavena na Apache Solr.

DevOps část zahrnuje:

- správu Solr schema
- verzování indexových definic
- nasazení Solr core / collections
- reindexace při změnách datového modelu

---

## Artefakty

Výstupem build procesu jsou různé typy artefaktů:

- backend aplikace (JAR / WAR)
- worker balíčky
- konfigurační balíčky
- Solr schema a indexové konfigurace

Artefakty jsou publikovány prostřednictvím CI pipeline (GitHub Actions).

---


## Shrnutí

DevOps část popisuje:

> jak se systém Kramerius sestavuje, testuje a dostává do releasů

Neřeší runtime chování ani detailní konfiguraci prostředí.

## Navazujici dokumentace

- ➡️ [Zakladni pojmy](../../core-concepts/index.md)
- ➡️ [Architektura](../../architecture/index.md)
- ➡️ [Konfigurace](../../configuration/index.md)
- ➡️ [Verzovani](../../versioning/index.md)
