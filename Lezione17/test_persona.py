import unittest
from persona import Persona
from dottore import Dottore
from paziente import Paziente
from fatture import Fattura

class TestPersona(unittest.TestCase):
    def setUp(self) -> None:
        self.persona = Persona("Mario","Rossi")
        self.persona.setAge(30)

    def test_persona(self):
        self.assertEqual(self.persona.getName(), "Mario")
        self.assertEqual(self.persona.getLastname(), "Rossi")
        self.assertEqual(self.persona.getAge(),30)

class TestDottore(unittest.TestCase):
    def setUp(self):
        self.dottore = Dottore("Silvio","Verdi","Chirurgo",32.00)
        self.dottore.setAge(43)

    def test_dottore(self):
        self.assertEqual(self.dottore.getName(), "Silvio")
        self.assertEqual(self.dottore.getLastname(), "Verdi")
        self.assertEqual(self.dottore.getAge(),43)
        self.assertEqual(self.dottore.getSpecialization(),"Chirurgo")
        self.assertEqual(self.dottore.getParcel(),32.00)
        self.assertEqual(self.dottore.isAValidDoctor(),True)
        self.dottore.setAge(15)
        self.assertEqual(self.dottore.isAValidDoctor(),False)

class TestPaziente(unittest.TestCase):
    def setUp(self):
        self.paziente = Paziente("Luigi","Bianchi","A003")
        self.paziente.setAge(27)

    def test_paziente(self):
        self.assertEqual(self.paziente.getName(), "Luigi")
        self.assertEqual(self.paziente.getLastname(), "Bianchi")
        self.assertEqual(self.paziente.getAge(),27)
        self.assertEqual(self.paziente.getIdCode(),"A003")

class TestFattura(unittest.TestCase):
    def setUp(self):
        dottore1 = Dottore("Maurizio","Merluzzo","Veterinario",71.00)
        dottore1.setAge(50)
        paziente1 = Paziente("Giorgio","Verdi","B71")
        paziente2 = Paziente("Gianni","Morandi","C72")
        self.fattura = Fattura(dottore1,[paziente1,paziente2])

    def test_fattura(self):
        self.assertEqual(self.fattura.getFatture(),2)
        self.assertEqual(self.fattura.getSalary(),142.00)
        paziente3 = Paziente("Marione","Neri","Z04")




if __name__ == '__main__':
    unittest.main()