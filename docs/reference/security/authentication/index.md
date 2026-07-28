[Úvod](../../../index.md) > [Reference](../../index.md)  / [Zabezpečení](../index.md)

# Autentizace

Kramerius používá OAuth 2.0 Access Token ve formátu JWT.

## Podporovane standardy

- OAuth 2.0
- OpenID Connect
- JWT

## Token

Kramerius očekává token v hlavičce:

```http
Authorization: Bearer <token>
```

### CDK hlavicka
...

### [Token model](token-model.md)

### [Token lifecycle](token-lifecycle.md)


## User Principal

Po úspěšné validaci tokenu vzniká interní reprezentace uživatele.

### [Role](../roles/index.md)

## Authentication Errors

| Error | Description |
|--------|--------|
| Invalid token | Token cannot be validated |
| Expired token | Token expired |
| Missing token | No token provided |


