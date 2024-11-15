class F1Data2022:
    def __init__(self):
        self.nameAndpoints = {
            "Max Verstappen": ("Red Bull", 454),
            "Charles Leclerc": ("Ferrari", 308),
            "Sergio Perez": ("Red Bull", 305),
            "George Russell": ("Mercedes", 275),
            "Carlos Sainz": ("Ferrari", 246),
            "Lewis Hamilton": ("Mercedes", 240),
            "Lando Norris": ("McLaren", 122),
            "Esteban Ocon": ("Alpine", 92),
            "Fernando Alonso": ("Alpine", 81),
            "Valtteri Bottas": ("Alfa Romeo", 49),
            "Sebastian Vettel": ("Aston Martin", 37),
            "Daniel Ricciardo": ("McLaren", 37),
            "Kevin Magnussen": ("Haas", 25),
            "Pierre Gasly": ("AlphaTauri", 23),
            "Lance Stroll": ("Aston Martin", 23),
            "Mick Schumacher": ("Haas", 12),
            "Yuki Tsunoda": ("AlphaTauri", 12),
            "Guanyu Zhou": ("Alfa Romeo", 6),
            "Alexander Albon": ("Williams", 4),
            "Nicholas Latifi": ("Williams", 2),
            "Nyck De Vries": ("Williams", 2),
            "Nico Hulkenberg": ("Aston Martin", 0)
        }

        self.colors = {
            "Red Bull": '#1E41FF',  # Bluish black
            "Ferrari": '#DC0000',  # Ferrari red
            "Mercedes": '#00D2BE',  # Sky blue
            "McLaren": '#FF8700',  # Papaya orange
            "Alpine": '#FF5F5F',  # Pink
            "AlphaTauri": '#2B4562',  # Dark blue like VISA
            "Aston Martin": '#006F62',  # Bluish green
            "Alfa Romeo": '#B0B7BD',  # Gray
            "Williams": '#005AFF',  # Light blue
            "Haas": '#B6BABD'  # Light gray
        }

        self.team_points = {
            "Red Bull": 759,
            "Ferrari": 554,
            "Mercedes": 515,
            "Alpine": 173,
            "McLaren": 159,
            "Alfa Romeo": 55,
            "Aston Martin": 55,
            "Haas": 37,
            "AlphaTauri": 35,
            "Williams": 8
        }

    def get_team_points(self):
        return self.team_points
