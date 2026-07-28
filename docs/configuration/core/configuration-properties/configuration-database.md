[Úvod](../../../index.md) > [Konfigurace](../../index.md)  / [Core](../index.md) / [Configuration properties](index.md)

# Databaze konfigurace

Tato stránka poskytuje **referenční přehled konfiguračních parametrů SQL databaze**. Obsahuje defaultní hodnoty, účel a doporučené nastavení.

Konfigurace se načítá z:

- **Default**: uvnitř JAR souboru knihovny `configuration.properties`
- **Uživatelské přetížení**: soubor `$USER_HOME/.kramerius4/configuration.properties`

Uživatel může ve svém souboru předefinovat libovolnou hodnotu z defaultního souboru.


---


| Property | Description |
|---|---|
| jdbcUrl | JDBC connection URL |
| jdbcUserName | Database username |
| jdbcUserPass | Database password |
| jdbcMaximumPoolSize | Maximum JDBC pool size |
| jdbcConnectionTimeout | Connection timeout in milliseconds |

Database connectivity used by the application and internal services.

## Example

jdbcUrl=jdbc:postgresql://localhost/kramerius4  
jdbcUserName=fedoraAdmin  
jdbcUserPass=fedoraAdmin


---
