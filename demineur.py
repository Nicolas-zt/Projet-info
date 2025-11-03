import numpy as np
import random as rd

class Grille:
    
    
    def __init__(self,taille,nb_bombes):   
        self.taille = taille
        self.nb_bombes = nb_bombes        
        self.grid_value = np.zeros(taille)
        
        self.grid = np.array( [ [ Cases(False, True) for i in range (taille[0])] for i in range (taille[1])])
        print(self.grid)
        
        
        c = 0
        while c < nb_bombes:
            pos =(rd.randint(0,self.taille[0]-1),rd.randint(0,self.taille[1]-1))
            
            if self.grid_value[pos] != -1:         
                self.grid_value[pos] = -1
                c+=1
           
        for l in range(len(self.grid_value)):
            for c in range(len(self.grid_value[0])):  # Itération sur les cases dont on cherche le voisinage
            
                if self.grid_value[l,c] != -1:    # Pas de test sur les cases piégées
                                        
                    used = []

                    for i in range(-1,2):    # Itération sur les voisins de la case testée
                        for j in range(-1,2):
                                                       
                            if i==0 and j==0:
                                pass                           
                            
                            else:
                                                                
                                x = max(0,min(l+i,self.taille[0]-1))    #Limite des bords gauche-droite
                                y = max(0,min(c+j,self.taille[1]-1))    #Limite des bords haut-bas                               
                                
                                if (x,y) not in used and self.grid_value[x,y] == -1:
                                    self.grid_value[l,c] +=1  #Comptage des bombes voisines
                                    used.append((x,y))  #On évite de compter plusieurs fois une bombe
        
        
        
        for i in range(len(self.grid_value)):               #On associe la grille de valeurs à la grille de cases
            for j in range(len(self.grid_value[0])):
                self.grid[i,j].valeur = self.grid_value[i,j]
        
        
    def __str__(self):
        
        for i in range(len(self.grid_value)):              
            for j in range(len(self.grid_value[0])):
                if self.grid[i,j].cachée == True:
                    self.grid_value[i,j] = np.nan
                else:
                    self.grid_value[i,j] = self.grid[i,j].valeur
                    
                if self.grid[i,j].marquée == True:
                    self.grid_value[i,j] = 00
                    
                    
                
        return str(self.grid_value)
    
        
    
    def play(self):
        
        
        while self.nb_bombes > 0:
            
            print(self)
           
            drapeaux = input("Donnez une liste de cases sur lesquelles mettre un drapeau : " + "\n").split()  #Marquage des cases souhaitées
            
            if len(drapeaux) != 0:
                
                for lc in drapeaux: 

                   l,c = int(lc[0]) , int(lc[1])
                   self.grid[l,c].marquée = True
                  
                   
                   if self.grid[l,c].piégée == True:
                       self.nb_bombes -= 1
                    
            
            
            
            l,c = input("Donnez les coordonnées de la case à tester : " + "\n")  #Choix de la case à tester
        
            l,c = int(l) , int(c)
            case_choisie = self.grid[l,c]
            
            if case_choisie.valeur == -1:  
                
                print("Vous avez perdu")
                case_choisie.cachée = False
                print(G)
                break
                
            else: 
                self.suppression(l,c)
                # case_choisie.cachée = False
                # for i in range(-1,2):    # Itération sur les voisins de la case testée
                #     for j in range(-1,2):
                                                   
                #         if i==0 and j==0:
                #             pass                           
                        
                        
                #         else:
                                                            
                #             x = max(0,min(l+i,self.taille[0]-1))    #Limite des bords gauche-droite
                #             y = max(0,min(c+j,self.taille[1]-1))    #Limite des bords haut-bas 
                #             self.grid[x,y].cachée = False
                
        if self.nb_bombes == 0:
            print("Félicitations, vous avez gagné")
            
    def suppression(self,l,c):
        
        Voisins = []
        print(l,c)
        self.grid[l,c].cachée = False
        
        for i in range(-1,2):
            for j in range(-1,2):
            
                if i == 0 and j == 0:
                    pass
                else:
                    Voisins.append(self.grid[l+i,c+j])
                    
        for voisin in Voisins:
            
            if voisin.valeur != 0:
                pass
            else:
                
                try:
                    x = max(0,min(l+i,self.taille[0]-1))    
                    y = max(0,min(c+j,self.taille[1]-1))
                    print("coordonnées du voisin récursif: " + str(l+x) + str(j+y))
                    self.suppression(l+x,c+y)
                except:
                    pass
                
                
                
class Cases:
    
    
    def __init__(self,piégée,cachée,marquée = False,valeur = 0):     
        self.piégée = piégée
        self.cachée = cachée
        self.marquée = marquée
        self.valeur = valeur
        if piégée == False:
            self.valeur = valeur
        
    def ajout_drapeau(self):
        
        if self.cachée == True:
            self.marquée = True
        
        else:
            
            pass
        
    def __str__(self):
        
        return str(self.valeur)
        
        
        
        
if __name__ == "__main__":
    
    G = Grille((10,10),10)
    G.play()