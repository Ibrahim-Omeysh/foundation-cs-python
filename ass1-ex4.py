def main():
    list=[]
    n=input('please insert the lenght of your list: ')
    while (not n.isnumeric()):
        n=input('please insert a valid input: ')
    for i in range(0,int(n)):
        num=int(input('please insert your number: ' ))
        list.append(num)
    def even(list1) :
        list2=[]
        for i in range(len(list1)):
         if list1[i]%2==0 :
            list2.append(list1[i])
        return list2
    print( 'input:' , list, ' output:' , even(list))                  
main()