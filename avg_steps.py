import csv

#infile = open('steps.csv','r')
#csvfile = csv.reader(infile,delimiter=',')

months = ['0','Janurary','Feburary','March','April','May','June','July','August','September','October','November','December']

outfile = open('avg_steps.csv','w') 
#data_frame=  
#writer = csv.writer(outfile,delimiter=',',newline='')

print('Month | Average steps\n')
outfile.write('Month | Average steps\n')

num=1

for num in range(1,13):

    steps = 0
    avg = 0 
    days = 0

    infile = open('steps.csv','r')

    csvfile = csv.reader(infile, delimiter=',')

    next(csvfile)
    i=1

    for record in csvfile:
        
        if str(i) == record[0]:  #I need it to add all the steps and then divide it by the total number of days
            steps += int(record[1])
            days  += 1

            print(steps)
            print(days)
            print(months[i])

            

        else:
            avg = float(steps/days)

            print('%.0f'% avg)

            avg = str(avg)


            outfile.write(months[i] + ',' + avg)
            
            
            steps = record[i]
            days = i

            #outfile.write(months[i],avg)
            # 
    infile.close()
outfile.close()




