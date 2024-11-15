class F1Data2017:
    def __init__(self):
        self.nameAndpoints = {
            "Lewis Hamilton": ("Mercedes", 363),
            "Sebastian Vettel": ("Ferrari", 317),
            "Valtteri Bottas": ("Mercedes", 305),
            "Kimi Raikkonen": ("Ferrari", 205),
            "Daniel Ricciardo": ("Red Bull", 200),
            "Max Verstappen": ("Red Bull", 168),
            "Sergio Perez": ("Force India", 100),
            "Esteban Ocon": ("Force India", 87),
            "Carlos Sainz": ("Toro Rosso", 54),
            "Nico Hulkenberg": ("Renault", 43),
            "Felipe Massa": ("Williams", 43),
            "Lance Stroll": ("Williams", 40),
            "Romain Grosjean": ("Haas", 28),
            "Kevin Magnussen": ("Haas", 19),
            "Fernando Alonso": ("McLaren", 17),
            "Stoffel Vandoorne": ("McLaren", 13),
            "Jolyon Palmer": ("Renault", 8),
            "Pascal Wehrlein": ("Sauber", 5),
            "Marcus Ericsson": ("Sauber", 0)
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
        }

        self.team_points = { 
            "Mercedes": 668, 
            "Ferrari": 522, 
            "Red Bull": 368, 
            "Force India": 187, 
            "Williams": 83, 
            "Renault": 57, 
            "Toro Rosso": 53, 
            "Haas": 47, 
            "McLaren": 30, 
            "Sauber": 2, 
        } 
    def get_team_points(self): 
        return self.team_points
