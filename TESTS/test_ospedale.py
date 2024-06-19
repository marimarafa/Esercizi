from Lezione17.Ospedale.persona import Persona
import unittest
from unittest import TestCase

class TestPersona(TestCase):
    def setUp(self):
        pass
      
    def test_init(self):
        persona = Persona(first_name=1245,last_name=2356)
        result1 = type(persona.getName())is str
        message1 = "Error. The attribute first name"
        self.assertEqual(result1,False,message1)

        result2 = type(persona.getLastName()) is str 
        message2 = "Error. The attribute last name should be a string"
        self.assertEqual(result2,False,message2)


    def test_setName(self):
        persona = Persona(first_name="mario",last_name="rossi")
        persona.setName("marco")
        result = persona.getName()
        message = "Error. The name should be marco not mario"
        self.assertEqual(result,"marco",message)
    
    def test_setLastName(self):
        persona = Persona(first_name="mario",last_name="rossi")
        persona.setLastName("verdi")
        result = persona.getLastName()
        message = "Error. The last name should be verdi not rossi"
        self.assertEqual(result,"verdi",message)
    
    def test_setAge(self):
        persona = Persona(first_name="mario",last_name="rossi")
        persona.setAge(42)
        result = persona.getAge()
        message = "Error. The function should return the age"
        self.assertEqual(result,42,message)

from Lezione17.Ospedale.dottore import Dottore

class TestDottore(TestCase):
    def setUp(self):
        pass
    
    def test_init(self):
        dottore = Dottore(first_name="marco",last_name="rossi",specialization= "dentista",parcel=22.3)
        result1 = type(dottore.getSpecialization()) is str
        message1 = "Error. The attribute specialization should be a string"
        self.assertEqual(result1,True,message1)

        result2 = type(dottore.getParcel()) is float
        message2 = "Error, the attribute parcel should be a float"
        self.assertEqual(result2,True,message2)
        
    def test_SetSpecialization(self):
        dottore = Dottore(first_name="marco",last_name="rossi",specialization= "dentista",parcel=22.3)
        dottore.setSpecialization("pediatria")
        result = dottore.getSpecialization()
        message = "Error. The attribute specialization should be pediatria"
        self.assertEqual(result,"pediatria",message)
    
    def test_SetParcel(self):
        dottore = Dottore(first_name="marco",last_name="rossi",specialization= "dentista",parcel=22.3)
        dottore.setParcel(45.76)
        result = dottore.getParcel()
        message = "Error. The attribute parcel should be 45.76"
        self.assertEqual(result,45.76,message)
        
    def test_IsAValidDoctor(self):
        dottore1 = Dottore(first_name="marco",last_name="rossi",specialization= "dentista",parcel=22.3)
        dottore1.setAge(20)
        result = dottore1.isAValidDoctor()
        message = "Error . The doctors age should be more then 30 "
        self.assertEqual(result,False,message)
        
        dottore1.setAge(50)
        result1 = dottore1.isAValidDoctor()
        message1 = "Error . The doctors age should be more then 30 "
        self.assertEqual(result1,True,message1)
    
        
        
        
        
        



   
        




    
    





if __name__ == "__main__":
    unittest.main()

#sul terminale : python3 -m unittest -v