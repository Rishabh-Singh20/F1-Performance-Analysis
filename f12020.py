class F1Data2020:
    def __init__(self):
        self.nameAndpoints = {
            "Lewis Hamilton": ("Mercedes", 347),
            "Valtteri Bottas": ("Mercedes", 223),
            "Max Verstappen": ("Red Bull", 214),
            "Sergio Perez": ("Racing Point", 125),
            "Daniel Ricciardo": ("Renault", 119),
            "Carlos Sainz": ("McLaren", 105),
            "Alexander Albon": ("Red Bull", 105),
            "Charles Leclerc": ("Ferrari", 98),
            "Lando Norris": ("McLaren", 97),
            "Pierre Gasly": ("AlphaTauri", 75),
            "Lance Stroll": ("Racing Point", 75),
            "Esteban Ocon": ("Renault", 62),
            "Sebastian Vettel": ("Ferrari", 33),
            "Daniil Kvyat": ("AlphaTauri", 32),
            "Nico Hulkenberg": ("Racing Point", 10),
            "Kimi Raikkonen": ("Alfa Romeo", 4),
            "Antonio Giovinazzi": ("Alfa Romeo", 4),
            "George Russell": ("Williams", 3),
            "Romain Grosjean": ("Haas", 2),
            "Kevin Magnussen": ("Haas", 1),
            "Nicholas Latifi": ("Williams", 0)
        }

        self.colors = {
            "Mercedes": '#00D2BE',  # Sky blue
            "Red Bull": '#1E41FF',  # Bluish black
            "Racing Point": '#F596C8',  # Pink
            "Renault": '#FFF500',  # Yellow
            "McLaren": '#FF8700',  # Papaya orange
            "Ferrari": '#DC0000',  # Ferrari red
            "AlphaTauri": '#2B4562',  # Dark blue like VISA
            "Alfa Romeo": '#B0B7BD',  # Gray
            "Williams": '#005AFF',  # Light blue
            "Haas": '#B6BABD'  # Light gray
        }

        self.team_points = {
            "Mercedes": 573,
            "Red Bull": 319,
            "McLaren": 202,
            "Racing Point": 195,
            "Renault": 181,
            "Ferrari": 131,
            "AlphaTauri": 107,
            "Alfa Romeo": 8,
            "Haas": 3,
            "Williams": 0
        }
    
    def get_team_points(self):
        return self.team_points