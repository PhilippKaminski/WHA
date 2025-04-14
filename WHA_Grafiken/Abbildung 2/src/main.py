import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Stil & Schrift
sns.set_style("whitegrid")
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman"]

# Farben (Blaue Pastell-Palette)
colors = {
    "Deutschland": "#7C83C2",
    "Westdeutschland": "#90B7D5",
    "Ostdeutschland": "#B59ADA"
}

# Daten Laden
data_path = os.path.join(os.path.dirname(__file__), "..", "data", "gender_pay_gap.csv")
df = pd.read_csv(data_path)

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df['Year'], df['Deutschland'], color=colors["Deutschland"],
        marker='o', linestyle='-', linewidth=2, markersize=4,
        label='Deutschland insgesamt')
ax.plot(df['Year'], df['Westdeutschland'], color=colors["Westdeutschland"],
        marker='s', linestyle='-', linewidth=2, markersize=4,
        label='Westdeutschland')
ax.plot(df['Year'], df['Ostdeutschland'], color=colors["Ostdeutschland"],
        marker='^', linestyle='-', linewidth=2, markersize=4,
        label='Ostdeutschland')

# Grafik Beschriftung (mit labelpad für mehr Abstand)
ax.set_xlabel("Jahr", fontsize=18, labelpad=15)
ax.set_ylabel("Gender Pay Gap (%)", fontsize=18, labelpad=15)
ax.tick_params(axis='both', labelsize=18)
ax.legend(fontsize=18, frameon=True, shadow=True)

# X-Achsen-Ticks (alle 5 Jahre)
ticks = [1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025]
ax.set_xticks(ticks)

# Y-Achsen-Bereich
ax.set_ylim(0, 35)

# Layout anpassen und Grafik speichern (kein unnötiger Rand)
plt.tight_layout()
output_dir = os.path.join(os.path.dirname(__file__), "..", "output", "figures")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "gender_pay_gap.png")
plt.savefig(output_path, dpi=300)
plt.show()
