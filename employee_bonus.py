def main():
    import csv

    infile = ('EmployeePay.csv','r')

    csvfile = csv.reader(infile,delimiter=',')
    next(csvfile)


    for i in csvfile:
        #infile.readlines()
    #infile.readline()
    #Repeating structure
        print('ID:',i[0])
        print('Full name:',i[1])
        print('Total salary:',i[3])

        input()

#def cal_total():
    #Calculate total here, location 4 & 5 in the list
main()
