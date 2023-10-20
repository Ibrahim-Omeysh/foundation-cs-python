def main():
    n=input('please insert your words: ')
    def reverseString(m):
         x=""
         for i in reversed (range(0,len(m))):
            x=x+m[i]
         return x
    print(reverseString(n))
main()