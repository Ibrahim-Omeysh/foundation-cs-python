import requests
import validators
import json

######-----task1: open tab------########## 
   
    ###### First check input url ########

def checkUrl():
    valide_url=False
    while not valide_url:
        url=input("Please insert the url  : ")
        url="http://"+url
        validation=validators.url(url)##### return true if valid url #####
        if validation:
             valide_url=True
             print(url)
             return url
        else:
             print(" -url you entered is not valid or input format is wrong ,please try again \n -check if url start with (www.) and end with (.com .lb .gov ext....)\n -you don't have to write https:// if you try to ")

    ######### check title ################

def checkTitle():
    title=input("please, insert title:")
    while  not title.isalnum():
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

def checkIndexexist(data,index):##### check if index exist in data #####
    index=int(index)
    if index > 0 and index <= len(data):
        return True
    else:
        print("index no found")

    ############# close tab ##########
def closeTab(data,index):
    if index =="":
        data.pop(len(data)-1)
        print( '\n last tab closed successfully ')
    else:
        c=checkIndexexist(data,index)
        index=int(index)
        if c==True:
             index+=-1
             del data[index]
             print("tab at index", index-1,"closed successfully")
    return data


########## ----------- third task : switch tabs -----------####################

def switchTab(data,index):
    if index=="":   ####### display the last url###############
         url_to_display="http://"+data[int(len(data))]["Url"]
         html_content=requests.get(url_to_display)
         print(html_content.text)
    else:
        c=checkIndexexist(data,index)
        if c==1:
             url_to_display="http://"+data[int(index)]["Url"]
             html_content=requests.get(url_to_display)
             print(html_content.text)
        else:
             print("index not found , please try again")

####### ----------- fourth task : display all tabs-----------###########

def displayAllTabs(data):
    for tab in data:
        print("-Title-:",tab["Title"])
        if "NestedTabs" in tab:
            for nestedtab in tab["NestedTabs"]:
                print("       Nested tab : " , "-Title-:", nestedtab['Title'])

######### ------------ fifth task: create nested tabs --------- ############

def creatNestedTabs(data,index,title,url):
    new_tab={"Title": title, "Url": url}
    lastindex=len(data)-1
    if index=="":
        if len(data[lastindex])==2:
             data[lastindex]["NestedTabs"]=[new_tab]
        else:
             data[lastindex]["NestedTabs"].append(new_tab)
    else:
        index=int(index)-1
        if len(data[index])==2:
             data[index]["NestedTabs"]=[new_tab]
        else:
             data[index]["NestedTabs"].append(new_tab)
    return data

######## ----------- six task : clear all tabs ----------------#########

def clearAllTabs(data):
    data.clear()
    print("all opened tabs are closed succefuly")
    return data

####### --------------- seven task : save tabs to json file ----------################

def saveTabs(data,filepath):
    jsondata=json.dumps(data,indent=1)
    with open (filepath ,'w') as filetosave:
        filetosave.write(jsondata)

########## ------------ final task :  read from file ---------------##################
def  readfromfile(filepath):
    with open(filepath,'r') as readfile:
        jsondata=json.load(readfile)
    print("importing data from file finished")
    return jsondata
        
############## --------------- display menu ---------------------###################
def displayMenu():
    n=0
    print('\n1) Open Tab \n2) Close Tab\n3) Switch Tab \n4)  Display All Tabs\n5) Open Nested Tab \n6) Clear All Tabs \n7) Save Tabs \n8) Import Tabs \n 9) Exit')
    print('\n please choose an option: ')
    while not n.isnumeric():
        n=input("please insert number between 1 and 9 : ")
        while n!=9:

            if n==1:
                title=checkTitle()
                url=checkUrl()
                open_tabs=openTab(open_tabs,title,url)
                print(" tab added successfully :D ")

            if n==2:
                index=checkNumericIndex()
                open_tabs=closeTab(open_tabs,index)
                


     
def main():
    open_tabs=[{'Title': 'microsoft', 'Url': 'www.microsoft.com'},
                {'Title': 'git', 'Url': 'www.github.com'},
                {'Title': 'python', 'Url': 'www.python.org',"NestedTabs":[{'Title': 'w3school', 'Url': 'www.w3school.com'},{'Title': 'git', 'Url': 'www.github.com'}]},
                {'Title': 'youtube', 'Url': 'www.youtube.com'}]
    
    # print(open_tabs)
    #index=checkNumericIndex()
    # closeTab(open_tabs,index)
    # switchTab(open_tabs,index)
    #displayAllTabs(open_tabs)
    #open_tabs=creatNestedTabs(open_tabs,index,title,url)
    #displayAllTabs(open_tabs)
    # clearAllTabs(open_tabs)
    #saveTabs(open_tabs,'C:/Users/Barho/OneDrive/Documents/GitHub/foundation-cs-python/ibrahim omeysh midterm/tabsjson.json')
    print(readfromfile('C:/Users/Barho/OneDrive/Documents/GitHub/foundation-cs-python/ibrahim omeysh midterm/tabsjson.json'))

main()