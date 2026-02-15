import streamlit as st
import pandas as pd
from salary.models import SalaryInput, TaxYear
from salary.calculator import calculate_salary
from streamlit_echarts import st_echarts
from ui import colored_badge 

def format_euro(value: float) -> str:
    return f"{value:,.0f}".replace(",", ".") + " €"

# Titolo pagina
st.set_page_config(page_title="Simulatore Stipendio Netto", page_icon="💰", layout="centered")

# Heading

st.title("💰 Simulatore Retribuzione Netta")
st.write("Calcola il netto annuale e mensile a partire dalla RAL.")

# Input

ral = st.number_input(
    "Inserisci la RAL (€)",
    min_value=0,
    value=30000,
    step=1000,
    format="%d"
)

mensilita = st.selectbox(
    "Numero mensilità",
    options=[12, 13, 14],
    index=1,
)

anno = st.selectbox(
    "Anno fiscale",
    options=[2026, 2025],
    index=0,
    disabled=True
)

st.markdown(
    """
    <div style="color: grey; font-style: italic; font-size: 14px; text-align: right;">
        lavoratore dipendente a tempo indeterminato a Milano senza agevolazioni
    </div>
    """,
    unsafe_allow_html=True
)

# Bottone per il calcolo

if st.button("Calcola netto"):

    if ral <= 0:
        st.error("Inserisci una RAL maggiore di zero.")
    else:
        # Creazione input model
        input_data = SalaryInput(
            ral=ral,
            mensilita=mensilita,
            tax_year=TaxYear(year=anno),
        )

        result = calculate_salary(input_data)

        # Output

        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                label="💰 Netto annuale",
                value=f"{result.netto_annuo:,.2f} €"
            )

        with col2:
            st.metric(
                label="📅 Netto mensile",
                value=f"{result.netto_mensile:,.2f} €"
            )
        
        st.divider()

        # DETTAGLIO SEMPLIFICATO

        st.subheader("🧾 Dove finiscono i soldi del tuo stipendio")

        with st.expander("Contributi", True, icon="👴🏼"):
            st.caption("Quota che versi per la tua pensione futura.")
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write("Contributi previdenziali")
            with col2:
                valore = round(-result.contributi, 2)
                colored_badge(valore)
        with st.expander("IRPEF", True, icon="💸"):
            st.caption("L’imposta principale sul tuo reddito.")
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write("IRPEF lorda (prima degli sconti):")
            with col2:
                valore = round(-result.irpef_lorda, 2)
                colored_badge(valore)

            col1, col2 = st.columns([4, 1])
            with col1:
                st.write("Detrazioni lavoro dipendente:")
            with col2:
                valore = round(result.detrazioni_lavoro, 2)
                colored_badge(valore)

            col1, col2 = st.columns([4, 1])
            with col1:
                st.write("Bonus cuneo fiscale:")
            with col2:
                valore = round(result.detrazione_cuneo_fiscale, 2)
                colored_badge(valore)

            col1, col2 = st.columns([4, 1])
            with col1:
                st.write("👉 IRPEF netta (quella che paghi davvero):")
            with col2:
                valore = round(-result.irpef_netta, 2)
                colored_badge(valore)

            col1, col2 = st.columns([4, 1])
            with col1:
                st.write("Somma integrativa:")
            with col2:
                valore = round(result.somma_integrativa, 2)
                colored_badge(valore)
            
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write("Trattamento Integrativo:")
            with col2:
                valore = round(result.trattamento_integrativo, 2)
                colored_badge(valore)

            

        with st.expander("Addizionali", True, icon="🌆"):
            st.caption("Imposte locali trattenute da Regione e Comune.")
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write("Addizionale regionale:")
            with col2:
                valore = round(-result.addizionale_regionale, 2)
                colored_badge(valore)

            col1, col2 = st.columns([4, 1])
            with col1:
                st.write("Addizionale comunale:")
            with col2:
                valore = round(-result.addizionale_comunale, 2)
                colored_badge(valore)
        
        # FINALE 

        st.divider()

        st.subheader("🛖 Quanto porti a casa")

        totale_tasse = (
            result.contributi +
            result.irpef_netta +
            result.addizionale_regionale +
            result.addizionale_comunale
        )

        percentuale_tasse = totale_tasse / result.ral
        percentuale_netto = result.netto_annuo / result.ral

        percentuale_netto = max(0.0, min(1.0, percentuale_netto))

        st.progress(percentuale_netto)

        st.write(
            f"Su {format_euro(result.ral)} di RAL:\n"
            f"- 💸 {format_euro(totale_tasse)} vanno in tasse e contributi\n"
            f"- 💰 {format_euro(result.netto_annuo)} ti restano"
        )
        st.success(
            f"Lo Stato trattiene {format_euro(totale_tasse)} "
            f"({percentuale_tasse*100:.1f}% del tuo lordo)."
        )



