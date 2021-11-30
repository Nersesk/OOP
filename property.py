class UserMail:
    def __init__(self,login,email):
        self.login=login
        self.__email=email
    def get_email(self):
        return self.__email
    def set_email(self,new_email):
        a=new_email.count('@')
        if a==1:
            c=new_email.find('@')
            if '.' in new_email[c+1:]:
                self.__email=new_email
        else:
            print("Ошибочная почта")

    email=property(fget=get_email,fset=set_email)
k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)  # prince@wait.you
k.email = [1, 2, 3] # Ошибочная почта
k.email = 'prince@still@.wait'  # Ошибочная почта
k.email = 'prince@still.wait'
print(k.email)  # prince@still.wait
