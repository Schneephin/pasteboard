/**
 * Formulareingaben Ueberprüfung
 * @author Andreas Fendel <andreas.fendel@gmx.de>
 */
function pruefeFormular(f){
	// Variablen fuer gefundene Fehler
    var fehler = "";
	// Schleife - Fuer jedes Formularelement ein Durchlauf
    for (var i = 0; i < f.elements.length; i++) {
        var element = f.elements[i];
        // Ueberprüfung ueberspringen wenn kein Pflichtfeld
		// Alle Elemente die mit "_P" Ende werden ueberprueft
        if (element.name.lastIndexOf("_P") != element.name.length - 2) {
            continue;
        }
		// Formularfeld entsprechende Ueberpruefung auswaehlen und durchfuehren
        switch (element.type) {
			// Textfeld, Passwortfeld und Textbereiche pruefen
            case "text":
            case "password":
            case "textarea":
				// Pruefen ob eine Eingabe vorliegt
                if (element.value == ""){
                    fehler += "\nTextfeld '" + element.name + "'";
                }
                break;
            // Einfache Auswahlliste prüfen ob Element ausgewählt
            case "select-one":
                if (element.value == "" || element.selectedIndex == -1) {
                    fehler += "\nListe '" + element.name + "'";
                }
                break;
			// Prüfen ob eine Checkbox ausgewaehlt wurde 
            case "checkbox":
                if (!element.checked) {
                    fehler += "\nCheckbox'" + element.name + "'";
                }
                break;
			// Prüfen ob mindestens ein Element ausgewählt wurde
            case "select-multiple":
                if (element.selectedIndex == -1) {
                    fehler += "\nListe '" + element.name + "'";
                }
                break;
			// Prüfen ob mindestens ein Element ausgewählt wurde
            case "radio":
				// Fuer die pruefung benoetigte Variablen
                var gruppenname = element.name;
                var gruppe = f.elements[gruppenname];
                var ok = false;
				// Alle zugehöhrigen Elemente prüfen
                for (var j = 0; j < gruppe.length; j++) {
                    if (gruppe[j].checked) {
                        // Wenn ein Element gewählt wurde wahr
						ok = true;
                    }
                } // Wenn kein Element gewählt wurde falsch
				// Fehlerausgabe wenn kein Element ausgewaehlt wurde 				
                if (!ok) {
                    fehler += "\nRadiobuttongruppe '" + gruppenname + "'";
                }
                break;
        }
    }
	// Wenn kein Fehler dann wahr
    if (fehler == "") {
        return true;
	// Wenn ein Fehler dann Falsch und Ausgabe der Fehler
    } else {
		alert(unescape("Die folgenden Felder wurden nicht vollst%E4ndig ausgef%FCllt%3A\n" + fehler));
        return false;
    }
}
