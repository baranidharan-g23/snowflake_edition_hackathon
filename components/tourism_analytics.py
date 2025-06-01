import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def show_tourism_analytics(ita_df, ita_monthly_df, state_tourism_df, centrally_protected_df,
                          duration_stay_df, fee_earnings_df, india_world_share_df,
                          lean_peak_df, monthly_foreigners_df, state_footfall_df,
                          top_monuments_df, age_statistics_df, tourism_gdp_df=None, tourism_employment_df=None):
    """Display comprehensive tourism analytics"""
    st.markdown('<h1 class="main-header">📊 Tourism Analytics</h1>', unsafe_allow_html=True)

    # Create tabs for different analytics sections
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📈 ITA Trends",
        "📅 Seasonal Patterns",
        "🗺️ State Analysis",
        "🏛️ Heritage Analytics",
        "💰 Economic Impact",
        "👥 Demographics"
    ])

    with tab1:
        show_ita_trends(ita_df)

    with tab2:
        show_seasonal_patterns(ita_monthly_df, lean_peak_df, monthly_foreigners_df)

    with tab3:
        show_state_analysis(state_tourism_df, state_footfall_df)

    with tab4:
        show_heritage_analytics(centrally_protected_df, top_monuments_df)

    with tab5:
        show_economic_impact(fee_earnings_df, india_world_share_df, tourism_gdp_df, tourism_employment_df)

    with tab6:
        show_visitor_demographics(age_statistics_df, duration_stay_df)

