import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------------------------
# Hauptscript: Plottet die Verteilung der Verdienermodelle 
# (nur für Ost und West) mit internen Prozentbeschriftungen 
# und einer mittig eingebetteten Legende.
# Nur die Zahlen in den Balken (Prozentwerte) werden bold dargestellt.
# Alle übrigen Texte bleiben normal (nur Größe 16).
# -----------------------------------------------------

def main():
    # 1) Stil & Schrift setzen
    sns.set_style("whitegrid")
    plt.rcParams["font.family"] = "serif"
    plt.rcParams["font.serif"] = ["Times New Roman"]
    plt.rcParams["xtick.labelsize"] = 16
    plt.rcParams["ytick.labelsize"] = 16
    
    # 2) Farben definieren
    colors_categories = {
        "beide_vollzeit": "#B59ADA",             # tiefes Pastell-Blau
        "frau_teilzeit_mann_vollzeit": "#90B7D5", # tiefes Pastell-Violett
        "Rest": "#7C83C2"                        # gedeckter Violett/Blauton
    }
    
    # 3) Daten laden
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "gender_pay_gap.csv")
    df = pd.read_csv(data_path)

    # 4) Figure und Achse vorbereiten (Größe: 10 x 4, schmaleres Plotfeld)
    fig, ax = plt.subplots(figsize=(10, 4))
    
    # Balkenhöhe definieren (schmaler als Standard)
    bar_height = 0.5  
    y_positions = range(len(df))  # Positionen: 0 (West) und 1 (Ost)
    
    # 5) Gestapelte Balken erstellen
    # Doppelverdienermodell
    ax.barh(
        y=y_positions,
        width=df["beide_vollzeit"],
        color=colors_categories["beide_vollzeit"],
        label="Doppelverdienermodell",
        height=bar_height
    )
    
    # Traditionelles Zuverdienermodell
    ax.barh(
        y=y_positions,
        width=df["frau_teilzeit_mann_vollzeit"],
        left=df["beide_vollzeit"],
        color=colors_categories["frau_teilzeit_mann_vollzeit"],
        label="Traditionelles Zuverdienermodell",
        height=bar_height
    )
    
    # Rest
    ax.barh(
        y=y_positions,
        width=df["Rest"],
        left=df["beide_vollzeit"] + df["frau_teilzeit_mann_vollzeit"],
        color=colors_categories["Rest"],
        label="Rest",
        height=bar_height
    )
    
    # 6) Prozentangaben in die Balken schreiben (weiße Beschriftung, size 16, bold)
    for i, row in df.iterrows():
        # Berechnung der Mittelpunkte der Segmente
        x1 = row["beide_vollzeit"] / 2
        x2 = row["beide_vollzeit"] + row["frau_teilzeit_mann_vollzeit"] / 2
        x3 = row["beide_vollzeit"] + row["frau_teilzeit_mann_vollzeit"] + row["Rest"] / 2
        
        ax.text(x1, i, f"{row['beide_vollzeit']}%", ha='center', va='center', 
                color='white', fontsize=16, fontweight="bold")
        ax.text(x2, i, f"{row['frau_teilzeit_mann_vollzeit']}%", ha='center', va='center', 
                color='white', fontsize=16, fontweight="bold")
        ax.text(x3, i, f"{row['Rest']}%", ha='center', va='center', 
                color='white', fontsize=16, fontweight="bold")
    
    # 7) Achsenbeschriftungen (Größe 16, normal gewichtet)
    ax.set_xlabel("Anteil in %", fontsize=16)
    ax.set_ylabel("Region", fontsize=16)
    ax.set_yticks(list(y_positions))
    ax.set_yticklabels(df["Region"], rotation=0)
    ax.set_xlim(0, 100)
    
    # 8) Legende mittig zwischen den Balken einbetten, ohne Bold
    ax.legend(loc='center', bbox_to_anchor=(0.5, 0.5), ncol=3,
              prop={'size': 16}, frameon=True)
    
    # 9) Layout anpassen und Grafik speichern
    plt.tight_layout()
    output_dir = os.path.join(os.path.dirname(__file__), "..", "output", "figures")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "verteilung_vollzeit_teilzeit.png")
    plt.savefig(output_path, dpi=300)
    
    # 10) Plot anzeigen
    plt.show()

if __name__ == "__main__":
    main()
