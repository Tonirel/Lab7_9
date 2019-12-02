'''
Created on Nov 13, 2019

@author: Tonirel
'''


class UIStudent:
    
    def __init__(self,service,state):
        self.__service=service
        self.__state=state
    
    
    '''def UI_add_random(self):
        nr=int(input("Dati numarul de studenti: "))
        random_name_list=['Ion','Pop','Stefan','Adrian']
        random_ID_list=[]
        random_grup_list=[]
        for i in range (0,10000,1):
            random_ID_list.append(i)
            random_grup_list.append(i)
    
        k=int(0)
        while k<nr:
            ID=choice(random_ID_list)
            nume=choice(random_name_list)
            grup=choice(random_grup_list)
            try:
                self.__service.create_student(ID,nume,grup)
                k+=1
            except Exception:
                pass
    ''' 
          
    def UI_help(self):
        print("")
        print("--------------------MENIU--------------------")
        print("")
        print("meniu studenti : Meniul studentilor")
        print("meniu probleme : Meniul problemelor")
        print("meniu note : Meniul notelor")
        print("exit : Iesire din aplicatie")
        print("")
        
    def UI_help_studenti(self):
        print("")
        print('--------------------MENIU STUDENTI--------------------')
        print("")
        print('print studenti : Optiunea de a printa lista de studenti')
        print('adaugare student : Optiunea de a adauga un student in lista de studenti')
        print('stergere studenti : Optiunea de a sterge toti studentii din lista de studenti')
        print('modificare student : Optiunea de a modifica un student')
        print('cautare student : Optiunea de a cauta studenti dupa ID, nume sau grupa')
        print("return : Iesire din meniul studentiilor")
        print("")
         
    def UI_studenti_menu(self):
        commands={
            "print studenti":self.UI_print_studenti,
            #"print studenti file":self.UI_print_studenti_file,
            "adaugare student":self.UI_add_student,
            #"random":self.UI_add_random,
            "stergere studenti":self.UI_stergere_studenti,
            "modificare student":self.UI_modificare_student,
            "cautare student":self.UI_cautare_student
            }
        while True:
            self.UI_help_studenti()
            command=input("Dati comanda: ")
            if command=='return':
                print("Iesire din meniul studentiilor...")
                return 
            if command in commands:
                try:
                    commands[command]()
                except ValueError as ex:
                    print(str(ex))
            else:
                print("Comanda invalida")
    #from Memory            
    def UI_print_studenti(self):
        print("")
        print("Lista studentilor: ")
        for student in self.__service.get_all():
            print('ID: ',student.get_ID(),', Nume: ',student.get_nume(),', Grup: ',student.get_grup())
    
    #from File  
    '''def UI_print_studenti_file(self):      
        print("")
        print("Lista studentilor: ")
        for student in self.__repo.get_all():
            print('ID: ',student.get_ID(),', Nume: ',student.get_nume(),', Grup: ',student.get_grup())
    '''       
    def UI_stergere_studenti(self):   
        self.__service.erase_repo()
        print("Studentii au fost stersi cu succes!")
    
    def UI_modificare_student(self):
        while True:
            ID=input("Dati ID-ul studentului pe care doriti sa-l modificati: ")
            try:
                ID=int(ID)
                if ID<0:
                    raise Exception ("ID-ul nu poate sa fie negativ!")
                student=self.__service.cautare_student_ID(ID)
                ID=student.get_ID()
            except Exception as ex:
                print(str(ex)) 
            ID0=input("Dati noul id: ")
            nume=input("Dati noul nume: ")
            grup=input("Dati noua grupa: ")
            try:
                ID0=int(ID0)
                grup=int(grup)
                self.__service.modificare_student(ID,ID0,nume,grup)
                print("")
                print("Student modificat cu succes!")
                return
            
            except Exception as ex:
                print(str(ex))  
                 
    def UI_add_student(self):
        while True:
            ID=input('Introduceti ID: ')
            nume=input("Introduceti nume: ")
            grup=input("Introduceti grupa: ")
            try:
                ID=int(ID)
                grup=int(grup)
                self.__service.create_student(ID, nume, grup)
                print("")
                print("Student adaugat cu succes!")
                break
            except Exception as ex:
                print(str(ex))
      
    def UI_cautare_student(self):
        if self.__state.lenght(self.__service.get_all())==0:
            print("Lista studentilor este goala!")
            return
        while True:
            command=input("Alegeti criteriul de cautare(id/nume/grupa): ")
            if command=='id':
                ID=input("Dati ID: ")
                try:
                    ID=int(ID)
                    if ID<0:
                        raise Exception ("ID-ul nu poate sa fie negativ!")
                    student=self.__service.cautare_student_ID(ID)
                    print('ID: ',student.get_ID(),', Nume: ',student.get_nume(),', Grup: ',student.get_grup())
                    break
                except Exception as ex:
                    print(str(ex))
            elif command=='nume':
                nume=input("Dati nume: ")
                try:
                    
                    ok=1
                    for caracter in nume:
                        if (caracter>='A' and caracter<='Z') or (caracter>='a' and caracter <='z') or caracter==' ':
                            ok=1
                        else:
                            ok=0
                            break
                    if ok==0:
                        raise Exception ("Numele poate sa contina doar litere!")
                    lista=self.__service.cautare_student_nume(nume)
                    if self.__state.lenght(lista)==0:
                        print("Nu exista astfel de studenti!")
                    else:
                        for student in lista:
                            print('ID: ',student.get_ID(),', Nume: ',student.get_nume(),', Grup: ',student.get_grup())
                    break
                except Exception as ex:
                    print(str(ex))
            elif command=='grupa':
                grup=input("Dati grupa: ")
                try:
                    grup=int(grup)
                    if grup<0:
                        raise Exception ("Grupa nu poate sa fie nr negativ!")
                    lista=self.__service.cautare_student_grup(grup)
                    if self.__state.lenght(lista)==0:
                        print("Nu exista astfel de studenti!")
                    else:
                        for student in lista:
                            print('ID: ',student.get_ID(),', Nume: ',student.get_nume(),', Grup: ',student.get_grup())
                    break
                except Exception as ex:
                    print(str(ex))
            
    

