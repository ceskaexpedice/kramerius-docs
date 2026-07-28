# Úvod 

Článek popisuje zapojení digitální knihovny K7 ddo režimu DNNT.  
Popisovaná verze: **[7.0.32](https://github.com/ceskaexpedice/kramerius/releases/tag/v7.0.32)**  
Minimální verze aprobovaná Národní knihovnou ČR pro zpřístupnění dokumentů v režimu DNNT: **7.0.29**

## Licence

Ve verzi K7 se upustilo od názvosloví `dnnt značky` a nahradili ji `licence` v obecnějším slova smyslu. Veškeré přístupy na chráněná i nechráněná díla jsou řízeny licencí.  Na základě rozhodnutí vývojového týmu se rozeznávají dva typy licencí: 

### Globální licence
Globální licence mají působnost po celé ČR a měly by být definovány a interpretovány stejně.  Všechny globální licence jsou definovány [zde](https://github.com/ceskaexpedice/kramerius/wiki/Core_Concepts_security_Licence) a jsou přítomny ve standardní distribuci krameria. Mezi globální licence patří i licence 

* [dnnto](https://github.com/ceskaexpedice/kramerius/wiki/Core_Concepts_Security_DNNT-online-licence)
* [dnntt](https://github.com/ceskaexpedice/kramerius/wiki/DNNT-termin%C3%A1lov%C3%A1-licence)

Poznámka: Od 1.1.2024 se od licence `dnntt` upustilo. Seznam DNNT již tuto licenci novým dílům nepřiřazuje a starší díla se postupně převádí na licenci `dnnto` případně se jim licence ubírá. (Pokudy bylo dílo ze seznamu vyřazeno)

### Lokální licence

Slouží k tomu aby si jednotlivé instituce mohly definovat vlastní licencea je vždy prefixovaná zkratkou knihovny.  Příklad: `knav_VIP` případně `mzk_public-muo`,`mzk_public-contract`.  

Licence jsou vidět v administračním rozhrání na následující cestě: 

**Správa oprávnění** &#8658; **Licence**

![image](https://github.com/ceskaexpedice/kramerius/assets/675753/55b6de45-19a4-4cf7-b181-50e1578ae59a)

## Příznak policy - public / private

V rámci vývojových schůzek se dohodlo, že se pro všechny instance přistupující do DNNT a ČDK **opustí příznak policy:public/private a je nahradí je lícencí**: 

 * [public](https://github.com/ceskaexpedice/kramerius/wiki/Licence-pro-d%C3%ADla-ve%C5%99ejn%C3%A1-dle-autorsk%C3%A9ho-z%C3%A1kona)
 * [onsite](https://github.com/ceskaexpedice/kramerius/wiki/Licence-pro-d%C3%ADla-dosutpn%C3%A1-pouze-v-prostor%C3%A1ch-knihovny)

Pro snadné překlopení příznaku na licence vznikl proces, který je popsán [zde](https://github.com/ceskaexpedice/kramerius/wiki/Proces-p%C5%99evodu-p%C5%99%C3%ADznaku-policy)


## Práva

Práva jsou definována obdobně jako v K5, jedná se o vazbu role, akce, dodatečné podmínky a licence.  Práva lze definovat na následující cestě:

**Správa oprávnění** &#8658; **Akce**

a pro přistup k dnnto dokumentům by situace mohla vypadat následovně: 

![image](https://github.com/ceskaexpedice/kramerius/assets/675753/e22ba7e1-cb38-4b36-8f84-28547bbfeb98)

Tedy uživatel s rolí **dnnt_users** bude schopen číst dokumenty, které budou mít licencí **dnnto**.  


_Poznámka:Název role `dnnt_users` je pouze označením a může být ve skutečnosti pojmenována libovolně. Klíčové je, aby daná role byla správně propojena s licencí._

## Logování

Logování pro NKP je dostupné na cestě: **Správa oprávnění** &#8658; **Statistiky** &#8658;  **Generování logů pro NK** &#8658;  **Generovat NKP logy**

![image](https://github.com/ceskaexpedice/kramerius/assets/675753/3e28722a-b3c6-45aa-8d75-595d500ce045)

Tlačítkem se spustí proces, který vygeneruje logy a připraví zip soubor dostupný přímo z administračního rozhraní. Na proces je možno rovněž navázat emailovou notifikaci. Pro tuto notifikaci je nutno definovat : 

- Musí být nakonigurované proměnné v souboru `mail.properties`:
   - Proměnné pro nastavení přístupu na smtp server.  Definice je popsána zde - https://docs.oracle.com/javaee/7/api/javax/mail/package-summary.html#package.description
- V souboru `configuration.properties` nasledující: 
```
nkp.logs.notification.from=emailová adresa odesílatele
nkp.logs.notification.recipients=emailové adresy příjmeců oddělené čárkami
nkp.logs.notification.subject=Předmět zprávy
nkp.logs.notification.text=Text mailu. Pro vložení nového řádku použijte escape sekvenci \n. P Pokud chcete vložit čárku, je třeba ji escapovat pomocí \, .
```      

### Zapojení do statistického modulu

Pro zapojení do statistického modulu je potřeba udělat tři kroky. 

1.  Vytvoření servisního účtu, kterým bude modul přistupovat. Postup je vidět [zde](https://github.com/ceskaexpedice/kramerius/wiki/Servisn%C3%AD-%C3%BA%C4%8Dty-v-keycloaku) 
2.  Přiřadit roli servisnímu účtu. Například: **pristup_do_statistik**
3.  V administračník rozhraní řiřadit akci  **Export statistik**
  
![image](https://github.com/user-attachments/assets/fc626f4f-7ad7-4659-9a96-0192045f3788)


Struktura logů odpovídá původnímu formátu definovanému [zde](https://github.com/ceskaexpedice/kramerius/wiki/DNNT-%E2%80%90-K5#logov%C3%A1n%C3%AD)

## Synchronizace s aplikací SDNNT

Synchronizace se seznamem je podobná jako v K5 verzi. V aplikaci je možné ji nalézt kliknutím na **Repozitář** &#8658; **Hromadné úpravy** &#8658;  ** &#8658;  **Spustit proces kontroly SDNNT/Kramerius** 


![image](https://github.com/ceskaexpedice/kramerius/assets/675753/cab4f366-dda6-483a-a5e9-a3bc9d42fc7f)

Výsledkem je opětovný dialogový okno rozdílů mezi seznamem DNNT a konkrétní instancí Krameria. Tento dialog je dostupný pomocí tlačítka  **Zobrazit výsledek procesu**

![image](https://github.com/ceskaexpedice/kramerius/assets/675753/240b2673-1bbb-4f06-82b6-0ef4453bdf03)

## eduid.cz/Keycloak


V digitální knihovně K7 se pro autentizaci používá systém Keycloak, který je nutné integrovat do federace eduid.cz. Standardní distribuce Keycloaku tuto funkcionalitu nenabízí, a proto je používán upravený fork dostupný na adrese https://github.com/eosc-kc/keycloak. Plný popis instalace je vidět [zde](https://github.com/ceskaexpedice/kramerius/wiki/Guides_Security_Keycloak-a-eduID).

 
### Nastavení atributů pro keycloak

Atributy přebíráné z federace se definují přímo na federaci pomocí cesty:
**Kramerius(realm)** &#8658; **SAML Federation** &#8658;   **eduid** ** &#8658;  **Mappers** 

![image](https://github.com/ceskaexpedice/kramerius/assets/675753/2f0d6311-383b-46d6-8e28-b4e800a61ef5)


První atribut uvedu screenshotem, ostatní pouze výčtem: 
![image](https://github.com/ceskaexpedice/kramerius/assets/675753/df8a1248-daa5-4c30-b6c6-7bb19f24427f)

Stejně tak je třeba nadefinovat následující parametry: 

1. `Name = cn, Attribute Name = urn:oid:2.5.4.3, Friendly name = cn`
1. `Name = displayName, Attribute Name = urn:oid:2.16.840.1.113730.3.1.241, Friendly name = displayName `
1. `Name = schacHomeOrganization, Attribute Name = urn:oid:1.3.6.1.4.1.25178.1.2.9, Friendly name = schacHomeOrganization`
1. `Name = eduPersonScopedAffiliation, Attribute Name = urn:oid:1.3.6.1.4.1.5923.1.1.1.9, Friendly name = eduPersonScopedAffiliation`
1. `Name = eduPersonUniqueId, Attribute Name = urn:oid:1.3.6.1.4.1.5923.1.1.1.13, Friendly name = eduPersonUniqueId`
1. `Name = email importer, Attribute Name = urn:oid:0.9.2342.19200300.100.1.3, Friendly name = mail`
1. `Name = eduPersonPrincipalName, Attribute Name = urn:oid:1.3.6.1.4.1.5923.1.1.1.6, Friendly name = eduPersonPrincipalName`
1. `Name = eduPersonEntitlement, Attribute Name = urn:oid:1.3.6.1.4.1.5923.1.1.1.7, Friendly name = eduPersonEntitlement`
1. `Name = firstname importer, Attribute Name = urn:oid:2.5.4.42, Friendly name = givenName`
1. `Name = lastname importer, Attribute Name = urn:oid:2.5.4.4, Friendly name = sn`
1. `Name =username importer, Mapper type = Username Template Importer, Template= ${ALIAS}.${NAMEID}, Target=BROKER_USERNAME`
1. `Name =DNNTUser mapper, Mapper type = Advanced Attribute to role, Syncmode=force`
```
key:eduPersonScopedAffiliation, value:member.*
key:eduPersonEntitlement, value:urn:mace:dir:entitlement:common-lib-terms
```   
13. `Name =DNNTUsersMapper_CUNI, Mapper type = Advanced Attribute to role, Syncmode=force`
```
key:eduPersonScopedAffiliation, value:library-walk-in.*
key:eduPersonEntitlement, value:urn:mace:dir:entitlement:common-lib-terms
```   


Tyto atributy se projevují ve všech přihlášených uživatelích přes federace a jdou vidět přímo v keycloaku: 

![image](https://github.com/ceskaexpedice/kramerius/assets/675753/dd357653-c8f2-43d8-8fcb-a6f54de00497)

a pokud jsou správně nastavené mappery na role, je vidět u přihlášeného uživatele i role `dnnt_users`

![image](https://github.com/ceskaexpedice/kramerius/assets/675753/e77f376e-2fc5-4152-938b-8a107e2323eb)



Pro správnou propagaci do NKP logů je ještě nutné zajistit, aby se atributy přenášely společně s přístupovým JWT tokenem. To je zajištěno pomocí nastavení: 


**Kramerius(realm)** &#8658; **Clients(krameriusClient)** &#8658;  **Mappers** 

![image](https://github.com/ceskaexpedice/kramerius/assets/675753/dcca7cf8-e95a-4d06-8e87-b09a8adcbdef)


Jedná se pouze kopírování atributů uživatele: 

![image](https://github.com/ceskaexpedice/kramerius/assets/675753/ae80a9ad-44ba-4ca0-bdf4-94de9f264f44)

Do JWT tokenu => Všechny atributu co máme k uživateli aby se projevili i přístupovém JWT tokenu :

![image](https://github.com/ceskaexpedice/kramerius/assets/675753/d5ee38a6-c97c-462b-bc11-95e36a0e66aa)



