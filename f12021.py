class F1Data2021:
    def __init__(self):
        self.nameAndpoints = {
            "Max Verstappen": ("Red Bull", 395.5),
            "Lewis Hamilton": ("Mercedes", 387.5),
            "Valtteri Bottas": ("Mercedes", 226),
            "Sergio Perez": ("Red Bull", 190),
            "Carlos Sainz": ("Ferrari", 164.5),
            "Lando Norris": ("McLaren", 160),
            "Charles Leclerc": ("Ferrari", 159),
            "Daniel Ricciardo": ("McLaren", 115),
            "Pierre Gasly": ("AlphaTauri", 110),
            "Fernando Alonso": ("Alpine", 81),
            "Esteban Ocon": ("Alpine", 74),
            "Sebastian Vettel": ("Aston Martin", 43),
            "Lance Stroll": ("Aston Martin", 34),
            "Yuki Tsunoda": ("AlphaTauri", 32),
            "George Russell": ("Williams", 16),
            "Kimi Raikkonen": ("Alfa Romeo", 10),
            "Nicholas Latifi": ("Williams", 7),
            "Antonio Giovinazzi": ("Alfa Romeo", 3),
            "Mick Schumacher": ("Haas", 0),
            "Robert Kubica": ("Alfa Romeo", 0),
            "Nikita Mazepin": ("Haas", 0)
        }

        self.colors = {
            "Red Bull": '#1E41FF',  # Bluish black
            "Mercedes": '#00D2BE',  # Sky blue
            "Ferrari": '#DC0000',  # Ferrari red
            "McLaren": '#FF8700',  # Papaya orange
            "AlphaTauri": '#2B4562',  # Dark blue like VISA
            "Alpine": '#FF5F5F',  # Pink
            "Aston Martin": '#006F62',  # Bluish green
            "Williams": '#005AFF',  # Light blue
            "Alfa Romeo": '#B0B7BD',  # Gray
            "Haas": '#B6BABD'  # Light gray
        }

        self.team_points = {
            "Mercedes": 613.5,
            "Red Bull": 585.5,
            "Ferrari": 323.5,
            "McLaren": 275,
            "Alpine": 155,
            "AlphaTauri": 142,
            "Aston Martin": 77,
            "Williams": 23,
            "Alfa Romeo": 13, 
            "Haas": 0
        }

    def get_team_points(self):
        return self.team_points