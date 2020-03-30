# Create a program that will generate employee 
# contracts based being given the following inputs:
# - Employee data
# - Contract type
# There are three different contract types and therefore we need to give our program
# the name of the template it should populate. 
# The program should be intelligent enough to know, what data should be populated 
# into which contract type.
# Employee Data:
# Paste the following dictionary into a text file created using text editor 
# and save it under employees.txt. You should remember the place where you store it, 
# because you will need to open it in your program.

{'X12345' : {'ID': 'X12345', 'full_name': 'Jack Frank',
            'birthdate': '1.1.1970' , 'job_title' : 'welder',
            'position_from':'1.5.2015', 'contract_start':'1.2.2013',
            'contract_end':'31.12.2020', 'salary': 123456},
'X54321' : {'ID': 'X54321', 'full_name': 'Bob Doe',
            'birthdate': '8.8.1971' , 'job_title' : 'machinist',
            'position_from':'1.8.2016', 'contract_start':'1.8.2014',
            'contract_end':'31.12.2021', 'salary': 23451}}

# Contract templates:
# Please store the following text templates under the corresponding names. 
# Templates can be stored in a separate directory Note that the templates need to be adjusted 
# in order Python fill the data into correct places in the document:
# - salary_change.txt
# - job_change.txt
# - contract_prolongation.txt

            