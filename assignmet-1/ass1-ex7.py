def main():
    def creatList():
        list1=[]
# check first value
        n=input('please insert the lenght of your list: ')
        while (not n.isnumeric()):
            n=input('please insert a valid input: ')
# check list number validity
        while (int(len(list1))<int(n) ):
            num=input('please insert the numbers: ')
            if  num.isnumeric():
                list1.append(num)
            else:
                print('Warning this is not a valid number')
        listSort(list1)
        return list1   

# sort list
    def listSort(arr):
        n = len(arr)
        for i in range(n-1):
            for j in range(0, n - i - 1):
                if float(arr[j]) > float(arr[j + 1]):
                     arr[j], arr[j + 1] = arr[j + 1], arr[j]
  
# avrage list
    def avgList(numbs):
        s=0
        l=len(numbs)
        for i in range(l):
            s=s+int(numbs[i])
        return s/l
#  median list
    def medList(numbs):
        m=len(numbs)/2
        if m - int(m)>0:
            return numbs[int(m)]
        else:
            m=int(m) 
            return (float(numbs[m]) + float(numbs[m-1]))/2

# rangelist
    def rangeList(numbs):
        return (int(numbs[len(numbs)-1]) - int(numbs[0]))
    
# modelist
    def modeList(numbs):
        n = len(numbs)
        md1=1
        md2=None
        for i in range(n):
            c=0
            for j in range(i, n):
                if numbs[i]==numbs[j]:
                    c+=1
            if c>md1:
                md1=c
                md2=numbs[i]
        if md2 is None:
            return "none",0
        else:
            return md2, md1  

# variance list 
    def varianceList (numbs):
        m= float(avgList(numbs)) 
        l=len(numbs)
        sumv=0
        x=0
        for i in range(l):
            x=float(numbs[i])-m
            x= x**2
            sumv += x
        sumv = float(sumv/l)
        return sumv            
# Standard Deviation list
    def sdList(numbs):
        return varianceList(numbs)**0.5

# execution
    print ('hello , this program takes a list of numbers as input and calculates their descriptive statistics')
    list1=creatList() 
    n=0      
    while n != 9:
        print('\n1) Enter a new list\n2) Calculate Mean\n3) Calculate Median\n4) Calculate Mode\n5) Calculate Range\n6) Calculate Variance\n7) Calculate Standard Deviation\n8) Print List\n9) Exit')
        n=input('\nplease choose an option: ')
        while (not n.isnumeric()):
            n=input('\nplease insert a valid input: ')
        n=int(n)      
        if n==1:
            list1=creatList()
        elif n==2:
            print('\nThe Mean of this list is :', avgList(list1))
        elif n==3:
            print('\nThe Median of this list is :', medList(list1))
        elif n==4: 
            print('\nThe Mode of this list is :',modeList(list1)[0] ,' has been reapted',modeList(list1)[1] ,'time')
        elif n==5:
            print('\nThe Range of this list is :', rangeList(list1))
        elif n==6:
            print('\nThe Variance of this list is :', varianceList(list1))
        elif n==7:
            print('\nThe Standard Deviation of this list is :',sdList(list1))
        elif n==8:
            print(list1)
        else: 
            exit()
main()        