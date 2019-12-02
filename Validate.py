'''
Created on Nov 13, 2019

@author: Tonirel
'''

class ValidateStudent:
    
    def validate_student(self,student):
        '''
        Functie ce valideaza datele studentului - student
        input: student - un student
        output: ---
        raises: Exception if ID or grup are less than 0 and if nume doesn't contain just letters
        '''
        if student.get_ID()<0:
            raise Exception ("ID incorect!")
        if student.get_grup()<0:
            raise Exception ("Grupa incorecta!")
        nume=student.get_nume()
        ok=1
        for caracter in nume:
            if (caracter>='A' and caracter<='Z') or (caracter>='a' and caracter <='z') or caracter==' ':
                ok=1
            else:
                ok=0
                break
        if ok==0:
            raise Exception ("Numele poate sa contina doar litere!")
        
        
class ValidateProblema:
    
    def validate_problema(self,problema):
        '''
        Functie ce valideaza problema - problema
        input: problema - o problema
        output: ---
        raises Exception is nrlab or nrpr or deadline are less than 0 
        '''
        if problema.get_nrlab()<0:
            raise Exception ("Numar laborator incorect!")
        if problema.get_nrpr()<0:
            raise Exception ("Numar problema incorect!")
        if problema.get_deadline()<0:
            raise Exception ("Deadline incorect!")

class ValidateNota:
    
    def validate_nota(self,nota):
        '''
        Functia ce valideaza daca o nota(float) este cuprinsa intre 0 si 10
        '''
        nota0=nota.get_nota()
        if nota0<0 or nota0>10:
            raise Exception ("Nota nu poate sa fie negativa sau mai mare decat 10!")
        