'''
Created on Nov 13, 2019

@author: Tonirel
'''

class Student:
    '''
    Clasa Student ce are ID,nume,grup
    '''
    def __init__(self,ID,nume,grup):
        self.__ID=ID
        self.__nume=nume
        self.__grup=grup
        
    def get_ID(self):
        return self.__ID
    
    def get_nume(self):
        return self.__nume
    
    def get_grup(self):
        return self.__grup
    
    def set_ID(self,ID):
        self.__ID=ID
        
    def set_nume(self,nume):
        self.__nume=nume
        
    def set_grup(self,grup):
        self.__grup=grup
        
    
        
class Problema:
    '''
    Clasa Problema ce are nrlab,nrpr,descriere,deadline
    '''
    def __init__(self,nrlab,nrpr,descriere,deadline):
        self.__nrlab=nrlab
        self.__nrpr=nrpr
        self.__descriere=descriere
        self.__deadline=deadline        
        
    def get_nrlab(self):
        return self.__nrlab
        
    def get_nrpr(self):
        return self.__nrpr
        
    def get_descriere(self):
        return self.__descriere
        
    def get_deadline(self):
        return self.__deadline
        
    def set_nrlab(self,nrlab):
        self.__nrlab=nrlab
            
    def set_nrpr(self,nrpr):
        self.__nrpr=nrpr
        
    def set_descriere(self,descriere):
        self.__descriere=descriere
            
    def set_deadline(self,deadline):
        self.__deadline=deadline    
            
class Nota:
    '''
    clase notelor ce are ca parametrii un student, o problema si un numar
    '''
    def __init__(self,Student,Problema,nota):
        self.__student = Student
        self.__problema = Problema
        self.__nota = nota

    def set_nota(self, value):
        self.__nota = value

    def get_student(self):
        return self.__student

    def get_student_ID(self):
        return self.__student.get_ID()
    
    def get_student_name(self):
        return self.__student.get_nume()

    def get_problema(self):
        return self.__problema

    def get_problema_nrlab(self):
        return self.__problema.get_nrlab()

    def get_problema_nrpr(self):
        return self.__problema.get_nrpr()
    
    def get_nota(self):
        return self.__nota
