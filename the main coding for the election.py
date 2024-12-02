import csv
with open("//Macintosh HD//Users//edirinjalogho//Documents//coding//project_1//FullDataFor2024.csv", newline="") as csvfile:
     reader = csv.DictReader(csvfile)
Options = ["List the Constituency" , "List the region", "List the Constuency type", "List the valid votes","Vote"]

class Constituency:
    def __init__(self,t):
        self.details = t
    def __str__(self):
         return self

class Vote:
    def __init__(self,Constituency,Region,Country,Results):
        self.Constituency = Constituency
        self.Region = Region
        self.Contry = Country
        self.Results = Results

    
    def process(self):
        print("Your vote is processing, please wait one moment")

    def finish(self):
        print("Your vote has been fully prossed into the system")

def Menu():
    while Choice < 0 or Choice > 4:
     print("Welcome to the Election, it's great to have you here")
     print("Choose your option(please intput a number)")
     print("Option Number\tOption")
     optionNumber = 0
     for option in Options:
          print(optionNumber,"\t\t",option)
          optionNumber += 1
try:
    Choice = int(input("What number would like to choose?"))
except:
     Choice = -1
 


