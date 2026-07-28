# Token model

Kramerius používá OpenID Connect (OIDC) Bearer tokeny vydávané systémem Keycloak jako vstupní identitu uživatele.

Token představuje externí bezpečnostní identitu získanou z Keycloak a případně z federovaných identity providerů.

Kramerius tento token:

- validuje
- interpretuje
- transformuje do interního bezpečnostního modelu

Tento dokument popisuje strukturu tokenu a význam jednotlivých částí z pohledu Krameria.

---

## Vztah ke Keycloak

Token je vydáván Keycloak realm serverem.

Typické vlastnosti tokenu:

- JWT formát
- OIDC kompatibilní
- Bearer token
- časově omezená platnost

Konfigurace Keycloak není součástí tohoto dokumentu.

Viz: ➡️ [Konfigurace](../../../configuration/security/keycloak.md)

---

## Role a atributy

Token obsahuje dva odlišné typy bezpečnostních informací.

### Role

Role představují:

- skupiny
- oprávnění
- autorizační vstupy

Zdroj:

- realm_access.roles
- případně mappery

---

### Atributy

Atributy představují:

- identitu uživatele
- federované informace
- metadata identity

Zdroj:

- identity provider
- LDAP
- SAML
- mappery

---


## Standardní OIDC část tokenu

Token obsahuje standardní OIDC metadata:

| Pole | Význam |
|---|---|
| exp | čas expirace tokenu |
| iat | čas vydání tokenu |
| auth_time | čas autentizace uživatele |
| jti | unikátní identifikátor tokenu |
| iss | issuer (Keycloak realm URL) |
| aud | audience |
| sub | unikátní identifikátor uživatele |
| typ | typ tokenu |
| azp | autorizovaný klient |
| session_state | identifikátor session |
| sid | session identifier |
| acr | authentication context |


## Realm role

Pole `realm_access.roles` obsahuje realm role definované v Keycloak.

Typické role:

- `dnnt_users`
- `special-needs`
- `default-roles-kramerius`
- `offline_access`
- `uma_authorization`

Tyto role reprezentují:

- skupiny uživatelů
- globální oprávnění
- technické Keycloak role
- vstup pro autorizaci v Krameriu


## Client role

Pole `resource_access` obsahuje role navázané na konkrétní Keycloak klienty.

Typický příklad:

- `manage-account`
- `manage-account-2fa`
- `view-profile`

Tyto role:

- jsou specifické pro Keycloak klienta
- většinou nejsou používány pro business autorizaci v Krameriu
- slouží především interním funkcím Keycloaku


## Identity atributy

Token může obsahovat další atributy identity.

Typické atributy:

| Atribut | Význam |
|---|---|
| preferred_username | uživatelské jméno |
| displayName | zobrazované jméno |
| email | email uživatele |
| email_verified | informace o ověření emailu |


## Federované atributy

Při použití federace identity mohou být do tokenu přidány federované atributy.

Typické atributy:

| Atribut | Význam |
|---|---|
| eduPersonPrincipalName | federovaný login |
| eduPersonUniqueId | unikátní federovaný identifikátor |
| eduPersonEntitlement | federovaná oprávnění |
| eduPersonScopedAffiliation | afiliace uživatele |
| affiliation | další afiliace |

Tyto atributy pocházejí typicky z:

- SAML identity providerů
- LDAP
- externích federací
- Keycloak mapperů

---


## Vztah ke Kramerius Security Contextu

Kramerius nepoužívá token přímo jako interní bezpečnostní model.

Místo toho:

1. validuje token
2. extrahuje identity a role
3. interpretuje atributy
4. aplikuje role enrichment
5. vytváří interní Security Context

---

## Role enrichment

Kramerius může nad rámec tokenu:

- doplnit další role
- mapovat externí role
- odvodit oprávnění z atributů
- přidat doménová oprávnění

Výsledná autorizace tedy nemusí odpovídat pouze původnímu tokenu.

---

## Oddělení odpovědností

| Vrstva | Odpovědnost |
|---|---|
| Keycloak | autentizace a vydání tokenu |
| Token | přenos identity |
| Kramerius Security Context | interní reprezentace identity |
| Authorization layer | rozhodování o přístupu |

---

## Bezpečnostní poznámky

Kramerius:

- důvěřuje validovanému tokenu
- neudržuje server-side session
- autentizuje každý request samostatně
- používá token pouze po dobu jeho platnosti

---

## Příklad tokenu

```text
{
  "exp": 1773355421,
  "iat": 1773319423,
  "auth_time": 1773319421,
  "jti": "9afc4bec-25ee-44f5-9ead-36b5162a62b3",
  "iss": "https://eduid.inovatika.dev/realms/kramerius",
  "aud": "account",
  "sub": "35a534c4-e444-4451-88fa-3f9056ec9f26",
  "typ": "Bearer",
  "azp": "krameriusClient",
  "session_state": "42fe7ea5-3b22-4941-aba5-5948fb790eac",
  "acr": "1",

  "realm_access": {
    "roles": [
      "dnnt_users",
      "offline_access",
      "special-needs",
      "default-roles-kramerius",
      "uma_authorization"
    ]
  },

  "resource_access": {
    "account": {
      "roles": [
        "manage-account",
        "manage-account-2fa",
        "manage-account-links",
        "manage-account-basic-auth",
        "view-profile"
      ]
    }
  },

  "scope": "profile email",
  "sid": "42fe7ea5-3b22-4941-aba5-5948fb790eac",
  "eduPersonEntitlement": "urn:mace:dir:entitlement:common-lib-terms",
  "email_verified": false,
  "eduPersonScopedAffiliation": "member@inovatika.dev##employee@inovatika.dev",
  "affiliation": "member@inovatika.dev##employee@inovatika.dev",
  "displayName": "Petr Podsednik",
  "eduPersonPrincipalName": "pepo@inovatika.dev",
  "eduPersonUniqueId": "2222@inovatika.dev",
  "preferred_username": "pepo"
}
```


## Shrnutí

OIDC token představuje vstupní identitu uživatele získanou z Keycloak.

Kramerius z tokenu vytváří vlastní interní bezpečnostní model, který kombinuje:

- identity atributy
- role
- federované informace
- interní role enrichment
- doménová oprávnění