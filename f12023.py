class F1Data2023:
    def __init__(self):
        self.nameAndpoints = {
            "Max Verstappen": ("Red Bull", 575),
            "Sergio Perez": ("Red Bull", 285),
            "Lewis Hamilton": ("Mercedes", 234),
            "Fernando Alonso": ("Aston Martin", 206),
            "Charles Leclerc": ("Ferrari", 206),
            "Lando Norris": ("McLaren", 205),
            "Carlos Sainz": ("Ferrari", 200),
            "George Russell": ("Mercedes", 175),
            "Oscar Piastri": ("McLaren", 97),
            "Lance Stroll": ("Aston Martin", 74),
            "Pierre Gasly": ("Alpine", 62),
            "Esteban Ocon": ("Alpine", 58),
            "Alexander Albon": ("Williams", 27),
            "Yuki Tsunoda": ("AlphaTauri", 17),
            "Valtteri Bottas": ("Alfa Romeo", 10),
            "Nico Hulkenberg": ("Haas", 9),
            "Daniel Ricciardo": ("AlphaTauri", 6),
            "Zhou Guanyu": ("Alfa Romeo", 6),
            "Kevin Magnussen": ("Haas", 3),
            "Liam Lawson": ("AlphaTauri", 2),
            "Logan Sargeant": ("Williams", 1),
            "Nyck De Vries": ("AlphaTauri", 0)
        }

        self.colors = {
            "Red Bull": '#1E41FF',  # Bluish black
            "McLaren": '#FF8700',  # Papaya orange
            "Ferrari": '#DC0000',  # Ferrari red
            "Mercedes": '#00D2BE',  # Sky blue
            "Aston Martin": '#006F62',  # Bluish green
            "Haas": '#B6BABD',  # Light gray
            "AlphaTauri": '#2B4562',  # Dark blue like VISA
            "Alpine": '#FF5F5F',  # Pink
            "Williams": '#005AFF',  # Light blue
            "Alfa Romeo": '#B0B7BD',  # Gray
        }

        self.team_points = {
            "Red Bull": 860,
            "Mercedes": 409,
            "Ferrari": 406,
            "McLaren": 302,
            "Aston Martin": 280,
            "Alpine": 120,
            "Williams": 28,
            "AlphaTauri":25,
            "Alfa Romeo": 16,
            "Haas": 12
        }
    def get_team_points(self):
        return self.team_points