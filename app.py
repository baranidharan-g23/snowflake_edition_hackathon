import streamlit as st
import pandas as pd

# Import components
from components.data_loader import (
    load_all_data, load_unesco_data, load_top_monuments_domestic_data, load_top_monuments_foreign_data,
    load_centrally_protected_domestic_data, load_centrally_protected_foreign_data,
    load_tourism_gdp_data, load_tourism_employment_data,
    load_fee_earnings_data, load_india_world_share_data, load_ita_data, load_ita_monthly_data,
    load_duration_stay_data, load_age_statistics_data, load_all_lean_peak_data,
    load_state_tourism_data, load_state_domestic_tourist_arrivals_data,
    load_state_foreign_tourist_arrivals_data, load_state_total_tourist_arrivals_data,
    load_festivals_data, load_dance_data, load_heritage_sites_data
)
from components.homepage import show_homepage
from components.festivals import show_festivals_section
from components.dance_forms import show_dance_section
from components.heritage_sites import show_heritage_section
from components.chapter1_heritage_heartbeat import show_heritage_heartbeat
from components.chapter2_economic_multiplier import show_economic_multiplier
from components.chapter3_travelers_journey import show_travelers_journey
from components.chapter4_regional_tapestry import show_regional_tapestry
from styles.css_styles import apply_custom_css, apply_dance_styles, apply_sidebar_styles

# Page configuration
st.set_page_config(
    page_title="Indian Cultural Heritage & Tourism",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply CSS styles
apply_custom_css()
apply_dance_styles()
apply_sidebar_styles()

def main():
    # Home
    if st.sidebar.button("🏠 Home", use_container_width=True):
        st.session_state.page = "🏠 Home"

    # Arts & Culture Section
    st.sidebar.markdown("### 🎭 Arts & Culture")
    if st.sidebar.button("🎪 Festivals", use_container_width=True):
        st.session_state.page = "🎪 Festivals"
    if st.sidebar.button("💃 Dance Forms", use_container_width=True):
        st.session_state.page = "💃 Dance Forms"
    if st.sidebar.button("🏛️ Heritage Sites", use_container_width=True):
        st.session_state.page = "🏛️ Heritage Sites"

    # Tourism Story Section
    st.sidebar.markdown("### 📖 India's Tourism Story")
    if st.sidebar.button("🏛️ Chapter 1: Heritage Heartbeat", use_container_width=True):
        st.session_state.page = "🏛️ Chapter 1: Heritage Heartbeat"
    if st.sidebar.button("💰 Chapter 2: Economic Multiplier", use_container_width=True):
        st.session_state.page = "💰 Chapter 2: Economic Multiplier"
    if st.sidebar.button("🌍 Chapter 3: Traveler's Journey", use_container_width=True):
        st.session_state.page = "🌍 Chapter 3: Traveler's Journey"
    if st.sidebar.button("🗺️ Chapter 4: Regional Tapestry", use_container_width=True):
        st.session_state.page = "🗺️ Chapter 4: Regional Tapestry"

    # Initialize page if not set
    if 'page' not in st.session_state:
        st.session_state.page = "🏠 Home"

    page = st.session_state.page

    # Load all data using the data loader (for existing components)
    data = load_all_data()

    if page == "🏠 Home":
        show_homepage(
            data['festivals_df'],
            data['ita_df'],
            data['state_tourism_df'],
            data['tourism_gdp_df'],
            data['tourism_employment_df']
        )
    elif page == "🎪 Festivals":
        show_festivals_section(data['festivals_df'])
    elif page == "💃 Dance Forms":
        show_dance_section(data['dance_df'])
    elif page == "🏛️ Heritage Sites":
        show_heritage_section()
    elif page == "🏛️ Chapter 1: Heritage Heartbeat":
        # Load heritage data
        unesco_df = load_unesco_data()
        top_monuments_domestic_df = load_top_monuments_domestic_data()
        top_monuments_foreign_df = load_top_monuments_foreign_data()
        centrally_protected_domestic_df = load_centrally_protected_domestic_data()
        centrally_protected_foreign_df = load_centrally_protected_foreign_data()

        show_heritage_heartbeat(
            unesco_df,
            top_monuments_domestic_df,
            top_monuments_foreign_df,
            centrally_protected_domestic_df,
            centrally_protected_foreign_df
        )

    elif page == "💰 Chapter 2: Economic Multiplier":
        # Load economic data
        tourism_gdp_df = load_tourism_gdp_data()
        tourism_employment_df = load_tourism_employment_data()
        fee_earnings_df = load_fee_earnings_data()
        india_world_share_df = load_india_world_share_data()

        show_economic_multiplier(
            tourism_gdp_df,
            tourism_employment_df,
            fee_earnings_df,
            india_world_share_df
        )

    elif page == "🌍 Chapter 3: Traveler's Journey":
        # Load traveler data
        ita_df = load_ita_data()
        ita_monthly_df = load_ita_monthly_data()
        stay_duration_df = load_duration_stay_data()
        age_statistics_df = load_age_statistics_data()
        all_lean_peak_data = load_all_lean_peak_data()

        show_travelers_journey(
            ita_df,
            ita_monthly_df,
            stay_duration_df,
            age_statistics_df,
            all_lean_peak_data
        )

    elif page == "🗺️ Chapter 4: Regional Tapestry":
        # Load regional tourism data using new table structure
        state_total_df = load_state_total_tourist_arrivals_data()
        state_foreign_df = load_state_foreign_tourist_arrivals_data()
        state_domestic_df = load_state_domestic_tourist_arrivals_data()

        show_regional_tapestry(
            state_total_df,
            state_domestic_df,
            state_foreign_df,
        )

if __name__ == "__main__":
    main()
