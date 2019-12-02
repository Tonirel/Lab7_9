'''
Created on Nov 13, 2019

@author: Tonirel
'''

from Tests import Tests
from UI import UIStudent,UIProblema,UINota
from Repository import RepositoryStudent, RepositoryProblema, RepositoryNota
from Service import ServiceStudent, ServiceProblema, ServiceNota
from Validate import ValidateStudent, ValidateProblema, ValidateNota
from State import State

def run():
    '''
    Functia ce ruleaza aplicatia
    '''
    
    #repo_file=RepositoryStudentFile('Studenti')
    
    #Initializing State
    state=State()


    #Initializing Student
    valid_student=ValidateStudent()
    repo_student=RepositoryStudent()
    service_student=ServiceStudent(repo_student,valid_student,state)
    ui_student=UIStudent(service_student,state)
    
    #Initializing Problema
    valid_problema=ValidateProblema()
    repo_problema=RepositoryProblema()
    service_problema=ServiceProblema(repo_problema,valid_problema,state)
    ui_problema=UIProblema(service_problema,state)
    
    #Initializing Nota
    valid_nota=ValidateNota()
    repo_nota=RepositoryNota()
    service_nota=ServiceNota(repo_nota,valid_nota,repo_student,repo_problema,state)
    ui_nota=UINota(service_student,service_problema,service_nota,state)
    
    #Initializing Tests
    tests=Tests(service_student,service_problema,repo_student,repo_problema,valid_student,valid_problema,state,repo_nota,service_nota)
    
    #Running Tests
    tests.run_all_tests()
    
    
    commands={
        'meniu studenti':ui_student.UI_studenti_menu,
        'meniu probleme':ui_problema.UI_probleme_menu,
        'meniu note':ui_nota.UI_note_menu
        }
    
    # v--------------ASIGNARE--------------v
    
    service_student.create_student(1 , "Ion" , 211)
    service_student.create_student(2 , "Vasile" , 212)
    service_student.create_student(3 , "George" , 213)
    service_student.create_student(4 , "Istvan" , 214)
    service_student.create_student(5 , "Gigi" , 215)
    
    service_problema.create_problema(1 , 1 , "Descriere 1" , 2)
    service_problema.create_problema(1 , 2 , "Descriere 2" , 2)
    service_problema.create_problema(1 , 3 , "Descriere 3" , 2)
    service_problema.create_problema(2 , 1 , "Descriere 1" , 2)
    service_problema.create_problema(2 , 2 , "Descriere 2" , 2)
    service_problema.create_problema(2 , 3 , "Descriere 3" , 2)
    service_problema.create_problema(3 , 1 , "Descriere 1" , 2)
    service_problema.create_problema(3 , 2 , "Descriere 2" , 2)
    service_problema.create_problema(3 , 3 , "Descriere 3" , 2)
    
    studenti=repo_student.get_all()
    probleme=repo_problema.get_all()
    
    '''service_nota.creare_nota(studenti[0], probleme[2], 10)
    service_nota.creare_nota(studenti[2], probleme[7], 10)
    service_nota.creare_nota(studenti[0], probleme[1], 5)
    service_nota.creare_nota(studenti[1], probleme[5], 10)
    service_nota.creare_nota(studenti[3], probleme[1], 5)
    service_nota.creare_nota(studenti[4], probleme[2], 9)
    service_nota.creare_nota(studenti[3], probleme[3], 2)
    service_nota.creare_nota(studenti[0], probleme[0], 4)'''
    service_nota.creare_nota(studenti[0], probleme[4], 10)
    service_nota.creare_nota(studenti[0], probleme[7], 10)
    service_nota.creare_nota(studenti[0], probleme[4], 9)
    service_nota.creare_nota(studenti[0], probleme[7], 9)
    service_nota.creare_nota(studenti[0], probleme[1], 7)
    service_nota.creare_nota(studenti[0], probleme[2], 6)
    
    # ^--------------ASIGNARE--------------^
    
    while True:
        ui_student.UI_help()
        command=input("Dati comanda: ")
        if command=='exit':
            print("Iesire din aplicatie...")
            return 
        if command in commands:
            try:
                commands[command]()
            except ValueError as ex:
                print(str(ex))
        else:
            print("Comanda invalida")

run()