def main():
    n=input('please enter your iPv4 : ')
    ip=n.split('.')
    if len(ip)!=4:
        print('ip not valid')
    else:
        for i in ip:
            if int(i)>255 or int(i) <0:
                print('invalide ip')
                break

main()