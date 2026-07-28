# Solr cloud

Kramerius 7 umožňuje provozovat vyhledávací databázi v prostředí solr cloud.  Rozdíl mezi standardním solrem a solr cloud řešením je v možnosti "rozbít" kolekci na více částí - **shardů** a tím pak umožnit přiměřenou odezvu solru i při větším počtu dokumentů. Rozhodnutí o tom co zvolit bude vždy záležet na velikosti instance. Standardně se doporučuje velikost **standardní** instance do 15O GB dat na disku. 

Pro inspiraci uvádím tabulku instancí, kde je použitý solr cloud

| Organizace | Počet dokumentů | Počet shardů |
|------------|-----------------|--------------|
| CDK        | 72 milionů      | 5 shardů     |
| SNK        | 57 milionů      | 5 shardů     |


Pro použití v K7 je nutno povolit konfigurační proměnnou `solrSearch.useCompositeId=true`.  Proměnná instruuje indexer aby použil složený identifikátor při indexaci **composteId** a tím docílíl to, že dokuenty patřící významově k sobě (periodikum a ročníky periodika, výtisky, stránky, atd..) budou vždy ležet na stejném shardu. 


