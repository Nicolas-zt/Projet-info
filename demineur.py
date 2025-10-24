import numpy as np

class Grille:
    
    
    def __init__(self,taille,nb_bombes):
        
        self.taille = taille
        self.nb_bombes = nb_bombes
        
class Cases:
    
    
    def __init__(self,piégée):
        
        self.piégée = piégée
        
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
    
    G = Grille((20,20),10)