
import csv

infile = ('EmployeePay.csv','r')

csvfile = csv.reader(infile,delimiter=',')
next(csvfile)

infile.readline()

for record in csvfile:
    print('ID:',record[0])
    print('Full name:',record[1]+' '+record[2])
    print('Total salary:',record[3])

input()