Tento návod popisuje základní vývojové nastavení Keycloaku pro použití s Krameriem.

Předpoklady
běžící instance Krameria, Java runtime, lokální vývojové prostředí

1. Stažení a spuštění Keycloaku
... viz deployment on-premise 
   Stáhněte distribuční balíček Keycloaku a rozbalte jej.
   Spusťte server s port offsetem, aby nedošlo ke kolizi s Krameriem:
   Keycloak poběží na portu 8083
   je povolena možnost nahrání skriptů do realmu
 
2. Inicializace administrátorského účtu
   Po prvním spuštění:
   otevřete administrační rozhraní Keycloaku
   vytvořte administrátorský účet
   přihlaste se do admin konzole

3. Konfigurace realmu a klienta
   V administrační konzoli:
   vytvořte realm kramerius
   vytvořte klient krameriusClient
   doporučený typ: public (client authentication disabled)

4. Uživatelé a role
   Vytvořte následující role:
   common_users
   public_users
   kramerius_admin
   k4_admins
   Vytvořte uživatele (např. krameriusAdmin) a přiřaďte jim odpovídající role.
   Volitelně lze nakonfigurovat externí identity providery (Shibboleth, Facebook, …).

5. Použití token proxy endpointu
   Kramerius poskytuje endpoint pro získání access tokenu:
   URL: search/api/auth/token
   metoda: POST

V těle požadavku jsou předány přihlašovací údaje uživatele.
