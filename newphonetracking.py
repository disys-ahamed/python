class phonetracking:
    def __init__(self):
        self.__work ={"time_spent":eval(input("enter time that you spent for work in mins"))}
        if type(self.__work["time_spent"])== int:
            print("success")
        else:
            raise TypeError("Error made")
        self.__whatsapp   = {"time_spent":int(input("enter whatsapp used time in mins")), "notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__Instagram ={"time_spent":int(input("enter insta used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__Snapchat  = {"time_spent":int(input("enter Snapchat used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__Phone     ={"time_spent":int(input("enter phone used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__Youtube   ={"time_spent":int(input("enter youtube used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
    def display(self):
        print("Time spent in sunday \n")
        print("work or study ; ",self.__work["time_spent"],"mins spent")
        print("whatsapp ; ",self.__whatsapp["time_spent"],"mins used")
        print("Snapchat ;",self.__Snapchat["time_spent"],"mins used")
        print("Instagram ;",self.__Instagram["time_spent"],"mins used")
        print("Youtube ;",self.__Youtube["time_spent"],"mins used")
        print("Phone ;",self.__Phone["time_spent"],"mins used","\n")
        print("Notification recived in sunday \n")
        print("whatsapp ;",self.__whatsapp["notification_recived"],"notification received")
        print("Snapchat ;",self.__Snapchat["notification_recived"],"notification received")
        print("Instagram ;",self.__Instagram["notification_recived"],"notification received")
        print("Youtube ;",self.__Youtube["notification_recived"],"notification received")
        print("Phone ;",self.__Phone["notification_recived"],"notification received","\n")
        print("data usage in sunday \n")
        print("whatsapp ;",self.__whatsapp["data used"],"mb data used")
        print("Snapchat ;",self.__Snapchat["data used"],"mb data used")
        print("Instagram ;",self.__Instagram["data used"],"mb data used")
        print("Youtube;",self.__Youtube["data used"],"mb data used")
        print("Phone ;",self.__Phone["data used"],"mb data used","\n")
        self.a=(self.__Phone["time_spent"]+self.__whatsapp["time_spent"]+self.__Snapchat["time_spent"]+self.__Instagram["time_spent"]+self.__Youtube["time_spent"])
        self.b=(self.__whatsapp["data used"]+self.__Snapchat["data used"]+self.__Instagram["data used"]+self.__Youtube["data used"]+self.__Phone["data used"])
        print("total time spend for entertainment",self.a)
        print("total data used",self.b)
        if(self.__work["time_spent"]==self.a):
            print("you have spent equal time ")
        elif(self.__work["time_spent"]>self.a):
            print("you have spent more time on work ")
        else:
            print("try to more concentrate on work than entertainment")
            
    def monday(self):
        self.__whatsapp   = {"time_spent":int(input("enter whatsapp used time in mins")), "notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__Instagram ={"time_spent":int(input("enter insta used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__Snapchat  = {"time_spent":int(input("enter Snapchat used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__Phone     ={"time_spent":int(input("enter phone used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__work ={"time_spent":eval(input("enter time that you spent for work in mins"))}
        if type(self.__work["time_spent"])== int:
            print("success")
        else:
            raise TypeError("Error made")
        self.__Youtube   ={"time_spent":int(input("enter youtube used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
    def views(self):
        print("Time used  in monday \n")
        print("work or study ; ",self.__work["time_spent"],"mins spent")
        print("whatsapp ;",self.__whatsapp["time_spent"],"mins used")
        print("Snapchat ;",self.__Snapchat["time_spent"],"mins used")
        print("Instagram ;",self.__Instagram["time_spent"],"mins used")
        print("Youtube ;",self.__Youtube["time_spent"],"mins used")
        print("Phone ;",self.__Phone["time_spent"],"mins used","\n")
        print((self.__Phone["time_spent"],"mins used")+(self.__whatsapp["time_spent"],"mins used"))
        print("Notification recived in a day \n")
        print("whatsapp ;",self.__whatsapp["notification_recived"],"notification received")
        print("Snapchat ;",self.__Snapchat["notification_recived"],"notification received")
        print("Instagram ;",self.__Instagram["notification_recived"],"notification received")
        print("Youtube ;",self.__Youtube["notification_recived"],"notification received")
        print("Phone ;",self.__Phone["notification_recived"],"notification received","\n")
        print("data usage in a day \n")
        print("whatsapp ;",self.__whatsapp["data used"],"mb data used")
        print("Snapchat ;",self.__Snapchat["data used"],"mb data used")
        print("Instagram ;",self.__Instagram["data used"],"mb data used")
        print("Youtube;",self.__Youtube["data used"],"mb data used")
        print("Phone ;",self.__Phone["data used"],"mb data used","\n")
        self.c=(self.__Phone["time_spent"]+self.__whatsapp["time_spent"]+self.__Snapchat["time_spent"]+self.__Instagram["time_spent"]+self.__Youtube["time_spent"])
        self.d=(self.__whatsapp["data used"]+self.__Snapchat["data used"]+self.__Instagram["data used"]+self.__Youtube["data used"]+self.__Phone["data used"])
        print("total time spend for entertainment",self.c)
        print("total data used",self.d)
        if(self.__work["time_spent"]==self.c):
            print("you have spent equal time ")
        elif(self.__work["time_spent"]>self.c):
            print("you have spent more time on work ")
        else:
            print("try to more concentrate on work than entertainment")
    def tuesday(self):
        self.__work ={"time_spent":eval(input("enter time that you spent for work in mins"))}
        if type(self.__work["time_spent"])== int:
            print("success")
        else:
            raise TypeError("Error made")
        self.__whatsapp   = {"time_spent":int(input("enter whatsapp used time in mins")), "notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__Instagram ={"time_spent":int(input("enter insta used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__Snapchat  = {"time_spent":int(input("enter Snapchat used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__Phone     ={"time_spent":int(input("enter phone used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__Youtube   ={"time_spent":int(input("enter youtube used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
    def view(self):
        print("Time used  in tuesday \n")
        print("work or study ; ",self.__work["time_spent"],"mins spent")
        print("whatsapp ;",self.__whatsapp["time_spent"],"mins used")
        print("Snapchat ;",self.__Snapchat["time_spent"],"mins used")
        print("Instagram ;",self.__Instagram["time_spent"],"mins used")
        print("Youtube ;",self.__Youtube["time_spent"],"mins used","mins used")
        print("Phone ;",self.__Phone["time_spent"],"\n")
        print("Notification recived in a day \n")
        print("whatsapp ;",self.__whatsapp["notification_recived"],"notification received")
        print("Snapchat ;",self.__Snapchat["notification_recived"],"notification received")
        print("Instagram ;",self.__Instagram["notification_recived"],"notification received")
        print("Youtube ;",self.__Youtube["notification_recived"],"notification received")
        print("Phone ;",self.__Phone["notification_recived"],"notification received","\n")
        print("data usage in a day \n")
        print("whatsapp ;",self.__whatsapp["data used"],"mb data used")
        print("Snapchat ;",self.__Snapchat["data used"],"mb data used")
        print("Instagram ;",self.__Instagram["data used"],"mb data used")
        print("Youtube;",self.__Youtube["data used"],"mb data used")
        print("Phone ;",self.__Phone["data used"],"mb data used","\n")
        self.e=(self.__Phone["time_spent"]+self.__whatsapp["time_spent"]+self.__Snapchat["time_spent"]+self.__Instagram["time_spent"]+self.__Youtube["time_spent"])
        self.f=(self.__whatsapp["data used"]+self.__Snapchat["data used"]+self.__Instagram["data used"]+self.__Youtube["data used"]+self.__Phone["data used"])
        print("total time spend for entertainment",self.e)
        print("total data used",self.f)
        if(self.__work["time_spent"]==self.e):
            print("you have spent equal time ")
        elif(self.__work["time_spent"]>self.e):
            print("you have spent more time on work ")
        else:
            print("try to more concentrate on work than entertainment")
    def wednesday(self):
        self.__work ={"time_spent":eval(input("enter time that you spent for work in mins"))}
        if type(self.__work["time_spent"])== int:
            print("success")
        else:
            raise TypeError("Error made")
        self.__whatsapp   = {"time_spent":int(input("enter whatsapp used time in mins")), "notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__Instagram ={"time_spent":int(input("enter insta used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__Snapchat  = {"time_spent":int(input("enter Snapchat used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__Phone     ={"time_spent":int(input("enter phone used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__Youtube   ={"time_spent":int(input("enter youtube used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
    def show(self):
        print("Time used  in wednesday \n")
        print("work or study ; ",self.__work["time_spent"],"mins spent")
        print("whatsapp ;",self.__whatsapp["time_spent"],"mins used")
        print("Snapchat ;",self.__Snapchat["time_spent"],"mins used")
        print("Instagram ;",self.__Instagram["time_spent"],"mins used")
        print("Youtube ;",self.__Youtube["time_spent"],"mins used")
        print("Phone ;",self.__Phone["time_spent"],"mins used","\n")
        print("Notification recived in a day \n")
        print("whatsapp ;",self.__whatsapp["notification_recived"],"notification received")
        print("Snapchat ;",self.__Snapchat["notification_recived"],"notification received")
        print("Instagram ;",self.__Instagram["notification_recived"],"notification received")
        print("Youtube ;",self.__Youtube["notification_recived"],"notification received")
        print("Phone ;",self.__Phone["notification_recived"],"notification received","\n")
        print("data usage in a day \n")
        print("whatsapp ;",self.__whatsapp["data used"],"mb data used")
        print("Snapchat ;",self.__Snapchat["data used"],"mb data used")
        print("Instagram ;",self.__Instagram["data used"],"mb data used")
        print("Youtube;",self.__Youtube["data used"],"mb data used")
        print("Phone ;",self.__Phone["data used"],"mb data used","\n")
        self.g=(self.__Phone["time_spent"]+self.__whatsapp["time_spent"]+self.__Snapchat["time_spent"]+self.__Instagram["time_spent"]+self.__Youtube["time_spent"])
        self.h=(self.__whatsapp["data used"]+self.__Snapchat["data used"]+self.__Instagram["data used"]+self.__Youtube["data used"]+self.__Phone["data used"])
        print("total time spend for entertainment",self.g)
        print("total data used",self.h)
        if(self.__work["time_spent"]==self.g):
            print("you have spent equal time ")
        elif(self.__work["time_spent"]>self.g):
            print("you have spent more time on work ")
        else:
            print("try to more concentrate on work than entertainment")
    def thursday(self):
        self.__work ={"time_spent":eval(input("enter time that you spent for work in mins"))}
        if type(self.__work["time_spent"])== int:
            print("success")
        else:
            raise TypeError("Error made")
        self.__whatsapp   = {"time_spent":int(input("enter whatsapp used time in mins")), "notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__Instagram ={"time_spent":int(input("enter insta used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__Snapchat  = {"time_spent":int(input("enter Snapchat used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__Phone     ={"time_spent":int(input("enter phone used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__Youtube   ={"time_spent":int(input("enter youtube used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
    def shows(self):
        print("Time used  in thursday \n")
        print("work or study ; ",self.__work["time_spent"],"mins spent")
        print("whatsapp ;",self.__whatsapp["time_spent"],"mins used")
        print("Snapchat ;",self.__Snapchat["time_spent"],"mins used")
        print("Instagram ;",self.__Instagram["time_spent"],"mins used")
        print("Youtube ;",self.__Youtube["time_spent"],"mins used")
        print("Phone ;",self.__Phone["time_spent"],"mins used","\n")
        print("Notification recived in a day \n")
        print("whatsapp ;",self.__whatsapp["notification_recived"],"notification received")
        print("Snapchat ;",self.__Snapchat["notification_recived"],"notification received")
        print("Instagram ;",self.__Instagram["notification_recived"],"notification received")
        print("Youtube ;",self.__Youtube["notification_recived"],"notification received")
        print("Phone ;",self.__Phone["notification_recived"],"notification received","\n")
        print("data usage in a day \n")
        print("whatsapp ;",self.__whatsapp["data used"],"mb data used")
        print("Snapchat ;",self.__Snapchat["data used"],"mb data used")
        print("Instagram ;",self.__Instagram["data used"],"mb data used")
        print("Youtube;",self.__Youtube["data used"],"mb data used")
        print("Phone ;",self.__Phone["data used"],"mb data used","\n")
        self.s=(self.__Phone["time_spent"]+self.__whatsapp["time_spent"]+self.__Snapchat["time_spent"]+self.__Instagram["time_spent"]+self.__Youtube["time_spent"])
        self.t=(self.__whatsapp["data used"]+self.__Snapchat["data used"]+self.__Instagram["data used"]+self.__Youtube["data used"]+self.__Phone["data used"])
        print("total time spend for entertainment",self.s)
        print("total data used",self.t)
        if(self.__work["time_spent"]==self.s):
            print("you have spent equal time ")
        elif(self.__work["time_spent"]>self.s):
            print("you have spent more time on work ")
        else:
            print("try to more concentrate on work than entertainment")
    def friday(self):
        self.__work ={"time_spent":eval(input("enter time that you spent for work in mins"))}
        if type(self.__work["time_spent"])== int:
            print("success")
        else:
            raise TypeError("Error made")
        self.__whatsapp   = {"time_spent":int(input("enter whatsapp used time in mins")), "notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__Instagram ={"time_spent":int(input("enter insta used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__Snapchat  = {"time_spent":int(input("enter Snapchat used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__Phone     ={"time_spent":int(input("enter phone used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__Youtube   ={"time_spent":int(input("enter youtube used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
    def call(self):
        print("Time used  in friday \n")
        print("work or study ; ",self.__work["time_spent"],"mins spent")
        print("whatsapp ;",self.__whatsapp["time_spent"],"mins used")
        print("Snapchat ;",self.__Snapchat["time_spent"],"mins used")
        print("Instagram ;",self.__Instagram["time_spent"],"mins used")
        print("Youtube ;",self.__Youtube["time_spent"],"mins used")
        print("Phone ;",self.__Phone["time_spent"],"mins used","\n")
        print("Notification recived in a day \n")
        print("whatsapp ;",self.__whatsapp["notification_recived"],"notification received")
        print("Snapchat ;",self.__Snapchat["notification_recived"],"notification received")
        print("Instagram ;",self.__Instagram["notification_recived"],"notification received")
        print("Youtube ;",self.__Youtube["notification_recived"],"notification received")
        print("Phone ;",self.__Phone["notification_recived"],"notification received","\n")
        print("data usage in a day \n")
        print("whatsapp ;",self.__whatsapp["data used"],"mb data used")
        print("Snapchat ;",self.__Snapchat["data used"],"mb data used")
        print("Instagram ;",self.__Instagram["data used"],"mb data used")
        print("Youtube;",self.__Youtube["data used"],"mb data used")
        print("Phone ;",self.__Phone["data used"],"mb data used","\n")
        self.u=(self.__Phone["time_spent"]+self.__whatsapp["time_spent"]+self.__Snapchat["time_spent"]+self.__Instagram["time_spent"]+self.__Youtube["time_spent"])
        self.v=(self.__whatsapp["data used"]+self.__Snapchat["data used"]+self.__Instagram["data used"]+self.__Youtube["data used"]+self.__Phone["data used"])
        print("total time spend for entertainment",self.u)
        print("total data used",self.v)
        if(self.__work["time_spent"]==self.u):
            print("you have spent equal time ")
        elif(self.__work["time_spent"]>self.u):
            print("you have spent more time on work ")
        else:
            print("try to more concentrate on work than entertainment")
    def saturday(self):
        self.__work ={"time_spent":eval(input("enter time that you spent for work in mins"))}
        if type(self.__work["time_spent"])== int:
            print("success")
        else:
            raise TypeError("Error made")
        self.__whatsapp   = {"time_spent":int(input("enter whatsapp used time in mins")), "notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__Instagram ={"time_spent":int(input("enter insta used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__Snapchat  = {"time_spent":int(input("enter Snapchat used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__Phone     ={"time_spent":int(input("enter phone used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
        self.__Youtube   ={"time_spent":int(input("enter youtube used time in mins")),"notification_recived":int(input("enter notification received in numbers")),"data used":int(input("enter data usage in mb"))}
    def calls(self):
        print("Time used  in saturday \n")
        print("work or study ; ",self.__work["time_spent"],"mins spent")
        print("whatsapp ;",self.__whatsapp["time_spent"],"mins used")
        print("Snapchat ;",self.__Snapchat["time_spent"],"mins used")
        print("Instagram ;",self.__Instagram["time_spent"],"mins used")
        print("Youtube ;",self.__Youtube["time_spent"],"mins used")
        print("Phone ;",self.__Phone["time_spent"],"mins used","\n")
        print("Notification recived in a day \n")
        print("whatsapp ;",self.__whatsapp["notification_recived"],"notification received")
        print("Snapchat ;",self.__Snapchat["notification_recived"],"notification received")
        print("Instagram ;",self.__Instagram["notification_recived"],"notification received")
        print("Youtube ;",self.__Youtube["notification_recived"],"notification received")
        print("Phone ;",self.__Phone["notification_recived"],"notification received","\n")
        print("data usage in a day \n")
        print("whatsapp ;",self.__whatsapp["data used"],"mb data used")
        print("Snapchat ;",self.__Snapchat["data used"],"mb data used")
        print("Instagram ;",self.__Instagram["data used"],"mb data used")
        print("Youtube;",self.__Youtube["data used"],"mb data used")
        print("Phone ;",self.__Phone["data used"],"mb data used","\n")
        self.x=(self.__Phone["time_spent"]+self.__whatsapp["time_spent"]+self.__Snapchat["time_spent"]+self.__Instagram["time_spent"]+self.__Youtube["time_spent"])
        self.y=(self.__whatsapp["data used"]+self.__Snapchat["data used"]+self.__Instagram["data used"]+self.__Youtube["data used"]+self.__Phone["data used"])
        print("total time spend for entertainment",self.x)
        print("total data used",self.y)
        if(self.__work["time_spent"]==self.x):
            print("you have spent equal time ")
        elif(self.__work["time_spent"]>self.y):
            print("you have spent more time on work ")
        else:
            print("try to more concentrate on work than entertainment")
    
aha = phonetracking()
aha.display()
aha.monday()
aha.views()
aha.tuesday()
aha.view()
aha.wednesday()
aha.show()
aha.thursday()
aha.shows()
aha.friday()
aha.call()
aha.saturday()
aha.calls()
