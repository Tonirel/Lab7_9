'''
Created on Nov 13, 2019

@author: Tonirel
'''

from Domain import Student, Problema, Nota



        
             
class ServiceStudent:
    def __init__(self,repo,valid,state):
        self.__repo=repo
        self.__valid=valid
        self.__state=state
        
    def get_all(self):
        '''
        Functie ce returneaza toti studentii
        '''
        return self.__repo.get_all()
        
    def erase_repo(self):
        '''
        Functie ce sterge toti studentii din lista studentiilor
        '''
        return self.__repo.erase()
    
    def create_student(self,ID,nume,grup):
        '''
        Functie ce creeaza un student
        input : ID - ID-ul unui student, nume - numele unui student, grup - grupa unui student
        output : student - un student
        ID,grup - int
        nume - str
        '''
        student=Student(ID,nume,grup)
        self.__valid.validate_student(student)
        self.__repo.add_student(student)
        #self.__repo.add_student_file(student)  
        
        
    def cautare_student_ID(self,ID):
        '''
        Functie ce cauta studenti dupa ID
        input: studenti - lista studentilor, ID - un ID
        output: lista studentilor cautati
        '''
        
        for student in self.__repo.get_all():
            ID0=student.get_ID()
            if int(ID0)==int(ID):
                return student 
    
    def cautare_student_nume(self,nume):
        '''
        Functie ce cauta studenti dupa nume
        input: studenti - lista studentilor, nume - un nume
        output: lista studentilor cautati
        '''
        lista=self.__state.create_state()
        for student in self.__repo.get_all():
            if student.get_nume()==nume:
                self.__state.add(lista,student)
        return lista
    
    def modificare_student(self,ID,ID0,nume,grup):
        '''
        Functie ce modifica un student
        input : ID - variabila dupa care cautam studentul // ID0,nume,grup - variabilele
                ce urmeaza sa le primeasca studentul
        output : studentul modificat
        '''
        for student in self.__repo.get_all():
            if student.get_ID()==ID:
                student.set_ID(ID0)
                student.set_nume(nume)
                student.set_grup(grup)
                return
        
    def cautare_student_grup(self,grup):
        '''
        Functie ce cauta studenti dupa grupa
        input: studenti - lista studentilor, grup - un grupa
        output: lista studentilor cautati
        '''
        lista=self.__state.create_state()
        for student in self.__repo.get_all():
            if int(student.get_grup())==int(grup):
                self.__state.add(lista,student)
        return lista
  
    

class ServiceProblema:
    
    def __init__(self,repo,valid,state):
        self.__repo=repo
        self.__valid=valid
        self.__state=state
        
    def get_all(self):
        '''
        Functie ce returneaza toate problemele
        '''
        return self.__repo.get_all()
        
    def erase_repo(self):
        '''
        Functie ce sterge lista de probleme
        '''
        return self.__repo.erase()
    
    def create_problema(self,nrlab,nrpr,descriere,deadline):
        '''
        Functie ce creeaza o problema
        input: nrlab - numarul laboratorului, nrpr - numarul problemei, descriere - descrierea problemei, deadline - deadline-ul problemei
        output: problema - o problema
        nrlab,nrpr,deadline - int
        descriere - str
        '''
        problema=Problema(nrlab,nrpr,descriere,deadline)
        self.__valid.validate_problema(problema)
        self.__repo.add_problema(problema)

    def cautare_problema_nrlab_nrpr(self,nrlab,nrpr):
        '''
        Functie ce cauta o problema dupa nrlab si nrpr
        input : nrlab , nrpr - int
        output : lista de probleme
        '''
        for problema in self.__repo.get_all():
            if int(problema.get_nrlab())==int(nrlab) and int(problema.get_nrpr())==int(nrpr):
                return problema
                
         
      
    def modificare_problema(self,NRLAB,NRPR,nrlab,nrpr,descriere,deadline):
        '''
        Functie ce modifica o problema
        input : NRLAB, NRPR - cele initiale // nrlab,nrpr,descriere,deadline - cele noi
        output : problema modificata
        '''
        for problema in self.__repo.get_all():
            if problema.get_nrlab()==NRLAB and problema.get_nrpr()==NRPR:
                problema.set_nrlab(nrlab)
                problema.set_nrpr(nrpr)
                problema.set_descriere(descriere)
                problema.set_deadline(deadline)
                return
             
    def cautare_problema_nrlab(self,nrlab):
        '''
        Functie ce cauta probleme dupa nrlab
        input : nrlab - int
        output : lista de probleme
        '''
        lista=self.__state.create_state()
        for problema in self.__repo.get_all():
            if problema.get_nrlab()==nrlab:
                self.__state.add(lista,problema)
        return lista
    
    def cautare_problema_nrpr(self,nrpr):
        '''
        Functie ce cauta probleme dupa nrpr
        input : nrpr - int
        output : lista de probleme
        '''
        lista=self.__state.create_state()
        for problema in self.__repo.get_all():
            if problema.get_nrpr()==nrpr:
                self.__state.add(lista,problema)
        return lista
    
    def cautare_problema_deadline(self,deadline):
        '''
        Functie ce cauta probleme dupa deadline
        input : deadline - int
        output : lista de probleme
        '''
        lista=self.__state.create_state()
        for problema in self.__repo.get_all():
            if problema.get_deadline()==deadline:
                self.__state.add(lista,problema)
        return lista
    