class UIProblema:
    
    def __init__(self,service,state):
        self.__service=service
        self.__state=state
    
    def UI_help_probleme(self):
        print("")
        print('--------------------MENIU PROBLEME--------------------')
        print("")
        print('print probleme : Optiunea de a printa lista de probleme')
        print('adaugare problema : Optiunea de a adauga o probleme in lista de probleme')
        print('stergere probleme : Optiunea de a sterge toate problemele din lista de probleme')
        print('modificare problema : Optiunea de a modifica o problema')
        print('cautare probleme : Optiunea de a cauta problee dupa nrlab,nrpr,deadline')
        print("return : Iesire din meniul problemelor")
        print("") 
        
    def UI_probleme_menu(self):
        commands={
            "print probleme":self.UI_print_probleme,
            "adaugare problema":self.UI_add_problema,
            "stergere probleme":self.UI_stergere_probleme,
            "modificare problema":self.UI_modificare_probleme,
            "cautare probleme":self.UI_cautare_problema
            }
        while True:
            self.UI_help_probleme()
            command=input("Dati comanda: ")
            if command=='return':
                print("Iesire din meniul problemelor...")
                return 
            if command in commands:
                try:
                    commands[command]()
                except ValueError as ex:
                    print(str(ex))
            else:
                print("Comanda invalida")
                
    def UI_print_probleme(self):
        print("")
        print("Lista problemelor: ")
        for problema in self.__service.get_all():
            print('nrlab: ',problema.get_nrlab(),', nrpr: ',problema.get_nrpr(),', deadline: ',problema.get_deadline())
            print('Descriere: ',problema.get_descriere())
            
    def UI_stergere_probleme(self):   
        self.__service.erase_repo()
        print("Problemele au fost sterse cu succes!") 
    
    def UI_modificare_probleme(self):
        while True:
            nrlab=input("Dati nrlab a problemei pe care doriti sa o modificati: ")
            nrpr=input("Dati nrpr a problemei pe care doriti sa o modificati: ")
            try:
                nrlab=int(nrlab)
                nrpr=int(nrpr)
                if nrlab<0 or nrpr<0:
                    raise Exception ("nrlab si nrpr nu pot sa fie numere negative!")
                problema=self.__service.cautare_problema_nrlab_nrpr(nrlab,nrpr)
                NRLAB=problema.get_nrlab()
                NRPR=problema.get_nrpr()
            except Exception as ex:
                print(str(ex)) 
            nrlab=input("Dati noul nrlab: ")
            nrpr=input("Dati noul nrpr: ")
            descriere=input("Dati noua descriere: ")
            deadline=input("Dati noul deadline: ")
            try:
                nrlab=int(nrlab)
                nrpr=int(nrpr)
                deadline=int(deadline)
                self.__service.modificare_problema(NRLAB,NRPR,nrlab,nrpr,descriere,deadline)
                print("")
                print("Problema modificata cu succes!")
                return
            except Exception as ex:
                print(str(ex))
    
    def UI_add_problema(self):
        while True:
            nrlab=input('Introduceti nrlab: ')
            nrpr=input("Introduceti nrpr: ")
            descriere=input("Introduceti descriere: ")
            deadline=input("Introduceti deadline: ")
            try:
                nrlab=int(nrlab)
                nrpr=int(nrpr)
                deadline=int(deadline)
                self.__service.create_problema(nrlab,nrpr,descriere,deadline)
                print("")
                print("Problema adaugat cu succes!")
                break
            except Exception as ex:
                print(str(ex))
                
    def UI_cautare_problema(self):
        if self.__state.lenght(self.__service.get_all())==0:
            print("Lista problemelor este goala!")
            return
        while True:
            command=input("Alegeti criteriul de cautare(nrlab,nrpr,deadline): ")
            if command=='nrlab':
                nrlab=input("Dati nrlab: ")
                try:
                    nrlab=int(nrlab)
                    if nrlab<0:
                        raise Exception ("nrlab nu poate sa fie negativ!")
                    lista=self.__service.cautare_problema_nrlab(nrlab)
                    break
                except Exception as ex:
                    print(str(ex))
            elif command=='nrpr':
                nrpr=input("Dati nrpr: ")
                try:
                    nrpr=int(nrpr)
                    if nrpr<0:
                        raise Exception ("nrpr nu poate sa fie negativ!")
                    lista=self.__service.cautare_problema_nrpr(nrpr)
                    break
                except Exception as ex:
                    print(str(ex))
            elif command=='deadline':
                deadline=input("Dati deadline: ")
                try:
                    deadline=int(deadline)
                    if deadline<0:
                        raise Exception ("deadline nu poate sa fie negativ!")
                    lista=self.__service.cautare_problema_deadline(deadline)
                    break
                except Exception as ex:
                    print(str(ex))
            else:
                print("Criteriu invalid!")
        if self.__state.lenght(lista)==0:
            print("Nu exista astfel de probleme!")
        else:
            for problema in lista:
                print('nrlab: ',problema.get_nrlab(),', nrpr: ',problema.get_nrpr(),', deadline: ',problema.get_deadline())
                print('Descriere: ',problema.get_descriere())

