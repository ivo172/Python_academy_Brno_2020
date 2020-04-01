# Create a program that will generate employee contracts based being given
# the following inputs: - Employee data - Contract type There are three
# different contract types and therefore we need to give our program the name
# of the template it should populate. The program should be intelligent
# enough to know, what data should be populated into which contract type.
# Employee Data: Paste the following dictionary into a text file created
# using text editor and save it under employees.txt. You should remember the
# place where you store it, because you will need to open it in your program.

# {'X12345': {'ID': 'X12345', 'full_name': 'Jack Frank',
#                    'birthdate': '1.1.1970', 'job_title': 'welder',
#                    'position_from': '1.5.2015', 'contract_start': '1.2.2013',
#                    'contract_end': '31.12.2020', 'salary': 123456},
#         'X54321': {'ID': 'X54321', 'full_name': 'Bob Doe',
#                    'birthdate': '8.8.1971', 'job_title': 'machinist',
#                    'position_from': '1.8.2016', 'contract_start': '1.8.2014',
#                    'contract_end': '31.12.2021', 'salary': 23451}}

# Contract templates: Please store the following text templates under the
# corresponding names. Templates can be stored in a separate directory Note
# that the templates need to be adjusted in order Python fill the data into
# correct places in the document: - salary_change.txt - job_change.txt -
# contract_prolongation.txt

import os.path
import json

path = os.path.dirname(__file__)


def add_salary_change(read_text, full_name, id, birthdate, salary):
    # will add new employee in 'salary_change.txt'
    read_text = read_text.replace('{full_name}', full_name)
    read_text = read_text.replace('{ID}', id)
    read_text = read_text.replace('{birthdate}', birthdate)
    read_text = read_text.replace('{salary}', salary)
    return read_text


def add_job_change(read_text, full_name, id, birthdate, job_title,
                   position_from):  # will add new employee in 'job_change.txt'
    read_text = read_text.replace('{full_name}', full_name)
    read_text = read_text.replace('{ID}', id)
    read_text = read_text.replace('{birthdate}', birthdate)
    read_text = read_text.replace('{job_title}', job_title)
    read_text = read_text.replace('{position_from}', position_from)
    return read_text


def add_contract_prolong(read_text, full_name, id, birthdate, contract_end):
    # will add new employee in 'contract_end.txt'
    read_text = read_text.replace('{full_name}', full_name)
    read_text = read_text.replace('{ID}', id)
    read_text = read_text.replace('{birthdate}', birthdate)
    read_text = read_text.replace('{contract_end}', contract_end)
    return read_text


print('Please select the option number of action you want to perform:')
print('0. salary change')
print('1. job change')
print('2. contract prolongation')
index_file = int(input())


with open(path + '\employees.txt', 'r', encoding='utf-8') as employees:
    read_employees = employees.read()
    read_employees = json.loads(read_employees.replace("'", '"')) # convert str in dict

i = 'X12345'

id = read_employees[i]['ID']
full_name = read_employees[i]['full_name']
birthdate = read_employees[i]['birthdate']
job_title = read_employees[i]['job_title']
position_from = read_employees[i]['position_from']
contract_start = read_employees[i]['contract_start']
salary = read_employees[i]['salary']
print(id, full_name, birthdate, job_title, position_from, contract_start, salary)



if index_file == 0: # salary
    with open(path + '\salary_change.txt', 'r', encoding='utf-8') as text:
        read_text = text.read()         # open and read salary_change.txt
    result = add_salary_change(read_text, 'Ivo Marek', '123458', '27.4.1965',
                               '2.550')
    with open(path + '\salary_change_new.txt', 'w', encoding='utf-8') as text:
        text.write(result)              # open and write salary_change_new.txt
elif index_file == 1: # job change
    with open(path + '\job_change.txt', 'r', encoding='utf-8') as text:
        read_text = text.read()         # open and read job_change.txt
    result = add_job_change(read_text, 'Ivo Marek', '123458', '27.4.1965',
                            'mechanik', '27.1.1965')
    with open(path + '\job_change_new.txt', 'w', encoding='utf-8') as text:
        text.write(result)              # open and write job_change_new.txt
elif index_file == 2: # contract prolongation
    with open(path + '\contract_prolongation.txt', 'r', encoding='utf-8') as text:
        read_text = text.read()         # open and read contract_prolong.txt
    result = add_contract_prolong(read_text, 'Ivo Marek', '123458', '27.4.1965',
                                  '31.1.2020')
    with open(path + '\contract_prolong_new.txt', 'w', encoding='utf-8') as text:
        text.write(result)              # open and write job_change_new.txt
else:
    print('Or 0, 1 or 2')
