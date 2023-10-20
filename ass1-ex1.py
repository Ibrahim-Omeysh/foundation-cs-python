def main():
    n=input('please insert a number > 0: ')
    while (not n.isnumeric()):
        n=input('please insert a valid input: ')

    def fact(x):
        x=int(x)
        if x==1 or x==0 :
             return 1
        else:
            return (x*fact(x-1))
    
    print('the factoriel of' ,n, 'is =',fact(n))
main()