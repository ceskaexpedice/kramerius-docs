# IIIF

Kromě standardního zobrazení obrázků v jejich nativním formátu má aplikace Kramerius 5 možnost prezentovat je pomocí integrované prohlížečky Seadragon (http://www.zoom.it).
Prohlížečka Seadragon je aktivována pro konkrétní zobrazovaný digitální objekt (například stránku monografie), 
pokud jeho FOXML definice obsahuje v datastreamu RELS-EXT RDF literál `<kramerius4:tiles-url>`.  Je možno využít dvě alternativy:

Využít produkt IIP server (https://web.archive.org/web/20190226234031/https://help.oldmapsonline.org/jpeg2000)

➡️ [Konfigurace image serveru](image-server.md)

Zde slouží Kramerius jako prostředník. Klientské dotazy na jednotlivé dlaždice přeposílá IIP serveru a sám se stará pouze o autorizaci požadavku. Hodnotou literálu `<kramerius4:tiles-url>` je přímo URL na zoomovaný obrázek v IIP serveru.

Příklady definic v RELS-EXT:

```
<kramerius4:tiles-url>http://192.168.1.1/fcgi-bin/iipsrv.fcgi?DeepZoom=/mzk03/001/042/654/2619265924.jp2</kramerius4:tiles>

<kramerius4:tiles-url>http://imageserver.mzk.cz/mzk03/001/066/607/2619320306/1</kramerius4:tiles-url>

<kramerius4:tiles-url>http://iipserv.nkp.cz/fcgi-bin/iipsrv.fcgi?Zoomify=/home/k4/iip-data/2619265924.jp2</kramerius4:tiles-url>

```

## Navazujici dokumentace

- ➡️ [Reference](../../reference/image-server/index.md)
