class PhoneBook:
    def __init__(self):
        self.__numberlist=[]
        self.__namelist=[]
        self.__emailList=[]
        self.__DobList=[]
        self.__GroupList=[]
        self.__number=int(input("enter how many phonenumber want to save in phonebook:"))
        for i in range(self.__number):
            self.__name=input("enter your name")
            self.__namelist.append(self.__name)
            self.__phonenumber=input("enter your mobile number")
            if len(self.__phonenumber)==10:
                self.__numberlist.append(self.__phonenumber)
                print("verified")
            else:
                raise NumberError("enter 10 digits ")
            self.__mailid = input("Enter Mail ID :")
            if type(self.__mailid) == str:
                if len(self.__mailid) <25:
                    self.__emailList.append(self.__mailid)
                    print(self.__mailid)
                    print("Email id verified sucessfully \n")
                else:
                    raise TypeError("check your Emailid")
            else:
                raise ValueError("Invalid Email Address")
            self.__dob=str(input("enter date of birth"))
            self.__DobList.append(self.__dob)
            self.__Group=str(input("Enter Group Name"))
            self.__GroupList.append(self.__Group)
            print(self.__namelist,"\n",self.__numberlist,"\n",self.__emailList,"\n",self.__DobList,"\n",self.__GroupList)
            
    def search(self):
        self.SearchName = str(input("\nEnter the name that you to want search : "))

        print("Search result:")

        if self.SearchName in self.__namelist:
            index = self.__namelist.index(self.SearchName)
            self.__phonenumber = self.__numberlist[index]
            self.__mailid = self.__emailList[index]
            self.__dob=self.__DobList[index]
            self.__Group=self.__GroupList[index]
            print("Name:",self.SearchName,"Phone Number:",self.__phonenumber,"Email:",self.__mailid,"Date of Birth:",self.__dob,"Groupname",self.__Group)

        else:
            print("Name Not Found")
            
                    
ahamed=PhoneBook()
ahamed.search()
