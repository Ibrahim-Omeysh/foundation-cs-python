def main():
    n=input('please insert a number > 0: ')
    while (not n.isnumeric()):
        n=input('please insert a valid input: ')
    def div(x):
        x=int(x)
        d=[]
        str='all the number can divide 0 be smart :P'
        if x==1: return 1
        elif x==0: return str
        else:
            for i in range(1,x//2):
                if (x % i)==0:
                    d.append(i)
        return d 
    print('the numbers that can devide', n ,'is:',div(n))
main()