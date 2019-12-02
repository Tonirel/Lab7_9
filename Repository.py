'''
Created on Nov 13, 2019

@author: Tonirel
'''



        
class RepositoryStudent:
    
    def __init__(self):
        self.__studenti = []
        
    
    def get_all(self):
        return self.__studenti
    
    def get_lenght(self):
        return len(self.__studenti)
    
    def erase(self):
        self.__studenti = []
        
    def add_student(self,student):
        '''
        Functie ce adauga studentul - student in lista - studenti
        input: studenti - lista de studenti, student - un student
        output: ---
        '''
        for student0 in self.__studenti:
            if student.get_ID() == student0.get_ID():
                raise Exception ("Acest ID exista deja!")
        self.__studenti.append(student)
 
 
'''class RepositoryStudentFile(RepositoryStudent):
    
    def __init__(self,file_name):
        RepositoryStudent.__init__(self)
        self.__file_name=file_name
        self.load()
        
        
    def create_student_from_line(self,line):
        lines=line.split(" ")
        student=Student(lines[0],lines[1],lines[2])
        return student
        
    def load(self):
        file=open(self.__file_name)
        for line in file:
            if line.strip()=="":
                continue
            
            student = self.create_student_from_line(line)
            
            RepositoryStudent.add_student(self, student)
        file.close()  


    def add_student_file(self,student):
        lista=self.get_all()
        for student0 in lista:
            if student.get_ID() == student0.get_ID():
                raise Exception ("Acest ID exista deja!")
        RepositoryStudent.add_student(self, student)
        self.add_to_file(student)
        
    def add_to_file(self,student):
        file = open(self.__file_name,"a")
        line = str(student.get_ID())+" "+str(student.get_nume())+" "+str(student.get_grup())
        file.write("\n")
        file.write(line)
        file.close()
'''      
        
class RepositoryProblema:
    
    def __init__(self):
        self.__probleme = []
    
    def get_all(self):
        return self.__probleme
    
    def get_lenght(self):
        return len(self.__probleme)
    
    def erase(self):
        self.__probleme = []
        
    def add_problema(self,problema):
        '''
        Functie ce adauga elementul - problema in lista - probleme
        input: probleme - lista problemelor, problema - o problema
        output: ---
        '''
        for problema0 in self.__probleme:
            if problema.get_nrlab() == problema0.get_nrlab() and problema.get_nrpr()== problema0.get_nrpr():
                raise Exception ('Aceasta problema exista deja!\nNumar laborator si numar problema exista deja!')
        self.__probleme.append(problema)

class RepositoryNota:
    
    def __init__(self):
        self.__note = []
        
    def get_all(self):
        return self.__note
    
    def get_lenght(self):
        return len(self.__note)
    
    def erase(self):
        self.__note= []
        
    def add_nota(self,nota):
        '''
        Functia ce adauga o nota in lista notelor
        '''
        self.__note.append(nota)
        