class F1Data2015:
    def __init__(self):
        self.nameAndpoints = {
            "Lewis Hamilton": ("Mercedes", 381),
            "Nico Rosberg": ("Mercedes", 322),
            "Sebastian Vettel": ("Ferrari", 278),
            "Kimi Raikkonen": ("Ferrari", 150),
            "Valtteri Bottas": ("Williams", 136),
            "Felipe Massa": ("Williams", 121),
            "Daniil Kvyat": ("Red Bull", 95),
            "Daniel Ricciardo": ("Red Bull", 92),
            "Sergio Perez": ("Force India", 78),
            "Nico Hulkenberg": ("Force India", 58),
            "Romain Grosjean": ("Lotus", 51),
            "Max Verstappen": ("Toro Rosso", 49),
            "Pastor Maldonado": ("Lotus", 27),
            "Felipe Nasr": ("Sauber", 27),
            "Carlos Sainz": ("Toro Rosso", 18),
            "Jenson Button": ("McLaren", 16),
            "Fernando Alonso": ("McLaren", 11),
            "Marcus Ericsson": ("Sauber", 9),
            "Roberto Merhi": ("Manor", 0),
            "Alexander Rossi": ("Manor", 0),
            "Will Stevens": ("Manor", 0)
        }

        self.team_points = {
            "Mercedes": 703,
            "Ferrari": 428,
            "Williams": 320,
            "Red Bull": 187,
            "Force India": 136,
            "Lotus": 78,
            "Sauber": 36,
            "Toro Rosso": 30,
            "McLaren": 27,
            "Manor": 0
        }
        
        self.colors = {
            "Mercedes": '#00D2BE',  # Sky blue
            "Ferrari": '#DC0000',  # Ferrari red
            "Williams": '#005AFF',  # Light blue
            "Red Bull": '#1E41FF',  # Bluish black
            "Force India": '#FF8000',  # Orange
            "Lotus": '#FFB800',  # Yellow
            "Toro Rosso": '#000080',  # Navy blue
            "McLaren": '#FFD700',  # Gold
            "Sauber": '#0066FF',  # Medium blue
            "Manor": '#FF0000',  # Red
        }

    def get_team_points(self):
        return self.team_points