from sys import exit, argv
from csv import reader, DictReader

def main()
   
   # Only accepting the correct input
    if len(argv) != 3 :
        print("error, dna.py sequence.txt database.csv")
        exit(1)
        
    #openning the file
     with open(argv[1], "r") as peoplefile:
        reader = list(csv.reader(peoplefile))
        reader[0].remove"name"
        i = reader[0]
    
    with open(argv[2], "r")  as sequence:
        dna = sequence.read  
    

    
