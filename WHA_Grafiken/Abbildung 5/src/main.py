import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Stil & Schrift
sns.set_style("whitegrid")
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman"]

# Farben (angepasste Pastell-Farben)
colors = {
    "Ost": "#B59ADA",   # tiefes, professionelles Pastellviolett
    "West": "#90B7D5",  # kräftiges, dunkles Pastellblau
}

# Daten Laden
data_path = os.path.join(os.path.dirname(__file__), "..", "data", "betreuungsquote.csv")
df = pd.read_csv(data_path)

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Hinzufügen des hellgrauen Blocks für "Wiedervereinigung" von 1990 bis 1991
ax.axvspan(1990, 1991, color='lightgrey', alpha=0.5, zorder=0)
# Angepasster Text: kleiner und etwas tiefer (hier y=30, fontsize=14)
ax.text(1990.5, 30, 'Wiedervereinigung', ha='center', va='center', fontsize=14, color='black', rotation=90, zorder=1)

# Plotten der Zeitreihen
ax.plot(df['Jahr'], df['Ost'], color=colors["Ost"],
        marker='^', linestyle='-', linewidth=2, markersize=4,
        label='Ostdeutschland')
ax.plot(df['Jahr'], df['West'], color=colors["West"],
        marker='s', linestyle='-', linewidth=2, markersize=4,
        label='Westdeutschland')

# Grafik Beschriftung mit mehr Abstand durch labelpad
ax.set_xlabel("Jahr", fontsize=18, labelpad=15)
ax.set_ylabel("Betreuungsquote (%)", fontsize=18, labelpad=15)
ax.tick_params(axis='both', labelsize=18)
ax.legend(fontsize=18, frameon=True, shadow=True)

# X-Achsen-Ticks: ab 1985 im 5-Jahresschritt
ticks = list(range(1985, 2026, 5))
ax.set_xticks(ticks)

# Y-Achsen-Bereich – anpassen, sodass beide Datenreihen gut sichtbar sind
ax.set_ylim(0, 90)

# Minimiert den unnötigen Rand, während der labelpad die Beschriftungen absetzt.
plt.tight_layout()

# Grafik Speicher
output_dir = os.path.join(os.path.dirname(__file__), "..", "output", "figures")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "betreuungsquote.png")
plt.savefig(output_path, dpi=300)
plt.show()
