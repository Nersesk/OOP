class UserMail:
    def __init__(self,login,email):
        self.login=login
        self.__email=email
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,new_email):
        a=new_email.count('@')
        if a==1:
            c=new_email.find('@')
            if '.' in new_email[c+1:]:
                self.__email=new_email
        else:
            print("Wrong  Email")

