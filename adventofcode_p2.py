import csv 
  
# Open the file  
with open('data_adventofcode_2.csv') as file_obj: 
      
    # Create a reader object by passing the file  
    # to the reader method 
    r = csv.reader(file_obj, delimiter=';') 
      
    # Iterate over each row in the csv file  
    # using the reader object 
    lignes = []
    for ligne in r: 
        ligne_nette = []
        for item in ligne:
            if item.strip():
                ligne_nette.append(item.strip())
        lignes.append(ligne_nette)
        

# Check if all rows are strictly increasing or decreasing 

def augmente(ligne) :
    """returns true if a row is increasing by one or two""" 
    for i in range(len(ligne)-1) :
        if not( int(ligne[i]) < int(ligne[i+1]) and 1 <= (int(ligne[i+1]) - int(ligne[i])) <= 3) : 
            return False
    return True
        

def diminution(ligne) :
    """returns true if a row is decreasing by one or two""" 
    for i in range(len(ligne)-1) : 
        if not(int(ligne[i]) > int(ligne[i+1]) and 1 <= (int(ligne[i]) - int(ligne[i+1])) <= 3) : 
            return False
    return True

def problem_damper(ligne) : 
    """checks if removing one element makes the row increasing or decreasing"""
    for i in range(len(ligne)) : 
        nouvelle_ligne = ligne[:i] + ligne[i+1:]
        if augmente(nouvelle_ligne) or diminution(nouvelle_ligne) :
            return True 
    return False

safe = 0         
for ligne in lignes : 
    if augmente(ligne) or diminution(ligne) : 
        safe += 1
        
print(safe) # prints 670

# Part two

safe2 = 0         
for ligne in lignes : 
    if augmente(ligne) or diminution(ligne) : 
        safe2 += 1 
    elif problem_damper(ligne) : 
        safe2 += 1 

print(safe2) # prints 700