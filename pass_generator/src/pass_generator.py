import random
import string
from abc import ABC, abstractmethod
from nltk.corpus import words

class Pass_generator(ABC):
    @abstractmethod
    def generate():
        pass


class Pin_code(Pass_generator):
    def __init__(self, number = 5, seprator = ""):
        self.number = number
        self.seprator = seprator

    def generate(self):
        return self.seprator.join([random.choice(string.digits) for i in range(self.number)])  
    
class Random_password(Pass_generator):
    def __init__(self,number= 6, seprator= "", include_number = False,includ_symbol= False ):
        self.number = number
        self.seprator = seprator
        self.character = string.ascii_letters

        if includ_symbol:
            self.character += string.punctuation

        if include_number:
            self.character += string.digits

    def generate(self):
        return self.seprator.join([random.choice(self.character) for i in range(self.number)])
    

class Memorable_password(Pass_generator):
    def __init__(self, number_of_words=5, vocabulary=None, capitalize=False, seprator=""):
        self.number_of_words = number_of_words
        self.seprator = seprator 
        self.capitalize = capitalize

        if vocabulary is None:
            vocabulary = words.words()
        self.vocabulary = vocabulary
      
    def generate(self):
        password = [random.choice(self.vocabulary) for i in range(5)]
        if self.capitalize:
            password = [word.upper() if random.choice([True, False]) else word.lower()  for word in password] 
        return(self.seprator.join(password))
    

    
if __name__ == "__main__":
    m_obj = Memorable_password(capitalize=True, seprator="_")
    r_obj = Random_password()
    p_obj = Pin_code()

    print(m_obj.generate())
    print(r_obj.generate())
    print(p_obj.generate())