import csv

#infile = open('steps.csv','r')
#csvfile = csv.reader(infile,delimiter=',')

months = ['Janurary','Feburary','March','April','May','June','July','August','September','October','November','December']

outfile = open('avg_steps.csv','w')

writer = csv.writer(outfile,delimiter=',',newline='')

print('Month | Average steps\n')

num=1

for num in range(1,13):

    steps = 0
    avg = 0 
    days = 0

    infile = open('steps.csv','r')
    csvfile = csv.reader(infile,delimiter=',')

    for record in csvfile:
        
        if str(i) == record[0]:  #I need it to add all the steps and then divide it by the total number of days
            steps = steps + int(record[1])
            days = days + 1
            avg = (steps / days)
            
    outfile.write()
    infile.close()

outfile.close()

