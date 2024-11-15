class F1Data2019:
    def __init__(self):
        self.nameAndpoints = {
            "Lewis Hamilton": ("Mercedes", 413),
            "Valtteri Bottas": ("Mercedes", 326),
            "Max Verstappen": ("Red Bull", 278),
            "Charles Leclerc": ("Ferrari", 264),
            "Sebastian Vettel": ("Ferrari", 240),
            "Carlos Sainz": ("McLaren", 96),
            "Pierre Gasly": ("Toro Rosso", 95),
            "Alexander Albon": ("Toro Rosso", 92),
            "Daniel Ricciardo": ("Renault", 54),
            "Sergio Perez": ("Racing Point", 52),
            "Lando Norris": ("McLaren", 49),
            "Kimi Raikkonen": ("Alfa Romeo", 43),
            "Daniil Kvyat": ("Toro Rosso", 37),
            "Nico Hulkenberg": ("Renault", 37),
            "Lance Stroll": ("Racing Point", 21),
            "Kevin Magnussen": ("Haas", 20),
            "Romain Grosjean": ("Haas", 8),
            "Antonio Giovinazzi": ("Alfa Romeo", 4),
            "Robert Kubica": ("Williams", 1),
            "George Russell": ("Williams", 0)
        }

        self.colors = {
            "Mercedes": '#00D2BE',  # Sky blue
            "Ferrari": '#DC0000',  # Ferrari red
            "Red Bull": '#1E41FF',  # Bluish black
            "Renault": '#FFF500',  # Yellow
            "McLaren": '#FF8700',  # Papaya orange
            "Racing Point": '#F596C8',  # Pink
            "Toro Rosso": '#000080',  # Navy blue
            "Haas": '#B6BABD',  # Light gray
            "Alfa Romeo": '#B0B7BD',  # Gray
            "Williams": '#005AFF'  # Light blue
        }

        self.team_points = {
            "Mercedes": 739,
            "Ferrari": 504,
            "Red Bull": 417,
            "McLaren": 145,
            "Renault": 91,
            "Toro Rosso": 85,
            "Racing Point": 73,
            "Alfa Romeo": 57,
            "Haas": 28,
            "Williams": 1
        }
    def get_team_points(self):
        return self.team_points