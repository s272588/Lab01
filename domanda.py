
import random
class Domanda():
    def __init__(self,testo_domanda,livello_difficolta,risposta_corretta,opzioni):
        self.testo=testo_domanda
        self.livello=livello_difficolta
        self.risposta=risposta_corretta
        self.opzioni=opzioni

    def mostra_testo(self):
        return self.testo
    def mostra_difficolta(self):
        return self.livello
    def èCorretto(self,opzione):
        if opzione==self.risposta:
            return True
        else : return False
    def shuffleOpzioni(self):
        shuffle=[]
        for i in range(4):
            r=random.randrange(0,3,1)
            shuffle[i]=self.opzioni[r]
            if(shuffle.__contains__(self.opzioni[r])):
                i=i-1
        return shuffle

class CollezioneDomande:
    def __init__(self):
        self._listaDomande=[]
        self.maxLivello=0
    def append(self,domanda):
        self._listaDomande.append(domanda)
        if(self.maxLivello<domanda.mostra_difficolta()):
            maxLivello=domanda.mostra_difficolta()
    def collezionePerLivello(self,livello):
        domandeLivelloAttuale=[]
        for d in self._listaDomande:
            if(d.mostra_difficoltà()==livello):
                domandeLivelloAttuale.append(d)

        return domandeLivelloAttuale
    def estrazionePerLivello(self,livello):
        domandeLivelloAttuale=self.collezionePerLivello(livello)
        ind=random.randint(0,domandeLivelloAttuale.__len__())
        return domandeLivelloAttuale(ind)
    def livelloMassimo(self):
        return self.maxLivello

