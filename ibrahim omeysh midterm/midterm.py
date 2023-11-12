import requests

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
     new_tab={'Title':title,'Url':url}
     data.append(new_tab)
     return data

#########-------second task : close tab-------###########

    ####### checking index #########

def checkNumericIndex():##### cheking input########
    index=input("insert index:")
    if index =="":
        return index
    while not index.isdigit():
        index=input('please, insert a numeric index: ')
    return index

def checkIndex(data,index):##### check if index exist in data #####
    index=int(index)
    if index > 0 and index <= len(data):
        return True
    else:
        print("index no found")

    ############# close tab ##########

def closeTab(data,index):
    if index =="":
        data.pop(len(data)-1)
    else:
        c=checkIndex(data,index)
        index=int(index)
        if c==True:
             index+=-1
             del data[index]
            
    print(data)

########## ----------- third task : switch tabs -----------####################

def switchTab(data,index):
    if index=="":   ####### display the last url###############
        url_to_display="http://"+data[int(len(data))]["Url"]
        html_content=requests.get(url_to_display)
        print(html_content.text)
    else:
        c=checkIndex(data,index)
        if c==1:
            url_to_display="http://"+data[int(index)]["Url"]
            html_content=requests.get(url_to_display)
            print(html_content.text)
        else:
            print("index not found , please try again")

####### ----------- fourth task : display all tabs-----------###########

def displayAllTabs(data):
    for tab in data:
        print("-Title-:",tab["Title"],"-Url-:", tab["Url"])
        if "nestedtab" in tab:
            for nestedtab in tab["nestedtab"]:
                print("       nested tab :  ", "-Title-:",nestedtab["Title"], "-Url-:",nestedtab["Url"],)

######### ------------ fifth task: creat nested tabs --------- ############

def creatNestedTabs(data,index,title,url):
    new_tab={'Title': title, 'Url': url}
    data[1]["NestedTab"]=new_tab


     
def main():
    open_tabs=[{'Title': 'microsoft', 'Url': 'www.microsoft.com'},
                {'Title': 'git', 'Url': 'www.github.com'},
                {'Title': 'hacker', 'Url': 'www.python.org',"nestedtab":[{'Title': 'dfgger', 'Url': 'www.dfggdf.com'},{'Title': 'git', 'Url': 'www.github.com'}]},
                {'Title': 'midgdfcrosoft', 'Url': 'www.dfgdfggf.com'}]
    # title=checkTitle()
    # url=checkUrl()
    # open_tabs=openTab(open_tabs,title,url)
    # print(open_tabs)
    # index=checkNumericIndex()
    #closeTab(open_tabs,index)
    # switchTab(open_tabs,index)
    # displayAllTabs(open_tabs)
    

main()