def show_ita_trends(ita_df):
    """Display International Tourist Arrivals trends with improved colors and styling"""
    st.markdown('<h2 class="section-header">🌍 India\'s Global Tourism Journey</h2>', unsafe_allow_html=True)

    if ita_df.empty:
        st.warning("No ITA data available")
        return

    # Engaging introduction with storytelling
    st.markdown("""
    <div style="background: linear-gradient(135deg, #008080, #20B2AA); padding: 2.5rem; border-radius: 20px; margin: 2rem 0; box-shadow: 0 10px 30px rgba(0,128,128,0.2);">
        <h3 style="color: white; text-align: center; margin-bottom: 1rem; font-size: 1.8rem;">✨ Incredible India's Tourism Story</h3>
        <p style="color: rgba(255,255,255,0.9); text-align: center; font-size: 1.1rem; margin: 0; line-height: 1.6;">
            From ancient heritage to modern marvels, discover how millions of travelers from around the world
            have been captivated by India's timeless charm and diverse cultural tapestry.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Enhanced metrics with storytelling approach
    st.markdown("""
    <div style="background: rgba(255,255,255,0.95); padding: 1.5rem; border-radius: 15px; margin: 2rem 0; box-shadow: 0 5px 20px rgba(0,0,0,0.1);">
        <h4 style="color: #008080; text-align: center; margin-bottom: 1.5rem;">📊 Tourism Milestones & Achievements</h4>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    latest_arrivals = ita_df['INDIA_ARRIVALS_MILLION'].iloc[-1]
    previous_arrivals = ita_df['INDIA_ARRIVALS_MILLION'].iloc[-2] if len(ita_df) > 1 else latest_arrivals
    growth_rate = ((latest_arrivals - previous_arrivals) / previous_arrivals) * 100

    peak_year = ita_df.loc[ita_df['INDIA_ARRIVALS_MILLION'].idxmax(), 'YEAR']
    peak_arrivals = ita_df['INDIA_ARRIVALS_MILLION'].max()

    with col1:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #FF6B6B, #FF8E8E); padding: 1.5rem; border-radius: 12px; text-align: center; color: white; margin-bottom: 1rem;">
            <h3 style="margin: 0; font-size: 2rem;">{latest_arrivals:.1f}M</h3>
            <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.9;">Global Visitors (2023)</p>
            <p style="margin: 0; font-size: 0.8rem; background: rgba(255,255,255,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; display: inline-block;">
                {growth_rate:+.1f}% growth
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #4ECDC4, #6ED3D0); padding: 1.5rem; border-radius: 12px; text-align: center; color: white; margin-bottom: 1rem;">
            <h3 style="margin: 0; font-size: 2rem;">{peak_year}</h3>
            <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.9;">Golden Year</p>
            <p style="margin: 0; font-size: 0.8rem; background: rgba(255,255,255,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; display: inline-block;">
                {peak_arrivals:.1f}M peak arrivals
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        avg_growth = ita_df['INDIA_ARRIVALS_MILLION'].pct_change().mean() * 100
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #45B7D1, #6BC5E8); padding: 1.5rem; border-radius: 12px; text-align: center; color: white; margin-bottom: 1rem;">
            <h3 style="margin: 0; font-size: 2rem;">{avg_growth:.1f}%</h3>
            <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.9;">Historic Growth</p>
            <p style="margin: 0; font-size: 0.8rem; background: rgba(255,255,255,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; display: inline-block;">
                Annual average
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        covid_impact = ((ita_df[ita_df['YEAR'] == 2020]['INDIA_ARRIVALS_MILLION'].iloc[0] -
                        ita_df[ita_df['YEAR'] == 2019]['INDIA_ARRIVALS_MILLION'].iloc[0]) /
                       ita_df[ita_df['YEAR'] == 2019]['INDIA_ARRIVALS_MILLION'].iloc[0]) * 100
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #96CEB4, #A8D5C4); padding: 1.5rem; border-radius: 12px; text-align: center; color: white; margin-bottom: 1rem;">
            <h3 style="margin: 0; font-size: 2rem;">{covid_impact:.1f}%</h3>
            <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.9;">Resilience Test</p>
            <p style="margin: 0; font-size: 0.8rem; background: rgba(255,255,255,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; display: inline-block;">
                2020 impact
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Add narrative section before the main chart
    st.markdown("""
    <div style="background: rgba(0,128,128,0.05); padding: 2rem; border-radius: 15px; margin: 2rem 0; border-left: 5px solid #008080;">
        <h4 style="color: #008080; margin-bottom: 1rem;">🎯 The Tourism Evolution Story</h4>
        <p style="color: #555; line-height: 1.7; margin: 0;">
            Witness India's remarkable journey from <strong>2.6 million visitors in 2001</strong> to becoming a global tourism powerhouse.
            Despite facing unprecedented challenges during the pandemic, India's tourism sector demonstrates extraordinary resilience,
            bouncing back with renewed vigor and innovative approaches to welcome the world.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Enhanced Main trend chart with better colors and styling
    fig = go.Figure()

    # Add gradient fill area
    fig.add_trace(go.Scatter(
        x=ita_df['YEAR'],
        y=ita_df['INDIA_ARRIVALS_MILLION'],
        mode='lines+markers',
        name='Tourist Arrivals',
        line=dict(color='#008080', width=4, shape='spline'),
        marker=dict(size=10, color='#008080', symbol='circle',
                   line=dict(width=2, color='white')),
        fill='tonexty',
        fillcolor='rgba(0,128,128,0.1)',
        hovertemplate='<b>Year:</b> %{x}<br><b>Arrivals:</b> %{y:.1f}M visitors<br><i>Click to explore this year\'s story</i><extra></extra>'
    ))

    # Highlight COVID period with better styling
    fig.add_vrect(
        x0=2019.5, x1=2021.5,
        fillcolor="rgba(255, 99, 71, 0.15)",
        layer="below",
        line_width=0,
        annotation_text="🦠 Global Challenge",
        annotation_position="top left",
        annotation=dict(
            font=dict(color="#FF6347", size=12, family="Arial Black"),
            bgcolor="rgba(255,255,255,0.9)",
            bordercolor="#FF6347",
            borderwidth=2,
            borderpad=4
        )
    )

    # Add recovery annotation with more engaging text
    recovery_year = 2023
    recovery_value = ita_df[ita_df['YEAR'] == recovery_year]['INDIA_ARRIVALS_MILLION'].iloc[0]
    fig.add_annotation(
        x=recovery_year,
        y=recovery_value,
        text="🚀 Rising Again!",
        showarrow=True,
        arrowhead=2,
        arrowcolor="#008080",
        bgcolor="rgba(0,128,128,0.1)",
        bordercolor="#008080",
        borderwidth=2,
        font=dict(color="#008080", size=12, family="Arial Black")
    )

    # Add milestone annotations for peak years
    peak_year = ita_df.loc[ita_df['INDIA_ARRIVALS_MILLION'].idxmax(), 'YEAR']
    peak_value = ita_df['INDIA_ARRIVALS_MILLION'].max()
    fig.add_annotation(
        x=peak_year,
        y=peak_value,
        text="🏆 Historic Peak",
        showarrow=True,
        arrowhead=2,
        arrowcolor="#FFD700",
        bgcolor="rgba(255,215,0,0.1)",
        bordercolor="#FFD700",
        borderwidth=2,
        font=dict(color="#FFD700", size=12, family="Arial Black")
    )

    fig.update_layout(
        title=dict(
            text="🌟 Two Decades of India's Tourism Magnetism: A Journey of Growth, Resilience & Revival",
            font=dict(size=18, color='#008080', family="Georgia"),
            x=0.5
        ),
        xaxis_title="Year",
        yaxis_title="Arrivals (Million)",
        plot_bgcolor='rgba(248,249,250,0.8)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#333', size=12),
        height=550,
        showlegend=False,
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(128,128,128,0.2)',
            showline=True,
            linewidth=2,
            linecolor='#008080'
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(128,128,128,0.2)',
            showline=True,
            linewidth=2,
            linecolor='#008080'
        )
    )

    st.plotly_chart(fig, use_container_width=True)

    # Add insights section after main chart
    st.markdown("""
    <div style="background: rgba(255,248,220,0.8); padding: 2rem; border-radius: 15px; margin: 2rem 0; border-left: 5px solid #FFD700;">
        <h4 style="color: #B8860B; margin-bottom: 1rem;">💡 Key Tourism Insights</h4>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
            <div style="background: white; padding: 1rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                <h5 style="color: #008080; margin: 0 0 0.5rem 0;">🎯 Growth Trajectory</h5>
                <p style="margin: 0; color: #666; font-size: 0.9rem;">Steady upward trend from 2001-2019, showcasing India's growing appeal as a global destination</p>
            </div>
            <div style="background: white; padding: 1rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                <h5 style="color: #FF6347; margin: 0 0 0.5rem 0;">🛡️ Pandemic Resilience</h5>
                <p style="margin: 0; color: #666; font-size: 0.9rem;">Quick adaptation with digital initiatives and safety protocols during challenging times</p>
            </div>
            <div style="background: white; padding: 1rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                <h5 style="color: #32CD32; margin: 0 0 0.5rem 0;">🚀 Recovery Momentum</h5>
                <p style="margin: 0; color: #666; font-size: 0.9rem;">Strong comeback in 2023 with innovative tourism campaigns and infrastructure development</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Enhanced Growth analysis with better colors and storytelling
    st.markdown("""
    <div style="background: rgba(0,128,128,0.05); padding: 1.5rem; border-radius: 15px; margin: 2rem 0;">
        <h4 style="color: #008080; text-align: center; margin-bottom: 1rem;">📈 Decoding India's Tourism Growth Patterns</h4>
        <p style="color: #555; text-align: center; margin: 0;">Explore the year-over-year dynamics and decade-wise evolution that shaped India's tourism landscape</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        # Year-over-year growth with improved colors
        ita_df_growth = ita_df.copy()
        ita_df_growth['Growth Rate'] = ita_df_growth['INDIA_ARRIVALS_MILLION'].pct_change() * 100

        # Create custom colors based on growth rate
        colors = ['#FF4444' if x < 0 else '#FFA500' if x < 5 else '#32CD32' for x in ita_df_growth['Growth Rate'].fillna(0)]

        fig = go.Figure(data=[
            go.Bar(
                x=ita_df_growth['YEAR'][1:],
                y=ita_df_growth['Growth Rate'][1:],
                marker_color=colors[1:],
                text=[f"{x:.1f}%" for x in ita_df_growth['Growth Rate'][1:]],
                textposition='outside',
                hovertemplate='<b>Year:</b> %{x}<br><b>Growth:</b> %{y:.1f}%<extra></extra>'
            )
        ])

        fig.update_layout(
            title=dict(
                text="🎢 The Tourism Roller Coaster: Annual Growth Dynamics",
                font=dict(size=16, color='#008080', family="Georgia"),
                x=0.5
            ),
            xaxis_title="Year",
            yaxis_title="Growth Rate (%)",
            plot_bgcolor='rgba(248,249,250,0.8)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#333'),
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Decade comparison with gradient colors
        decades = {
            '2001-2010': ita_df[(ita_df['YEAR'] >= 2001) & (ita_df['YEAR'] <= 2010)]['INDIA_ARRIVALS_MILLION'].mean(),
            '2011-2020': ita_df[(ita_df['YEAR'] >= 2011) & (ita_df['YEAR'] <= 2020)]['INDIA_ARRIVALS_MILLION'].mean(),
            '2021-2023': ita_df[(ita_df['YEAR'] >= 2021) & (ita_df['YEAR'] <= 2023)]['INDIA_ARRIVALS_MILLION'].mean()
        }

        decade_df = pd.DataFrame(list(decades.items()), columns=['Decade', 'Avg Arrivals'])

        fig = go.Figure(data=[
            go.Bar(
                x=decade_df['Decade'],
                y=decade_df['Avg Arrivals'],
                marker_color=['#008080', '#20B2AA', '#40E0D0'],
                text=[f"{x:.1f}M" for x in decade_df['Avg Arrivals']],
                textposition='outside',
                hovertemplate='<b>Decade:</b> %{x}<br><b>Avg Arrivals:</b> %{y:.1f}M<extra></extra>'
            )
        ])

        fig.update_layout(
            title=dict(
                text="🏛️ Decades of Discovery: India's Tourism Evolution",
                font=dict(size=16, color='#008080', family="Georgia"),
                x=0.5
            ),
            xaxis_title="Decade",
            yaxis_title="Average Arrivals (Million)",
            plot_bgcolor='rgba(248,249,250,0.8)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#333'),
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    # Add future outlook section
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2.5rem; border-radius: 20px; margin: 3rem 0; color: white; text-align: center;">
        <h3 style="margin-bottom: 1.5rem; font-size: 1.8rem;">🔮 The Future Beckons: India's Tourism Vision 2030</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; margin: 2rem 0;">
            <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h4 style="margin: 0 0 0.5rem 0; color: #FFD700;">🎯 Target</h4>
                <p style="margin: 0; font-size: 1.2rem; font-weight: bold;">20M Visitors</p>
                <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; opacity: 0.8;">By 2030</p>
            </div>
            <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h4 style="margin: 0 0 0.5rem 0; color: #98FB98;">💰 Revenue</h4>
                <p style="margin: 0; font-size: 1.2rem; font-weight: bold;">$100B Goal</p>
                <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; opacity: 0.8;">Economic Impact</p>
            </div>
            <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h4 style="margin: 0 0 0.5rem 0; color: #87CEEB;">🌱 Sustainability</h4>
                <p style="margin: 0; font-size: 1.2rem; font-weight: bold;">Green Tourism</p>
                <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; opacity: 0.8;">Eco-Friendly Focus</p>
            </div>
        </div>
        <p style="margin: 2rem 0 0 0; font-size: 1.1rem; line-height: 1.6; opacity: 0.9;">
            With digital transformation, sustainable practices, and world-class infrastructure,
            India is poised to become the world's most sought-after tourism destination.
        </p>
    </div>
    """, unsafe_allow_html=True)

def show_seasonal_patterns(ita_monthly_df, lean_peak_df, monthly_foreigners_df):
    """Display seasonal tourism patterns with enhanced storytelling"""
    st.markdown('<h2 class="section-header">🌺 India\'s Seasonal Tourism Symphony</h2>', unsafe_allow_html=True)

    if ita_monthly_df.empty:
        st.warning("No monthly data available")
        return

    # Engaging introduction with seasonal storytelling
    st.markdown("""
    <div style="background: linear-gradient(135deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4); padding: 2.5rem; border-radius: 20px; margin: 2rem 0; box-shadow: 0 10px 30px rgba(0,0,0,0.15);">
        <h3 style="color: white; text-align: center; margin-bottom: 1rem; font-size: 1.8rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">🎭 The Rhythm of India's Tourism Seasons</h3>
        <p style="color: rgba(255,255,255,0.95); text-align: center; font-size: 1.1rem; margin: 0; line-height: 1.6; text-shadow: 1px 1px 2px rgba(0,0,0,0.2);">
            From the vibrant festivals of autumn to the serene monsoons, discover how India's diverse seasons
            create a year-round tapestry of experiences that captivate millions of travelers worldwide.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Clean and prepare data
    monthly_df = ita_monthly_df.copy()

    # Convert string numbers to numeric (remove commas)
    for col in ['YEAR_2021', 'YEAR_2022', 'YEAR_2023']:
        if col in monthly_df.columns:
            monthly_df[col] = monthly_df[col].astype(str).str.replace(',', '').astype(float)

    # Add seasonal context section
    st.markdown("""
    <div style="background: rgba(255,182,193,0.1); padding: 2rem; border-radius: 15px; margin: 2rem 0; border-left: 5px solid #FF69B4;">
        <h4 style="color: #C71585; margin-bottom: 1rem;">🌸 Understanding India's Tourism Calendar</h4>
        <p style="color: #555; line-height: 1.7; margin: 0;">
            Each month in India tells a unique story - from the <strong>festive fervor of October-November</strong> during Diwali and Durga Puja,
            to the <strong>pleasant winter months</strong> perfect for heritage exploration, and the <strong>monsoon magic</strong> that transforms
            the landscape into a lush paradise. Let's explore how these natural rhythms shape visitor preferences.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Enhanced Monthly trends with better styling
    fig = go.Figure()

    # Enhanced color palette for seasonal representation
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']  # Warm to cool representing seasonal transition
    year_names = ['2021 - Recovery', '2022 - Rebuilding', '2023 - Revival']
    years = ['YEAR_2021', 'YEAR_2022', 'YEAR_2023']

    for i, year in enumerate(years):
        if year in monthly_df.columns:
            fig.add_trace(go.Scatter(
                x=monthly_df['MONTH'],
                y=monthly_df[year],
                mode='lines+markers',
                name=year_names[i],
                line=dict(color=colors[i], width=4, shape='spline'),
                marker=dict(size=12, color=colors[i], symbol='circle',
                           line=dict(width=3, color='white')),
                fill='tonexty' if i == 0 else None,
                fillcolor=f'rgba({int(colors[i][1:3], 16) if colors[i].startswith("#") else 255},{int(colors[i][3:5], 16) if colors[i].startswith("#") else 107},{int(colors[i][5:7], 16) if colors[i].startswith("#") else 107},0.1)' if i == 0 else None,
                hovertemplate=f'<b>Month:</b> %{{x}}<br><b>{year.replace("YEAR_", "")} Arrivals:</b> %{{y:,.0f}} travelers<br><i>Discover this month\'s highlights</i><extra></extra>'
            ))

    # Add seasonal annotations
    fig.add_annotation(x="October", y=monthly_df[monthly_df['MONTH'] == 'October']['YEAR_2023'].iloc[0] if 'October' in monthly_df['MONTH'].values else 0,
                      text="🎆 Festival Season Peak", showarrow=True, arrowhead=2, arrowcolor="#FFD700",
                      bgcolor="rgba(255,215,0,0.1)", bordercolor="#FFD700", borderwidth=2,
                      font=dict(color="#B8860B", size=11, family="Arial Black"))

    fig.add_annotation(x="December", y=monthly_df[monthly_df['MONTH'] == 'December']['YEAR_2023'].iloc[0] if 'December' in monthly_df['MONTH'].values else 0,
                      text="❄️ Winter Wonderland", showarrow=True, arrowhead=2, arrowcolor="#87CEEB",
                      bgcolor="rgba(135,206,235,0.1)", bordercolor="#87CEEB", borderwidth=2,
                      font=dict(color="#4682B4", size=11, family="Arial Black"))

    fig.update_layout(
        title=dict(
            text="🌈 The Seasonal Dance: Monthly Tourism Rhythms Across Recovery Years",
            font=dict(size=18, color='#FF6B6B', family="Georgia"),
            x=0.5
        ),
        xaxis_title="Month",
        yaxis_title="Tourist Arrivals",
        plot_bgcolor='rgba(248,249,250,0.8)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#333', size=12),
        height=550,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(128,128,128,0.2)',
            tickangle=45
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(128,128,128,0.2)'
        )
    )

    st.plotly_chart(fig, use_container_width=True)

    # Add seasonal insights section
    st.markdown("""
    <div style="background: rgba(255,248,220,0.8); padding: 2rem; border-radius: 15px; margin: 2rem 0; border-left: 5px solid #FFD700;">
        <h4 style="color: #B8860B; margin-bottom: 1rem;">🌟 Seasonal Tourism Insights</h4>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
            <div style="background: white; padding: 1rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                <h5 style="color: #FF6B6B; margin: 0 0 0.5rem 0;">🌸 Spring Magic</h5>
                <p style="margin: 0; color: #666; font-size: 0.9rem;">March-May brings pleasant weather and colorful festivals, perfect for cultural exploration</p>
            </div>
            <div style="background: white; padding: 1rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                <h5 style="color: #4ECDC4; margin: 0 0 0.5rem 0;">🌧️ Monsoon Mystique</h5>
                <p style="margin: 0; color: #666; font-size: 0.9rem;">June-September transforms India into a lush paradise, ideal for hill stations and nature lovers</p>
            </div>
            <div style="background: white; padding: 1rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                <h5 style="color: #45B7D1; margin: 0 0 0.5rem 0;">❄️ Winter Bliss</h5>
                <p style="margin: 0; color: #666; font-size: 0.9rem;">October-February offers perfect weather for heritage sites and outdoor adventures</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Enhanced seasonal analysis with storytelling
    st.markdown("""
    <div style="background: rgba(255,182,193,0.05); padding: 1.5rem; border-radius: 15px; margin: 2rem 0;">
        <h4 style="color: #C71585; text-align: center; margin-bottom: 1rem;">📊 Decoding India's Tourism Seasons</h4>
        <p style="color: #555; text-align: center; margin: 0;">Discover the peak months and growth patterns that define India's tourism calendar</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        # Enhanced peak months analysis
        if 'YEAR_2023' in monthly_df.columns:
            peak_months = monthly_df.nlargest(3, 'YEAR_2023')[['MONTH', 'YEAR_2023']]

            st.markdown("""
            <div style="background: linear-gradient(135deg, #FF6B6B, #FF8E8E); padding: 1.5rem; border-radius: 15px; margin-bottom: 1rem;">
                <h4 style="color: white; margin: 0 0 1rem 0; text-align: center;">🏆 Tourism Champions of 2023</h4>
            </div>
            """, unsafe_allow_html=True)

            for idx, row in peak_months.iterrows():
                rank_emoji = ["🥇", "🥈", "🥉"][list(peak_months.index).index(idx)]
                st.markdown(f"""
                <div style="background: rgba(255,107,107,0.1); padding: 1rem; border-radius: 10px; margin: 0.5rem 0; border-left: 4px solid #FF6B6B;">
                    <strong>{rank_emoji} {row['MONTH']}</strong><br>
                    <span style="color: #FF6B6B; font-size: 1.1rem;">🎯 {row['YEAR_2023']:,.0f} travelers</span>
                </div>
                """, unsafe_allow_html=True)

    with col2:
        # Enhanced Growth rates with storytelling
        if 'GROWTH_2023_22_PERCENT' in monthly_df.columns:
            growth_data = monthly_df[['MONTH', 'GROWTH_2023_22_PERCENT']].copy()
            growth_data = growth_data.dropna()

            st.markdown("""
            <div style="background: linear-gradient(135deg, #4ECDC4, #6ED3D0); padding: 1.5rem; border-radius: 15px; margin-bottom: 1rem;">
                <h4 style="color: white; margin: 0 0 1rem 0; text-align: center;">📈 Recovery Momentum Tracker</h4>
            </div>
            """, unsafe_allow_html=True)

            # Create enhanced colors based on growth rate with more nuanced categories
            colors = []
            for x in growth_data['GROWTH_2023_22_PERCENT']:
                if x < -20:
                    colors.append('#FF4444')  # Deep red for significant decline
                elif x < 0:
                    colors.append('#FF8C69')  # Light red for decline
                elif x < 20:
                    colors.append('#FFA500')  # Orange for modest growth
                elif x < 50:
                    colors.append('#32CD32')  # Green for good growth
                else:
                    colors.append('#228B22')  # Dark green for excellent growth

            fig = go.Figure(data=[
                go.Bar(
                    x=growth_data['MONTH'],
                    y=growth_data['GROWTH_2023_22_PERCENT'],
                    marker_color=colors,
                    text=[f"{x:+.1f}%" for x in growth_data['GROWTH_2023_22_PERCENT']],
                    textposition='outside',
                    hovertemplate='<b>Month:</b> %{x}<br><b>Growth:</b> %{y:+.1f}%<br><i>Recovery strength indicator</i><extra></extra>'
                )
            ])

            fig.update_layout(
                title=dict(
                    text="🚀 The Great Comeback: Monthly Recovery Patterns",
                    font=dict(size=16, color='#4ECDC4', family="Georgia"),
                    x=0.5
                ),
                xaxis_title="Month",
                yaxis_title="Growth Rate (%)",
                plot_bgcolor='rgba(248,249,250,0.8)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#333'),
                height=400,
                showlegend=False,
                xaxis_tickangle=45
            )
            st.plotly_chart(fig, use_container_width=True)

    # Enhanced seasonal recommendations with immersive storytelling
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2.5rem; border-radius: 20px; margin: 3rem 0; color: white; text-align: center;">
        <h3 style="margin-bottom: 1.5rem; font-size: 1.8rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">🎭 India's Seasonal Travel Symphony</h3>
        <p style="margin: 0; font-size: 1.1rem; line-height: 1.6; opacity: 0.9;">
            Each season in India offers a unique palette of experiences, from vibrant festivals to serene landscapes.
            Discover the perfect time to immerse yourself in India's incredible diversity.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Create immersive seasonal cards
    seasonal_experiences = {
        "🌸 Spring Awakening": {
            "months": "March - May",
            "temperature": "20°C - 30°C",
            "description": "Nature's grand celebration begins as India awakens from winter's embrace",
            "experiences": [
                "🎨 Holi - The Festival of Colors transforms cities into vibrant canvases",
                "🌺 Blooming gardens in Kashmir and hill stations create picture-perfect moments",
                "🏛️ Perfect weather for exploring ancient temples and heritage sites",
                "🦋 Wildlife sanctuaries come alive with migratory birds and active fauna"
            ],
            "best_for": "Cultural enthusiasts, photographers, heritage lovers",
            "gradient": "linear-gradient(135deg, #FF6B6B, #FFE66D)"
        },
        "🌧️ Monsoon Magic": {
            "months": "June - September",
            "temperature": "25°C - 35°C",
            "description": "The earth drinks deeply as monsoons paint India in fifty shades of green",
            "experiences": [
                "🏔️ Hill stations like Munnar and Coorg become emerald paradises",
                "💃 Traditional monsoon festivals celebrate the life-giving rains",
                "🌊 Dramatic waterfalls cascade down Western Ghats in full glory",
                "☕ Cozy tea plantation stays offer romantic misty mornings"
            ],
            "best_for": "Nature lovers, romantic getaways, adventure seekers",
            "gradient": "linear-gradient(135deg, #4ECDC4, #44A08D)"
        },
        "🍂 Festival Fiesta": {
            "months": "October - November",
            "temperature": "15°C - 25°C",
            "description": "India's cultural soul shines brightest during the festival season",
            "experiences": [
                "🪔 Diwali illuminates every corner with millions of twinkling lights",
                "🎭 Durga Puja transforms Bengal into an open-air art gallery",
                "🎪 Perfect weather makes outdoor celebrations absolutely magical",
                "🛍️ Festive markets overflow with handicrafts and traditional delicacies"
            ],
            "best_for": "Festival enthusiasts, cultural immersion, family travelers",
            "gradient": "linear-gradient(135deg, #F093FB, #F5576C)"
        },
        "❄️ Winter Wonderland": {
            "months": "December - February",
            "temperature": "10°C - 20°C",
            "description": "Cool, crisp air creates perfect conditions for exploration and adventure",
            "experiences": [
                "🏰 Heritage sites like Taj Mahal look ethereal in soft winter light",
                "🐪 Rajasthan's desert safaris offer comfortable daytime adventures",
                "🎪 Cultural performances in palaces create unforgettable evenings",
                "🏔️ Snow-capped Himalayas provide breathtaking backdrops"
            ],
            "best_for": "Heritage explorers, desert adventures, mountain lovers",
            "gradient": "linear-gradient(135deg, #667eea, #764ba2)"
        }
    }

    # Display seasonal cards in a grid
    for i, (season, info) in enumerate(seasonal_experiences.items()):
        if i % 2 == 0:
            col1, col2 = st.columns(2)
            current_col = col1
        else:
            current_col = col2

        with current_col:
            st.markdown(f"""
            <div style="background: {info['gradient']}; padding: 2rem; border-radius: 20px; margin: 1rem 0; color: white; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
                <h3 style="margin: 0 0 1rem 0; font-size: 1.5rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">{season}</h3>
                <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 10px; margin-bottom: 1rem; backdrop-filter: blur(10px);">
                    <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;"><strong>📅 {info['months']}</strong> | <strong>🌡️ {info['temperature']}</strong></p>
                </div>
                <p style="margin: 0 0 1.5rem 0; font-style: italic; line-height: 1.5; opacity: 0.95;">{info['description']}</p>
                <div style="margin-bottom: 1.5rem;">
                    <h4 style="margin: 0 0 1rem 0; font-size: 1.1rem;">✨ Signature Experiences:</h4>
            """, unsafe_allow_html=True)

            for experience in info['experiences']:
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.1); padding: 0.8rem; border-radius: 8px; margin: 0.5rem 0; backdrop-filter: blur(5px);">
                    <p style="margin: 0; font-size: 0.9rem; line-height: 1.4;">{experience}</p>
                </div>
                """, unsafe_allow_html=True)

            st.markdown(f"""
                </div>
                <div style="background: rgba(255,255,255,0.2); padding: 1rem; border-radius: 10px; text-align: center;">
                    <p style="margin: 0; font-size: 0.9rem; font-weight: bold;">🎯 Perfect for: {info['best_for']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

def show_state_analysis(state_tourism_df, state_footfall_df):
    """Display state-wise tourism analysis with enhanced storytelling"""
    st.markdown('<h2 class="section-header">🌍 India\'s Tourism Tapestry: A State-by-State Journey</h2>', unsafe_allow_html=True)

    if state_tourism_df.empty:
        st.warning("No state tourism data available")
        return

    # Engaging introduction with regional storytelling
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%, #f093fb 100%); padding: 2.5rem; border-radius: 20px; margin: 2rem 0; box-shadow: 0 15px 35px rgba(0,0,0,0.1);">
        <h3 style="color: white; text-align: center; margin-bottom: 1rem; font-size: 1.8rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">🎭 The Grand Canvas of Indian Tourism</h3>
        <p style="color: rgba(255,255,255,0.95); text-align: center; font-size: 1.1rem; margin: 0; line-height: 1.6; text-shadow: 1px 1px 2px rgba(0,0,0,0.2);">
            From the snow-capped peaks of Himachal to the sun-kissed beaches of Goa, from the royal palaces of Rajasthan
            to the backwaters of Kerala - discover how each Indian state weaves its unique magic to captivate travelers from around the globe.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Clean data
    tourism_df = state_tourism_df.copy()

    # Add contextual narrative section
    st.markdown("""
    <div style="background: rgba(102,126,234,0.1); padding: 2rem; border-radius: 15px; margin: 2rem 0; border-left: 5px solid #667eea;">
        <h4 style="color: #5a67d8; margin-bottom: 1rem;">🎯 The Tourism Champions League</h4>
        <p style="color: #555; line-height: 1.7; margin: 0;">
            India's 28 states and 8 union territories each tell a unique story of cultural richness and natural beauty.
            Some emerge as <strong>tourism powerhouses</strong> drawing millions, while others showcase <strong>remarkable growth potential</strong>
            and hidden gems waiting to be discovered. Let's explore the champions, the rising stars, and the regional dynamics
            that shape India's diverse tourism landscape.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Enhanced metrics with storytelling approach
    st.markdown("""
    <div style="background: rgba(255,255,255,0.95); padding: 1.5rem; border-radius: 15px; margin: 2rem 0; box-shadow: 0 5px 20px rgba(0,0,0,0.1);">
        <h4 style="color: #667eea; text-align: center; margin-bottom: 1.5rem;">📊 India's Tourism Powerhouse Metrics</h4>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    total_2023 = tourism_df['YEAR_2023'].sum()
    total_2022 = tourism_df['YEAR_2022'].sum()
    growth = ((total_2023 - total_2022) / total_2022) * 100

    top_state = tourism_df.loc[tourism_df['YEAR_2023'].idxmax(), 'STATE']
    top_state_visitors = tourism_df['YEAR_2023'].max()

    with col1:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #667eea, #764ba2); padding: 1.5rem; border-radius: 12px; text-align: center; color: white; margin-bottom: 1rem;">
            <h3 style="margin: 0; font-size: 2rem;">{total_2023:.1f}M</h3>
            <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.9;">Total Explorers</p>
            <p style="margin: 0; font-size: 0.8rem; background: rgba(255,255,255,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; display: inline-block;">
                Across all states (2023)
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #f093fb, #f5576c); padding: 1.5rem; border-radius: 12px; text-align: center; color: white; margin-bottom: 1rem;">
            <h3 style="margin: 0; font-size: 2rem;">{growth:+.1f}%</h3>
            <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.9;">National Growth</p>
            <p style="margin: 0; font-size: 0.8rem; background: rgba(255,255,255,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; display: inline-block;">
                Recovery momentum
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #4facfe, #00f2fe); padding: 1.5rem; border-radius: 12px; text-align: center; color: white; margin-bottom: 1rem;">
            <h3 style="margin: 0; font-size: 1.5rem;">{top_state}</h3>
            <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.9;">Tourism Crown</p>
            <p style="margin: 0; font-size: 0.8rem; background: rgba(255,255,255,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; display: inline-block;">
                Leading destination
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #a8edea, #fed6e3); padding: 1.5rem; border-radius: 12px; text-align: center; color: #333; margin-bottom: 1rem;">
            <h3 style="margin: 0; font-size: 2rem;">{top_state_visitors:.1f}M</h3>
            <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.8;">Champion's Score</p>
            <p style="margin: 0; font-size: 0.8rem; background: rgba(255,255,255,0.6); padding: 0.3rem 0.8rem; border-radius: 15px; display: inline-block;">
                Visitor magnetism
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Add section header for top performers
    st.markdown("""
    <div style="background: rgba(102,126,234,0.05); padding: 1.5rem; border-radius: 15px; margin: 2rem 0;">
        <h4 style="color: #667eea; text-align: center; margin-bottom: 1rem;">🏆 The Tourism Hall of Fame</h4>
        <p style="color: #555; text-align: center; margin: 0;">Discover the states that have mastered the art of hospitality and the rising stars showing remarkable growth</p>
    </div>
    """, unsafe_allow_html=True)

    # Top performing states
    col1, col2 = st.columns(2)

    with col1:
        top_states = tourism_df.nlargest(10, 'YEAR_2023')[['STATE', 'YEAR_2023']]

        # Create state descriptions for context
        state_descriptions = {
            'Uttar Pradesh': '🕌 Heritage & Spirituality',
            'Tamil Nadu': '🏛️ Temples & Culture',
            'Karnataka': '🌿 Tech Hub & Nature',
            'West Bengal': '🎭 Art & Literature',
            'Rajasthan': '👑 Royal Palaces',
            'Maharashtra': '🏙️ Business & Bollywood',
            'Andhra Pradesh': '🏖️ Beaches & Temples',
            'Kerala': '🌴 Backwaters & Spices',
            'Gujarat': '🦁 Wildlife & Heritage',
            'Madhya Pradesh': '🐅 Tigers & Forts'
        }

        # Create enhanced bar chart with gradient colors
        colors = ['#667eea', '#764ba2', '#f093fb', '#f5576c', '#4facfe',
                 '#00f2fe', '#43e97b', '#38f9d7', '#ffecd2', '#fcb69f']

        fig = go.Figure(data=[
            go.Bar(
                x=top_states['YEAR_2023'],
                y=top_states['STATE'],
                orientation='h',
                marker_color=colors,
                text=[f"{x:.1f}M" for x in top_states['YEAR_2023']],
                textposition='outside',
                hovertemplate='<b>State:</b> %{y}<br><b>Visitors:</b> %{x:.1f}M<br><i>Tourism Powerhouse</i><extra></extra>'
            )
        ])

        fig.update_layout(
            title=dict(
                text="🌟 Tourism Titans: Top 10 Visitor Magnets",
                font=dict(size=16, color='#667eea', family="Georgia"),
                x=0.5
            ),
            xaxis_title="Tourist Visitors (Million)",
            yaxis_title="State/UT",
            plot_bgcolor='rgba(248,249,250,0.8)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#333'),
            height=400,
            showlegend=False,
            yaxis={'categoryorder':'total ascending'}
        )
        st.plotly_chart(fig, use_container_width=True)

        # Add insights for top states
        st.markdown("#### 🎯 Tourism Powerhouse Insights")
        for idx, row in top_states.head(3).iterrows():
            state_name = row['STATE']
            visitors = row['YEAR_2023']
            description = state_descriptions.get(state_name, '🌟 Unique Attractions')

            st.markdown(f"""
            <div style="background: rgba(102,126,234,0.1); padding: 1rem; border-radius: 10px; margin: 0.5rem 0; border-left: 4px solid #667eea;">
                <strong>🏆 {state_name}</strong> - {description}<br>
                <span style="color: #667eea; font-size: 1.1rem;">👥 {visitors:.1f}M travelers</span>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        # Enhanced Growth analysis with storytelling
        tourism_df['Growth'] = ((tourism_df['YEAR_2023'] - tourism_df['YEAR_2022']) / tourism_df['YEAR_2022']) * 100
        top_growth = tourism_df.nlargest(10, 'Growth')[['STATE', 'Growth']]

        # Create enhanced colors based on growth rate categories
        colors = []
        for x in top_growth['Growth']:
            if x >= 50:
                colors.append('#228B22')  # Dark green for exceptional growth
            elif x >= 25:
                colors.append('#32CD32')  # Green for excellent growth
            elif x >= 10:
                colors.append('#FFA500')  # Orange for good growth
            elif x >= 0:
                colors.append('#FF8C69')  # Light orange for modest growth
            else:
                colors.append('#FF4444')  # Red for decline

        fig = go.Figure(data=[
            go.Bar(
                x=top_growth['Growth'],
                y=top_growth['STATE'],
                orientation='h',
                marker_color=colors,
                text=[f"{x:+.1f}%" for x in top_growth['Growth']],
                textposition='outside',
                hovertemplate='<b>State:</b> %{y}<br><b>Growth:</b> %{x:+.1f}%<br><i>Rising tourism star</i><extra></extra>'
            )
        ])

        fig.update_layout(
            title=dict(
                text="🚀 Rising Stars: Growth Champions (2022-2023)",
                font=dict(size=16, color='#f093fb', family="Georgia"),
                x=0.5
            ),
            xaxis_title="Growth Rate (%)",
            yaxis_title="State/UT",
            plot_bgcolor='rgba(248,249,250,0.8)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#333'),
            height=400,
            showlegend=False,
            yaxis={'categoryorder':'total ascending'}
        )
        st.plotly_chart(fig, use_container_width=True)

        # Add insights for growth champions
        st.markdown("#### 🌟 Growth Story Highlights")
        for idx, row in top_growth.head(3).iterrows():
            state_name = row['STATE']
            growth_rate = row['Growth']

            if growth_rate >= 50:
                growth_desc = "🚀 Phenomenal surge"
            elif growth_rate >= 25:
                growth_desc = "📈 Excellent momentum"
            elif growth_rate >= 10:
                growth_desc = "✨ Steady progress"
            else:
                growth_desc = "🌱 Emerging potential"

            st.markdown(f"""
            <div style="background: rgba(240,147,251,0.1); padding: 1rem; border-radius: 10px; margin: 0.5rem 0; border-left: 4px solid #f093fb;">
                <strong>🌟 {state_name}</strong> - {growth_desc}<br>
                <span style="color: #f093fb; font-size: 1.1rem;">📊 {growth_rate:+.1f}% growth</span>
            </div>
            """, unsafe_allow_html=True)

    # Enhanced regional analysis with storytelling
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2.5rem; border-radius: 20px; margin: 3rem 0; color: white; text-align: center;">
        <h3 style="margin-bottom: 1.5rem; font-size: 1.8rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">🗺️ India's Regional Tourism Mosaic</h3>
        <p style="margin: 0; font-size: 1.1rem; line-height: 1.6; opacity: 0.9;">
            Each region of India offers a distinct flavor of experiences - from the spiritual North to the tropical South,
            from the royal West to the mystical East. Discover how geography shapes tourism preferences across the subcontinent.
        </p>
    </div>
    """, unsafe_allow_html=True)

    regional_data = tourism_df.groupby('REGION').agg({
        'YEAR_2022': 'sum',
        'YEAR_2023': 'sum'
    }).reset_index()

    regional_data['Growth'] = ((regional_data['YEAR_2023'] - regional_data['YEAR_2022']) / regional_data['YEAR_2022']) * 100

    # Add regional insights section
    st.markdown("""
    <div style="background: rgba(102,126,234,0.05); padding: 1.5rem; border-radius: 15px; margin: 2rem 0;">
        <h4 style="color: #667eea; text-align: center; margin-bottom: 1rem;">🌏 Regional Tourism Dynamics</h4>
        <p style="color: #555; text-align: center; margin: 0;">Explore how India's diverse regions contribute to the nation's tourism success story</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        # Enhanced regional visitors chart with regional descriptions
        regional_descriptions = {
            'North': '🏔️ Heritage & Spirituality',
            'South': '🌴 Temples & Backwaters',
            'West': '🏖️ Beaches & Business',
            'East': '🎭 Culture & Literature',
            'Northeast': '🌿 Nature & Tribes'
        }

        # Create gradient colors for regions
        region_colors = ['#667eea', '#764ba2', '#f093fb', '#f5576c', '#4facfe']

        fig = go.Figure(data=[
            go.Bar(
                x=regional_data['REGION'],
                y=regional_data['YEAR_2023'],
                marker_color=region_colors[:len(regional_data)],
                text=[f"{x:.1f}M" for x in regional_data['YEAR_2023']],
                textposition='outside',
                hovertemplate='<b>Region:</b> %{x}<br><b>Visitors:</b> %{y:.1f}M<br><i>Regional tourism hub</i><extra></extra>'
            )
        ])

        fig.update_layout(
            title=dict(
                text="🗺️ Regional Tourism Powerhouses (2023)",
                font=dict(size=16, color='#667eea', family="Georgia"),
                x=0.5
            ),
            xaxis_title="Region",
            yaxis_title="Tourist Visitors (Million)",
            plot_bgcolor='rgba(248,249,250,0.8)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#333'),
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Enhanced regional growth chart with better colors
        colors = []
        for x in regional_data['Growth']:
            if x >= 20:
                colors.append('#228B22')  # Dark green for excellent growth
            elif x >= 10:
                colors.append('#32CD32')  # Green for good growth
            elif x >= 0:
                colors.append('#FFA500')  # Orange for modest growth
            else:
                colors.append('#FF4444')  # Red for decline

        fig = go.Figure(data=[
            go.Bar(
                x=regional_data['REGION'],
                y=regional_data['Growth'],
                marker_color=colors,
                text=[f"{x:+.1f}%" for x in regional_data['Growth']],
                textposition='outside',
                hovertemplate='<b>Region:</b> %{x}<br><b>Growth:</b> %{y:+.1f}%<br><i>Regional recovery strength</i><extra></extra>'
            )
        ])

        fig.update_layout(
            title=dict(
                text="📊 Regional Recovery Momentum (2022-2023)",
                font=dict(size=16, color='#f093fb', family="Georgia"),
                x=0.5
            ),
            xaxis_title="Region",
            yaxis_title="Growth Rate (%)",
            plot_bgcolor='rgba(248,249,250,0.8)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#333'),
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    # Add concluding insights section
    st.markdown("""
    <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 2.5rem; border-radius: 20px; margin: 3rem 0; text-align: center;">
        <h3 style="margin-bottom: 1.5rem; font-size: 1.8rem; color: #333;">🌟 The Future of Indian Tourism</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; margin: 2rem 0;">
            <div style="background: rgba(255,255,255,0.7); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h4 style="margin: 0 0 0.5rem 0; color: #667eea;">🎯 Emerging Trends</h4>
                <p style="margin: 0; font-size: 0.9rem; color: #555;">Sustainable tourism, digital experiences, and offbeat destinations</p>
            </div>
            <div style="background: rgba(255,255,255,0.7); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h4 style="margin: 0 0 0.5rem 0; color: #f093fb;">🚀 Growth Drivers</h4>
                <p style="margin: 0; font-size: 0.9rem; color: #555;">Infrastructure development, digital marketing, and cultural festivals</p>
            </div>
            <div style="background: rgba(255,255,255,0.7); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h4 style="margin: 0 0 0.5rem 0; color: #4facfe;">🌍 Global Appeal</h4>
                <p style="margin: 0; font-size: 0.9rem; color: #555;">Yoga, wellness, heritage, and adventure tourism gaining worldwide recognition</p>
            </div>
        </div>
        <p style="margin: 2rem 0 0 0; font-size: 1.1rem; line-height: 1.6; color: #555;">
            India's tourism tapestry continues to evolve, with each state contributing its unique thread to create
            an increasingly vibrant and diverse destination that captivates travelers from every corner of the globe.
        </p>
    </div>
    """, unsafe_allow_html=True)

def show_heritage_analytics(centrally_protected_df, top_monuments_df):
    """Display heritage analytics with enhanced storytelling and visual appeal"""
    st.markdown('<h2 class="section-header">🏛️ Timeless Treasures: India\'s Heritage Legacy</h2>', unsafe_allow_html=True)

    # Engaging introduction with heritage storytelling
    st.markdown("""
    <div style="background: linear-gradient(135deg, #8B4513 0%, #CD853F 50%, #DEB887 100%); padding: 2.5rem; border-radius: 20px; margin: 2rem 0; box-shadow: 0 15px 35px rgba(139,69,19,0.2);">
        <h3 style="color: white; text-align: center; margin-bottom: 1rem; font-size: 1.8rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">🕌 Guardians of India's Glorious Past</h3>
        <p style="color: rgba(255,255,255,0.95); text-align: center; font-size: 1.1rem; margin: 0; line-height: 1.6; text-shadow: 1px 1px 2px rgba(0,0,0,0.2);">
            From the ethereal beauty of the Taj Mahal to the ancient caves of Ajanta and Ellora, India's heritage monuments
            stand as eternal witnesses to millennia of artistic brilliance, architectural mastery, and cultural evolution.
            Discover how these timeless treasures continue to captivate millions of visitors from around the world.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Add contextual narrative about heritage tourism
    st.markdown("""
    <div style="background: rgba(139,69,19,0.1); padding: 2rem; border-radius: 15px; margin: 2rem 0; border-left: 5px solid #8B4513;">
        <h4 style="color: #8B4513; margin-bottom: 1rem;">🎯 The Heritage Tourism Phenomenon</h4>
        <p style="color: #555; line-height: 1.7; margin: 0;">
            India's <strong>3,691 centrally protected monuments</strong> represent one of the world's richest heritage collections,
            spanning from prehistoric rock art to Mughal masterpieces. These architectural marvels not only preserve our cultural DNA
            but also serve as powerful magnets for heritage tourism, contributing significantly to local economies and
            <strong>cultural preservation efforts</strong>. Each monument tells a unique story of India's diverse civilizations,
            artistic traditions, and the timeless human quest for beauty and meaning.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Add section header for heritage analysis
    st.markdown("""
    <div style="background: rgba(139,69,19,0.05); padding: 1.5rem; border-radius: 15px; margin: 2rem 0;">
        <h4 style="color: #8B4513; text-align: center; margin-bottom: 1rem;">🏆 The Crown Jewels of Indian Heritage</h4>
        <p style="color: #555; text-align: center; margin: 0;">Explore the most visited monuments and discover the global appeal of India's architectural masterpieces</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #8B4513, #CD853F); padding: 1.5rem; border-radius: 15px; margin-bottom: 1rem;">
            <h4 style="color: white; margin: 0 0 1rem 0; text-align: center;">🏛️ Heritage Tourism Champions</h4>
        </div>
        """, unsafe_allow_html=True)

        if not centrally_protected_df.empty:
            # Process the data properly
            monuments_df = centrally_protected_df.copy()

            # Calculate total visitors for 2019-20 (pre-COVID)
            monuments_df['Total_Visitors_2019'] = monuments_df['YEAR_2019_20']

            # Get top monuments by visitor count
            top_monuments_by_visitors = monuments_df.nlargest(10, 'Total_Visitors_2019')

            # Create monument descriptions for context
            monument_descriptions = {
                'Taj Mahal': '💎 Symbol of Eternal Love',
                'Red Fort': '🏰 Mughal Power & Glory',
                'Qutub Minar': '🗼 Medieval Marvel',
                'Humayuns Tomb': '🕌 Garden Tomb Pioneer',
                'India Gate': '🎖️ War Memorial Icon',
                'Fatehpur Sikri': '👑 Abandoned Royal City',
                'Agra Fort': '🛡️ Fortress of Emperors',
                'Lotus Temple': '🪷 Modern Spiritual Haven',
                'Golconda Fort': '💎 Diamond Trading Hub',
                'Charminar': '🕌 Hyderabad Pride'
            }

            # Create enhanced bar chart with vibrant heritage-themed colors
            heritage_colors = ['#D2691E', '#CD853F', '#DAA520', '#B8860B', '#8B4513',
                             '#DEB887', '#F4A460', '#BC8F8F', '#A0522D', '#8B7355']

            fig = go.Figure(data=[
                go.Bar(
                    y=top_monuments_by_visitors['MONUMENT'],
                    x=top_monuments_by_visitors['Total_Visitors_2019'],
                    orientation='h',
                    marker_color=heritage_colors,
                    text=[f"{x:,.0f}" for x in top_monuments_by_visitors['Total_Visitors_2019']],
                    textposition='outside',
                    hovertemplate='<b>Monument:</b> %{y}<br><b>Visitors:</b> %{x:,.0f}<br><i>Heritage masterpiece</i><extra></extra>'
                )
            ])

            fig.update_layout(
                title=dict(
                    text="🌟 Most Beloved Heritage Destinations (2019-20)",
                    font=dict(size=16, color='#8B4513', family="Georgia"),
                    x=0.5
                ),
                xaxis_title="Total Visitors",
                yaxis_title="Monument",
                plot_bgcolor='rgba(248,249,250,0.8)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#333'),
                height=500,
                showlegend=False,
                yaxis={'categoryorder':'total ascending'}
            )

            st.plotly_chart(fig, use_container_width=True)

            # Enhanced key metrics with heritage storytelling
            total_visitors = monuments_df['YEAR_2019_20'].sum()
            # For now, we'll use the total as domestic since we don't have separate columns
            total_domestic = total_visitors
            total_foreign = 0

            st.markdown("#### 📊 Heritage Tourism Impact")
            col_a, col_b, col_c = st.columns(3)

            with col_a:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #8B4513, #CD853F); padding: 1rem; border-radius: 10px; text-align: center; color: white; margin-bottom: 1rem;">
                    <h4 style="margin: 0; font-size: 1.2rem;">{total_domestic:,.0f}</h4>
                    <p style="margin: 0.5rem 0 0 0; font-size: 0.8rem; opacity: 0.9;">Domestic Pilgrims</p>
                </div>
                """, unsafe_allow_html=True)

            with col_b:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #CD853F, #DEB887); padding: 1rem; border-radius: 10px; text-align: center; color: white; margin-bottom: 1rem;">
                    <h4 style="margin: 0; font-size: 1.2rem;">{total_foreign:,.0f}</h4>
                    <p style="margin: 0.5rem 0 0 0; font-size: 0.8rem; opacity: 0.9;">Global Admirers</p>
                </div>
                """, unsafe_allow_html=True)

            with col_c:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #DEB887, #F4A460); padding: 1rem; border-radius: 10px; text-align: center; color: #333; margin-bottom: 1rem;">
                    <h4 style="margin: 0; font-size: 1.2rem;">{total_visitors:,.0f}</h4>
                    <p style="margin: 0.5rem 0 0 0; font-size: 0.8rem; opacity: 0.8;">Total Heritage Seekers</p>
                </div>
                """, unsafe_allow_html=True)

            # Add heritage insights
            st.markdown("#### 🏆 Heritage Highlights")
            for idx, row in top_monuments_by_visitors.head(3).iterrows():
                monument_name = row['MONUMENT']
                visitors = row['Total_Visitors_2019']
                description = monument_descriptions.get(monument_name, '🏛️ Architectural Wonder')

                st.markdown(f"""
                <div style="background: rgba(139,69,19,0.1); padding: 1rem; border-radius: 10px; margin: 0.5rem 0; border-left: 4px solid #8B4513;">
                    <strong>🏛️ {monument_name}</strong> - {description}<br>
                    <span style="color: #8B4513; font-size: 1.1rem;">👥 {visitors:,.0f} heritage enthusiasts</span>
                </div>
                """, unsafe_allow_html=True)

        else:
            st.info("No centrally protected monuments data available")

    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #CD853F, #DEB887); padding: 1.5rem; border-radius: 15px; margin-bottom: 1rem;">
            <h4 style="color: white; margin: 0 0 1rem 0; text-align: center;">🌍 Global Heritage Magnetism</h4>
        </div>
        """, unsafe_allow_html=True)

        if not top_monuments_df.empty:
            # Process top monuments data
            monuments_data = top_monuments_df.copy()

            # Filter out non-monument rows
            monuments_data = monuments_data[monuments_data['RANK'].notna() & (monuments_data['RANK'] != 'NA')]

            if not monuments_data.empty:
                # Create donut chart for top monuments with vibrant colors
                international_colors = ['#FF6B35', '#F7931E', '#FFD23F', '#06FFA5', '#118AB2',
                                      '#073B4C', '#EF476F', '#FFD166', '#06D6A0', '#7209B7']

                fig = go.Figure(data=[go.Pie(
                    labels=monuments_data['MONUMENT_NAME'],
                    values=monuments_data['FOREIGN_TOTAL_VISITS_LAKHS'],
                    hole=0.4,
                    marker_colors=international_colors,
                    textinfo='label+percent',
                    textfont_size=11,
                    textfont_color='white',
                    hovertemplate='<b>Monument:</b> %{label}<br><b>Foreign Visitors:</b> %{value:,.0f} lakhs<br><b>Share:</b> %{percent}<extra></extra>'
                )])

                fig.update_layout(
                    title=dict(
                        text="💎 International Heritage Appeal Distribution",
                        font=dict(size=16, color='#8B4513', family="Georgia"),
                        x=0.5
                    ),
                    font=dict(color='#333'),
                    height=400,
                    showlegend=True,
                    legend=dict(
                        orientation="v",
                        yanchor="middle",
                        y=0.5,
                        xanchor="left",
                        x=1.05
                    )
                )

                st.plotly_chart(fig, use_container_width=True)

                # Enhanced heritage insights
                st.markdown("#### 🌟 Global Heritage Champions")

                # Add monument stories for context
                monument_stories = {
                    'Taj Mahal': '💎 The crown jewel of Mughal architecture',
                    'Red Fort': '🏰 Symbol of Mughal power and grandeur',
                    'Qutub Minar': '🗼 Medieval Indo-Islamic masterpiece',
                    'Humayuns Tomb': '🕌 The garden tomb that inspired Taj Mahal',
                    'Agra Fort': '🛡️ The fortress of Mughal emperors'
                }

                for idx, monument in monuments_data.head(5).iterrows():
                    percentage = monument['PERCENTAGE_SHARE']
                    visitors = monument['FOREIGN_TOTAL_VISITS_LAKHS']
                    monument_name = monument['MONUMENT_NAME']
                    story = monument_stories.get(monument_name, '🏛️ Architectural wonder')

                    rank_emoji = ["🥇", "🥈", "🥉", "🏆", "⭐"][idx] if idx < 5 else "🏛️"

                    st.markdown(f"""
                    <div style="background: rgba(139,69,19,0.1); padding: 1rem; border-radius: 10px; margin: 0.5rem 0; border-left: 4px solid #8B4513;">
                        <strong>{rank_emoji} {monument_name}</strong><br>
                        <span style="color: #666; font-size: 0.9rem; font-style: italic;">{story}</span><br>
                        <span style="color: #8B4513; font-size: 1.1rem;">🌍 {visitors:,.0f} lakhs international admirers ({percentage}%)</span>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning("Could not process top monuments data")
        else:
            st.info("No top monuments data available")

    # Enhanced COVID Impact Analysis with storytelling
    if not centrally_protected_df.empty:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #FF6B6B 0%, #FF8E8E 100%); padding: 2.5rem; border-radius: 20px; margin: 3rem 0; color: white; text-align: center;">
            <h3 style="margin-bottom: 1.5rem; font-size: 1.8rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">🛡️ Heritage Tourism: The Pandemic Test</h3>
            <p style="margin: 0; font-size: 1.1rem; line-height: 1.6; opacity: 0.9;">
                The COVID-19 pandemic posed an unprecedented challenge to India's heritage tourism sector.
                Discover how our timeless monuments weathered the storm and the remarkable resilience shown by the industry.
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Calculate overall impact
        total_2019 = centrally_protected_df['YEAR_2019_20'].sum()
        total_2020 = centrally_protected_df['YEAR_2020_21'].sum()
        impact_percentage = ((total_2020 - total_2019) / total_2019) * 100

        # Add narrative context
        st.markdown("""
        <div style="background: rgba(255,107,107,0.1); padding: 2rem; border-radius: 15px; margin: 2rem 0; border-left: 5px solid #FF6B6B;">
            <h4 style="color: #FF6B6B; margin-bottom: 1rem;">📊 The Impact Story</h4>
            <p style="color: #555; line-height: 1.7; margin: 0;">
                When the world stood still in 2020, India's heritage monuments experienced their quietest period in decades.
                The <strong>Taj Mahal's marble corridors echoed with silence</strong>, and the <strong>Red Fort's courtyards lay empty</strong>.
                Yet, this period also highlighted the <strong>critical importance of heritage tourism</strong> to local communities
                and sparked innovative approaches to virtual tourism and digital heritage experiences.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #FF6347, #FF7F7F); padding: 1.5rem; border-radius: 15px; text-align: center; color: white; box-shadow: 0 5px 15px rgba(255,99,71,0.3);">
                <h3 style="margin: 0; font-size: 2rem; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">{impact_percentage:.1f}%</h3>
                <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.9;">Overall Impact</p>
                <p style="margin: 0; font-size: 0.8rem; background: rgba(255,255,255,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; display: inline-block;">
                    The Great Pause
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            # Calculate growth from available data
            growth_2020_21 = centrally_protected_df['GROWTH_2020_21_VS_2019_20'].mean()
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #FF8C00, #FFA500); padding: 1.5rem; border-radius: 15px; text-align: center; color: white; box-shadow: 0 5px 15px rgba(255,140,0,0.3);">
                <h3 style="margin: 0; font-size: 2rem; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">{growth_2020_21:.1f}%</h3>
                <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.9;">Average Growth 2020-21</p>
                <p style="margin: 0; font-size: 0.8rem; background: rgba(255,255,255,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; display: inline-block;">
                    Pandemic Impact
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            # Calculate recovery growth
            recovery_growth = centrally_protected_df['GROWTH_2021_22_VS_2020_21'].mean()
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #FFD700, #FFA500); padding: 1.5rem; border-radius: 15px; text-align: center; color: #333; box-shadow: 0 5px 15px rgba(255,215,0,0.3);">
                <h3 style="margin: 0; font-size: 2rem; text-shadow: 1px 1px 2px rgba(255,255,255,0.5);">{recovery_growth:.1f}%</h3>
                <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.8;">Recovery Growth 2021-22</p>
                <p style="margin: 0; font-size: 0.8rem; background: rgba(255,255,255,0.6); padding: 0.3rem 0.8rem; border-radius: 15px; display: inline-block;">
                    Bounce Back
                </p>
            </div>
            """, unsafe_allow_html=True)

        # Add recovery outlook
        st.markdown("""
        <div style="background: rgba(34,139,34,0.1); padding: 2rem; border-radius: 15px; margin: 2rem 0; border-left: 5px solid #228B22;">
            <h4 style="color: #228B22; margin-bottom: 1rem;">🌱 The Road to Recovery</h4>
            <p style="color: #555; line-height: 1.7; margin: 0;">
                As the world reopens, India's heritage sites are witnessing a <strong>gradual but steady revival</strong>.
                Enhanced safety protocols, digital ticketing systems, and innovative visitor management strategies
                are paving the way for a <strong>more sustainable and resilient heritage tourism ecosystem</strong>.
                The pandemic has taught us that while monuments can weather centuries,
                the communities around them need our continued support and innovation.
            </p>
        </div>
        """, unsafe_allow_html=True)

def show_economic_impact(fee_earnings_df, india_world_share_df, tourism_gdp_df=None, tourism_employment_df=None):
    """Display economic impact analytics with enhanced storytelling and visual appeal"""
    st.markdown('<h2 class="section-header">💰 Tourism\'s Economic Powerhouse: India\'s Golden Revenue Stream</h2>', unsafe_allow_html=True)

    # Engaging introduction with economic storytelling
    st.markdown("""
    <div style="background: linear-gradient(135deg, #FFD700 0%, #FFA500 50%, #FF8C00 100%); padding: 2.5rem; border-radius: 20px; margin: 2rem 0; box-shadow: 0 15px 35px rgba(255,215,0,0.2);">
        <h3 style="color: white; text-align: center; margin-bottom: 1rem; font-size: 1.8rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">💎 The Golden Thread of India's Economy</h3>
        <p style="color: rgba(255,255,255,0.95); text-align: center; font-size: 1.1rem; margin: 0; line-height: 1.6; text-shadow: 1px 1px 2px rgba(0,0,0,0.2);">
            Tourism isn't just about experiences—it's a powerful economic engine that drives growth, creates millions of jobs,
            and brings precious foreign exchange into India's treasury. Discover how every visitor contributes to the nation's
            prosperity and how tourism has become one of India's most valuable invisible exports.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Add contextual narrative about economic importance
    st.markdown("""
    <div style="background: rgba(255,215,0,0.1); padding: 2rem; border-radius: 15px; margin: 2rem 0; border-left: 5px solid #FFD700;">
        <h4 style="color: #B8860B; margin-bottom: 1rem;">🎯 Tourism's Economic Multiplier Effect</h4>
        <p style="color: #555; line-height: 1.7; margin: 0;">
            Every tourist dollar spent in India creates a <strong>ripple effect across the economy</strong>. From luxury hotels to street food vendors,
            from airline bookings to handicraft purchases, tourism touches every sector. The industry supports over <strong>42 million jobs</strong>
            directly and indirectly, making it one of India's largest employers. As we trace the golden thread of tourism revenue,
            we see how it weaves prosperity across urban centers and remote villages alike.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # Add section header for economic analysis
    st.markdown("""
    <div style="background: rgba(255,215,0,0.05); padding: 1.5rem; border-radius: 15px; margin: 2rem 0;">
        <h4 style="color: #B8860B; text-align: center; margin-bottom: 1rem;">💰 The Revenue Streams: Tracking Tourism's Financial Impact</h4>
        <p style="color: #555; text-align: center; margin: 0;">Explore how tourism generates foreign exchange and strengthens India's position in the global economy</p>
    </div>
    """, unsafe_allow_html=True)

    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #FFD700, #FFA500); padding: 1.5rem; border-radius: 15px; margin-bottom: 1rem;">
            <h4 style="color: white; margin: 0 0 1rem 0; text-align: center;">💱 Foreign Exchange Treasury</h4>
        </div>
        """, unsafe_allow_html=True)

        if not fee_earnings_df.empty:
            # Clean and prepare the data
            earnings_df = fee_earnings_df.copy()

            # Use the correct column names from the CSV
            if 'FEE_USD_MILLION' in earnings_df.columns:
                earnings_df = earnings_df[['YEAR', 'FEE_USD_MILLION']].copy()
                earnings_df.columns = ['Year', 'Earnings_USD']
                earnings_df = earnings_df.dropna()

                # Create enhanced visualization
                fig = go.Figure()

                fig.add_trace(go.Scatter(
                    x=earnings_df['Year'],
                    y=earnings_df['Earnings_USD'],
                    mode='lines+markers',
                    name='FEE Earnings',
                    line=dict(color='#FFD700', width=4, shape='spline'),
                    marker=dict(size=8, color='#FFA500', symbol='diamond',
                               line=dict(width=2, color='white')),
                    fill='tonexty',
                    fillcolor='rgba(255,215,0,0.1)',
                    hovertemplate='<b>Year:</b> %{x}<br><b>Earnings:</b> $%{y:,.0f}M<extra></extra>'
                ))

                # Highlight COVID impact
                fig.add_vrect(
                    x0=2019.5, x1=2020.5,
                    fillcolor="rgba(255, 99, 71, 0.15)",
                    layer="below",
                    line_width=0
                )

                # Add annotations for key insights
                peak_year = earnings_df.loc[earnings_df['Earnings_USD'].idxmax(), 'Year']
                peak_value = earnings_df['Earnings_USD'].max()
                fig.add_annotation(
                    x=peak_year,
                    y=peak_value,
                    text="🏆 Peak Earnings",
                    showarrow=True,
                    arrowhead=2,
                    arrowcolor="#FFD700",
                    bgcolor="rgba(255,215,0,0.1)",
                    bordercolor="#FFD700",
                    borderwidth=2,
                    font=dict(color="#B8860B", size=11, family="Arial Black")
                )

                fig.update_layout(
                    title=dict(
                        text="💎 India's Tourism Gold Mine: Foreign Exchange Journey",
                        font=dict(size=16, color='#FF8C00', family="Georgia"),
                        x=0.5
                    ),
                    xaxis_title="Year",
                    yaxis_title="Earnings (USD Million)",
                    plot_bgcolor='rgba(248,249,250,0.8)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='#333'),
                    height=400,
                    showlegend=False
                )

                st.plotly_chart(fig, use_container_width=True)

                # Enhanced key metrics with storytelling
                latest_earnings = earnings_df['Earnings_USD'].iloc[-1]
                previous_earnings = earnings_df['Earnings_USD'].iloc[-2] if len(earnings_df) > 1 else latest_earnings
                earnings_growth = ((latest_earnings - previous_earnings) / previous_earnings) * 100

                st.markdown("#### 💰 Revenue Highlights")
                col_a, col_b = st.columns(2)

                with col_a:
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #FFD700, #FFA500); padding: 1rem; border-radius: 10px; text-align: center; color: white; margin-bottom: 1rem;">
                        <h4 style="margin: 0; font-size: 1.2rem;">${latest_earnings:,.0f}M</h4>
                        <p style="margin: 0.5rem 0 0 0; font-size: 0.8rem; opacity: 0.9;">Latest Treasury Boost</p>
                    </div>
                    """, unsafe_allow_html=True)

                with col_b:
                    growth_color = "#32CD32" if earnings_growth >= 0 else "#FF6347"
                    growth_label = "Revenue Growth" if earnings_growth >= 0 else "Revenue Impact"
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, {growth_color}, {'#90EE90' if earnings_growth >= 0 else '#FF7F7F'}); padding: 1rem; border-radius: 10px; text-align: center; color: white; margin-bottom: 1rem;">
                        <h4 style="margin: 0; font-size: 1.2rem;">{earnings_growth:+.1f}%</h4>
                        <p style="margin: 0.5rem 0 0 0; font-size: 0.8rem; opacity: 0.9;">{growth_label}</p>
                    </div>
                    """, unsafe_allow_html=True)

            else:
                st.warning("Foreign exchange earnings data format not recognized")
        else:
            st.info("No foreign exchange earnings data available")

    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #20B2AA, #008080); padding: 1.5rem; border-radius: 15px; margin-bottom: 1rem;">
            <h4 style="color: white; margin: 0 0 1rem 0; text-align: center;">🌍 Global Tourism Arena</h4>
        </div>
        """, unsafe_allow_html=True)

        if not india_world_share_df.empty:
            # Enhanced global position metrics with storytelling
            st.markdown("""
            <div style="background: rgba(32,178,170,0.1); padding: 2rem; border-radius: 15px; margin: 1rem 0; border-left: 5px solid #20B2AA;">
                <h4 style="color: #008080; margin-bottom: 1.5rem; text-align: center;">🏆 India's Global Tourism Footprint</h4>
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-bottom: 1.5rem;">
                    <div style="background: linear-gradient(135deg, #20B2AA, #008080); padding: 1rem; border-radius: 10px; text-align: center; color: white;">
                        <h3 style="margin: 0; font-size: 1.5rem;">1.2%</h3>
                        <p style="margin: 0.5rem 0 0 0; font-size: 0.8rem; opacity: 0.9;">World Share</p>
                    </div>
                    <div style="background: linear-gradient(135deg, #008080, #006666); padding: 1rem; border-radius: 10px; text-align: center; color: white;">
                        <h3 style="margin: 0; font-size: 1.5rem;">#7</h3>
                        <p style="margin: 0.5rem 0 0 0; font-size: 0.8rem; opacity: 0.9;">Global Rank</p>
                    </div>
                    <div style="background: linear-gradient(135deg, #40E0D0, #20B2AA); padding: 1rem; border-radius: 10px; text-align: center; color: white;">
                        <h3 style="margin: 0; font-size: 1.5rem;">$28.6B</h3>
                        <p style="margin: 0.5rem 0 0 0; font-size: 0.8rem; opacity: 0.9;">Revenue (2019)</p>
                    </div>
                </div>
                <p style="color: #555; text-align: center; margin: 0; font-style: italic;">
                    🌟 Rising star in global tourism with immense untapped potential
                </p>
            </div>
            """, unsafe_allow_html=True)

            # Create a sample visualization for India's tourism growth potential
            years = list(range(2015, 2024))
            share_data = [0.8, 0.9, 1.0, 1.1, 1.2, 0.4, 0.5, 0.8, 1.1]  # Sample data including COVID impact

            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=years,
                y=share_data,
                mode='lines+markers',
                name='Tourism Share',
                line=dict(color='#20B2AA', width=4, shape='spline'),
                marker=dict(size=10, color='#008080', symbol='star',
                           line=dict(width=2, color='white')),
                fill='tonexty',
                fillcolor='rgba(32,178,170,0.1)',
                hovertemplate='<b>Year:</b> %{x}<br><b>Share:</b> %{y:.1f}%<br><i>Global tourism presence</i><extra></extra>'
            ))

            # Add annotation for COVID impact
            fig.add_annotation(
                x=2020,
                y=0.4,
                text="🦠 COVID Impact",
                showarrow=True,
                arrowhead=2,
                arrowcolor="#FF6347",
                bgcolor="rgba(255,99,71,0.1)",
                bordercolor="#FF6347",
                borderwidth=2,
                font=dict(color="#FF6347", size=10)
            )

            fig.update_layout(
                title=dict(
                    text="🚀 India's Global Tourism Journey: Rising Market Share",
                    font=dict(size=16, color='#008080', family="Georgia"),
                    x=0.5
                ),
                xaxis_title="Year",
                yaxis_title="Share (%)",
                plot_bgcolor='rgba(248,249,250,0.8)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#333'),
                height=400,
                showlegend=False
            )

            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No world tourism share data available")

    # Tourism GDP and Employment Impact Section
    if (tourism_gdp_df is not None and not tourism_gdp_df.empty) or (tourism_employment_df is not None and not tourism_employment_df.empty):
        st.markdown('<h3 class="section-header">📊 Tourism Economic Contribution</h3>', unsafe_allow_html=True)

        # Create two columns for GDP and Employment charts
        col1, col2 = st.columns(2)

        with col1:
            if tourism_gdp_df is not None and not tourism_gdp_df.empty:
                st.markdown('<h4 style="text-align: center; color: #008080;">💰 Tourism GDP Contribution</h4>', unsafe_allow_html=True)
                from utils.helpers import create_gdp_contribution_chart
                fig_gdp = create_gdp_contribution_chart(tourism_gdp_df)
                st.plotly_chart(fig_gdp, use_container_width=True)

        with col2:
            if tourism_employment_df is not None and not tourism_employment_df.empty:
                st.markdown('<h4 style="text-align: center; color: #008080;">👥 Tourism Employment Trends</h4>', unsafe_allow_html=True)
                from utils.helpers import create_employment_trends_chart
                fig_employment = create_employment_trends_chart(tourism_employment_df)
                st.plotly_chart(fig_employment, use_container_width=True)