class ServiceNota:
    
    def __init__(self,repo_nota,valid_nota,repo_student,repo_problema,state):
        self.__repo_nota=repo_nota
        self.__repo_student=repo_student
        self.__repo_problema=repo_problema
        self.__valid_nota=valid_nota
        self.__state=state
    
    def erase_repo(self):
        '''
        Sterge lista de note
        '''
        return self.__repo.erase()
    
    def get_note(self):
        '''
        Returneaza toate notele
        '''
        return self.__repo_nota.get_all()
    
    def get_note_lenght(self):
        '''
        Returneaza lungimea listei de note
        '''
        return self.__repo_nota.get_lenght()
    
    def creare_nota(self,student0,problema0,nota0):
        '''
        Functia de creeare a notelor ce are ca parametrii:
        un student, o problema, si o nota(float)
        output : ---
        '''
        
        OK_ID=False
        OK_NRLAB=False
        OK_NRPR=False
        
        for student in self.__repo_student.get_all():
            if student.get_ID()==student0.get_ID():
                OK_ID=True
                
        for problema in self.__repo_problema.get_all():
            if problema.get_nrlab()==problema0.get_nrlab():
                OK_NRLAB=True
        
        for problema in self.__repo_problema.get_all():
            if problema.get_nrpr()==problema0.get_nrpr():
                OK_NRPR=True
        
        if OK_ID == True and OK_NRLAB == True and OK_NRPR == True: 
            nota=Nota(student0,problema0,nota0)
            self.__valid_nota.validate_nota(nota)
            self.__repo_nota.add_nota(nota)
        else:
            raise Exception ("Nu exista un student / o problema cu astfel de ID/NRLAB/NRPR!")

    def sortare_nota(self):
        '''
        Functie ce sorteaza lista de note dupa nota
        '''
        note = self.__repo_nota.get_all()
        for i in range(0,len(note)-1,1):
            for j in range(i+1,len(note),1):
                if note[i].get_nota()<note[j].get_nota():
                    note[i],note[j]=note[j],note[i]
        return note
    
    def sortare_nume(self):
        '''
        Functie ce sorteaza lista de note dupa numele studentului
        '''
        note = self.__repo_nota.get_all()
        for i in range(0,len(note)-1,1):
            for j in range(i+1,len(note),1):
                if note[i].get_student_name()>note[j].get_student_name():
                    note[i],note[j]=note[j],note[i]
        return note
    
    def corigenti(self):
        '''
        Functie ce extrage doar studentii ce au note mai mici decat 5
        '''
        note = self.__repo_nota.get_all()
        for i in range(0,len(note)-1,1):
            for j in range(i+1,len(note),1):
                if note[i].get_nota()<note[j].get_nota():
                    note[i],note[j]=note[j],note[i]
        lista = []
        for nota in note:
            if nota.get_nota()<5:
                lista.append(nota)
        return lista
    
    def greatest_nrlab(self):
        '''
        Functie ce sorteaza lista de note in functie de cele mai mari note la lab-uri
        '''
        laboratoare = [] #lista de laburi
        medie = []       #lista de medii
        medie0 = []      #lista de nrlaburi la o medie
        note = self.__repo_nota.get_all()
        
        for nota in note:
            if nota.get_problema_nrlab() not in laboratoare: #gasim lista de nrlab
                laboratoare.append(nota.get_problema_nrlab())
        
        for i in range(0,len(laboratoare),1):  #initializam lista medie
            medie.append(float(0))
            
        for i in range(0,len(laboratoare),1):  #initializam lista medie0
            medie0.append(float(0))
            
        for nota in note:                      #calculam suma notelor
            for i in range(0,len(laboratoare),1):
                if nota.get_problema_nrlab() == laboratoare[i]: 
                    medie[i]+=float(nota.get_nota())
                    medie0[i]+=float(1)
                    
        for i in range(0,len(medie),1):        #facem media notelor
            medie[i]=medie[i]/medie0[i]
            
            
        for i in range(0,len(medie)-1,1):      #sortam cele doua liste (laboratoare,medie)
            for j in range(i+1,len(medie),1): 
                if medie[i]<medie[j]:
                    laboratoare[i],laboratoare[j]=laboratoare[j],laboratoare[i]
                    medie[i],medie[j]=medie[j],medie[i]
                if medie[i]==medie[j]:
                    if laboratoare[i]>laboratoare[j]:
                        laboratoare[i],laboratoare[j]=laboratoare[j],laboratoare[i]
                        medie[i],medie[j]=medie[j],medie[i]
        
        
        return laboratoare,medie
           
                
            
        
        