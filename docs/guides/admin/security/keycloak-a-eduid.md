K rozjetí eduID federace je potřeba použít [fork Keycloaku](https://github.com/eosc-kc/keycloak) verze 18 (verze 22 ještě nebyla testována) vyvíjeným EOSC. Dole jsou zmíněny připadné problémy a řešení související s EOSC Keycloakem a eduID.

Jak rozjet:
1. Nainstalovat nejnovější [release](https://github.com/eosc-kc/keycloak/releases) (nejlépe od verze [18.0.1-2.17) a nainstalovat s přihlašovacím motivem vytvořeným MZK. Release motivu je možno získat [zde](https://github.com/ceskaexpedice/keycloak-kramerius-theme/releases/tag/7.0.32) 


2. Rozjet Keycloak příkazem `kc.sh --verbose start`. Další přidatné konfigurace Keycloaku jsou popsány [zde](https://www.keycloak.org/server/configuration). Keycloak běží na výchozím portu 8080.

Jak nakonfigurovat s eduID:
1. Udělat potřebné kroky 3 a 4 dle návodu popsány na této [stránce](https://github.com/ceskaexpedice/kramerius/wiki/DEL_SEC_K7_Keycloak).
2. Přidat v realmu `kramerius` `cs` a `en` locale v `Realm settings` -> `Themes` -> `Supported Locales`
3. Povolit v realmu `kramerius` duplikátní maily uživatelů `Realm settings` -> `Login` -> `Duplicate emails`
4. V Keycloak konzoli v realmu `kramerius` přidat novou federaci v modulu `SAML federation` -> `Add federation` -> `SAML v2.0 federation`

| SAML federation   ||
|---|---|
| Alias | eduid |
| Import from (ČDK filtr) | 	https://raw.githubusercontent.com/moravianlibrary/cdk-idp-list/main/idp.xml |
| Update frequency | 720 (6 hours) |
| Category | Identity providers |

### Identity Providers federation config

| Name | Option
|---|---|
| Sync Mode | force
| NameID Policy Format | Transient 

#### Principals

| Principal Type | Attribute 
|---|---|
| Attribute \[Name\] | urn:oid:1.3.6.1.4.1.5923.1.1.1.13 |

nebo přes POST na API endpoint `/admin/realms/kramerius/saml-federations/instances` s JSONem
```
{
        'providerId': 'saml',
        'entityIdDenyList': [],
        'entityIdAllowList': [],
        'registrationAuthorityDenyList': [],
        'registrationAuthorityAllowList': [],
        'categoryAllowList': {},
        'category': 'Identity Providers',
        'categoryDenyList': {},
        'config': {
            'nameIDPolicyFormat': 'urn:oasis:names:tc:SAML:2.0:nameid-format:transient',
            'principalType': 'SUBJECT',
            'postBindingResponse': 'true',
            'xsltOverride': '',
            'wantAssertionsEncrypted': 'optional',
            'spEntityId': kc_url + '/realms/kramerius',
            'postBindingLogoutReceivingRequest': '',
            'wantAuthnRequestsSigned': '',
            'wantLogoutRequestsSigned': '',
            'wantAssertionsSigned': '',
            'signSpMetadata': '',
            'attributeConsumingServiceIndex': '',
            'syncMode': 'FORCE',
            'multiplePrincipals': '[{"principalType":"ATTRIBUTE","principalAttribute":"urn:oid:1.3.6.1.4.1.5923.1.1.1.13"}]',
        },
        'url': 'https://raw.githubusercontent.com/moravianlibrary/cdk-idp-list/main/idp.xml',
        'alias': 'eduid',
        'updateFrequencyInMins': 720,
    }
```
5. Přidat potřebné mappery atributů ve federaci `SAML federation` -> `eduid` -> `mappers`
6. Vygenerovat validní SAML metadata [skriptem](https://github.com/moravianlibrary/keycloak-metadata-helper) a přidat metadata do vaší entity v [MetaMan](https://metaman.eduid.cz/)

## Jak přidat ručně mapper v `SAML federation` -> `eduid` -> `mappers`
Například pro [`eduPersonUniqueId`](https://www.eduid.cz/cs/tech/attributes/edupersonuniqueid):
1. `create`
2. 'Mapper Type' = 'Attribute Importer'
3. 'Name' = 'eduPersonUniqueId'
4. 'Sync Mode Override' = 'force' (nepovinná hodnota, záleží na vašem užití)
5. 'Attribute Name' = 'urn:oid:1.3.6.1.4.1.5923.1.1.1.13'
6. 'Friendly Name' = 'eduPersonUniqueId'
7. 'Name Format' = 'ATTRIBUTE_FORMAT_URI'
8. 'User Attribute Name' = 'eduPersonUniqueId' (tento název atributu bude uložen v uživateli Keycloaku)
9. 'isRequired' = 'On'  

## DNNT
Seznam institucí zapojených do DNNT je k nalezení v repozitáří [NLCR/KramVS](https://github.com/NLCR/KramVS).

Obsahuje:
- Metadata ID NDK 
- Seznam institucí zapojených do DNNT přes eduID

## Případné problémy a řešení
### Problémy s IDP metadaty
Kvůli chybě v EOSC Keycloaku je nutné mít v metadatech poskytovatelů identit `transient` nameid na prvním místě, pokud používáte vlastní zdroj metadat místo filtrovaných metadat od [ČDK](https://raw.githubusercontent.com/moravianlibrary/cdk-idp-list/main/idp.xml).

Správně:
```
<md:NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:transient</md:NameIDFormat>
<md:NameIDFormat>urn:mace:shibboleth:1.0:nameIdentifier</md:NameIDFormat>
<md:NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:persistent</md:NameIDFormat>
```
Špatně:
```
<md:NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:persistent</md:NameIDFormat>
<md:NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:transient</md:NameIDFormat>
<md:NameIDFormat>urn:mace:shibboleth:1.0:nameIdentifier</md:NameIDFormat>
```

### Jak ukládat `username` uživatelů přicházejících z federace?
V Moravské zemské knihovně je to řešeno takto: 
- Vytvořte mapper typu `Username Template Importer`, template: `${ALIAS}.${NAMEID}`, Target: `BROKER_USERNAME`

### Keycloak Kramerius theme
Problémy s motivem případně řešte s kolegy v Moravské zemské knihovně. 
