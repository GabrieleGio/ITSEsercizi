class Documento:
    def __init__(self):
        self.testo = ""
    
    def getText(self):
        return self.testo
    
    def setText(self,testo):
        self.testo = testo

    def isInText(self,chiave):
        parole = self.testo.split()
        for parola in parole:
            if parola == chiave:
                return True
            else:
                return False
            
class Email(Documento):
    def __init__(self):
        super().__init__()
        self.mittente = ""
        self.destinatario = ""
        self.titolo = ""

    def getMittente(self):
        return self.mittente
    
    def getDestinatario(self):
        return self.destinatario
    
    def getTitolo(self):
        return self.titolo
    
    def setMittente(self,mittente):
        self.mittente = mittente

    def setDestinatario(self,destinatario):
        self.destinatario = destinatario

    def setTitolo(self,titolo):
        self.titolo = titolo

    def getText(self):
        email = f"Da: {self.getMittente()}, A: {self.getDestinatario()}\nTitolo: {self.getTitolo()}\nMessaggio: {self.testo}"
        return email
    
    def writeToFile(self,percorso):
        file = open(percorso,"w")
        file.write(self.getText())
        file.close()


class File(Documento):
    def __init__(self,nomePercorso):
        super().__init__()
        self.nomePercorso = nomePercorso

    def leggiTestoDaFile(self):
        file = open(self.nomePercorso)
        self.setText(file.read())
        file.close()

    def getText(self):
        filebello = f"Percorso: {self.nomePercorso}\nContenuto: {self.testo}"
        return filebello
    



documento1 = Documento()
documento1.setText("Ciao sono Mario")
email1 = Email()
email1.setDestinatario("Mario")
email1.setMittente("Luigi")
email1.setTitolo("Ciao")
email1.setText("Ciao come stai oggi?")
email1.writeToFile("/home/user/Scrivania/ITSEsercizi/ITSEsercizi/Lezione24/documentMario.txt")
file1 = File("/home/user/Scrivania/ITSEsercizi/ITSEsercizi/Lezione24/document.txt")
file1.leggiTestoDaFile()
print(file1.getText())
