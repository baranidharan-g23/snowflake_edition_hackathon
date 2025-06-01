import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from PIL import Image
import os
from styles.css_styles import apply_heritage_chapter_background

def get_site_description(site):
    """Get site description handling different possible column names"""
    description = 'A magnificent UNESCO World Heritage Site showcasing India\'s rich cultural heritage.'
    for col in ['DESCRIPTION', 'Description', 'description', 'DETAILS', 'details', 'SUMMARY', 'summary']:
        if col in site.index and pd.notna(site.get(col)):
            description = site.get(col)
            break
    return description

def show_heritage_heartbeat(unesco_df, top_monuments_domestic_df, top_monuments_foreign_df,
                           centrally_protected_domestic_df, centrally_protected_foreign_df):
    """Chapter 1: The Heritage Heartbeat - Interactive UNESCO Sites and Monument Tourism Story"""

    # Apply heritage-specific background styling
    apply_heritage_chapter_background()

    # Enhanced Chapter Header with Dynamic Stats
    if not unesco_df.empty:
        total_unesco_sites = len(unesco_df)

        # Handle different possible column names for year
        year_column = None
        for col in ['Year', 'YEAR', 'year', 'INSCRIPTION_YEAR', 'inscription_year']:
            if col in unesco_df.columns:
                year_column = col
                break

        if year_column:
            latest_site_year = unesco_df[year_column].max()
            earliest_site_year = unesco_df[year_column].min()
            heritage_span = latest_site_year - earliest_site_year
        else:
            latest_site_year = 2024
            earliest_site_year = 1983
            heritage_span = 41
    else:
        total_unesco_sites = 43
        heritage_span = 41
        latest_site_year = 2024

    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #8B4513, #D2691E, #CD853F); padding: 3rem; border-radius: 25px; margin: 2rem 0; text-align: center; box-shadow: 0 15px 35px rgba(139,69,19,0.3); position: relative; overflow: hidden;">
        <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.3;"></div>
        <div style="position: relative; z-index: 1;">
            <h1 style="color: white; font-size: 3.5rem; margin-bottom: 1rem; text-shadow: 3px 3px 6px rgba(0,0,0,0.4); font-family: 'Georgia', serif; animation: fadeInUp 1s ease-out;">
                🏛️ Chapter 1: The Heritage Heartbeat
            </h1>
            <p style="color: rgba(255,255,255,0.95); font-size: 1.4rem; margin: 1rem 0; line-height: 1.6; text-shadow: 1px 1px 3px rgba(0,0,0,0.3);">
                Where Ancient Stones Tell Timeless Stories - India's UNESCO Legacy & Monument Magnificence
            </p>
            <div style="display: flex; justify-content: center; gap: 3rem; margin-top: 2rem; flex-wrap: wrap;">
                <div style="text-align: center;">
                    <div style="font-size: 2.5rem; font-weight: bold; color: #FFD700;">{total_unesco_sites}</div>
                    <div style="font-size: 1rem; color: rgba(255,255,255,0.9);">UNESCO Sites</div>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 2.5rem; font-weight: bold; color: #98FB98;">{heritage_span}+</div>
                    <div style="font-size: 1rem; color: rgba(255,255,255,0.9);">Years of Recognition</div>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 2.5rem; font-weight: bold; color: #FFE4B5;">5000+</div>
                    <div style="font-size: 1rem; color: rgba(255,255,255,0.9);">Years of Heritage</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Interactive Story Introduction
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(139,69,19,0.08), rgba(210,105,30,0.05)); padding: 2rem; border-radius: 20px; margin: 2rem 0; border-left: 6px solid #8B4513; position: relative;">
        <h3 style="color: #8B4513; margin-bottom: 1.5rem; font-family: 'Georgia', serif; font-size: 1.8rem;">📜 The Living Chronicle of India's Heritage</h3>
        <p style="color: #555; line-height: 1.8; font-size: 1.1rem; margin-bottom: 1.5rem;">
            From the <strong style="color: #8B4513;">majestic Ajanta Caves (1983)</strong> to the recent <strong style="color: #8B4513;">Moidams of Assam (2024)</strong>,
            India's UNESCO World Heritage Sites represent over <strong>4 decades of global recognition</strong>.
            Each monument tells a story spanning millennia - from ancient Buddhist art to Mughal grandeur,
            from colonial architecture to living traditions.
        </p>
        <div style="background: rgba(139,69,19,0.1); padding: 1.5rem; border-radius: 15px; margin-top: 1.5rem;">
            <p style="color: #8B4513; font-size: 1.2rem; font-weight: bold; margin: 0; text-align: center;">
                💰 Together, they create a <span style="color: #D2691E; font-size: 1.4rem;">₹1.92 economic multiplier</span> for every rupee invested in heritage tourism
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Interactive UNESCO Sites Showcase
    if not unesco_df.empty:
        # Create UNESCO sites with visitor data integration
        unesco_with_visitors = unesco_df.copy()

        # Map UNESCO sites to monument visitor data
        unesco_monument_mapping = {
            'Taj Mahal': 'Taj Mahal',
            'Agra Fort': 'Agra Fort',
            'Fatehpur Sikri': 'Fatehpur Sikri',
            'Red Fort Complex': 'Red Fort',
            'Qutb Minar and its Monuments': 'Qutub Minar',
            'Humayun\'s Tomb': 'Humayun Tomb',
            'Sun Temple': 'Sun Temple Konark',
            'Monuments at Mahabalipuram': 'Group of Monuments Mamallapuram',
            'Ellora Caves': 'Ellora Caves',
            'Ajanta Caves': 'Ajanta Caves'
        }

        # Determine the correct column names for UNESCO sites
        site_column = None
        for col in ['SITE', 'Site', 'site', 'NAME', 'name', 'SITE_NAME', 'site_name']:
            if col in unesco_with_visitors.columns:
                site_column = col
                break

        if not site_column:
            st.warning("Could not find site name column in UNESCO data. Expected columns: SITE, Site, site, NAME, name, SITE_NAME, site_name")
            return

        # Add visitor data to UNESCO sites
        if not top_monuments_domestic_df.empty:
            for unesco_site, monument_name in unesco_monument_mapping.items():
                domestic_match = top_monuments_domestic_df[
                    top_monuments_domestic_df['MONUMENT_NAME'] == monument_name
                ]
                if not domestic_match.empty:
                    unesco_with_visitors.loc[
                        unesco_with_visitors[site_column] == unesco_site, 'Domestic_Visitors_Millions'
                    ] = domestic_match['DOMESTIC_TOTAL_VISITS_MILLIONS'].iloc[0]

        if not top_monuments_foreign_df.empty:
            for unesco_site, monument_name in unesco_monument_mapping.items():
                foreign_match = top_monuments_foreign_df[
                    top_monuments_foreign_df['MONUMENT_NAME'] == monument_name
                ]
                if not foreign_match.empty:
                    unesco_with_visitors.loc[
                        unesco_with_visitors[site_column] == unesco_site, 'Foreign_Visitors_Lakhs'
                    ] = foreign_match['FOREIGN_TOTAL_VISITS_LAKHS'].iloc[0]

        # Fill NaN values from centrally protected monuments data
        if not centrally_protected_domestic_df.empty and not centrally_protected_foreign_df.empty:
            for idx, site in unesco_with_visitors.iterrows():
                site_name = site[site_column]

                # Check if domestic visitors is NaN and try to get from centrally protected data
                if pd.isna(site.get('Domestic_Visitors_Millions')):
                    monument_name = unesco_monument_mapping.get(site_name)
                    if monument_name:
                        # Look for the monument in centrally protected data
                        domestic_match = centrally_protected_domestic_df[
                            centrally_protected_domestic_df['MONUMENT'].str.contains(monument_name, case=False, na=False)
                        ]
                        if not domestic_match.empty:
                            # Use latest year data (2023-24) and convert to millions
                            latest_visits = domestic_match['YEAR_2023_24'].iloc[0]
                            if pd.notna(latest_visits):
                                unesco_with_visitors.loc[idx, 'Domestic_Visitors_Millions'] = latest_visits / 1000000

                # Check if foreign visitors is NaN and try to get from centrally protected data
                if pd.isna(site.get('Foreign_Visitors_Lakhs')):
                    monument_name = unesco_monument_mapping.get(site_name)
                    if monument_name:
                        # Look for the monument in centrally protected data
                        foreign_match = centrally_protected_foreign_df[
                            centrally_protected_foreign_df['MONUMENT'].str.contains(monument_name, case=False, na=False)
                        ]
                        if not foreign_match.empty:
                            # Use latest year data (2023-24) and convert to lakhs
                            latest_visits = foreign_match['YEAR_2023_24'].iloc[0]
                            if pd.notna(latest_visits):
                                unesco_with_visitors.loc[idx, 'Foreign_Visitors_Lakhs'] = latest_visits / 100000

        # Interactive UNESCO Site Cards
        st.markdown("""
        <div style="background: linear-gradient(135deg, #8B4513, #D2691E, #CD853F); padding: 1rem; border-radius: 25px; margin: 1rem 0; text-align: center; box-shadow: 0 15px 35px rgba(139,69,19,0.3); position: relative; overflow: hidden;">
            <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.3;"></div>
            <div style="position: relative; z-index: 1;">
                <h1 style="color: white; font-size: 1.6rem; margin-bottom: 1rem; text-shadow: 3px 3px 6px rgba(0,0,0,0.4); font-family: 'Georgia', serif;">
                    🏛️ Top UNESCO Sites by Visitor Rankings
                </h1>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Get top 6 UNESCO sites by visitor data
        unesco_with_visitors_sorted = unesco_with_visitors.copy()
        unesco_with_visitors_sorted['Total_Visitors'] = (
            unesco_with_visitors_sorted.get('Domestic_Visitors_Millions', 0) * 1000 +
            unesco_with_visitors_sorted.get('Foreign_Visitors_Lakhs', 0)
        )

        top_unesco_sites = unesco_with_visitors_sorted.nlargest(6, 'Total_Visitors') if 'Total_Visitors' in unesco_with_visitors_sorted.columns else unesco_with_visitors_sorted.head(6)

        # Display top 6 UNESCO sites in festival-style card format (3 columns, 2 rows)
        for row in range(2):
            cols = st.columns(3)
            for col_idx in range(3):
                site_idx = row * 3 + col_idx
                if site_idx < len(top_unesco_sites):
                    site = top_unesco_sites.iloc[site_idx]

                    with cols[col_idx]:
                        # Create festival-style card for UNESCO site
                        display_unesco_heritage_card(site)

    # Interactive Monument Comparison - Single Page Layout
    if not top_monuments_domestic_df.empty and not top_monuments_foreign_df.empty:

        # Monument Popularity Comparison
        st.markdown("""
        <div style="background: linear-gradient(135deg, #8B4513, #D2691E, #CD853F); padding: 1rem; border-radius: 25px; margin: 1rem 0; text-align: center; box-shadow: 0 15px 35px rgba(139,69,19,0.3); position: relative; overflow: hidden;">
            <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.3;"></div>
            <div style="position: relative; z-index: 1;">
                <h1 style="color: white; font-size: 1.6rem; text-shadow: 3px 3px 6px rgba(0,0,0,0.4); font-family: 'Georgia', serif;">
                    🏆 Monument Popularity: Domestic vs International
                </h1>
                <p style="color: rgba(255,255,255,0.95); font-size: 1.3rem; margin: 0; line-height: 1.6; text-shadow: 1px 1px 3px rgba(0,0,0,0.3);">
                    Interactive comparison of visitor preferences across India's heritage monuments
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Create interesting comparison visualizations
        col1, col2 = st.columns(2)

        with col1:
            # Domestic Visitors - Donut Chart
            fig_domestic = go.Figure(data=[go.Pie(
                labels=top_monuments_domestic_df['MONUMENT_NAME'][:8],
                values=top_monuments_domestic_df['DOMESTIC_TOTAL_VISITS_MILLIONS'][:8],
                hole=0.5,
                marker=dict(
                    colors=['#FF6B35', '#F7931E', '#FFD23F', '#06FFA5', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'],
                    line=dict(color='#FFFFFF', width=2)
                ),
                textinfo='label+percent',
                textfont=dict(size=10, color='black'),
                hovertemplate='<b>%{label}</b><br>Visitors: %{value:.1f}M<br>Share: %{percent}<extra></extra>'
            )])

            fig_domestic.update_layout(
                title=dict(
                    text="🇮🇳 Domestic Visitor Distribution",
                    font=dict(size=16, color='#8B4513', family="Georgia"),
                    x=0.5,
                    xanchor='center'
                ),
                font=dict(color='#333', size=10),
                height=400,
                showlegend=False,
                plot_bgcolor='rgba(139,69,19,0.1)',
                paper_bgcolor='rgba(139,69,19,0.1)',
                annotations=[dict(text='Domestic<br>Visitors', x=0.5, y=0.5, font_size=14, showarrow=False, font_color='#8B4513')]
            )

            st.plotly_chart(fig_domestic, use_container_width=True)

        with col2:
            # Foreign Visitors - Sunburst Chart
            foreign_col = 'FOREIGN_TOTAL_VISITS_LAKHS' if 'FOREIGN_TOTAL_VISITS_LAKHS' in top_monuments_foreign_df.columns else 'FOREIGN_TOTAL_VISITS_THOUSANDS'

            fig_foreign = go.Figure(data=[go.Pie(
                labels=top_monuments_foreign_df['MONUMENT_NAME'][:8],
                values=top_monuments_foreign_df[foreign_col][:8],
                hole=0.5,
                marker=dict(
                    colors=['#E17055', '#FDCB6E', '#6C5CE7', '#A29BFE', '#FD79A8', '#E84393', '#00B894', '#00CEC9'],
                    line=dict(color='#FFFFFF', width=2)
                ),
                textinfo='label+percent',
                textfont=dict(size=10, color='black'),
                hovertemplate='<b>%{label}</b><br>Visitors: %{value:.1f}L<br>Share: %{percent}<extra></extra>'
            )])

            fig_foreign.update_layout(
                title=dict(
                    text="🌍 International Visitor Distribution",
                    font=dict(size=16, color='#D2691E', family="Georgia"),
                    x=0.5,
                    xanchor='center'
                ),
                font=dict(color='#333', size=10),
                height=400,
                showlegend=False,
                plot_bgcolor='rgba(139,69,19,0.1)',
                paper_bgcolor='rgba(139,69,19,0.1)',
                annotations=[dict(text='International<br>Visitors', x=0.5, y=0.5, font_size=14, showarrow=False, font_color='#D2691E')]
            )

            st.plotly_chart(fig_foreign, use_container_width=True)

        # Add insights below the charts
        st.markdown("""
        <div style="background: rgba(139,69,19,0.1); padding: 1.5rem; border-radius: 15px; margin-top: 2rem;">
            <h4 style="color: #8B4513; margin-bottom: 1rem;">💡 Key Insights</h4>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem;">
                <div style="background: white; padding: 1rem; border-radius: 10px; border-left: 4px solid #8B4513;">
                    <h5 style="color: #8B4513; margin: 0 0 0.5rem 0;">🇮🇳 Domestic Preference</h5>
                    <p style="margin: 0; font-size: 0.9rem; color: #666;">Taj Mahal dominates with 20.1M visitors, followed by Sun Temple Konark and Red Fort</p>
                </div>
                <div style="background: white; padding: 1rem; border-radius: 10px; border-left: 4px solid #D2691E;">
                    <h5 style="color: #D2691E; margin: 0 0 0.5rem 0;">🌍 International Appeal</h5>
                    <p style="margin: 0; font-size: 0.9rem; color: #666;">Taj Mahal leads international visitors too, showing universal appeal across cultures</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)





    # Enhanced Heritage Impact Story
    st.markdown("""
    <div style="background: linear-gradient(135deg, #8B4513, #D2691E); padding: 3rem; border-radius: 25px; margin: 3rem 0; color: white; text-align: center; position: relative; overflow: hidden;">
        <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="heritage-impact" patternUnits="userSpaceOnUse" width="30" height="30"><circle cx="15" cy="15" r="2" fill="rgba(255,255,255,0.1)"/></pattern></defs><rect width="100" height="100" fill="url(%23heritage-impact)"/></svg"></div>
        <div style="position: relative; z-index: 1;">
            <h2 style="margin-bottom: 2rem; font-size: 2.2rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); font-family: 'Georgia', serif;">
                🌟 The Heritage Impact: Beyond Tourism
            </h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; margin: 2rem 0;">
                <div style="background: rgba(255,255,255,0.15); padding: 2rem; border-radius: 20px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);">
                    <h3 style="margin: 0 0 1rem 0; color: #FFD700; font-size: 1.5rem;">🏛️ Cultural Preservation</h3>
                    <p style="margin: 0; font-size: 1rem; opacity: 0.9; line-height: 1.5;">Safeguarding 5000+ years of heritage for future generations</p>
                </div>
                <div style="background: rgba(255,255,255,0.15); padding: 2rem; border-radius: 20px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);">
                    <h3 style="margin: 0 0 1rem 0; color: #98FB98; font-size: 1.5rem;">💼 Economic Engine</h3>
                    <p style="margin: 0; font-size: 1rem; opacity: 0.9; line-height: 1.5;">₹1.92 multiplier effect supporting millions of livelihoods</p>
                </div>
                <div style="background: rgba(255,255,255,0.15); padding: 2rem; border-radius: 20px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);">
                    <h3 style="margin: 0 0 1rem 0; color: #87CEEB; font-size: 1.5rem;">🎓 Living Classrooms</h3>
                    <p style="margin: 0; font-size: 1rem; opacity: 0.9; line-height: 1.5;">Educational experiences connecting past with present</p>
                </div>
            </div>
            <div style="background: rgba(255,255,255,0.1); padding: 2rem; border-radius: 20px; margin-top: 2rem;">
                <p style="margin: 0; font-size: 1.3rem; line-height: 1.6; opacity: 0.95; font-weight: 300;">
                    India's heritage sites are not just monuments; they are <strong>economic engines</strong>,
                    <strong>cultural ambassadors</strong>, and <strong>bridges between past and future</strong>,
                    contributing billions to the economy while preserving invaluable human legacy.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def display_unesco_heritage_card(site):
    """Display UNESCO heritage site in festival-style card format"""

    # Site information
    domestic_visitors = site.get('Domestic_Visitors_Millions', 'N/A')
    foreign_visitors = site.get('Foreign_Visitors_Lakhs', 'N/A')

    # Handle different possible column names for year
    year = 'N/A'
    for col in ['YEAR', 'Year', 'year', 'INSCRIPTION_YEAR', 'inscription_year']:
        if col in site.index and pd.notna(site.get(col)):
            year = site.get(col)
            break

    # Handle different possible column names for location
    location = 'N/A'
    for col in ['LOCATION', 'Location', 'location', 'STATE', 'State', 'state']:
        if col in site.index and pd.notna(site.get(col)):
            location = site.get(col)
            break

    # Handle different possible column names for site name
    site_name = 'Unknown Site'
    for col in ['SITE', 'Site', 'site', 'NAME', 'name', 'SITE_NAME', 'site_name']:
        if col in site.index and pd.notna(site.get(col)):
            site_name = site.get(col)
            break

    # Handle different possible column names for image
    image_filename = 'default.jpg'
    for col in ['DOWNLOADED_DANCE_IMAGES', 'IMAGE', 'image', 'IMAGE_FILE', 'image_file']:
        if col in site.index and pd.notna(site.get(col)):
            image_filename = site.get(col)
            break

    # Load UNESCO site image
    image_path = f"Images/unesco_india_images/{image_filename}"

    # Create the card with festival-style design
    st.markdown(f"""
    <div style="background: white; border-radius: 20px; overflow: hidden; box-shadow: 0 15px 35px rgba(0,0,0,0.15);
                margin-bottom: 2rem; border: 3px solid #4ECDC4; transition: transform 0.3s ease;">
        <div style="position: relative;">
    """, unsafe_allow_html=True)

    # Display image or fallback
    try:
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image, use_container_width=True)
        else:
            # Fallback with gradient background
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #8B4513, #D2691E); color: white; padding: 4rem 2rem; text-align: center; height: 200px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
                <div style="font-size: 3.5rem; margin-bottom: 0.5rem;">🏛️</div>
                <div style="font-size: 1rem; font-weight: bold; opacity: 0.9;">{site_name}</div>
            </div>
            """, unsafe_allow_html=True)
    except Exception:
        # Exception fallback
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #8B4513, #D2691E); color: white; padding: 4rem 2rem; text-align: center; height: 200px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
            <div style="font-size: 3.5rem; margin-bottom: 0.5rem;">🏛️</div>
            <div style="font-size: 1rem; font-weight: bold; opacity: 0.9;">{site_name}</div>
        </div>
        """, unsafe_allow_html=True)

    # Card content in festival style
    st.markdown(f"""
        </div>
        <div style="padding: 1rem;">
            <h2 style="color: #8B4513; font-family: 'Playfair Display', serif; font-size: 1.3rem;
                       margin-bottom: 0.5rem; font-weight: bold; text-align: center;">
                🏛️ {site_name}
            </h2>
            <div style="margin-bottom: 0.8rem;">
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.3rem;">
                    <span style="font-size: 1rem; width: 20px;">📍</span>
                    <span style="color: #D2691E; font-weight: bold; font-size: 0.9rem;">{location}</span>
                </div>
            </div>
            <div style="background: rgba(139,69,19,0.1); padding: 1rem; border-radius: 10px; margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between; text-align: center;">
                    <div>
                        <div style="font-size: 1.2rem; font-weight: bold; color: #8B4513;">{domestic_visitors if domestic_visitors != 'N/A' else '—'}</div>
                        <div style="font-size: 0.8rem; color: #666;">Domestic (M)</div>
                    </div>
                    <div>
                        <div style="font-size: 1.2rem; font-weight: bold; color: #D2691E;">{foreign_visitors if foreign_visitors != 'N/A' else '—'}</div>
                        <div style="font-size: 0.8rem; color: #666;">Foreign (L)</div>
                    </div>
                </div>
            </div>
            <div style="color: #333; line-height: 1.6; font-family: 'Poppins', sans-serif; font-size: 0.85rem;">
                {get_site_description(site)[:120]}...
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
