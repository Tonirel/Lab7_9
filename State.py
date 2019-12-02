'''
Created on Nov 13, 2019

@author: Tonirel
'''

class State:
    
    def create_state(self):
        '''
        Functia ce creeaza o stare
        '''
        return []
    
    def add(self,state,element):
        '''
        Functia ce adauga un element intr-o stare
        '''
        state.append(element)
    
    def lenght(self,state):
        '''
        Functia ce calculeaza lungimea unei stari
        '''
        return len(state)