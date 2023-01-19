list1=[]
while True:
    print("1.create\n2.read\n3.update\n4.delete")
    option=int(input("enter the option := "))
    if option==1:
        lisst2=[input("enter the name :-"),input("enter the mobile number"),input("enter the password :- "),input("enter the gmail :- ")]
        list1.append(lisst2)
        print("your data ius insert")
    elif option==2:
        mobile=input("enter the same mobile number :- ")
        print("you are reading your data ",list1)
    elif option==3:
        mobile=input("enter the same mobile number :- ")
        choice=int(input("what do you want to update :- \t1.name\n\t\t\t\t2.mobile\n\t\t\t\t3.gmail\n")) 
        if choice==1:
            hun=input("enter new name :- ")
            lisst2[0]=hun
        elif choice==2:
            hun=input("enter new mobile :- ")
            lisst2[1]=hun
        elif choice==3:
            hun=input("enter new email :- ")
            lisst2=3
        else:
            print("nigam aap apni gand marao.....!!!!!")
    elif option==4:
        mobile=input("enter the same mobile number :- ")
        print("your crud has been deleted....!!!")
        list1.remove(lisst2)
        break
    else:
        print("NIGMA kali gaand ki gaand mein lund ...!")






# list1=[]
# while True:
#     print("1.create\n2.read\n3.update\n4.delete")
#     option=int(input("enter the option := "))
#     if option==1:
#         lisst2=[input("enter the name :-"),input("enter the mobile number"),input("enter the password :- "),input("enter the gmail :- ")]
#         list1.append(lisst2)
#         print("your data ius insert")
#     elif option==2:
#         mobile=input("enter the same mobile number :- ")
#         if mobile==lisst2[1]:
#             print("you are reading your data ",list1)
#         else:
#             print("invail input")
#     elif option==3:
#         mobile=input("enter the same mobile number :- ")
#         if mobile==lisst2[1]:
#             choice=int(input("what do you want to update :- \t1.name\n\t\t\t\t2.mobile\n\t\t\t\t3.gmail\n")) 
#             if choice==1:
#                 hun=input("enter new name :- ")
#                 lisst2[0]=hun
#             elif choice==2:
#                 hun=input("enter new mobile :- ")
#                 lisst2[1]=hun
#             elif choice==3:
#                 hun=input("enter new email :- ")
#                 lisst2=3
#             else:
#                 print("nigam aap apni gand marao.....!!!!!")
#         else:
#             print("invaild input")
#     elif option==4:
#         mobile=input("enter the same mobile number :- ")
#         if mobile==lisst2[1]:
#             print("your crud has been deleted....!!!")
#             list1.remove(lisst2)
#             break
#     else:
#         print("NIGMA kali gaand ki gaand mein lund ...!")












