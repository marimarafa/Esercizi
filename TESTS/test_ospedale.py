from Lezione17.Ospedale.persona import Persona
from Lezione17.Ospedale.fatture import Fattura
from Lezione17.Ospedale.dottore import Dottore
from Lezione17.Ospedale.paziente import Paziente
import unittest
from unittest import TestCase

class TestPersona(TestCase):
    def setUp(self):
        pass
      
    def test_init(self):
        persona = Persona(first_name=1245,last_name=2356)
        result1 = type(persona.__first_name and persona.__last_name) is str 
        message1 = "Error. The attribute first name and last name should be a string"
        self.assertEqual(result1,False,message1)


    # def test_setName ():
    #     pass

    # def test_persona(self):
       

    #     result2 =  type(persona.__eta()) is int
    #     message2 = "Error. The attribute age should be an integer"
    #     self.assertEqual(result2,True,message2)
        




    
    





if __name__ == "__main__":
    unittest.main()

#sul terminale : python3 -m unittest -v