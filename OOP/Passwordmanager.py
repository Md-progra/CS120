class Password_manager:
    def __init__(self):
        self.old_passwords = []
        self.current_password = self.old_passwords[-1]

    def get_password(self):
        return self.current_password
    

    def set_password(self):
        self.attempt= input("Enter password:")
        for i in range(len(self.old_passwords)):
            if self.old_passwords[i] == self.attempt:
                return "Wrong!!"
    def is_correct(self):
        if self.attempt == self.current_password:
            return True
        else:
            return False

