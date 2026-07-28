Servisní účet je možno vytvořit v keycloaku následujícím způsobem: 

## Vytvoření účtu

V realmu kramerius vytvořte nový objekt typu klient: 

![image](https://github.com/user-attachments/assets/63d5dbe3-8f68-477a-b0b8-d062573cd7e4)


![image](https://github.com/user-attachments/assets/8c50b39f-027e-475b-adfa-9fda9fa237b3)


Poté v nastavení klienta zvolit následující: 


![image](https://github.com/user-attachments/assets/26046896-919e-4add-a7a6-63dd812733e0)

![image](https://github.com/user-attachments/assets/ab5e654b-42a6-4ae3-985a-083865ae8747)

![image](https://github.com/user-attachments/assets/a72e93cd-44ea-4d9e-b002-5b8b6643469a)

a v sekci Advanced settings:

![image](https://github.com/user-attachments/assets/2f7a4883-4717-4e20-8991-58d675104b10)


Poté objekt uložit.   

V objektu client otevřít záložku s rolema pro servisní účet a servisnímu účtu přiřadit odpovídající roli.  Viz následující screenshot: 

![image](https://github.com/user-attachments/assets/5d67670c-c59a-4794-9dc4-263f1326262d)


## Použití - získání tokenu

Pro komunikaci přes API je důležité zná **clientId** a **secret**.   ClientId jsme vytvářeli spolu s objektem a v našem případě to je `service_account_a`, secret lze získat z následující cesty:

![image](https://github.com/user-attachments/assets/c90df2c9-569b-491c-a12f-73ee6803f921)


Získání tokenu je možno vyzkoušet přes OpenAPI následujícím endpointem: 

`https://<k7_instance>/search/openapi/exts/v7.0/index.html#/Z%C3%ADsk%C3%A1n%C3%AD%20servisn%C3%ADho%20tokenu/get_tokens__clientid_`


![image](https://github.com/user-attachments/assets/f5a3ada8-d4bf-4e39-907a-803772c18214)


a pak ve výsledku je vidět token: 

![image](https://github.com/user-attachments/assets/a183ad4c-be03-482d-92e5-5e8d2069c630)









 



