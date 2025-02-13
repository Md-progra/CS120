class clock:
    def __init__(self, time ):
        self.time = time


        print(f"Time is: {self.time}")

class calendar:
    def __init__(self,day,month,date):
        self.day = day
        self.month = month
        self.date = date
        print(f"Today is {self.day}, {self.date} of {self.month}")

class calendarclock(clock, calendar):
    
    def display(self):
        print(f"Time is: {self.time} and Today is {self.day}, {self.date} of {self.month}")


calenclock = calendarclock("10:30")

# Call the display method
calenclock.display()