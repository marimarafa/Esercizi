from persona import Persona
from paziente import Paziente
from dottore import Dottore
from fatture import Fattura
import unittest
from unittest import TestCase

class TestPersona(TestCase):
    def setUp(self):
        self.persona = Persona(first_name="mario",last_name="rossi")
        self.persona.setName("paolo")
        self.persona.setAge(23)
        self.persona.setLastName("verdi")
        result = type(self.persona.__first_name and self.persona.__last_name) is str 
        message :str = "Error. Gli attributi first name e last name devono essere una  stringa"
        self.assertEqual(result,True,message)






    







    





    
    
    





if __name__ == "__main__":
    unittest.main()

#sul terminale : python3 -m unittest -v