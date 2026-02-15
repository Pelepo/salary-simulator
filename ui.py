import streamlit as st

def colored_badge(value, suffix="€", decimals=2):
    valore = round(value, decimals)
    colore = "#dc2626" if valore < 0 else "#16a34a"

    st.markdown(
        f"""
        <div style="
            width:100%;
            text-align:right;
            font-size:15px;
            color:{colore};
            font-weight:500;
        ">
            {valore:,.2f} {suffix}
        </div>
        """,
        unsafe_allow_html=True
    )
