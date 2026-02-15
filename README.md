# 💰 Simulatore Retribuzione Netta

Prototipo di webApp sviluppata in Python (Streamlit) per stimare la retribuzione netta annuale e mensile a partire dalla RAL.

---

## Obiettivo del progetto

L'obiettivo del progetto è:

- Simulare la proiezione di retribuzione netta annuale e mensile partendo dalla RAL
- Mostrare tutte le voci che devono essere trattenute dal lordo in modo semplice e chiaro
- Strutturare le logiche in modo modulare e versionabile

Il modello rappresenta una simulazione semplificata e parametrizzabile. Eventuali evoluzioni possono riguardare l'estensione normativa, la generalizzazione territoriale e l’automatizzazione degli aggiornamenti fiscali.

## Ipotesi di simulazione

Il modello attuale considera:

- Lavoratore dipendente con un contratto a tempo indeterminato
- Residente a Milano
- Nessuna agevolazione fiscale
- Nessun familiare a carico

⚠️⚠️⚠️⚠️⚠️ Il modello non include il trattamento integrativo (ex Bonus IRPEF 100€)

## 🧮 Logica di calcolo

La RAL viene trasformata in netto secondo la seguente sequenza:

1. Contributi previdenziali lavoratore

9,19%

La componente contributiva a carico del lavoratore è stata modellata, per semplicità, con un’aliquota media del 9,19%, riferita alla componente IVS (Invalidità, Vecchiaia e Superstiti) dei contributi obbligatori.

⚠️ Le aliquote effettive possono variare in funzione del CCNL applicato, della dimensione dell'azienda (stiamo considerando una azienda con più di 15 dipendenti) della gestione previdenziale e di eventuali fondi integrativi

Source:
INPS – Aliquote contributive lavoratori dipendenti -> https://www.inps.it
Proia - INPS dei dipendenti -> http://www.proia.it/1/inps_dei_dipendenti_970948.html

2. IRPEF progressiva a scaglioni

fino a 28,000€ => 23%
fino a 50,000€ => 33% (Aggiornamento a seguito della Legge di Bilancio 2026)
oltre a 50,000€ => 43%

Source:
Agenzia delle Entrate – Aliquote e calcolo IRPEF -> https://www.agenziaentrate.gov.it/portale/imposta-sul-reddito-delle-persone-fisiche-irpef-/aliquote-e-calcolo-dell-irpef

3. Detrazioni per lavoro dipendente

fino a 15,000€ => 1,955€
15.000 € < Reddito IMPONIBILE ≤ 28.000 € => 1.910 + 1.190 × (28.000−reddito)​ / 13.000
28.000 € < Reddito IMPONIBILE ≤ 50.000 € => 1.910 × (50.000−reddito) / 22.000
oltre a 50,000€ => Nessuna detrazione
⚠️ Inoltre per i reddito COMPLESSIVI superiori a 25.000 euro e fino a 35.000 euro, l’importo della detrazione va aumentato di 65 euro.

Source:
Guida fiscale su detrazioni lavoro dipendente -> https://www.informazionefiscale.it/detrazioni-lavoro-dipendente-importo-calcolo

Per i lavoratori con reddito COMPLESSIVO tra 20.000 € e 40.000 € spetta una detrazione aggiuntiva sull’IRPEF:
Tra 20.000 € e 32.000 € => detrazione fissa di 1.000 €
Tra 32.000 € e 40.000 € => detrazione che diminuisce progressivamente da 1.000 € a 0 €
Oltre 40.000 € => nessuna detrazione

Source:
ANCE - Legge di Bilancio 2025 -> https://portale.assimpredilance.it/articoli/legge-di-bilancio-2025-lavoro-dipendente-le-novita-fiscali

4. Addizionale regionale

fino a 15,000€ => 1,23%

15.000 € < Reddito IMPONIBILE ≤ 28.000 € => 1,58%
28.000 € < Reddito IMPONIBILE ≤ 50.000 € => 1,72%

Oltre i 50.000 euro => 1,73%

Source:
Regione Lombardia – Addizionale IRPEF -> https://www.regione.lombardia.it/wps/portal/istituzionale/HP/DettaglioRedazionale/servizi-e-informazioni/cittadini/tributi-e-canoni/addizionale-irpef

5. Addizionale comunale

Reddito IMPONIBILE < 23,000€ => 0%
Reddito IMPONIBILE > 23,000€ => 0.8%

Source:
Comune di Milano – Addizionale comunale IRPEF -> https://www.comune.milano.it/argomenti/tributi/addizionale-comunale-irpef

6. Somma Integrativa

Per i lavoratori con reddito COMPLESSIVO fino a 20.000 € spetta una somma integrativa aggiuntiva in busta paga, calcolata in percentuale sul reddito:

Fino a 8.500 € => 7,1% del reddito
Tra 8.500 € e 15.000 € => 5,3% del reddito
Tra 15.000 € e 20.000 € => 4,8% del reddito
Oltre 20.000 € => nessuna somma integrativa

Source:
Guida fiscale su detrazioni lavoro dipendente -> https://www.informazionefiscale.it/detrazioni-lavoro-dipendente-importo-calcolo

6. Calcolo netto annuale e mensile

⚠️⚠️⚠️⚠️⚠️ Il modello non include il trattamento integrativo (ex Bonus IRPEF 100€)

---

## 🚀 Come eseguire il progetto

### 1. Creare ambiente virtuale

python3 -m venv venv
source venv/bin/activate

### 2. Installare dipendenze

pip install -r requirements.txt

### 3. Avviare l'app

streamlit run app.py
