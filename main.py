from domanda import Domanda,CollezioneDomande

f=open("domande.txt","r")
lista_da_file=f.readlines()
domande_raw=[]
listaDomande=CollezioneDomande()
for s in lista_da_file:
    if(s.isspace()):
        d=Domanda(domande_raw[0],domande_raw[1],domande_raw[2],domande_raw)
        listaDomande.append(d)
        domande_raw.clear()
    domande_raw.append(s)

