'''
Created on Nov 13, 2019

@author: Tonirel
'''

from Domain import Student,Problema, Nota


class Tests:
    def __init__(self,service_student,service_problema,repo_student,repo_problema,valid_student,valid_problema,state,repo_nota,service_nota):
        self.__service_student=service_student
        self.__service_problema=service_problema
        self.__repo_student=repo_student
        self.__repo_problema=repo_problema
        self.__validate_student=valid_student
        self.__validate_problema=valid_problema
        self.__state=state
        self.__repo_nota=repo_nota
        self.__service_nota=service_nota
        
    def run_all_tests(self):
        
        self.test_create_state()
        self.test_ServiceStudent()
        self.test_ServiceProblema()
        self.test_validate_student()
        self.test_validate_problema()
        self.test_repository_student()
        self.test_repository_problema()
        self.test_cautare_student_ID()
        self.test_cautare_student_nume()
        self.test_cautare_student_grup()
        self.test_cautare_problema_nrlab()
        self.test_cautare_problema_nrlab_nrpr()
        self.test_cautare_problema_deadline()
        self.test_adaugare_nota()
        self.test_service_nota_adaugare_nota()
        self.test_service_nota_sortare_nota()
        self.test_service_nota_sortare_nume()
        self.test_service_corigenti()
        
        #Stergem repo-urile ca sa nu apara probleme...
        self.__repo_student.erase()
        self.__repo_problema.erase()
        self.__repo_nota.erase()
        
    def test_create_state(self):
        s1=[]
        s=self.__state.create_state()
        assert s==s1
    
    def test_ServiceStudent(self):
        
        #create_student
        student0=Student(10,'John',216)
        ID=10
        nume='John'
        grup=216
        self.__service_student.create_student(ID, nume, grup)
        studenti=self.__repo_student.get_all()
        assert studenti[0].get_ID()==student0.get_ID()
        assert studenti[0].get_nume()==student0.get_nume()
        assert studenti[0].get_grup()==student0.get_grup()
        
        #add_student
        studenti=self.__state.create_state()
        ID=11
        nume='John'
        grup=216
        self.__service_student.create_student(ID, nume, grup)
        studenti=self.__repo_student.get_all()
        studenti0=self.__repo_student.get_all()
        assert studenti==studenti0
        
    def test_ServiceProblema(self):
        #create_problema
        problema0=Problema(1,2,'aef',3)
        self.__service_problema.create_problema(1,2,'aef',3)
        probleme=self.__repo_problema.get_all()
        assert probleme[0].get_nrlab()==problema0.get_nrlab()
        assert probleme[0].get_nrpr()==problema0.get_nrpr()
        assert probleme[0].get_descriere()==problema0.get_descriere()
        assert probleme[0].get_deadline()==problema0.get_deadline()
        
        #add_problema
        probleme=self.__state.create_state()
        self.__service_problema.create_problema(3,4,'aef',5)
        probleme=self.__repo_student.get_all()
        probleme0=self.__repo_student.get_all()
        assert probleme[0]==probleme0[0]
        
    def test_validate_student(self):
        
        self.__service_student.create_student(16,'John',216)
        studenti=self.__repo_student.get_all()
        student=studenti[0]
        
        self.__validate_student.validate_student(student)
        student.set_ID(-3)
        try:
            self.__validate_student.validate_student(student)
            assert False
        except Exception as ex:
            assert str(ex)=="ID incorect!"
        student.set_ID(10)
        student.set_nume('Mirc3a')
        try:
            self.__validate_student.validate_student(student)
            assert False
        except Exception as ex:
            assert str(ex)=="Numele poate sa contina doar litere!"
        student.set_nume('John')
        student.set_grup(-24)
        try:
            self.__validate_student.validate_student(student)
            assert False
        except Exception as ex:
            assert str(ex)=="Grupa incorecta!"
    
    def test_validate_problema(self):
        nrlab=6
        nrpr=2
        descriere='descriere0'
        deadline=2
        self.__service_problema.create_problema(nrlab, nrpr, descriere, deadline)
        probleme=self.__repo_problema.get_all()
        problema=probleme[0]
        
        self.__validate_problema.validate_problema(problema)
        problema.set_nrlab(-43)
        try:
            self.__validate_problema.validate_problema(problema)
            assert False
        except Exception as ex:
            assert str(ex)=="Numar laborator incorect!"
        problema.set_nrlab(1)
        problema.set_nrpr(-8)
        try:
            self.__validate_problema.validate_problema(problema)
            assert False
        except Exception as ex:
            assert str(ex)=="Numar problema incorect!"
        problema.set_nrpr(2)
        problema.set_deadline(-123)
        try:
            self.__validate_problema.validate_problema(problema)
            assert False
        except Exception as ex:
            assert str(ex)=="Deadline incorect!"
            
    def test_repository_student(self):
        ID=20
        nume='John'
        grup=216
        self.__service_student.create_student(ID, nume, grup)
        try:
            self.__service_student.create_student(ID,nume,grup)
            assert False
        except Exception as ex:
            assert str(ex)=='Acest ID exista deja!' 
    
    def test_repository_problema(self):
        nrlab=67
        nrpr=2
        descriere='Descriere1'
        deadline=2
        self.__service_problema.create_problema(nrlab, nrpr, descriere, deadline)
        try:
            self.__service_problema.create_problema(nrlab, nrpr, descriere, deadline)
            assert False
        except Exception as ex:
            assert str(ex)=='Aceasta problema exista deja!\nNumar laborator si numar problema exista deja!'
               
    def test_cautare_student_nume(self):
        ID=87
        nume='John'
        grup=216
        self.__repo_student.erase()
        self.__service_student.create_student(ID, nume, grup)
        studenti=self.__repo_student.get_all()
        studenti0=self.__service_student.cautare_student_nume('John')
        assert studenti==studenti0
        
    def test_cautare_student_ID(self):
        ID=87
        nume='John'
        grup=216
        self.__repo_student.erase()
        self.__service_student.create_student(ID, nume, grup)
        studenti=self.__repo_student.get_all()
        student=studenti[0]
        student0=self.__service_student.cautare_student_ID(87)
        assert student==student0
    
    def test_cautare_student_grup(self):
        ID=87
        nume='John'
        grup=216
        self.__repo_student.erase()
        self.__service_student.create_student(ID, nume, grup)
        studenti=self.__repo_student.get_all()
        studenti0=self.__service_student.cautare_student_grup(216)
        assert studenti==studenti0
        
    def test_cautare_problema_nrlab(self):
        nrlab=1
        nrpr=2
        descriere='Descriere1'
        deadline=2
        self.__repo_problema.erase()
        self.__service_problema.create_problema(nrlab,nrpr,descriere,deadline)
        probleme=self.__repo_problema.get_all()
        probleme0=self.__service_problema.cautare_problema_nrlab(1)
        assert probleme==probleme0
    
    def test_cautare_problema_nrlab_nrpr(self):
        nrlab=1
        nrpr=2
        descriere='Descriere1'
        deadline=3
        self.__repo_problema.erase()
        self.__service_problema.create_problema(nrlab,nrpr,descriere,deadline)
        probleme=self.__repo_problema.get_all()
        probleme0=self.__service_problema.cautare_problema_nrpr(2)
        assert probleme==probleme0
        
    def test_cautare_problema_deadline(self):
        nrlab=1
        nrpr=2
        descriere='Descriere1'
        deadline=3
        self.__repo_problema.erase()
        self.__service_problema.create_problema(nrlab,nrpr,descriere,deadline)
        probleme=self.__repo_problema.get_all()
        probleme0=self.__service_problema.cautare_problema_deadline(3)
        assert probleme==probleme0
        
    def test_adaugare_nota(self):
        self.__repo_nota.erase()
        student=Student(1,'Ion',2)
        problema=Problema(1,2,'ceva',3)
        nota0=10
        nota=Nota(student,problema,nota0)
        s=self.__state.create_state()
        self.__state.add(s,nota)
        self.__repo_nota.add_nota(nota)
        assert s==self.__repo_nota.get_all()
        self.__repo_nota.erase()
        
    def test_service_nota_adaugare_nota(self):
        self.__repo_nota.erase()
        student=Student(1,'Ion',2)
        problema=Problema(1,2,'ceva',3)
        nota0=10
        self.__repo_student.erase()
        self.__repo_problema.erase()
        self.__repo_student.add_student(student)
        self.__repo_problema.add_problema(problema)
        nota=Nota(student,problema,nota0)
        self.__service_nota.creare_nota(student,problema,nota0)
        s=self.__state.create_state()
        self.__state.add(s,nota)
        s0=self.__repo_nota.get_all()
        assert s[0].get_student_ID()==s0[0].get_student_ID()
        assert s[0].get_problema_nrpr()==s0[0].get_problema_nrpr()
        assert s[0].get_problema_nrlab()==s0[0].get_problema_nrlab()
        assert s[0].get_nota()==s0[0].get_nota()
        self.__repo_student.erase()
        self.__repo_problema.erase()
        self.__repo_nota.erase()
        
    def test_service_nota_sortare_nota(self):
        self.__repo_nota.erase()
        student=Student(1,'Ion',2)
        problema=Problema(1,2,'ceva',3)
        nota0=10
        nota1=7
        self.__repo_student.erase()
        self.__repo_problema.erase()
        self.__repo_student.add_student(student)
        self.__repo_problema.add_problema(problema)
        s=self.__state.create_state()
        self.__service_nota.creare_nota(student,problema,nota0)
        nota=Nota(student,problema,nota0)
        self.__state.add(s,nota)
        nota=Nota(student,problema,nota1)
        self.__state.add(s,nota)
        self.__service_nota.creare_nota(student,problema,nota1)
        s0 = self.__service_nota.sortare_nota()
        assert s[0].get_student_ID()==s0[0].get_student_ID()
        assert s[0].get_problema_nrpr()==s0[0].get_problema_nrpr()
        assert s[0].get_problema_nrlab()==s0[0].get_problema_nrlab()
        assert s[0].get_nota()==s0[0].get_nota()
        self.__repo_student.erase()
        self.__repo_problema.erase()
        self.__repo_nota.erase()
        
    def test_service_nota_sortare_nume(self):
        self.__repo_nota.erase()
        student=Student(1,'Ion',2)
        student0=Student(2,'Vasile',3)
        problema=Problema(1,2,'ceva',3)
        nota0=10
        nota1=7
        self.__repo_student.erase()
        self.__repo_problema.erase()
        self.__repo_student.add_student(student)
        self.__repo_problema.add_problema(problema)
        s=self.__state.create_state()
        nota=Nota(student,problema,nota0)
        self.__service_nota.creare_nota(student,problema,nota0)
        self.__state.add(s,nota)
        nota=Nota(student0,problema,nota1)
        self.__state.add(s,nota)
        self.__service_nota.creare_nota(student,problema,nota1)
        s0 = self.__service_nota.sortare_nume()
        assert s[0].get_student_ID()==s0[0].get_student_ID()
        assert s[0].get_problema_nrpr()==s0[0].get_problema_nrpr()
        assert s[0].get_problema_nrlab()==s0[0].get_problema_nrlab()
        assert s[0].get_nota()==s0[0].get_nota()
        self.__repo_student.erase()
        self.__repo_problema.erase()
        self.__repo_nota.erase()
        
    def test_service_corigenti(self):
        self.__repo_nota.erase()
        student=Student(1,'Ion',2)
        problema=Problema(1,2,'ceva',3)
        nota0=10
        nota1=4
        self.__repo_student.erase()
        self.__repo_problema.erase()
        self.__repo_student.add_student(student)
        self.__repo_problema.add_problema(problema)
        
        s=self.__state.create_state()
        nota=Nota(student,problema,nota1)
        self.__service_nota.creare_nota(student,problema,nota0)
        self.__state.add(s,nota)
        self.__service_nota.creare_nota(student,problema,nota1)
        s0 = self.__service_nota.corigenti()
        assert s[0].get_student_ID()==s0[0].get_student_ID()
        assert s[0].get_problema_nrpr()==s0[0].get_problema_nrpr()
        assert s[0].get_problema_nrlab()==s0[0].get_problema_nrlab()
        assert s[0].get_nota()==s0[0].get_nota()
        self.__repo_student.erase()
        self.__repo_problema.erase()
        self.__repo_nota.erase()
        
    