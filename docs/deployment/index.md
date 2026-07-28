# 🚢 Deployment

Tato kapitola popisuje **způsoby nasazení (deploymentu) systému Kramerius**.  
Kramerius je modulární systém a lze jej provozovat v různých prostředích podle velikosti instance, provozních požadavků a zkušeností provozovatele.

---

## Docker Compose

Pro zjednodušení instalace a provozu je k dispozici projekt **Kramerius Docker Compose**, který obsahuje všechny potřebné komponenty již kontejnerizované.

Charakteristiky:
- rychlé spuštění
- jednotné prostředí
- vhodné pro vývoj i produkční provoz menších a středních instancí
- nižší nároky na znalost infrastruktury

Typicky postačuje:
- nainstalovaný Docker
- nainstalovaný Docker Compose
- spuštění celé instance jedním příkazem

➡️ [Docker Compose](docker/index.md)

---

## Kubernetes

Pro velké nebo kritické instalace lze Kramerius provozovat v prostředí **Kubernetes**.

Tento způsob umožňuje:
- vysokou dostupnost
- horizontální škálování
- oddělení jednotlivých komponent
- integraci s existující cloudovou infrastrukturou

Je určen především pro:
- národní nebo centrální digitální knihovny
- instance s velmi velkým objemem dat
- provozní týmy se zkušeností s Kubernetes

➡️ [Kubernetes](kubernetes/index.md)

---

## On-premise (klasická instalace)

On-premise deployment znamená provoz Krameria jako sady samostatných služeb instalovaných přímo na server (nebo servery).

Typicky zahrnuje:
- Java (JDK)
- Apache Tomcat
- Kramerius jádro (search.war)
- SOLR
- Další podpůrné služby (Keycloak, databáze apod.)

Tento způsob poskytuje **maximální kontrolu nad prostředím**, ale vyžaduje více manuální konfigurace a správy.

➡️ [On Premise](on-premise/index.md)

---

## Jak zvolit správný způsob nasazení

Obecné doporučení:

- **Vývoj / testování** → Docker Compose
- **Menší produkční instance** → Docker Compose nebo On-premise
- **Velké produkční instance** → Kubernetes

Detailní požadavky (velikost indexu, dostupnost, bezpečnost, zálohování) jsou popsány v jednotlivých guidech.

---

## Navazujici dokumentace

- ➡️ [Architektura](../architecture/index.md)
- ➡️ [Reference](../reference/index.md)
- ➡️ [Navody](../guides/index.md)
