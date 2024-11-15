class F1Data2018:
    def __init__(self):
        self.nameAndpoints = {
            "Lewis Hamilton": ("Mercedes", 408),
            "Sebastian Vettel": ("Ferrari", 320),
            "Kimi Raikkonen": ("Ferrari", 251),
            "Max Verstappen": ("Red Bull", 249),
            "Valtteri Bottas": ("Mercedes", 247),
            "Daniel Ricciardo": ("Red Bull", 170),
            "Nico Hulkenberg": ("Renault", 69),
            "Sergio Perez": ("Force India", 62),
            "Kevin Magnussen": ("Haas", 56),
            "Carlos Sainz": ("Renault", 53),
            "Fernando Alonso": ("McLaren", 50),
            "Esteban Ocon": ("Force India", 49),
            "Charles Leclerc": ("Sauber", 39),
            "Romain Grosjean": ("Haas", 37),
            "Pierre Gasly": ("Toro Rosso", 29),
            "Stoffel Vandoorne": ("McLaren", 12),
            "Marcus Ericsson": ("Sauber", 9),
            "Lance Stroll": ("Williams", 6),
            "Brendon Hartley": ("Toro Rosso", 4),
            "Sergey Sirotkin": ("Williams", 1)
        }

        self.colors = {
            "Mercedes": '#00D2BE',  # Sky blue
            "Ferrari": '#DC0000',  # Ferrari red
            "Red Bull": '#1E41FF',  # Bluish black
            "Renault": '#FFF500',  # Yellow
            "Force India": '#FF8000',  # Orange
            "Haas": '#B6BABD',  # Light gray
            "McLaren": '#FF8700',  # Papaya orange
            "Sauber": '#0066FF',  # Medium blue
            "Toro Rosso": '#000080',  # Navy blue
            "Williams": '#005AFF'  # Light blue
        }
        self.team_points = { 
            "Mercedes": 655, 
            "Ferrari": 571, 
            "Red Bull": 419, 
            "Renault": 122, 
            "Haas": 93, 
            "McLaren": 62, 
            "Force India": 52, 
            "Sauber": 48, 
            "Toro Rosso": 33, 
            "Williams": 7  
        } 
    def get_team_points(self): 
        return self.team_points

