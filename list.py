names=['lisa','meher','fahmida','anna']
choice=0
while True:
    print('1.Add name in a list\n 2.deleta name from the list \n 3.replace a name in the list \n 4, view all name\n 5.press any other number to exit')
    user=int(input('enter your choice'))
    if user ==1 :
        newname=input('enter the name you want to add ')
        names.append(newname)
    if user ==2:
        name=input('enter the name you want to delete ')
        names.remove(name)
    if user ==3:
        replacename=input('enter the name you want to replace from the list ')
        if replacename in names :
            newname=input('enter the new name ')
            index=names.index(replacename)
            names[index]=newname  
        else:
            print('Invalid name')    
    if user ==4:
        print(names) 


