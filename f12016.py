class F1Data2016:
    def __init__(self):
        self.nameAndpoints = {
            "Nico Rosberg": ("Mercedes", 385),
            "Lewis Hamilton": ("Mercedes", 380),
            "Daniel Ricciardo": ("Red Bull", 256),
            "Sebastian Vettel": ("Ferrari", 212),
            "Max Verstappen": ("Red Bull", 204),
            "Kimi Raikkonen": ("Ferrari", 186),
            "Sergio Perez": ("Force India", 101),
            "Valtteri Bottas": ("Williams", 85),
            "Nico Hulkenberg": ("Force India", 72),
            "Fernando Alonso": ("McLaren", 54),
            "Felipe Massa": ("Williams", 53),
            "Carlos Sainz": ("Toro Rosso", 46),
            "Romain Grosjean": ("Haas", 29),
            "Daniil Kvyat": ("Toro Rosso", 25),
            "Jenson Button": ("McLaren", 21),
            "Kevin Magnussen": ("Renault", 7),
            "Felipe Nasr": ("Sauber", 2),
            "Pascal Wehrlein": ("Manor", 1),
            "Jolyon Palmer": ("Renault", 1),
            "Esteban Gutierrez": ("Haas", 0),
            "Marcus Ericsson": ("Sauber", 0),
            "Esteban Ocon": ("Manor", 0)
        }

        self.colors = {
            "Mercedes": '#00D2BE',  # Sky blue
            "Red Bull": '#1E41FF',  # Bluish black
            "Ferrari": '#DC0000',  # Ferrari red
            "Force India": '#FF8000',  # Orange
            "Williams": '#005AFF',  # Light blue
            "McLaren": '#FFD700',  # Gold
            "Toro Rosso": '#000080',  # Navy blue
            "Haas": '#B6BABD',  # Light gray
            "Renault": '#FFDC35',  # Yellow
            "Sauber": '#0066FF',  # Medium blue
            "Manor": '#FF0000',  # Red
        }

        self.team_points = { 
            "Mercedes": 765, 
            "Red Bull": 468, 
            "Ferrari": 398, 
            "Force India": 173, 
            "Williams": 138, 
            "McLaren": 76, 
            "Toro Rosso": 63, 
            "Haas": 29, 
            "Renault": 8, 
            "Sauber": 2, 
            "Manor": 1 
        } 
    def get_team_points(self): 
        return self.team_points
