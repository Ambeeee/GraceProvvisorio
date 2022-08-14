from Engine import Engine
from translate import Translator

# METTI NEI DATA
help = """
ISTRUZIONI

Usa sempre la parola chiave GRACE (minuscolo o maiuscolo non cambia) all'inizio del comando

Usa parole chiavi come:
    - traduci
    - cosa/che significa

La lingua di destinazione predefinita è l' ITALIANO.
per sceglierne un'altra basta scrivere " in (lingua) " alla fine della frase.

Per lingue attualmente supportate:      grace traduci !lang

ESEMPIO:
    grace traduci pitone in inglese
    grace cosa significa rust?

Per rileggere:                          grace traduci !help

BUON DIVERTIMENTO!
"""
dictionary = {
        "italiano": "it",
        "inglese": "en",
        "cinese": "zh"
    }




class Assistant(Engine):

    def translate(self, command):

        while True:

            if "usa" in command:
                print(help)
                break
            if "lingue" in command:
                for av_lang in dictionary:
                    print("\n" + av_lang) 
                break

            if (command[0] in ["cosa", "che"]) and command[1] == "significa":     del command[0]      
            command.pop(0)
            
            if command[-2] == "in":
                lang = command[-1]
                command.pop(-1)
                command.pop(-1)
            else:
                lingua = "italiano"

            traduci = " ".join(command)

            #TRADUTTORE
            translator= Translator(to_lang=dictionary[lang])
            translation = translator.translate(traduci)
            final_content = f"{traduci} in {lang} si dice {translation} "
            if lang == "italiano":
                final_content = f"{traduci} significa {translation} "
            return self.decor(final_content)
            
    def manage_actions(self, command):
        if command.startswith(self.name):
            if output.endswith("?"):    output = output.replace("?", "")
            command = output.replace(self.name, "", 1).split()

        match command[0]:
            case "traduci" | "significa" | "traduttore":
                self.say(self.translate(command))

    

Grace = Assistant("Ciao", 1, [1,"y"])

Grace.run()