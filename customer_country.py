import csv

infile = open('customers.csv','r')

csvfile = csv.reader(infile,delimiter=',')

next(csvfile)  #this skips the first line

outfile = open('customer_country.csv','w',newline='')

#writer = csv.writer(outfile,delimiter=',')


outfile.write('Full name, Country\n')
x = 1
for record in csvfile:
    outfile.write(record[1] +' '+record[2] +','+ record[4]+'\n')
    #list1.append(record[1] + record[2] + record[4])
    x = x + 1
print('Total numvber of customers:',x)
