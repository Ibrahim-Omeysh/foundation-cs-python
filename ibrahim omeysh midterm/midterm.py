######-----task1------########## 
   
    ###### First check input url ########

def checkUrl():
    valide_url=False
    while not valide_url:
        url=input("insert the url please: ")
        if (url[0:4]=="www." and url[-4:]==".com"):
            valide_url=True
            return url
        else:
            print("url format must start with ' www. ' and End with ' .com ' please try again \n")

    ######### check title ################

def checkTitle():
    title=input("please, insert title:")
    while  not title.isalpha():
        title=input("please, insert title without special characters:")
    return title
    
    ####### append titel and url ###########

def openTab(data,title,url):
    index=int(len(data)+1)
    data[index]={'Title':title,'Url':url}
    return data




        
def main():
    open_tabs={}
    title=checkTitle()
    url=checkUrl()
    open_tabs=openTab(open_tabs,title,url)
    print(open_tabs)
    

main()