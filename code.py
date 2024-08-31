dict={}

while(1):
    choice = int(input("1 for Adding Contacts \n 2 for Updating Contact Information \n 3 for Deleting Contacts \n 4 for Listing All Contacts \n 5 for Searching Contacts \n 6 for Listing Contacts by Initial Letter \n"))
    if(choice==1):
        phNo = int(input("enter phone number = "))
        name = input("enter your name = ")
        var = int(input("do you want to enter email address if yes type 1 and if no type 0 = "))
        if(var==1):
            email = input("enter email address = ")
            dict={phNo:name, phNo:email}
            print(dict)
        if(var==0):
            dict={phNo:name}
            print(dict)
    if(choice==2):
        a = int(input("if you want to update ph no type 1 else 0 = "))
        if(a==1):
            ophno = int(input("enter current ph no = "))
            uphNo = int(input("enter new ph no = "))
        b = int(input("if you want to update email type 1 else 0 = "))
        if(b==1):
            oemail = input("enter current email = ")
            uemail = input("new email = ")
  
        
    if(choice==3):
        name = input("enter name = ")
      
    if(choice==4):
        print(dict)
    if(choice==5):
        name = input("enter name = ")
        print(dict{phno:name})
        
            
        
