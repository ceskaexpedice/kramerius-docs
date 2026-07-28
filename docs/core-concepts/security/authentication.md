[Úvod](../../index.md) > [Základní koncepty](../../core-concepts/index.md) / [Zabezpečení](../../core-concepts/security/index.md)

# Autentizace

Autentizace odpovídá na otázku:

> Kdo je aktuální uživatel?

Kramerius přímo nespravuje uživatelské identity. Místo toho spoléhá na externí poskytovatele identity (Identity Provider, IdP), typicky Keycloak.

Po úspěšném přihlášení poskytovatel identity vydá bezpečnostní token obsahující informace o autentizovaném uživateli.

```text
User
  ↓
Role
```


## Výsledek autentizace

Výsledkem autentizace je autentizovaná identita reprezentovaná:

- identifikátorem uživatele
- uživatelským jménem
- přiřazenými rolemi
- dalšími atributy identity

Autentizovaná identita je připojena ke každému požadavku a stává se vstupem pro autorizaci.

## Navazujici dokumentace

- ➡️ [Architektura](../../architecture/security/authentication.md)
- ➡️ [Reference](../../reference/security/authentication/index.md)


