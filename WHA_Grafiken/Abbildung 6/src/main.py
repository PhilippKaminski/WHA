import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------------------------
# Hauptscript: Plottet den Gender Pay Gap nach Alter 
# -----------------------------------------------------

# 1) Stil & Schrift setzen
sns.set_style("whitegrid")
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman"]

# 2) Farben definieren
colors = {
    "West": "#90B7D5",     # Pastell-Blau
    "Ost": "#B59ADA",      # Pastell-Violett
    "Gesamt": "#7C83C2"    # Neutrales Violett/Blauton
}

def main():
    # 3) Daten laden
    data_path = os.path.join(
        os.path.dirname(__file__), 
        "..", 
        "data", 
        "gender_pay_gap_by_age.csv"
    )
    df = pd.read_csv(data_path)

    # 4) Plot vorbereiten
    fig, ax = plt.subplots(figsize=(10, 6))

    # X-Werte für kategoriale Daten (Indizes)
    x_values = range(len(df))

    # 5) Linien zeichnen
    ax.plot(x_values, df["Gesamt"], 
            color=colors["Gesamt"],
            marker='o', linestyle='-', linewidth=2, markersize=5,
            label='Deutschland gesamt')
    
    ax.plot(x_values, df["West"], 
            color=colors["West"],
            marker='s', linestyle='-', linewidth=2, markersize=5,
            label='Westdeutschland')
    
    ax.plot(x_values, df["Ost"], 
            color=colors["Ost"],
            marker='^', linestyle='-', linewidth=2, markersize=5,
            label='Ostdeutschland')

    # 6) Achsenbeschriftung mit labelpad (mehr Abstand)
    ax.set_xlabel("Altersgruppe", fontsize=18, labelpad=15)
    ax.set_ylabel("Gender Pay Gap (%)", fontsize=18, labelpad=15)
    ax.tick_params(axis='both', labelsize=16)

    # 7) X-Achsen-Kategorien manuell setzen
    ax.set_xticks(x_values)
    ax.set_xticklabels(df["Alter"], rotation=0)

    # 8) Legende oben links positionieren
    ax.legend(loc='upper left', fontsize=18, frameon=True, shadow=True)

    # 9) Y-Achsen-Bereich festlegen
    ax.set_ylim(0, 30)

    # 10) Layout anpassen und speichern (kein unnötiger Rand)
    plt.tight_layout()
    output_dir = os.path.join(os.path.dirname(__file__), "..", "output", "figures")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "gender_pay_gap_by_age.png")
    plt.savefig(output_path, dpi=300)

    # 11) Plot anzeigen
    plt.show()

if __name__ == "__main__":
    main()
