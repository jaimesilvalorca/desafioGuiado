class Personaje:
    def __init__(self,name):
        self.name = name
        self.experience = 0
        self.level = 1
        
    def __str__(self):
        return f"Nombre:{self.name} Nivel:{self.level} Experiencia: {self.experience}"
    
    def get_name(self):
        return self.name
    
    def set_status(self,experience):
        level_up = self.experience + experience
        
        while level_up >= 100:
            self.level = self.level + 1
            level_up = level_up - 100
            
        if level_up < 0 and self.level > 1:
            self.level = self.level - 1
            level_up = 0
        
        self.experience = level_up
    
    def get_status(self):
        return f"NOMBRE: {self.name} NIVEL: {self.level} EXP: {self.experience}"
    
        
    def __lt__(self, another_pj):
        return self.level < another_pj
    
    def __gt__(self, another_pj):
        return self.level > another_pj
    
    def __eq__(self, another_pj):
        return self.level == another_pj
    
    def chance_of_win(self, another_pj):
        if self < another_pj:
            return 0.33
        elif self > another_pj:
            return 0.66
        else:
            return 0.5
    
    def win(self):
        self.experience += 50
        if self.experience >= 100:
            self.level += self.experience // 100
            self.experience %= 100
    
    def lose(self):
        self.experience -= 30
        if self.experience < 0:
            self.experience = 0    

    @staticmethod
    def battle(probability):
        print(f"Con tu nivel actual, tienes {probability*100:.1f}% de probabildiades de ganar")
        print(f"si ganas, ganaras 50 puntos de experiencia y el orco perdera 30")
        print(f"si pierdes, perderas 30 puntos de experiencia y el orco ganara 50.")
        
        option = input(f"""Selecciona una opcion
                       1) Atacar
                       2) Huir""")
        return option