def main():
    import csv

    infile = open('EmployeePay.csv','r')

    csvfile = csv.reader(infile,delimiter=',')

    next(csvfile)
    
    index = 0
    for i in csvfile:
        print('ID:',i[0])
        print('Full Name:',i[1]+' '+i[2])
        print('Salary: ','$',i[3],sep='')
        print('Bonus: ',float(i[4])*100,' %',sep='')

        totalSal = int(i[3]) * (1 + float(i[4]))


        print('Total Salary: ','$',format(totalSal,'.2f'),sep = '')
        index +=1

        input()
        
        
main()


