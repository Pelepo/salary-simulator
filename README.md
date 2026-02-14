# 💰 Simulatore Retribuzione Netta

Prototipo di web application sviluppata in Python (Streamlit) per stimare la retribuzione netta annuale e mensile a partire dalla RAL (Retribuzione Annua Lorda).

---

## Obiettivo del progetto

L'obiettivo del progetto è:

- Simulare la proiezione di retribuzione netta annuale partendo dalla RAL
- Mostrare tutte le voci che devono essere trattenute dal lordo in modo semplice e chiaro
- Strutturare le logiche in modo modulare e versionabile

## Ipotesi di simulazione

Il modello attuale considera:

- Lavoratore dipendente con un contratto a tempo indeterminato
- Residente a Milano
- Nessuna agevolazione fiscale
- Nessun familiare a carico

## 🧮 Logica di calcolo

La RAL viene trasformata in netto secondo la seguente sequenza:

1. Contributi previdenziali lavoratore

9,19%

Source: https://www.randstad.it/blog-e-news/diritti-dei-lavoratori/trattenute-busta-paga/

2. IRPEF progressiva a scaglioni

fino a 28,000€ => 23%
fino a 50,000€ => 33% (Aggiornamento a seguito della Legge di Bilancio 2026)
oltre a 50,000€ => 43%

Source: https://www.agenziaentrate.gov.it/portale/imposta-sul-reddito-delle-persone-fisiche-irpef-/aliquote-e-calcolo-dell-irpef

3. Detrazioni per lavoro dipendente

fino a 15,000€ => 1,955€

15.000 € < Reddito ≤ 28.000 € => 1.910 + 1.190 × (28.000−reddito)​ / 13.000
28.000 € < Reddito ≤ 50.000 € => 1.910 × (50.000−reddito) / 22.000

oltre a 50,000€ => Nessuna detrazione

Source: https://www.informazionefiscale.it/detrazioni-lavoro-dipendente-importo-calcolo

4. Addizionale regionale

fino a 15,000€ => 1,23%

15.000 € < Reddito ≤ 28.000 € => 1,58%
28.000 € < Reddito ≤ 50.000 € => 1,72%

Oltre i 50.000 euro => 1,73%

Source: https://www.regione.lombardia.it/wps/portal/istituzionale/HP/DettaglioRedazionale/servizi-e-informazioni/cittadini/tributi-e-canoni/addizionale-irpef

5. Addizionale comunale

fino a 23,000€ => 0%
Oltre i 23,000€ => 0.8%

Source: https://www.comune.milano.it/argomenti/tributi/addizionale-comunale-irpef

6. Calcolo netto annuale e mensile

---

## 🚀 Come eseguire il progetto

### 1. Creare ambiente virtuale

python3 -m venv venv
source venv/bin/activate

### 2. Installare dipendenze

pip install -r requirements.txt

### 3. Avviare l'app

streamlit run app.py
