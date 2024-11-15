from matplotlib import pyplot as plt
from f12015 import F1Data2015
from f12016 import F1Data2016
from f12017 import F1Data2017
from f12018 import F1Data2018
from f12019 import F1Data2019
from f12020 import F1Data2020
from f12021 import F1Data2021
from f12022 import F1Data2022
from f12023 import F1Data2023
from f12024 import F1Data2024

season_classes = {
    2015: F1Data2015,
    2016: F1Data2016,
    2017: F1Data2017,
    2018: F1Data2018,
    2019: F1Data2019,
    2020: F1Data2020,
    2021: F1Data2021,
    2022: F1Data2022,
    2023: F1Data2023,
    2024: F1Data2024
}

# User input to choose between WDC and WCC
user_input = input("Enter if you would like to see the Drivers data or Teams data (WDC or WCC): ").strip().upper()

# Function to display the graph
def display_graph(data, title, x_label, y_label, labels, values, colors):
    width = 0.50

    plt.figure(figsize=(14, 8))
    bars = plt.bar(labels, values, width=width, color=colors)

    plt.title(title, fontsize=20, fontweight="bold")
    plt.xlabel(x_label, fontsize=12, fontweight='bold')
    plt.ylabel(y_label, fontsize=12, fontweight='bold')
    plt.xticks(rotation=90)

    for i in range(len(bars)):
        bar = bars[i]
        value = values[i]
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(value), ha='center', va='bottom', fontsize=10, fontweight='bold')

    plt.show()

# Handling user input
if user_input == "WDC":
    season = int(input("Enter the year of the season you want to see the graph of (2015 - 2024): "))
    if season in season_classes:
        f1data = season_classes[season]()
        driverData = list(f1data.nameAndpoints.keys())
        values = [v[1] for v in f1data.nameAndpoints.values()]
        colors = [f1data.colors[f1data.nameAndpoints[driver][0]] for driver in driverData]
        display_graph(f1data, f"Formula 1 Drivers and Their Points ({season} Season)", "Drivers", "Points", driverData, values, colors)
    else:
        print(f"Data for the season {season} is not available.")
elif user_input == "WCC":
    season = int(input("Enter the year of the season you want to see the graph of (2015 - 2024): "))
    if season in season_classes:
        f1data = season_classes[season]()
        teamData = list(f1data.get_team_points().keys())
        values = list(f1data.get_team_points().values())
        colors = [f1data.colors[team] for team in teamData]
        display_graph(f1data, f"Formula 1 Teams and Their Points ({season} Season)", "Teams", "Points", teamData, values, colors)
    else:
        print(f"Data for the season {season} is not available.")
else:
    print("Wrong Input!")


