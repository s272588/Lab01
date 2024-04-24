import random


class Domanda:
    def __init__(self, testo, difficolta, risposta_corretta, risposte_errate):
        self.testo = testo
        self.difficolta = difficolta
        self.risposta_corretta = risposta_corretta
        self.risposte_errate = risposte_errate


class Game:
    def __init__(self,file_domande,file_punti):
        self.file_domande = file_domande
        self.file_punti = file_punti
        self.domande = []
        self.carica_domande()
        self.max_difficolta = self.calcola_max_difficolta()

    def carica_domande(self):
        with open(self.file_domande, 'r') as f:
            lines = f.readlines()
            i = 0
            while i < len(lines):
                testo = lines[i].strip()
                difficolta = int(lines[i + 1].strip())
                risposta_corretta = lines[i + 2].strip()
                risposte_errate = [lines[i + 3].strip(), lines[i + 4].strip(), lines[i + 5].strip()]
                self.domande.append(Domanda(testo, difficolta, risposta_corretta, risposte_errate))
                i += 7  # Salta alla prossima domanda

    def calcola_max_difficolta(self):
        return max(domanda.difficolta for domanda in self.domande)

    def avvia_gioco(self):
        punteggio = 0
        livello = 0

        while livello <= self.max_difficolta:
            domanda = self.seleziona_domanda(livello)
            if not domanda:
                print(f"Nessuna domanda disponibile per il livello {livello}.")
                break

            print("\nLivello:", livello)
            print("Domanda:", domanda.testo)

            risposte = [domanda.risposta_corretta] + domanda.risposte_errate
            random.shuffle(risposte)

            for i, risposta in enumerate(risposte, start=1):
                print(f"{i}. {risposta}")

            risposta_utente = int(input("Seleziona la risposta (1-4): "))
            risposta_scelta = risposte[risposta_utente - 1]

            if risposta_scelta == domanda.risposta_corretta:
                print("Corretto!")
                punteggio += 1
                livello += 1
            else:
                print(f"Sbagliato! La risposta corretta era: {domanda.risposta_corretta}")
                break

        print("\nGioco terminato!")
        print(f"Il tuo punteggio è: {punteggio}")

        nickname = input("Inserisci il tuo nickname: ")
        self.salva_punteggio(nickname, punteggio)

    def seleziona_domanda(self, livello):
        domande_livello = [domanda for domanda in self.domande if domanda.difficolta == livello]
        if domande_livello:
            return random.choice(domande_livello)
        else:
            return None

    def salva_punteggio(self, nickname, punteggio):
        # Carica i punteggi esistenti
        punteggi = []
        try:
            with open(self.file_punti, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    name, score = line.strip().split()
                    punteggi.append((name, int(score)))
        except FileNotFoundError:
            pass

        # Aggiungi il nuovo punteggio
        punteggi.append((nickname, punteggio))

        # Ordina i punteggi in ordine decrescente
        punteggi.sort(key=lambda x: x[1], reverse=True)

        # Scrivi i punteggi aggiornati nel file
        with open(self.file_punti, 'w') as f:
            for name, score in punteggi:
                f.write(f"{name} {score}\n")


# Avvia il gioco
if __name__ == "__main__":
    game = Game("domande.txt", "punti.txt")
    game.avvia_gioco()

