#!/usr/bin/env python3
import re
class MyString:
    def __init__(self,value = ""):
            self.value = ""
            self.value = value 

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")  
                   
    def is_sentence(self):
        if self.value.endswith("."):
            return True
        else :
            return False    

    def is_question(self):
        if self.value.endswith("?"):
            return True
        else:
            return False 

    def is_exclamation(self):
        if self.value.endswith("!"):
            return True
        else :
            return False

    def count_sentences(self):
        if isinstance(self.value,str):
            parts = re.split(r'[.?!]\s*',self.value)
            sentences = [part for part in parts if part.strip()]
        return len(sentences)  
        

            
  
           
string = MyString("This is a string! It has three sentences. Right?")
print(string.count_sentences())