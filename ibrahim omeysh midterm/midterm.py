######-----task1: open tab------########## 
   
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
    
    ####### append title and url ###########

def openTab(data,title,url):
    index=int(len(data)+1)
    data[index]={'Title':title,'Url':url}
    return data

#########-------second task : close tab-------###########

    ####### checking index #########
def checkNumericIndex():
    index=input("insert index:")
    if index =="":
        return index
    while not index.isdigit():
        index=input('please, insert a numeric index: ')
    return index

def checkIndex(data,index):
    c=0
    for key in data:
        if key==int(index):
            c=1
    return c

    ############# close tab ##########

def closeTab(data,index):
    if index =="":
        data.popitem()
    else:
        c=checkIndex(data,index)
        if c==1:
             data.pop(int(index))
        else:
            print("index not found , please try again")
            
    print(data)



        
def main():
    open_tabs={1: {'Title': 'microsoft', 'Url': 'www.microsoft.com'},
               2: {'Title': 'git', 'Url': 'www.github.com'},
               3: {'Title': 'hacker', 'Url': 'www.hackerrank.com'}}
    title=checkTitle()
    url=checkUrl()
    open_tabs=openTab(open_tabs,title,url)
    print(open_tabs)
    index=checkNumericIndex()

    closeTab(open_tabs,index)
    

main()