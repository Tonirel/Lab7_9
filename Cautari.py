'''
Created on Nov 13, 2019

@author: Tonirel
'''

from Domain import Student,Problema
from State import State

class CautareStudent:
    def __init__(self,repo,state):
        self.__repo=repo
        self.__state=state
        
    def cautare_student_ID(self,ID):
        '''
        Functie ce cauta studenti dupa ID
        input: studenti - lista studentilor, ID - un ID
        output: lista studentilor cautati
        '''
        
        lista=self.__state.create_state()
        for student in self.__repo.get_all():
            if student.get_ID()==ID:
                self.__state.add(lista,student)
        return lista
    
    def cautare_student_nume(self,studenti,nume):
        '''
        Functie ce cauta studenti dupa nume
        input: studenti - lista studentilor, nume - un nume
        output: lista studentilor cautati
        '''
        state=State()
        student=Student(0,0,0)
        lista=state.create_state()
        for student in studenti:
            if student.get_nume()==nume:
                state.add(lista,student)
        return lista
    
    def cautare_student_grup(self,studenti,grup):
        '''
        Functie ce cauta studenti dupa grupa
        input: studenti - lista studentilor, grup - un grupa
        output: lista studentilor cautati
        '''
        state=State()
        student=Student(0,0,0)
        lista=state.create_state()
        for student in studenti:
            if student.get_grup()==grup:
                state.add(lista,student)
        return lista

class CautareProblema:
    
    def cautare_problema_deadline(self,probleme,deadline):
        '''
        Functie ce cauta probleme dupa deadline
        input: probleme - lista problemelor, deadline - un numar
        output: lista problemelor cautate
        '''
        state=State()
        problema=Problema(0,0,0,0)
        lista=state.create_state()
        for problema in probleme:
            if problema.get_deadline()==deadline:
                state.add(lista,problema)
        return lista
    
    
    def cautare_problema_nrlab(self,probleme,nrlab):
        '''
        Functie ce cauta probleme dupa nrlab
        input: probleme - lista problemelor, nrlab - un numar
        output: lista problemelor cautate
        '''
        state=State()
        problema=Problema(0,0,0,0)
        lista=state.create_state()
        for problema in probleme:
            if problema.get_nrlab()==nrlab:
                state.add(lista,problema)
        return lista
    
    
    def cautare_problema_nrlab_nrpr(self,probleme,nrlab,nrpr):
        '''
        Functie ce cauta probleme dupa nrlab,nrpr
        input: probleme - lista problemelor, nrlab,nrpr - numere
        output: lista problemelor cautate
        '''
        state=State()
        problema=Problema(0,0,0,0)
        lista=state.create_state()
        for problema in probleme:
            if problema.get_nrlab()==nrlab and problema.get_nrpr()==nrpr:
                state.add(lista,problema)
        return lista


