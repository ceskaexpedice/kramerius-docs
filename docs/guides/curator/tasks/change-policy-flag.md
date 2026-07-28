## Proces

Byl implementován proces pro změnu příznaku na licenci, který umožňuje přidávání licencí na místě (onsite) i veřejně (public) a také plánování procesu pro odebrání příznaku.

Licence jsou přidávány pouze na konkrétní úrovni a jsou zděděny směrem dolů, zatímco příznak, že dané dílo má licenci, je propagován směrem nahoru. Proces zahrnuje konfigurační proměnnou, která specifikuje, na které úrovni mají být licence přiřazovány. Zde je příklad pro monografie a periodika.

`processess.flag_to_license.models=monograph,monographunit,periodicalvolume`

Proces definovaný tímto způsobem přiděluje licence následovně:

* Periodika: - Licence bude přidělena na úrovni ročníků. To znamená, že všechny výtisky daného ročníku budou mít zděděnou tuto licenci. Periodikum samotné bude obsahovat informaci o tom, že obsahuje tituly s touto licencí.

* Monografie: - Pokud je monografie vícesvazková a obsahuje objekty monographunit, licence je přidělena na úrovni monographunit. V případě, že monografie není vícesvazková, tedy neobsahuje `monographunit`, licence je přidělena na úrovni celé monografie.

Pokud chceme přidělovat licence na úrovni výtisků, pak konfigurační proměnná by měla vypadat následovně:
`processess.flag_to_license.models=...,periodicalitem`

Implicitní hodnota je nastavena následovně: monograph, monographunit, periodicalvolume, manuscript, soundrecording, convolute, map, sheetmusic, graphic, archive, convolute

## Spuštění procesu 

Spuštění procesu je možno spustit z administračního rozhraní pomocí **menu Repositář &rarr; sekce Hromadné úpravy &rarr; tlačítko Změnit příznak na licenci**. 


![image](https://github.com/ceskaexpedice/kramerius/assets/675753/54b7f968-1f61-41eb-9b4c-f779a5bdee77)

![image](https://github.com/ceskaexpedice/kramerius/assets/675753/99974986-dab5-4468-ba3b-891b039a0fb1)





