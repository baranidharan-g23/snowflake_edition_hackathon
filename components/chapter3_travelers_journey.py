import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def apply_chapter3_background():
    """Apply moderate purple/blue background styling for Chapter 3"""
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #d6ebff, #e8d5f2, #ddd6fe);
        background-attachment: fixed;
        min-height: 100vh;
    }

    .main .block-container {
        background: rgba(214, 235, 255, 0.85);
        border-radius: 18px;
        padding: 2rem;
        margin-top: 1rem;
        box-shadow: 0 6px 24px rgba(79, 70, 229, 0.3);
        border: 2px solid rgba(79, 70, 229, 0.3);
    }

    /* Enhance contrast for better visibility */
    .stMarkdown, .stText, .stSelectbox, .stMultiSelect {
        color: #374151 !important;
    }

    /* Card styling */
    div[data-testid="metric-container"] {
        background: rgba(255, 255, 255, 0.95);
        border: 2px solid rgba(79, 70, 229, 0.4);
        padding: 1.3rem;
        border-radius: 12px;
        box-shadow: 0 4px 16px rgba(79, 70, 229, 0.25);
    }

    /* Section backgrounds */
    .stContainer > div {
        background: rgba(214, 235, 255, 0.7);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(79, 70, 229, 0.3);
        box-shadow: 0 3px 12px rgba(79, 70, 229, 0.2);
    }

    /* Header styling - exclude chapter banner headers */
    h1:not(.chapter-banner-title), h2, h3 {
        color: #4338ca !important;
    }
    </style>
    """, unsafe_allow_html=True)

def show_travelers_journey(ita_df, ita_monthly_df, stay_duration_df, age_statistics_df, all_lean_peak_data):
    """Chapter 3: The Traveler's Journey - Visitor Patterns, Demographics, and Seasonal Trends"""

    # Apply chapter-specific background styling
    apply_chapter3_background()

    # Chapter Header
    st.markdown("""
    <div style="background: linear-gradient(135deg, #4169E1, #6495ED, #87CEEB); padding: 3rem; border-radius: 25px; margin: 2rem 0; text-align: center; box-shadow: 0 15px 35px rgba(65,105,225,0.3);">
        <h1 class="chapter-banner-title" style="color: white; font-size: 3rem; margin-bottom: 1rem; text-shadow: 3px 3px 6px rgba(0,0,0,0.4); font-family: 'Georgia', serif;">
            🌍 Chapter 3: The Traveler's Journey
        </h1>
        <p style="color: white; font-size: 1.3rem; margin: 0; line-height: 1.6; text-shadow: 1px 1px 3px rgba(0,0,0,0.3);">
            22 Years of Global Wanderers - From 2.5M to 18.9M Visitors
        </p>
    </div>
    """, unsafe_allow_html=True)

    # The 22-Year Journey Introduction
    st.markdown("""
    <div style="background: rgba(65,105,225,0.05); padding: 2.5rem; border-radius: 20px; margin: 2rem 0; border-left: 6px solid #4169E1;">
        <h3 style="color: #4169E1; margin-bottom: 1.5rem; font-family: 'Georgia', serif;">🎯 The Great Tourism Transformation (2001-2023)</h3>
        <p style="color: #555; line-height: 1.8; font-size: 1.1rem; margin: 0;">
            From <strong>2.5 million visitors in 2001</strong> to <strong>18.9 million in 2023</strong> - India's tourism story
            is one of remarkable growth, resilience, and global appeal. This 22-year journey reveals changing visitor demographics,
            evolving seasonal patterns, and the diverse tapestry of international travelers who choose India as their destination.
            Each visitor brings their own story, stay duration, and seasonal preferences, creating a rich mosaic of global tourism patterns.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 22-Year Timeline Analysis
    if not ita_df.empty:
        st.markdown("""
        <style>
        .custom-header-1 {
            color: #FFFFFF !important;
            font-size: 1.5rem !important;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.4) !important;
            font-family: 'Georgia', serif !important;
            font-weight: bold !important;
            display: block !important;
        }
        </style>
        <div style="background: linear-gradient(135deg, #4169E1, #6495ED, #87CEEB); padding: 2.5rem; border-radius: 25px; margin: 2rem 0; text-align: center; box-shadow: 0 15px 35px rgba(65,105,225,0.3); position: relative; overflow: hidden;">
            <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.3;"></div>
            <div style="position: relative; z-index: 1;">
                <div class="custom-header-1">
                    📈 The 22-Year Growth Saga: India's Tourism Evolution
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Key milestones
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            start_visitors = ita_df['INDIA_ARRIVALS_MILLION'].iloc[0]
            start_year = ita_df['YEAR'].iloc[0]
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #4169E1, #6495ED); padding: 1.5rem; border-radius: 12px; text-align: center; color: white; margin-bottom: 1rem;">
                <h3 style="margin: 0; font-size: 2rem;">{start_visitors:.1f}M</h3>
                <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.9;">Starting Point</p>
                <p style="margin: 0; font-size: 0.8rem; background: rgba(255,255,255,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; display: inline-block;">
                    {start_year}
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            peak_visitors = ita_df['INDIA_ARRIVALS_MILLION'].max()
            peak_year = ita_df.loc[ita_df['INDIA_ARRIVALS_MILLION'].idxmax(), 'YEAR']
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #6495ED, #87CEEB); padding: 1.5rem; border-radius: 12px; text-align: center; color: white; margin-bottom: 1rem;">
                <h3 style="margin: 0; font-size: 2rem;">{peak_visitors:.1f}M</h3>
                <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.9;">Historic Peak</p>
                <p style="margin: 0; font-size: 0.8rem; background: rgba(255,255,255,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; display: inline-block;">
                    {peak_year}
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            latest_visitors = ita_df['INDIA_ARRIVALS_MILLION'].iloc[-1]
            latest_year = ita_df['YEAR'].iloc[-1]
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #87CEEB, #B0E0E6); padding: 1.5rem; border-radius: 12px; text-align: center; color: #4169E1; margin-bottom: 1rem;">
                <h3 style="margin: 0; font-size: 2rem;">{latest_visitors:.1f}M</h3>
                <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.9;">Current Level</p>
                <p style="margin: 0; font-size: 0.8rem; background: rgba(65,105,225,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; display: inline-block;">
                    {latest_year}
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col4:
            growth_multiple = latest_visitors / start_visitors
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #B0E0E6, #F0F8FF); padding: 1.5rem; border-radius: 12px; text-align: center; color: #4169E1; margin-bottom: 1rem;">
                <h3 style="margin: 0; font-size: 2rem;">{growth_multiple:.1f}x</h3>
                <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.9;">Growth Multiple</p>
                <p style="margin: 0; font-size: 0.8rem; background: rgba(65,105,225,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; display: inline-block;">
                    22 Years
                </p>
            </div>
            """, unsafe_allow_html=True)

        # Main Timeline Chart
        fig = go.Figure()

        # Add main trend line
        fig.add_trace(go.Scatter(
            x=ita_df['YEAR'],
            y=ita_df['INDIA_ARRIVALS_MILLION'],
            mode='lines+markers',
            name='Tourist Arrivals',
            line=dict(color='#4169E1', width=4, shape='spline'),
            marker=dict(size=12, color='#4169E1', symbol='circle', line=dict(width=2, color='white')),
            fill='tonexty',
            fillcolor='rgba(65,105,225,0.1)',
            hovertemplate='<b>Year:</b> %{x}<br><b>Arrivals:</b> %{y:.1f}M visitors<extra></extra>'
        ))

        # Highlight COVID period
        fig.add_vrect(
            x0=2019.5, x1=2021.5,
            fillcolor="rgba(255, 99, 71, 0.15)",
            layer="below",
            line_width=0
        )

        # Add pandemic annotation separately
        fig.add_annotation(
            x=2020.5,
            y=max(ita_df['INDIA_ARRIVALS_MILLION']) * 0.8,
            text="🦠 Pandemic Impact",
            showarrow=False,
            font=dict(color="#333", size=12),
            bgcolor="rgba(255, 99, 71, 0.1)",
            bordercolor="rgba(255, 99, 71, 0.5)",
            borderwidth=1
        )

        # Add recovery annotation
        fig.add_annotation(
            x=2023,
            y=latest_visitors,
            text="🚀 Strong Recovery",
            showarrow=True,
            arrowhead=2,
            arrowcolor="#4169E1",
            bgcolor="rgba(65,105,225,0.1)",
            bordercolor="#4169E1",
            borderwidth=2,
            font=dict(color="#333", size=12)
        )

        fig.update_layout(
            title=dict(
                text="🌟 India's 22-Year Tourism Journey: From Millions to Global Destination",
                font=dict(size=18, color='#4169E1', family="Georgia"),
                x=0.5,
                xanchor='center'
            ),
            xaxis=dict(
                title=dict(text="Year", font=dict(color='#333')),
                tickfont=dict(color='#333')
            ),
            yaxis=dict(
                title=dict(text="Arrivals (Million)", font=dict(color='#333')),
                tickfont=dict(color='#333')
            ),
            plot_bgcolor='rgba(248,249,250,0.8)',
            paper_bgcolor='rgba(214,235,255,0.8)',
            font=dict(color='#333', size=12),
            height=550,
            showlegend=False
        )

        st.plotly_chart(fig, use_container_width=True)

    # Age Demographics Analysis
    if not age_statistics_df.empty:
        st.markdown("""
        <style>
        .custom-header-2 {
            color: #FFFFFF !important;
            font-size: 1.5rem !important;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.4) !important;
            font-family: 'Georgia', serif !important;
            font-weight: bold !important;
            display: block !important;
        }
        .custom-subtitle-2 {
            color: rgba(255,255,255,0.95) !important;
            font-size: 1.2rem !important;
            margin: 0 !important;
            line-height: 1.6 !important;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.3) !important;
            display: block !important;
        }
        </style>
        <div style="background: linear-gradient(135deg, #4169E1, #6495ED, #87CEEB); padding: 2.5rem; border-radius: 25px; margin: 2rem 0; text-align: center; box-shadow: 0 15px 35px rgba(65,105,225,0.3); position: relative; overflow: hidden;">
            <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.3;"></div>
            <div style="position: relative; z-index: 1;">
                <div class="custom-header-2">
                    👥 The Age of Wanderers: Who Visits India?
                </div>
                <div class="custom-subtitle-2">
                    Understanding the demographic profile of India's international visitors
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Latest year age distribution
        latest_age_data = age_statistics_df.iloc[-1]
        age_columns = ['AGE_0_14', 'AGE_15_24', 'AGE_25_34', 'AGE_35_44', 'AGE_45_54', 'AGE_55_64', 'AGE_65_ABOVE FLOAT']
        age_labels = ['0-14', '15-24', '25-34', '35-44', '45-54', '55-64', '65+']

        # Clean age data
        age_values = []
        for col in age_columns:
            if col in latest_age_data:
                age_values.append(latest_age_data[col])
            else:
                age_values.append(0)

        col1, col2 = st.columns(2)

        with col1:
            # Age Distribution Pie Chart
            fig = go.Figure(data=[go.Pie(
                labels=age_labels,
                values=age_values,
                hole=0.4,
                marker_colors=['#4169E1', '#6495ED', '#87CEEB', '#B0E0E6', '#ADD8E6', '#87CEFA', '#4682B4'],
                hovertemplate='<b>Age Group:</b> %{label}<br><b>Percentage:</b> %{value:.1f}%<extra></extra>'
            )])

            fig.update_layout(
                title=dict(
                    text=f"👥 Age Distribution of Visitors ({latest_age_data['YEAR']})",
                    font=dict(size=16, color='#4169E1'),
                    x=0.5
                ),
                font=dict(color='#333'),
                height=400,
                showlegend=True,
                legend=dict(font=dict(color='#333')),
                plot_bgcolor='rgba(248,249,250,0.8)',
                paper_bgcolor='rgba(248,249,250,0.8)'
            )

            st.plotly_chart(fig, use_container_width=True)

        with col2:
            # Age trend over time for key groups
            fig = go.Figure()

            # Focus on key age groups
            key_groups = ['AGE_25_34', 'AGE_35_44', 'AGE_45_54']
            key_labels = ['25-34 (Prime Travel)', '35-44 (Family Travel)', '45-54 (Mature Travel)']
            colors = ['#4169E1', '#6495ED', '#87CEEB']

            for i, (col, label, color) in enumerate(zip(key_groups, key_labels, colors)):
                if col in age_statistics_df.columns:
                    fig.add_trace(go.Scatter(
                        x=age_statistics_df['YEAR'],
                        y=age_statistics_df[col],
                        mode='lines+markers',
                        name=label,
                        line=dict(color=color, width=3),
                        marker=dict(size=8, color=color)
                    ))

            fig.update_layout(
                title=dict(
                    text="📊 Age Group Trends Over Time",
                    font=dict(size=16, color='#4169E1'),
                    x=0.5
                ),
                xaxis=dict(
                    title=dict(text="Year", font=dict(color='#333')),
                    tickfont=dict(color='#333')
                ),
                yaxis=dict(
                    title=dict(text="Percentage of Visitors", font=dict(color='#333')),
                    tickfont=dict(color='#333')
                ),
                plot_bgcolor='rgba(248,249,250,0.8)',
                paper_bgcolor='rgba(214,235,255,0.8)',
                font=dict(color='#333'),
                height=400,
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(color='#333'))
            )

            st.plotly_chart(fig, use_container_width=True)

    # Stay Duration Analysis
    if not stay_duration_df.empty:
        st.markdown("""
        <style>
        .custom-header-3 {
            color: #FFFFFF !important;
            font-size: 1.5rem !important;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.4) !important;
            font-family: 'Georgia', serif !important;
            font-weight: bold !important;
            display: block !important;
        }
        </style>
        <div style="background: linear-gradient(135deg, #4169E1, #6495ED, #87CEEB); padding: 2.5rem; border-radius: 25px; margin: 2rem 0; text-align: center; box-shadow: 0 15px 35px rgba(65,105,225,0.3); position: relative; overflow: hidden;">
            <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.3;"></div>
            <div style="position: relative; z-index: 1;">
                <div class="custom-header-3">
                    ⏰ How Long Do Visitors Stay? Global Patterns Revealed
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Top 15 countries by latest year stay duration
        latest_stay = stay_duration_df[['COUNTRY_OF_NATIONALITY', 'YEAR_2023']].copy()
        latest_stay = latest_stay.dropna().sort_values('YEAR_2023', ascending=False).head(15)

        col1, col2 = st.columns(2)

        with col1:
            # Top countries by stay duration - Horizontal Funnel Chart
            top_10_stay = latest_stay.head(10)

            fig = go.Figure()

            # Create funnel chart
            fig.add_trace(go.Funnel(
                y=top_10_stay['COUNTRY_OF_NATIONALITY'],
                x=top_10_stay['YEAR_2023'],
                textinfo="value+percent initial",
                textfont=dict(size=12, color='black'),
                marker=dict(
                    color=['#4169E1', '#6495ED', '#87CEEB', '#B0E0E6', '#ADD8E6', '#87CEFA', '#4682B4', '#5F9EA0', '#778899', '#708090'][:len(top_10_stay)],
                    line=dict(width=2, color='white')
                ),
                connector=dict(line=dict(color='rgba(100, 149, 237, 0.3)', dash='dot')),
                hovertemplate='<b>%{y}</b><br>Stay Duration: %{x:.1f} days<br>Relative: %{percentInitial}<extra></extra>'
            ))

            fig.update_layout(
                title=dict(
                    text="🌍 Top Countries by Stay Duration (2023)",
                    font=dict(size=16, color='#6495ED'),
                    x=0.5
                ),
                xaxis=dict(
                    title=dict(text="Stay Duration (Days)", font=dict(color='#333')),
                    tickfont=dict(color='#333')
                ),
                yaxis=dict(
                    title=dict(text="Countries", font=dict(color='#333')),
                    tickfont=dict(color='#333')
                ),
                plot_bgcolor='rgba(248,249,250,0.8)',
                paper_bgcolor='rgba(248,249,250,0.8)',
                font=dict(color='#333'),
                height=500,
                margin=dict(l=150, r=50)
            )

            st.plotly_chart(fig, use_container_width=True)

        with col2:
            # Regional stay duration analysis
            regional_mapping = {
                'WESTERN EUROPE': ['United Kingdom', 'Germany', 'France', 'Italy', 'Spain', 'Netherlands'],
                'NORTH AMERICA': ['United States Of America', 'Canada'],
                'SOUTH ASIA': ['Bangladesh', 'Sri Lanka', 'Nepal', 'Pakistan'],
                'EAST ASIA': ['China', 'Japan'],
                'SOUTHEAST ASIA': ['Malaysia', 'Singapore', 'Thailand']
            }

            regional_stays = {}
            for region, countries in regional_mapping.items():
                region_data = stay_duration_df[stay_duration_df['COUNTRY_OF_NATIONALITY'].isin(countries)]
                if not region_data.empty:
                    regional_stays[region] = region_data['YEAR_2023'].mean()

            if regional_stays:
                regions = list(regional_stays.keys())
                durations = list(regional_stays.values())

                # Create radar chart for regional patterns
                fig = go.Figure()

                fig.add_trace(go.Scatterpolar(
                    r=durations,
                    theta=regions,
                    fill='toself',
                    fillcolor='rgba(100, 149, 237, 0.3)',
                    line=dict(color='#6495ED', width=3),
                    marker=dict(size=10, color='#4169E1'),
                    text=[f"{x:.1f} days" for x in durations],
                    textposition='middle center',
                    hovertemplate='<b>%{theta}</b><br>Avg Stay: %{r:.1f} days<extra></extra>'
                ))

                fig.update_layout(
                    polar=dict(
                        radialaxis=dict(
                            visible=True,
                            range=[0, max(durations) * 1.2],
                            gridcolor='rgba(100, 149, 237, 0.3)',
                            tickfont=dict(size=10)
                        ),
                        angularaxis=dict(
                            tickfont=dict(size=11, color='#4169E1')
                        ),
                        bgcolor='rgba(248,249,250,0.8)'
                    ),
                    title=dict(
                        text="🗺️ Regional Stay Duration Patterns",
                        font=dict(size=16, color='#6495ED'),
                        x=0.5
                    ),
                    font=dict(color='#333'),
                    height=500,
                    showlegend=False,
                    paper_bgcolor='rgba(214,235,255,0.8)',
                    plot_bgcolor='rgba(248,249,250,0.8)'
                )

                st.plotly_chart(fig, use_container_width=True)

    # Seasonal Patterns from Lean/Peak Data
    if all_lean_peak_data and any(not df.empty for df in all_lean_peak_data.values()):
        st.markdown("""
        <style>
        .custom-header-4 {
            color: #FFFFFF !important;
            font-size: 1.5rem !important;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.4) !important;
            font-family: 'Georgia', serif !important;
            font-weight: bold !important;
            display: block !important;
        }
        .custom-subtitle-4 {
            color: rgba(255,255,255,0.95) !important;
            font-size: 1.2rem !important;
            margin: 0 !important;
            line-height: 1.6 !important;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.3) !important;
            display: block !important;
        }
        </style>
        <div style="background: linear-gradient(135deg, #4169E1, #6495ED, #87CEEB); padding: 2.5rem; border-radius: 25px; margin: 2rem 0; text-align: center; box-shadow: 0 15px 35px rgba(65,105,225,0.3); position: relative; overflow: hidden;">
            <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.3;"></div>
            <div style="position: relative; z-index: 1;">
                <div class="custom-header-4">
                    🌸 Seasonal Preferences: When Different Nations Visit India
                </div>
                <div class="custom-subtitle-4">
                    Exploring peak and lean months for different nationalities
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Use latest year data
        latest_lean_peak = all_lean_peak_data.get(2023)
        if latest_lean_peak is not None and not latest_lean_peak.empty:

            col1, col2 = st.columns(2)

            with col1:
                # Peak months analysis - Simple Bar Chart
                peak_months = latest_lean_peak['PEAK_MONTH'].value_counts().head(8)

                fig = go.Figure()

                fig.add_trace(go.Bar(
                    x=peak_months.index,
                    y=peak_months.values,
                    marker=dict(
                        color=['#4169E1', '#6495ED', '#87CEEB', '#B0E0E6', '#ADD8E6', '#87CEFA', '#4682B4', '#5F9EA0'][:len(peak_months)],
                        line=dict(color='white', width=2)
                    ),
                    text=peak_months.values,
                    textposition='outside',
                    textfont=dict(size=12, color='#4169E1'),
                    hovertemplate='<b>%{x}</b><br>Countries: %{y}<br>Most popular peak month<extra></extra>'
                ))

                fig.update_layout(
                    title=dict(
                        text="🌟 Most Popular Peak Travel Months",
                        font=dict(size=16, color='#4169E1'),
                        x=0.5
                    ),
                    xaxis=dict(
                        title=dict(text="Month", font=dict(size=12, color='#4169E1')),
                        tickfont=dict(size=11, color='#4169E1')
                    ),
                    yaxis=dict(
                        title=dict(text="Number of Countries", font=dict(size=12, color='#4169E1')),
                        tickfont=dict(size=11, color='#4169E1')
                    ),
                    font=dict(color='#333'),
                    height=400,
                    plot_bgcolor='rgba(248,249,250,0.8)',
                    paper_bgcolor='rgba(248,249,250,0.8)',
                    showlegend=False
                )

                st.plotly_chart(fig, use_container_width=True)

            with col2:
                # Lean months analysis - Horizontal Bar Chart
                lean_months = latest_lean_peak['LEAN_MONTH'].value_counts().head(8)

                fig = go.Figure()

                fig.add_trace(go.Bar(
                    x=lean_months.values,
                    y=lean_months.index,
                    orientation='h',
                    marker=dict(
                        color=['#87CEEB', '#B0E0E6', '#ADD8E6', '#87CEFA', '#4682B4', '#5F9EA0', '#6495ED', '#4169E1'][:len(lean_months)],
                        line=dict(color='white', width=2)
                    ),
                    text=lean_months.values,
                    textposition='outside',
                    textfont=dict(size=12, color='#4169E1'),
                    hovertemplate='<b>%{y}</b><br>Countries: %{x}<br>Most common lean month<extra></extra>'
                ))

                fig.update_layout(
                    title=dict(
                        text="🌙 Most Common Lean Travel Months",
                        font=dict(size=16, color='#87CEEB'),
                        x=0.5
                    ),
                    xaxis=dict(
                        title=dict(text="Number of Countries", font=dict(size=12, color='#4169E1')),
                        tickfont=dict(size=11, color='#4169E1')
                    ),
                    yaxis=dict(
                        title=dict(text="Month", font=dict(size=12, color='#4169E1')),
                        tickfont=dict(size=11, color='#4169E1')
                    ),
                    font=dict(color='#333'),
                    height=400,
                    plot_bgcolor='rgba(248,249,250,0.8)',
                    paper_bgcolor='rgba(248,249,250,0.8)',
                    showlegend=False
                )

                st.plotly_chart(fig, use_container_width=True)

    # Journey Summary
    st.markdown("""
    <style>
    .custom-summary-header {
        color: #FFFFFF !important;
        margin-bottom: 1.5rem !important;
        font-size: 1.8rem !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3) !important;
        font-weight: bold !important;
        display: block !important;
    }
    </style>
    <div style="background: linear-gradient(135deg, #4169E1, #6495ED); padding: 2.5rem; border-radius: 20px; margin: 3rem 0; color: white; text-align: center;">
        <div class="custom-summary-header">
            🎯 The Traveler's Journey: Key Insights
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; margin: 2rem 0;">
            <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h4 style="margin: 0 0 0.5rem 0; color: #FFD700;">📈 Growth Story</h4>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">7.6x growth in 22 years</p>
            </div>
            <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h4 style="margin: 0 0 0.5rem 0; color: #98FB98;">👥 Demographics</h4>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">25-44 age group dominates</p>
            </div>
            <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h4 style="margin: 0 0 0.5rem 0; color: #87CEEB;">⏰ Stay Patterns</h4>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">Diverse duration preferences</p>
            </div>
        </div>
        <p style="margin: 2rem 0 0 0; font-size: 1.1rem; line-height: 1.6; opacity: 0.9;">
            From young backpackers to mature travelers, from quick business trips to extended cultural journeys,
            India welcomes a <strong>diverse global community</strong> with varying preferences and patterns.
        </p>
    </div>
    """, unsafe_allow_html=True)
