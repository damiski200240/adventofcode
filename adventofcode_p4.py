f = open('adventofcode_p4.txt', "r")
contenu = f.read()
# print(contenu)
lignes = contenu.strip().split('\n')
size_y = len(lignes)
size_x = max(len(l) for l in lignes)
# print(size_y)
# print(lignes)



#on commence par voir si notre mot XMAS est dans notre map, si X est dans le dernier caractere d'un colonne on peut pas trouver XMAS en vertical

XMAS = ['X','M','A','S']
taille = len(XMAS) # XMAS -> 4 
def checkXmas(cordx , cordy , dirx, diry ) : 
    bord_X = cordx + (taille - 1 ) * dirx 
    bord_Y = cordy + (taille- 1) * diry 
    if (bord_X < 0 or bord_X >= size_x or bord_Y < 0 or bord_Y >= size_y) : 
        return False # on peut pas trouve XMAS dans ce cas 
    for k in range(taille): 
        nx = cordx + k * dirx
        ny = cordy + k  * diry
        if (lignes[ny][nx] != XMAS[k]) : # si la nouvelle case n'est pas M A ou S dans cette ordre alors on peut pas trouver XMAS
            return False
        
    return True # on peut bouger dans ce cas 

directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

count = 0 
for x in range(size_x) : 
    for y in range(size_y):
        for dircetion in directions : 
            if checkXmas(x,y,dircetion[0], dircetion[1]) : 
                count += 1 

print(count) #2599


#partie 2 : X-MAS , on va verifier chaque A dans notre text pour voir s'il y a un MAS centré comme demandé


As = []
for y in range(size_y) : 
    for x in range(size_x):
        if lignes[y][x] == 'A' :
            As.append((x,y)) 

def checkmas(x,y) :
    if (x - 1 < 0 or x + 1 >= size_x or y - 1 < 0 or y + 1 >= size_y) :
        return False # hors map
    if ((lignes[y - 1][x - 1] == 'M' and lignes[y + 1][x + 1] == 'S') and
        (lignes[y - 1][x + 1] == 'M' and lignes[y + 1][x - 1] == 'S')):
        return True # 
    # 1ere        M        - S
    #                 A 
    #             M        - S

    
    if ((lignes[y - 1][x - 1] == 'S' and lignes[y + 1][x + 1] == 'M') and
        (lignes[y - 1][x + 1] == 'S' and lignes[y + 1][x - 1] == 'M')):
        return True
    # 2eme        S        - S
    #                 A 
    #             M        - M
    
    if ((lignes[y - 1][x - 1] == 'S' and lignes[y + 1][x + 1] == 'M') and
        (lignes[y - 1][x + 1] == 'M' and lignes[y + 1][x - 1] == 'S')):
        return True
    # 3eme        S        - M
    #                 A 
    #             M        - S
    
    if ((lignes[y - 1][x - 1] == 'M' and lignes[y + 1][x + 1] == 'S') and
        (lignes[y - 1][x + 1] == 'S' and lignes[y + 1][x - 1] == 'M')):
        return True
    
    # 4eme        M        - S
    #                 A 
    #             S        - M
    
    return False 
count_2nd = 0

for ax, ay in As: 
            if checkmas(ax, ay) : count_2nd += 1 

print(count_2nd) #1948