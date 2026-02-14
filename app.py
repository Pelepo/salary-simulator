import streamlit as st
import pandas as pd
from salary.models import SalaryInput, TaxYear
from salary.calculator import calculate_salary

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
    <div style="color: grey; font-style: italic; text-align: right;">
        lavoratore dipendente a tempo indeterminato che vive a Milano senza agevolazioni
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
                label="Netto annuale",
                value=f"{result.netto_annuo:,.2f} €"
            )

        with col2:
            st.metric(
                label="Netto mensile",
                value=f"{result.netto_mensile:,.2f} €"
            )

        st.subheader("📊 Dettaglio Tasse")

        data = [
            {
                "Dicitura formale": "Contributi previdenziali",
                "AKA": "Per la pensione",
                "Valore annuale": format_euro(result.contributi),
                "Valore mensile": format_euro(result.contributi / input_data.mensilita),
            },
            {
                "Dicitura formale": "IRPEF lorda",
                "AKA": "La tassa principale sul tuo reddito",
                "Valore annuale": format_euro(result.irpef_lorda),
                "Valore mensile": format_euro(result.irpef_lorda / input_data.mensilita),
            },
            {
                "Dicitura formale": "Detrazioni lavoro dipendente",
                "AKA": "Lo sconto base sulle tasse",
                "Valore annuale": format_euro(result.detrazioni_lavoro),
                "Valore mensile": format_euro(result.detrazioni_lavoro / input_data.mensilita),
            },
            {
                "Dicitura formale": "Detrazione cuneo fiscale",
                "AKA": "Bonus per ridurre le tasse",
                "Valore annuale": format_euro(result.detrazione_cuneo_fiscale),
                "Valore mensile": format_euro(result.detrazione_cuneo_fiscale / input_data.mensilita),
            },
            {
                "Dicitura formale": "Somma Integrativa",
                "AKA": "Bonus per redditi bassi",
                "Valore annuale": format_euro(result.somma_integrativa),
                "Valore mensile": format_euro(result.somma_integrativa / input_data.mensilita),
            },
            {
                "Dicitura formale": "IRPEF netta",
                "AKA": "Quello che davvero paghi allo Stato",
                "Valore annuale": format_euro(result.irpef_netta),
                "Valore mensile": format_euro(result.irpef_netta / input_data.mensilita),
            },
            {
                "Dicitura formale": "Addizionale regionale",
                "AKA": "La quota per la Regione",
                "Valore annuale": format_euro(result.addizionale_regionale),
                "Valore mensile": format_euro(result.addizionale_regionale / input_data.mensilita),
            },
            {
                "Dicitura formale": "Addizionale comunale",
                "AKA": "La quota per il Comune",
                "Valore annuale": format_euro(result.addizionale_comunale),
                "Valore mensile": format_euro(result.addizionale_comunale / input_data.mensilita),
            },
            {
                "Dicitura formale": "Reddito Netto",
                "AKA": "Cosa ti resta",
                "Valore annuale": format_euro(result.netto_annuo),
                "Valore mensile": format_euro(result.netto_mensile),
            },
            
        ]


        df = pd.DataFrame(data)

        st.dataframe(df, hide_index=True, width='stretch')


        percentuale_tasse = (
            result.contributi +
            result.irpef_netta +
            result.addizionale_regionale +
            result.addizionale_comunale
        ) / result.ral * 100

        st.info(
            f"Su una RAL di {format_euro(result.ral)}, "
            f"trattieni circa il {percentuale_tasse:.1f}% in tasse e contributi."
        )