class UINota:
    
    def __init__(self,service_student,service_problema,service_nota,state):
        self.__service_student = service_student
        self.__service_problema = service_problema
        self.__service_nota = service_nota
        self.__state = state

    def UI_help_note(self):
        print("")
        print('--------------------MENIU NOTE--------------------')
        print("")
        print("print note : Optiunea de a printa toate notele")
        print("asignare nota : Optiunea de a adauga o nota")
        print("sortare nume : Optiunea de a sorta studentii dupa nume (alfabetic)")
        print("sortare nota: Optiunea de a sorta studentii dupa nota (descrescator)")
        print("studenti corigenti: Optiunea de a selecta toti studentii cu note mai mici decat 5")
        print("laborator: Optiunea de a sorta nrlab cu cele mai mari note")
        print("return : Iesire din meniul notelor...")
        print("")
        
    def UI_note_menu(self):
        
        commands={
            'print note':self.UI_print_note,
            'asignare nota':self.UI_asignare_nota,
            'sortare nume':self.UI_sortare_nume,
            'sortare nota':self.UI_sortare_nota,
            'studenti corigenti':self.UI_corigent,
            'laborator':self.UI_greatest_nrlab
            }
        
        while True:
            self.UI_help_note()
            command=input("Dati comanda: ")
            if command=='return':
                print("Iesire din meniul notelor...")    
                return
            if command in commands:
                try:
                    commands[command]()
                except Exception as ex:
                    print(str(ex))
            else:
                print("Comanda invalida!")
                
    def UI_print_note(self):
        if self.__service_nota.get_note_lenght()==0:
            print("")
            print("Nu exista note!")
            return 
        print('Lista Notelor: ')
        print("")
        for nota in self.__service_nota.get_note():
            print('Student name:',nota.get_student_name(), ' , Numar Laborator:', nota.get_problema_nrlab(), \
                  ' , Numar problema:', nota.get_problema_nrpr(), ' , Nota:',nota.get_nota())
        
    def UI_asignare_nota(self):
        while True:
            ID_student=input("Dati ID-ul studentului: ")
            NRLAB_problema=input("Dati nrlab a problemei: ")
            NRPR_problema=input("Dati nrpr a problemei: ")
            nota=input("Dati nota: ")
            try:
                ID_student=int(ID_student)
                NRLAB_problema=int(NRLAB_problema)
                NRPR_problema=int(NRPR_problema)
                nota=float(nota)
                student=self.__service_student.cautare_student_ID(ID_student)
                problema=self.__service_problema.cautare_problema_nrlab_nrpr(NRLAB_problema,NRPR_problema)
                self.__service_nota.creare_nota(student,problema,nota)
                print("Nota asignata cu succes!")
                return
            except Exception as ex:
                print(str(ex))
            cmd=input("Incercati din nou? (da/nu): ")
            if cmd == 'nu':
                return
            
    def UI_sortare_nota(self):
        if self.__service_nota.get_note_lenght()==0:
            print("")
            print("Nu exista note!")
            return 
        lista = self.__service_nota.sortare_nota()
        for nota in lista:
            print('Student name:',nota.get_student_name(), ' , Numar Laborator:', nota.get_problema_nrlab(), \
                  ' , Numar problema:', nota.get_problema_nrpr(), ' , Nota:',nota.get_nota())
            
    def UI_sortare_nume(self):
        if self.__service_nota.get_note_lenght()==0:
            print("")
            print("Nu exista note!")
            return 
        lista = self.__service_nota.sortare_nume()
        for nota in lista:
            print('Student name:',nota.get_student_name(), ' , Numar Laborator:', nota.get_problema_nrlab(), \
                  ' , Numar problema:', nota.get_problema_nrpr(), ' , Nota:',nota.get_nota())
            
    def UI_corigent(self):
        if self.__service_nota.get_note_lenght()==0:
            print("")
            print("Nu exista note!")
            return 
        lista = self.__service_nota.corigenti()
        for nota in lista:
            print('Student name:',nota.get_student_name(), ' , Numar Laborator:', nota.get_problema_nrlab(), \
                  ' , Numar problema:', nota.get_problema_nrpr(), ' , Nota:',nota.get_nota())
            
    def UI_greatest_nrlab(self):
        if self.__service_nota.get_note_lenght()==0:
            print("")
            print("Nu exista note!")
            return
        laboratoare,medie = self.__service_nota.greatest_nrlab()
        for i in range(0,len(laboratoare),1):
            print("Nrlab:",laboratoare[i],"are media:",medie[i])
            
            
            