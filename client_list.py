def main():

    infile = open('clients.txt','r')

    x = 1

    for line in infile:
        name = line.rstrip('\n')
        print(x,'. ',name,sep='')
        x = x+1
    infile.close()
main()