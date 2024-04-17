# generating_presences

Vytvořte program pro naplnění JSON datové struktury (kompatibilní se systemdata.json) obsahující přítomnost uživatelů – studentů na vyučování. Primárně vyjděte z datového zdroje č. 6. Vytvořte program, který importuje data do GQL endpointů (s využitím mutací).

Společné podmínky
Testujte duplicitu dat, jednak přes externalid a jednak, kde je to možné, přes jména či jiné identifikátory.
Pro práci s html daty (získání html stránek) použijte knihovnu selenium (headless mode).
Vytvořte a publikujte pypi package. Součastí github respository (source for package) je i ipynb notebook s demonstrací využití (import package, run main code). Nechť je možné importovat funkci gather z root balíčku (pypi package).
Hlavní funkce gather() pracuje s následujícími parametry:
username: Přihlašovací jméno
password: Přihlašovací heslo
config: {paths: {planovaneudalosti: “”, planovanivyuky_attributy: “”, vav_departments: “”. … }} (defaultni hodnota)
output (systemdata.json, writetogql)
**extras (token!)
U entit naplňte všechny atributy, pokud ve zdroji některé atributy nejsou, domluvte se na jejich dummy values.
Pokud máte u entit k dispozici atributy navíc, navrhněte rozšíření GQL endpointu.
