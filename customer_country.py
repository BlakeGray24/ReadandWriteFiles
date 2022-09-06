import csv

infile = open('customers.csv','r')

csvfile = csv.reader(infile,delimiter=',')

next(csvfile)  #this skips the first line

outfile = open('customer_country.csv','w')

#writer = csv.writer(outfile,delimiter=',')

x = 1
for record in csvfile:
    outfile.write(record[1] + record[2] + record[4])
    x = x + 1
