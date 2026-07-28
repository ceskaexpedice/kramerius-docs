[Úvod](../../index.md) > [Konfigurace](../../configuration/index.md)

# Image server

Podpora protokolu IIIF, který je používán klientem Krameria pro funkci výřezů, vyžaduje instalaci imageserveru (balíček od MZK) verze `1.1`. 

U instancí, kde není použit Docker a místo NGINXe Apache, je potřeba nakonfigurovat následující (příklad v příslušném virtuálu):

```
...
    ScriptAlias "/cgi-bin/" "/usr/lib/cgi-bin/"
    ScriptAlias "/fcgi-bin/" "/usr/lib/cgi-bin/"

    <Directory "/usr/lib/cgi-bin">
        AllowOverride None
        Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
        <RequireAll>
            <RequireAny>
                Require ip 127.0.0.0/8
                Require host localhost
            </RequireAny>
        </RequireAll>
    </Directory>
        
    <IfModule mod_fcgid.c>
        <IfModule mod_mime.c>
            AddHandler fcgid-script .fcgi
        </IfModule>
        FcgidInitialEnv LOGFILE "/var/log/iipsrv/iipsrv.log"
        FcgidInitialEnv VERBOSITY "2"
        FcgidInitialEnv JPEG_QUALITY "80"
        FcgidInitialEnv MAX_IMAGE_CACHE_SIZE "16"
        FcgidInitialEnv MAX_LAYERS "-1"
        FcgidInitialEnv MAX_CVT "4000"
#       FcgidInitialEnv ALLOW_UPSCALING 0
#       FcgidInitialEnv KAKADU_READMODE 2
#       FcgidInitialEnv INTERPOLATION 1
#       FcgidInitialEnv MEMCACHED_SERVERS=127.0.0.1:11211
#       FcgidInitialEnv MEMCACHED_TIMEOUT=1800
        FcgidIdleTimeout 0
        FcgidMaxProcessesPerClass 4
    </IfModule>
...

    <IfModule mod_rewrite.c>
        RewriteEngine On
        LogLevel alert rewrite:trace1
    
        RewriteCond %{QUERY_STRING} ^Zoomify=([a-zA-Z0-9_\/\.\-]+)\/([a-zA-Z0-9\.\,\:]+)/([a-zA-Z0-9\.\,\:\!]+)/([0-9\.\!]+)/([a-zA-Z0-9]+).jpg$
        RewriteRule ^/cgi-bin/iipsrv.fcgi http://%{HTTP_HOST}/cgi-bin/iipsrv.fcgi?IIIF=%1/%2/%3/%4/native.jpg [L]
        
    </IfModule>

...
```
Klíčová jsou přepisovací pravidla v konfiguraci `mod_rewrite`.

V okamžiku, kdy uživatel provede výřez, přijde na server request z klienta, například:
```
"GET /search/iiif/uuid:d7d7cae6-4eed-11e9-8962-005056a2b051/1865,4099,736,418/full/0/default.jpg HTTP/1.1"
```
Ten je jádrem Krameria přepsán na:
```
"GET /cgi-bin/iipsrv.fcgi?Zoomify=/home/kramerius/image-server-root/2019/03/25/klg001-0000mj/UC_klg001-0000mj_0001.jp2/1602,3139,1531,1103/full/0/default.jpg HTTP/1.1"
```
Ten je dále přepsán pomocí výše uvedených pravidel na:
```
"GET /cgi-bin/iipsrv.fcgi?IIIF=/home/kramerius/image-server-root/2019/03/25/klg001-0000mj/UC_klg001-0000mj_0001.jp2/1602,3139,1531,1103/full/0/native.jpg HTTP/1.1"
```
a výřez to úspěšně vrátí.

Při ladění se zjistilo, že verze imageserveru, kterou máme nasazenou, nerozumí nastavení parametru kvality `default.jpg`, ale vyžaduje to přepsat na `native.jpg`. Jinak imageserver vrací status `400`:

![img-400-01](https://user-images.githubusercontent.com/8750622/67214337-df5ba700-f41f-11e9-9eaf-0c5fc06a2667.png)

![img-200-01](https://user-images.githubusercontent.com/8750622/67215146-429a0900-f421-11e9-9144-464f9a55aeb6.png)