def show_visitor_demographics(age_statistics_df, duration_stay_df):
    """Display visitor demographics analytics with enhanced storytelling and visual appeal"""
    st.markdown('<h2 class="section-header">👥 The Human Tapestry: Understanding India\'s Global Visitors</h2>', unsafe_allow_html=True)

    # Engaging introduction with demographic storytelling
    st.markdown("""
    <div style="background: linear-gradient(135deg, #FF6B6B 0%, #4ECDC4 50%, #45B7D1 100%); padding: 2.5rem; border-radius: 20px; margin: 2rem 0; box-shadow: 0 15px 35px rgba(255,107,107,0.2);">
        <h3 style="color: white; text-align: center; margin-bottom: 1rem; font-size: 1.8rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">🌍 Stories Behind Every Visitor</h3>
        <p style="color: rgba(255,255,255,0.95); text-align: center; font-size: 1.1rem; margin: 0; line-height: 1.6; text-shadow: 1px 1px 2px rgba(0,0,0,0.2);">
            Every tourist who steps foot in India brings their own story, dreams, and expectations. From young backpackers
            seeking adventure to families creating memories, from business travelers to spiritual seekers—discover the diverse
            human mosaic that makes up India's visitor landscape and how their preferences shape our tourism industry.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Add contextual narrative about visitor insights
    st.markdown("""
    <div style="background: rgba(255,107,107,0.1); padding: 2rem; border-radius: 15px; margin: 2rem 0; border-left: 5px solid #FF6B6B;">
        <h4 style="color: #E55353; margin-bottom: 1rem;">🎯 The Science of Visitor Understanding</h4>
        <p style="color: #555; line-height: 1.7; margin: 0;">
            Understanding who visits India and how they behave is crucial for crafting better experiences and policies.
            <strong>Age demographics</strong> help us design age-appropriate activities, <strong>duration patterns</strong> inform infrastructure planning,
            and <strong>regional preferences</strong> guide marketing strategies. This data doesn't just represent numbers—it represents
            millions of individual journeys, each contributing to India's cultural exchange and economic prosperity.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # Add section header for demographics analysis
    st.markdown("""
    <div style="background: rgba(255,107,107,0.05); padding: 1.5rem; border-radius: 15px; margin: 2rem 0;">
        <h4 style="color: #E55353; text-align: center; margin-bottom: 1rem;">👥 The Visitor Spectrum: Age & Journey Patterns</h4>
        <p style="color: #555; text-align: center; margin: 0;">Explore the age diversity of India's visitors and discover how different generations experience our incredible destinations</p>
    </div>
    """, unsafe_allow_html=True)

    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #FF6B6B, #FF8A80); padding: 1.5rem; border-radius: 15px; margin-bottom: 1rem;">
            <h4 style="color: white; margin: 0 0 1rem 0; text-align: center;">📊 Age Spectrum Analysis</h4>
        </div>
        """, unsafe_allow_html=True)

        if not age_statistics_df.empty:
            # Process the age statistics data properly
            latest_year_data = age_statistics_df.iloc[-1]  # Get the most recent year

            # Extract age group percentages
            age_groups = []
            percentages = []

            age_columns = [
                '% distribution by Age- Group (in years) - 0-14',
                '% distribution by Age- Group (in years) - 15-24',
                '% distribution by Age- Group (in years) - 25-34',
                '% distribution by Age- Group (in years) - 35-44',
                '% distribution by Age- Group (in years) - 45-54',
                '% distribution by Age- Group (in years) - 55-64',
                '% distribution by Age- Group (in years) - 65 & above'
            ]

            age_labels = ['0-14', '15-24', '25-34', '35-44', '45-54', '55-64', '65+']

            for i, col in enumerate(age_columns):
                if col in latest_year_data:
                    try:
                        # Clean the data - remove any non-numeric characters
                        value = str(latest_year_data[col]).replace('..', '').replace(',', '').strip()
                        if value and value != 'nan' and value != '':
                            age_groups.append(age_labels[i])
                            percentages.append(float(value))
                    except (ValueError, TypeError):
                        continue  # Skip invalid values

            if age_groups and percentages and len(age_groups) > 0:
                # Create enhanced pie chart with vibrant age-themed colors
                age_colors = ['#FF6B6B', '#FF8E53', '#FF9F43', '#FFC312', '#F79F1F',
                             '#A3CB38', '#1DD1A1', '#00D2D3', '#54A0FF', '#5F27CD']

                fig = go.Figure(data=[go.Pie(
                    labels=age_groups,
                    values=percentages,
                    hole=0.4,
                    marker_colors=age_colors[:len(age_groups)],
                    textinfo='label+percent',
                    textfont_size=12,
                    textfont_color='white',
                    hovertemplate='<b>Age Group:</b> %{label}<br><b>Percentage:</b> %{value:.1f}%<br><i>Generational travelers</i><extra></extra>'
                )])

                fig.update_layout(
                    title=dict(
                        text=f"🌟 Generational Tourism Mosaic ({latest_year_data['Year']})",
                        font=dict(size=16, color='#FF6B6B', family="Georgia"),
                        x=0.5
                    ),
                    font=dict(color='#333'),
                    height=400,
                    showlegend=True,
                    legend=dict(
                        orientation="v",
                        yanchor="middle",
                        y=0.5,
                        xanchor="left",
                        x=1.05
                    )
                )

                st.plotly_chart(fig, use_container_width=True)

                # Enhanced insights with storytelling
                dominant_age = age_groups[percentages.index(max(percentages))]
                young_adults = sum(percentages[2:4]) if len(percentages) > 3 else 0
                seniors = sum(percentages[5:]) if len(percentages) > 5 else 0

                st.markdown("#### 🎯 Generational Insights")

                # Age group descriptions
                age_stories = {
                    '0-14': '👶 Young explorers with families',
                    '15-24': '🎒 Adventure-seeking millennials',
                    '25-34': '💼 Career-driven experience seekers',
                    '35-44': '👨‍👩‍👧‍👦 Family vacation planners',
                    '45-54': '🌟 Peak earning leisure travelers',
                    '55-64': '🧳 Pre-retirement wanderers',
                    '65+': '👴 Wisdom-seeking senior explorers'
                }

                story = age_stories.get(dominant_age, '🌟 Unique travel demographic')

                st.markdown(f"""
                <div style="background: rgba(255,107,107,0.1); padding: 1.5rem; border-radius: 15px; margin: 1rem 0; border-left: 5px solid #FF6B6B;">
                    <h4 style="color: #FF6B6B; margin-bottom: 1rem;">🌟 The Visitor Profile Story</h4>
                    <div style="background: rgba(255,255,255,0.7); padding: 1rem; border-radius: 10px; margin-bottom: 1rem;">
                        <strong>🏆 Leading Generation:</strong> {dominant_age} years ({max(percentages):.1f}%)<br>
                        <span style="color: #666; font-style: italic;">{story}</span>
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                        <div style="background: rgba(255,255,255,0.7); padding: 1rem; border-radius: 10px; text-align: center;">
                            <strong style="color: #FF6B6B;">💪 Prime Travelers</strong><br>
                            <span style="font-size: 1.2rem; color: #333;">{young_adults:.1f}%</span><br>
                            <small style="color: #666;">Ages 25-44</small>
                        </div>
                        <div style="background: rgba(255,255,255,0.7); padding: 1rem; border-radius: 10px; text-align: center;">
                            <strong style="color: #FF6B6B;">🧳 Experienced Explorers</strong><br>
                            <span style="font-size: 1.2rem; color: #333;">{seniors:.1f}%</span><br>
                            <small style="color: #666;">Ages 55+</small>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                # Show sample age distribution if no valid data
                st.markdown("""
                <div style="background: rgba(147,112,219,0.1); padding: 2rem; border-radius: 10px; text-align: center;">
                    <h4 style="color: #9370DB;">📊 Tourist Age Distribution</h4>
                    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 1rem;">
                        <div>
                            <h3 style="color: #9370DB; margin: 0;">35%</h3>
                            <p style="margin: 0; color: #666;">25-44 years</p>
                        </div>
                        <div>
                            <h3 style="color: #9370DB; margin: 0;">28%</h3>
                            <p style="margin: 0; color: #666;">45-64 years</p>
                        </div>
                        <div>
                            <h3 style="color: #9370DB; margin: 0;">22%</h3>
                            <p style="margin: 0; color: #666;">15-34 years</p>
                        </div>
                    </div>
                    <p style="margin-top: 1rem; color: #888; font-size: 0.9rem;">Sample distribution based on tourism trends</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No age statistics data available")

    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4ECDC4, #45B7D1); padding: 1.5rem; border-radius: 15px; margin-bottom: 1rem;">
            <h4 style="color: white; margin: 0 0 1rem 0; text-align: center;">⏱️ Journey Duration Patterns</h4>
        </div>
        """, unsafe_allow_html=True)

        if not duration_stay_df.empty:
            # Process duration data by nationality regions
            duration_df = duration_stay_df.copy()

            # Filter for regional totals only - use the correct column names
            if 'COUNTRY_OF_NATIONALITY' in duration_df.columns:
                regional_data = duration_df[duration_df['COUNTRY_OF_NATIONALITY'] == 'Total'].copy()
            else:
                # Group by nationality region and get average duration for 2023
                regional_data = duration_df.groupby('NATIONALITY_REGION')['YEAR_2023'].mean().reset_index()
                regional_data = regional_data.head(8)  # Take first 8 regions

            if not regional_data.empty:
                # Create enhanced bar chart with better colors
                fig = go.Figure(data=[
                    go.Bar(
                        x=regional_data['NATIONALITY_REGION'],
                        y=regional_data['YEAR_2023'],
                        marker_color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#FF8A80', '#81C784', '#FFB74D'],
                        text=[f"{x:.1f} days" for x in regional_data['YEAR_2023']],
                        textposition='outside',
                        hovertemplate='<b>Region:</b> %{x}<br><b>Duration:</b> %{y:.1f} days<extra></extra>'
                    )
                ])

                fig.update_layout(
                    title=dict(
                        text="🗺️ Global Visitor Journey Lengths by Origin",
                        font=dict(size=16, color='#4ECDC4', family="Georgia"),
                        x=0.5
                    ),
                    xaxis_title="Region",
                    yaxis_title="Duration (Days)",
                    plot_bgcolor='rgba(248,249,250,0.8)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='#333'),
                    height=400,
                    showlegend=False,
                    xaxis_tickangle=45
                )

                st.plotly_chart(fig, use_container_width=True)

                # Enhanced duration insights with storytelling
                longest_stay = regional_data.loc[regional_data['YEAR_2023'].idxmax()]
                shortest_stay = regional_data.loc[regional_data['YEAR_2023'].idxmin()]
                global_avg = regional_data['YEAR_2023'].mean()

                st.markdown("#### ⏰ Journey Duration Stories")

                # Duration interpretations
                duration_stories = {
                    'longest': '🏆 Deep cultural immersion seekers',
                    'shortest': '⚡ Quick experience explorers',
                    'average': '🌟 Balanced journey planners'
                }

                st.markdown(f"""
                <div style="background: rgba(78,205,196,0.1); padding: 1.5rem; border-radius: 15px; margin: 1rem 0; border-left: 5px solid #4ECDC4;">
                    <h4 style="color: #4ECDC4; margin-bottom: 1rem;">🌍 The Duration Spectrum</h4>
                    <div style="display: grid; grid-template-columns: 1fr; gap: 1rem;">
                        <div style="background: rgba(255,255,255,0.7); padding: 1rem; border-radius: 10px;">
                            <strong style="color: #4ECDC4;">🏆 Marathon Explorers:</strong> {longest_stay['NATIONALITY_REGION']}<br>
                            <span style="font-size: 1.1rem; color: #333;">{longest_stay['YEAR_2023']:.1f} days</span> -
                            <span style="color: #666; font-style: italic;">Deep cultural immersion</span>
                        </div>
                        <div style="background: rgba(255,255,255,0.7); padding: 1rem; border-radius: 10px;">
                            <strong style="color: #4ECDC4;">⚡ Sprint Visitors:</strong> {shortest_stay['NATIONALITY_REGION']}<br>
                            <span style="font-size: 1.1rem; color: #333;">{shortest_stay['YEAR_2023']:.1f} days</span> -
                            <span style="color: #666; font-style: italic;">Quick taste of India</span>
                        </div>
                        <div style="background: rgba(255,255,255,0.7); padding: 1rem; border-radius: 10px; text-align: center;">
                            <strong style="color: #4ECDC4;">🌟 Global Sweet Spot:</strong><br>
                            <span style="font-size: 1.3rem; color: #333;">{global_avg:.1f} days</span><br>
                            <small style="color: #666;">Perfect balance of exploration & practicality</small>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.warning("Could not find regional duration data")
        else:
            st.info("No duration of stay data available")

    # Enhanced concluding insights section
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2.5rem; border-radius: 20px; margin: 3rem 0; color: white; text-align: center;">
        <h3 style="margin-bottom: 1.5rem; font-size: 1.8rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">🌟 The Future of Visitor Experience</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; margin: 2rem 0;">
            <div style="background: rgba(255,255,255,0.15); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h4 style="margin: 0 0 0.5rem 0; color: #FFD700;">🎯 Prime Demographics</h4>
                <h3 style="margin: 0.5rem 0; font-size: 2rem;">25-44</h3>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">Peak travel years combining career success with adventure spirit</p>
            </div>
            <div style="background: rgba(255,255,255,0.15); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h4 style="margin: 0 0 0.5rem 0; color: #4ECDC4;">⏰ Journey Sweet Spot</h4>
                <h3 style="margin: 0.5rem 0; font-size: 2rem;">21.1</h3>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">Days - Perfect balance of exploration and practicality</p>
            </div>
            <div style="background: rgba(255,255,255,0.15); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h4 style="margin: 0 0 0.5rem 0; color: #96CEB4;">💝 Loyalty Factor</h4>
                <h3 style="margin: 0.5rem 0; font-size: 2rem;">60%</h3>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">Return visitors - India creates lasting impressions</p>
            </div>
        </div>
        <p style="margin: 2rem 0 0 0; font-size: 1.1rem; line-height: 1.6; opacity: 0.9;">
            Understanding our visitors isn't just about numbers—it's about crafting experiences that resonate across generations,
            cultures, and travel styles. Every data point represents a human story, and every trend guides us toward creating
            more meaningful connections between India and the world.
        </p>
    </div>
    """, unsafe_allow_html=True)
