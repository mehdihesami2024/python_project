import random
import string
from abc import ABC, abstractmethod
from nltk.corpus import words

class Pass_generator(ABC):
    @abstractmethod
    def generate():
        pass


class Pin_code(Pass_generator):
    def __init__(self, length= 5, seprator = ""):
        self.length = length
        self.seprator = seprator

    def generate(self):
        return self.seprator.join([random.choice(string.digits) for i in range(self.length)])  
    
class Random_password(Pass_generator):
    def __init__(self,length= 6, seprator= "", include_number = False,includ_symbol= False ):
        self.length= length
        self.seprator = seprator
        self.character = string.ascii_letters

        if includ_symbol:
            self.character += string.punctuation

        if include_number:
            self.character += string.digits

    def generate(self):
        return self.seprator.join([random.choice(self.character) for i in range(self.length)])
    

class Memorable_password(Pass_generator):
    def __init__(self, number_of_words=5,  capitalize=False, seprator="", vocabulary=None,):
        self.number_of_words = number_of_words
        self.seprator = seprator 
        self.capitalize = capitalize

        if vocabulary is None:
            vocabulary = words.words()
        self.vocabulary = vocabulary
      
    def generate(self):
        password = [random.choice(self.vocabulary) for i in range(self.number_of_words)]
        if self.capitalize:
            password = [word.upper() if random.choice([True, False]) else word.lower()  for word in password] 
        return(self.seprator.join(password))
    

