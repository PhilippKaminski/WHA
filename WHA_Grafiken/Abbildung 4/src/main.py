import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Stil & Schrift
sns.set_style("whitegrid")
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman"]

# Farben definieren:
# Westdeutschland: bewährte tiefe Pastellblau-Töne
# Ostdeutschland: professionelle, tiefe Pastellviolett-Töne
colors = {
    "West_Maenner": "#5C7CA8",     # kräftiges, dunkleres Blau
    "West_Frauen": "#90B7D5",
    "Ost_Maenner": "#8A58B3",       # tiefes, professionelles Pastellviolett
    "Ost_Frauen": "#B59ADA"         # etwas hellerer Violettton, aber immer noch pastellig
}

# Pfad zur CSV-Datei
data_path = os.path.join(os.path.dirname(__file__), "..", "data", "gender_pay_gap.csv")
df = pd.read_csv(data_path)

# 'Jahr' als Ganzzahl und chronologisch sortieren
df['Jahr'] = df['Jahr'].astype(int)
df = df.sort_values(by="Jahr")

# Filter für den Bar Chart: Auswahl der Daten in 5-Jahres-Schritten
df_bars = df[df['Jahr'] % 5 == 0].copy()

# Berechnung des geschlechterbezogenen Abstands (Differenz in Prozentpunkten: Männer - Frauen)
df_bars['West_gap'] = df_bars['West_Maenner'] - df_bars['West_Frauen']
df_bars['Ost_gap'] = df_bars['Ost_Maenner'] - df_bars['Ost_Frauen']

# Plot erstellen
fig, ax = plt.subplots(figsize=(10, 6))

# --- Line Chart ---
# Markergröße wurde auf 4 angepasst.
# Westdeutschland: Männer und Frauen
ax.plot(df['Jahr'], df['West_Maenner'], color=colors["West_Maenner"],
        marker='o', linestyle='-', linewidth=2, markersize=0,
        label='Westdeutschland – Männer')
ax.plot(df['Jahr'], df['West_Frauen'], color=colors["West_Frauen"],
        marker='s', linestyle='-', linewidth=2, markersize=0,
        label='Westdeutschland – Frauen')
# Ostdeutschland: Männer und Frauen (violett)
ax.plot(df['Jahr'], df['Ost_Maenner'], color=colors["Ost_Maenner"],
        marker='^', linestyle='-', linewidth=2, markersize=0,
        label='Ostdeutschland – Männer')
ax.plot(df['Jahr'], df['Ost_Frauen'], color=colors["Ost_Frauen"],
        marker='D', linestyle='-', linewidth=2, markersize=0,
        label='Ostdeutschland – Frauen')

# --- Bar Chart für den geschlechterbezogenen Abstand ---
# Die Balken werden leicht versetzt dargestellt, um Überlagerungen zu vermeiden.
bar_width = 1
ax.bar(df_bars['Jahr'] - bar_width/2, df_bars['West_gap'], width=bar_width,
       color=colors["West_Maenner"], alpha=0.6,
       label='Westdeutschland – Geschlechterabstand')
ax.bar(df_bars['Jahr'] + bar_width/2, df_bars['Ost_gap'], width=bar_width,
       color=colors["Ost_Maenner"], alpha=0.6,
       label='Ostdeutschland – Geschlechterabstand')

# Achsenbeschriftungen und Ticks
ax.set_xlabel("Jahr", fontsize=18)
ax.set_ylabel("Erwerbsquote (%)", fontsize=18)
ax.tick_params(axis='both', labelsize=18)
# X-Achse: Ticks in 5-Jahres-Schritten von 1990 bis 2025
ticks = list(range(1990, 2026, 5))
ax.set_xticks(ticks)
# Y-Achsen-Bereich von 0 bis 100
ax.set_ylim(0, 100)

# Legende: minimal weiter unten, sodass sie zwischen Linien- und Balkendiagramm sitzt (mitte-rechts)
ax.legend(fontsize=16, frameon=True, shadow=True, loc='center right', bbox_to_anchor=(1, 0.4))

# Layout anpassen und Grafik speichern
plt.tight_layout()
output_dir = os.path.join(os.path.dirname(__file__), "..", "output", "figures")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "gender_pay_gap.png")
plt.savefig(output_path, dpi=300)
plt.show()
