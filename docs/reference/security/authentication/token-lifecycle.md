# Token lifecycle v Kramerius UI

Frontend aplikace Krameria používají:

- access token
- refresh token

pro správu autentizace uživatele.

Backend Krameria je stateless a neudržuje server-side session.

Veškerá práce s expirací tokenů probíhá na straně frontend aplikace.

---

## Login flow

Po úspěšném přihlášení získá frontend:

- access_token
- refresh_token
- expires_in
- refresh_expires_in

Typická odpověď:

{
"access_token": "...",
"expires_in": 300,
"refresh_token": "...",
"refresh_expires_in": 1800
}

Frontend uloží:

- access token
- refresh token
- čas expirace access tokenu
- čas expirace refresh tokenu

---

## Uložení expirace

Frontend vypočítává:

- access_token_expiry = now + expires_in
- refresh_token_expiry = now + refresh_expires_in

Tyto hodnoty slouží pro rozhodování o refresh flow.

---

## Běžné API requesty

Každý request na backend obsahuje:

Authorization: Bearer access_token

Backend:

- validuje JWT token
- nevytváří session
- neprovádí refresh tokenů

---

## Expirace access tokenu

Pokud access token expiroval:

- frontend nesmí request odeslat
- frontend musí nejprve provést refresh

Flow:

1. Angular zjistí expiraci access tokenu
2. frontend zavolá `/auth/refresh`
3. odešle refresh token
4. získá nový access token
5. opakuje původní request

---

## Expirace refresh tokenu

Pokud expiroval refresh token:

- frontend nesmí volat `/auth/refresh`
- frontend nesmí posílat requesty na backend

Uživatel musí provést nové přihlášení.

Flow:

1. Angular zjistí expiraci refresh tokenu
2. frontend provede redirect na login
3. uživatel se znovu autentizuje

---

## Doporučená rozhodovací logika

Před každým requestem:

1. pokud je access token validní
    - odeslat request

2. pokud access token expiroval, ale refresh token je validní
    - provést refresh
    - opakovat request

3. pokud expiroval i refresh token
    - redirect na login

---

## Refresh token rotation

Refresh operace může vrátit:

- nový access token
- nový refresh token

Frontend musí vždy:

- přepsat refresh token
- přepsat refresh token expiry

---

## Sliding vs fixed expiration

Chování refresh tokenu závisí na konfiguraci Keycloak.

Refresh token může být:

- fixed expiration
- sliding expiration

Tato konfigurace je součástí Keycloak realm nastavení.

---

## Angular implementace

Doporučená implementace používá HTTP interceptor.

Interceptor:

1. kontroluje expiraci tokenů
2. případně provede refresh
3. následně odešle request

---

## Proactive refresh

Doporučené zlepšení UX:

Nečekat na úplnou expiraci access tokenu.

Frontend může refresh provést dříve, například pokud:

- access token expiruje za méně než 30 sekund

Tím se omezí:

- race conditions
- paralelní refresh requesty
- selhání requestů během expirace

---

## Odpovědnost backendu

Backend Krameria je plně stateless.

Backend:

- pouze validuje token
- neobnovuje tokeny
- neřídí session
- neprovádí redirect na login

Veškerá správa token lifecycle je odpovědností frontend aplikace.

---

## Oddělení odpovědností

| Vrstva | Odpovědnost |
|---|---|
| Keycloak | vydání tokenů |
| Angular frontend | správa token lifecycle |
| Backend | validace JWT tokenu |
| JwtAuthenticationFilter | autentizace requestu |

---

## Shrnutí

Kramerius používá stateless autentizační model založený na:

- krátkodobém access tokenu
- refresh tokenu
- frontend řízeném refresh flow

Backend nikdy nespravuje session ani token refresh.