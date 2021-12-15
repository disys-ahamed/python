class swiggy:
    def __init__(self):
        self.__name=str(input("enter your first name"))
        self.__lastname=str(input("enter your last name"))
        self.__city=str(input("enter your city name"))
        if(self.__city=="chennai"):
            print("we are available in",self.__city)
        else:
            print("swiggy not available in",self.__city,"swiggy is available in only chennai")
            raise cityerror("cityerror")
        self.__phonenumber=(input("enter 10 digits phone number"))
        if len(self.__phonenumber)==10:
            print("phone number is valid")
        else:
            print("number is invalid")
            raise numbererror("invalid number")
        self.__address=str(input("enter your address"))

    def areas(self):
        print("self.__areas available")
        print("1.Porur\n2.Mannadi\n3.Tnagar\n4.perungudi\n5.Avadi")
        self.__area=int(input("please enter number of the area"))
        if self.__area==1:
            print("hotels available in Porur")
            self.__hotel_availables = [{"hotel":"ambur biryani", "rating":"5-star"},
                             {"hotel":"ibaco", "rating":"4.5-star"},
                             {"hotel":"sri krishna", "rating":"4.3-star"},
                             {"hotel":"A2B", "rating":"4.5-star"}]
            
        elif self.__area==2:
            print("hotels available in Mannadi")
            self.__hotel_availables = [{"hotel":"dindigul biryani", "rating":"5-star"},
                             {"hotel":"arcod biryani", "rating":"4.5-star"},
                             {"hotel":"hotel aryas", "rating":"4.3-star"},
                             {"hotel":"pizza hut", "rating":"4.5-star"}]
        elif self.__area==3:
            print("hotels available in nagar")
            self.__hotel_availables = [{"hotel":"hyderabadi  biryani", "rating":"5-star"},
                             {"hotel":"meat and eat", "rating":"4.5-star"},
                             {"hotel":"dominos", "rating":"4.3-star"},
                             {"hotel":"cfc", "rating":"4.5-star"}]
        elif self.__area==4:
            print("hotels available in perungudi")
            self.__hotel_availables = [{"hotel":"vaniyambadi biryani", "rating":"5-star"},
                             {"hotel":"gourmet", "rating":"4.5-star"},
                             {"hotel":"KFC", "rating":"4.3-star"},
                             {"hotel":"mughal biryani", "rating":"4.5-star"}]
        elif self.__area==5:
            print("hotels available in Avadi")
            self.__hotel_availables = [{"hotel":"thalapakatti biryani", "rating":"5-star"},
                             {"hotel":"muniyandi vilas", "rating":"4.5-star"},
                             {"hotel":"akash appam", "rating":"4.3-star"},
                             {"hotel":"aaa", "rating":"4.5-star"}]
        else:
            print("enter valid number")
            
    
    def display(self):
        for i in self.__hotel_availables:
            f={}
            f=i
            for p,q in f.items():
                print(p,"--",q)
        self.__hotel=str(input("enter hotel name"))
        self.__hotelname=("thalapakatti biryani","muniyandi vilas","akash appam","aaa","vaniyambadi biryani","gourmet","KFC","mughal biryani","hyderabadi biryani","meat and eat","dominos",
                   "cfc","dindigul biryani","arcod biryani","hotel aryas","pizza hut","ambur biryani","ibaco","sri krishna","A2B")
        self.dishes={"mutton biryani:200","dosa:30","chicken biryani:100","parotta:20"}
        for i in self.__hotelname:
            if i ==self.__hotel:
                print(i)
        for i in self.dishes:
            print(i)
        self.__a=200
        self.__b=30
        self.__c=100
        self.__d=20
        self.__foodname=str(input("enter food name"))
        self.__quantity=int(input("enter quantity"))
        if self.__foodname=="mutton biryani":
            self.__totalamount=self.__quantity*self.__a
            print("total amount",self.__totalamount)
        elif self.__foodname=="dosa":
            self.__totalamount=self.__quantity*self.__b
            print("total amount",self.__totalamount)
        elif self.__foodname=="chicken biryani":
            self.__totalamount=self.__quantity*self.__c
            print("total amount",self.__totalamount)
        elif self.__foodname=="parotta":
            self.__totalamount=self.__quantity*self.__d
            print("total amount",self.__totalamount)
        else:
            raise error("enter valid food")
    def Display(self):
        print("|************Order Details*************|")
        print("|Name:",self.__name,"   |")
        print("|--------------------------------------|")
        print("|Address:",self.__address,"   |")
        print("|--------------------------------------|")
        print("|city",self.__city,"   |")
        print("|--------------------------------------|")
        print("|phonenumber",self.__phonenumber)
        print("|--------------------------------------|")
        print("|total bill amount",self.__totalamount,"   |")
        print("|--------------------------------------|")

    def payment(self):
        print("select payment method\n","1.upi\n","2.Cash on delivery")
        self.__method=int(input("enter 1 or 2:"))
        if self.__method==1:
            upi=str(input("enter upi id"))
            if len(upi)>=5:
                pin=str(input("enter pin"))
                if len(pin)==4:
                    print("verification successful")
                else:
                    raise PinError("enter 4 digits of pin")
            else:
                raise UpiError("enter valid upi")
        elif self.__method==2:
            print("thank you")
        else:
            raise error("method error")
        print("YOUR ORDER IS PLACED SUCCESSFULLY")
        print("ORDER WILL BE DELIVERED IN 30 MINS")
        print("****THANK YOU****")
        
            

ahamed=swiggy()
ahamed.areas()
ahamed.display()
ahamed.Display()
ahamed.payment()
