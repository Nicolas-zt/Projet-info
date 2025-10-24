import numpy as np
import random as rd

class Grille:
    
    
    def __init__(self,taille,nb_bombes):   
        self.taille = taille
        self.nb_bombes = nb_bombes        
        self.grid = np.zeros(taille)
        
  
        c = 0
        while c < nb_bombes:
            pos =(rd.randint(0,self.taille[0]-1),rd.randint(0,self.taille[1]-1))
            
            if self.grid[pos] != -1:         
                self.grid[pos] = -1
                c+=1
           
        for l in range(len(self.grid)):
            for c in range(len(self.grid)):  # Itération sur les cases dont on cherche le voisinage
            
                if self.grid[l,c] != -1:    # Pas de test sur les cases piégées
                                        
                    used = []

                    for i in range(-1,2):    # Itération sur les voisins de la case testée
                        for j in range(-1,2):
                                                       
                            if i==0 and j==0:
                                pass                           
                            
                            else:
                                
                                
                                x = max(0,min(l+i,self.taille[0]-1))    #Limite des bords gauche-droite
                                y = max(0,min(c+j,self.taille[1]-1))    #Limite des bords haut-bas
                                
                                
                                if (x,y) not in used and self.grid[x,y] == -1:
                                    self.grid[l,c] +=1  #Comptage des bombes voisines
                                    used.append((x,y))  #On évite de compter plusieurs fois une bombe
                            
                            # Cases_cachees(piégée, False)
         
        
        
        
        
    def __str__(self):
        return str(self.grid)
    
    def play(self):
        
        while self.nb_bombes > 0:
            
            drapeaux = input("Donnez une liste de cases sur lesquelles mettre un drapeau")
            
            
            case_choisie = input("Donnez les coordonnées de la case à tester")
            
            
class Cases:
    
    
    def __init__(self,piégée,valeur = 0):     
        self.piégée = piégée
        if piégée == False:
            self.valeur = valeur
        
class Cases_decouvertes(Cases):
    
    
    def __init__(self,piégée):       
        super.__init__(piégée)
        
        
class Cases_cachees(Cases):
    
    
    def __init__(self,piégée,marquée):        
        super.__init__(piégée)
        self.marquée = False
        
    def ajout_drapeau(self):        
        self.marquée = True
        
        
        
        
        
if __name__ == "__main__":
    
    G = Grille((10,10),40)
    print(G)