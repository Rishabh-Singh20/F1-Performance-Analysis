class F1Data2024:
    def __init__(self):
        self.nameAndpoints = {
            "Max Verstappen": ("Red Bull", 393),
            "Lando Norris": ("McLaren", 331),
            "Charles Leclerc": ("Ferrari", 307),
            "Oscar Piastri": ("McLaren", 262),
            "Carlos Sainz": ("Ferrari", 244),
            "George Russell": ("Mercedes", 192),
            "Lewis Hamilton": ("Mercedes", 190),
            "Sergio Perez": ("Red Bull", 151),
            "Fernando Alonso": ("Aston Martin", 62),
            "Nico Hulkenberg": ("Haas", 31),
            "Yuki Tsunoda": ("VCARB", 28),
            "Pierre Gasly": ("Alpine", 26),
            "Lance Stroll": ("Aston Martin", 24),
            "Esteban Ocon": ("Alpine", 23),
            "Kevin Magnussen": ("Haas", 14),
            "Alexander Albon": ("Williams", 12),
            "Daniel Ricciardo": ("VCARB", 12),
            "Oliver Bearman": ("Haas", 7),
            "Franco Colapinto": ("Williams", 5),
            "Liam Lawson": ("VCARB", 4),
            "Zhou Guanyu": ("Kick Sauber", 0),
            "Valtteri Bottas": ("Kick Sauber", 0)
        }

        self.colors = {
            "Red Bull": '#1E41FF',  # Bluish black
            "McLaren": '#FF8700',  # Papaya orange
            "Ferrari": '#DC0000',  # Ferrari red
            "Mercedes": '#00D2BE',  # Sky blue
            "Aston Martin": '#006F62',  # Bluish green
            "Haas": '#B6BABD',  # Light gray
            "VCARB": '#2B4562',  # Dark blue like VISA
            "Alpine": '#FF5F5F',  # Pink
            "Williams": '#005AFF',  # Light blue
            "Kick Sauber": '#00FF00'  # Green
        }

        self.team_points = {
            "McLaren": 593,
            "Ferrari": 557,
            "Red Bull": 544,
            "Mercedes": 382,
            "Aston Martin": 86,
            "Alpine": 49,
            "Haas": 46,
            "VCARB": 44,
            "Williams": 17,
            "Kick Sauber": 0
        }
    def get_team_points(self):
        return self.team_points