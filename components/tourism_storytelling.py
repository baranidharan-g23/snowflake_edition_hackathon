import streamlit as st
import pandas as pd
from components.data_loader import (
    load_unesco_data, load_top_monuments_domestic_data, load_top_monuments_foreign_data,
    load_centrally_protected_domestic_data, load_centrally_protected_foreign_data,
    load_tourism_gdp_data, load_tourism_employment_data, load_fee_earnings_data,
    load_india_world_share_data, load_ita_data, load_ita_monthly_data,
    load_duration_stay_data, load_age_statistics_data, load_all_lean_peak_data,
    load_state_tourism_data, load_state_foreign_tourism_data, load_dance_data,
    load_festivals_data
)
from components.chapter1_heritage_heartbeat import show_heritage_heartbeat
from components.chapter2_economic_multiplier import show_economic_multiplier
from components.chapter3_travelers_journey import show_travelers_journey
from components.chapter4_regional_tapestry import show_regional_tapestry

def show_tourism_storytelling():
    """Main Tourism Storytelling Component - 4 Interactive Chapters"""

    # Main Header
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%); padding: 4rem 2rem; border-radius: 30px; margin: 2rem 0; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.15);">
        <h1 style="color: white; font-size: 3.5rem; margin-bottom: 1rem; text-shadow: 3px 3px 6px rgba(0,0,0,0.4); font-family: 'Georgia', serif;">
            📖 India's Tourism Story
        </h1>
        <p style="color: rgba(255,255,255,0.95); font-size: 1.4rem; margin: 1rem 0; line-height: 1.6; text-shadow: 1px 1px 3px rgba(0,0,0,0.3);">
            An Interactive Journey Through Heritage, Economics, Travelers & Regions
        </p>
        <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 15px; margin: 2rem auto; max-width: 600px; backdrop-filter: blur(10px);">
            <p style="color: white; margin: 0; font-size: 1.1rem; opacity: 0.9;">
                🏛️ Heritage • 💰 Economics • 🌍 Travelers • 🗺️ Regions
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Story Navigation
    st.markdown("""
    <div style="background: rgba(255,255,255,0.95); padding: 2rem; border-radius: 20px; margin: 2rem 0; box-shadow: 0 10px 25px rgba(0,0,0,0.1);">
        <h3 style="color: #333; text-align: center; margin-bottom: 1.5rem; font-family: 'Georgia', serif;">
            📚 Choose Your Chapter
        </h3>
        <p style="color: #666; text-align: center; line-height: 1.6; margin: 0;">
            Each chapter tells a unique story of India's tourism landscape. Navigate through heritage sites,
            economic impacts, traveler journeys, and regional diversity to discover the complete picture.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Chapter Selection
    chapter_options = [
        "🏛️ Chapter 1: The Heritage Heartbeat",
        "💰 Chapter 2: The Economic Multiplier Story",
        "🌍 Chapter 3: The Traveler's Journey",
        "🗺️ Chapter 4: The Regional Tapestry"
    ]

    selected_chapter = st.selectbox(
        "Select a chapter to explore:",
        chapter_options,
        index=0,
        help="Each chapter focuses on different aspects of India's tourism story"
    )

    # Load all required data
    with st.spinner("Loading tourism data..."):
        # Heritage data
        unesco_df = load_unesco_data()
        top_monuments_domestic_df = load_top_monuments_domestic_data()
        top_monuments_foreign_df = load_top_monuments_foreign_data()
        centrally_protected_domestic_df = load_centrally_protected_domestic_data()
        centrally_protected_foreign_df = load_centrally_protected_foreign_data()

        # Economic data
        tourism_gdp_df = load_tourism_gdp_data()
        tourism_employment_df = load_tourism_employment_data()
        fee_earnings_df = load_fee_earnings_data()
        india_world_share_df = load_india_world_share_data()

        # Traveler data
        ita_df = load_ita_data()
        ita_monthly_df = load_ita_monthly_data()
        stay_duration_df = load_duration_stay_data()
        age_statistics_df = load_age_statistics_data()
        all_lean_peak_data = load_all_lean_peak_data()

        # Regional data
        state_total_df = load_state_tourism_data()  # This loads total arrivals
        state_foreign_df = load_state_foreign_tourism_data()
        dance_df = load_dance_data()
        festivals_df = load_festivals_data()

        # Load domestic data separately
        try:
            state_domestic_df = pd.read_csv('Datasets/State_Wise_Domestic_Tourist_Arrivals_2017_2023.csv')
        except:
            state_domestic_df = pd.DataFrame()

    # Chapter Content
    if selected_chapter == "🏛️ Chapter 1: The Heritage Heartbeat":
        show_heritage_heartbeat(
            unesco_df,
            top_monuments_domestic_df,
            top_monuments_foreign_df,
            centrally_protected_domestic_df,
            centrally_protected_foreign_df
        )

    elif selected_chapter == "💰 Chapter 2: The Economic Multiplier Story":
        show_economic_multiplier(
            tourism_gdp_df,
            tourism_employment_df,
            fee_earnings_df,
            india_world_share_df
        )

    elif selected_chapter == "🌍 Chapter 3: The Traveler's Journey":
        show_travelers_journey(
            ita_df,
            ita_monthly_df,
            stay_duration_df,
            age_statistics_df,
            all_lean_peak_data
        )

    elif selected_chapter == "🗺️ Chapter 4: The Regional Tapestry":
        show_regional_tapestry(
            state_total_df,
            state_domestic_df,
            state_foreign_df,
            dance_df,
            festivals_df
        )

    # Chapter Navigation Footer
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 20px; margin: 3rem 0; text-align: center; color: white;">
        <h4 style="margin-bottom: 1rem; font-size: 1.5rem;">🔄 Continue Your Journey</h4>
        <p style="margin: 0; opacity: 0.9; line-height: 1.6;">
            Each chapter reveals different facets of India's incredible tourism story.
            Explore all four chapters to get the complete picture of how heritage, economics,
            travelers, and regions come together to create India's unique tourism landscape.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Data Summary Footer
    st.markdown("""
    <div style="background: rgba(102,126,234,0.05); padding: 2rem; border-radius: 15px; margin: 2rem 0; border-left: 5px solid #667eea;">
        <h5 style="color: #667eea; margin-bottom: 1rem;">📊 Complete Data Utilization</h5>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
            <div style="background: white; padding: 1rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <strong style="color: #8B4513;">Chapter 1:</strong><br>
                <small style="color: #666;">UNESCO Sites, Monuments, Heritage Data</small>
            </div>
            <div style="background: white; padding: 1rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <strong style="color: #2E8B57;">Chapter 2:</strong><br>
                <small style="color: #666;">GDP, Employment, Revenue, Global Rankings</small>
            </div>
            <div style="background: white; padding: 1rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <strong style="color: #4169E1;">Chapter 3:</strong><br>
                <small style="color: #666;">22-Year Data, Demographics, Seasonal Patterns</small>
            </div>
            <div style="background: white; padding: 1rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <strong style="color: #FF6347;">Chapter 4:</strong><br>
                <small style="color: #666;">State Data, 123 Dances, Festivals</small>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
