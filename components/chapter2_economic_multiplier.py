import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from styles.css_styles import apply_economic_chapter_background

def show_economic_multiplier(tourism_gdp_df, tourism_employment_df, fee_earnings_df, india_world_share_df):
    """Chapter 2: The Economic Multiplier Story - Tourism's Economic Impact"""

    # Apply economic-specific background styling
    apply_economic_chapter_background()

    # Chapter Header
    st.markdown("""
    <div style="background: linear-gradient(135deg, #2E8B57, #3CB371, #90EE90); padding: 3rem; border-radius: 25px; margin: 2rem 0; text-align: center; box-shadow: 0 15px 35px rgba(46,139,87,0.3);">
        <h1 style="color: white; font-size: 3rem; margin-bottom: 1rem; text-shadow: 3px 3px 6px rgba(0,0,0,0.4); font-family: 'Georgia', serif;">
            💰 Chapter 2: The Economic Multiplier Story
        </h1>
        <p style="color: rgba(255,255,255,0.95); font-size: 1.3rem; margin: 0; line-height: 1.6; text-shadow: 1px 1px 3px rgba(0,0,0,0.3);">
            How Every ₹1 in Tourism Becomes ₹1.92 - The Magic of Economic Multiplication
        </p>
    </div>
    """, unsafe_allow_html=True)

    # The Multiplier Story Introduction
    st.markdown("""
    <div style="background: rgba(46,139,87,0.05); padding: 2.5rem; border-radius: 20px; margin: 2rem 0; border-left: 6px solid #2E8B57;">
        <h3 style="color: #2E8B57; margin-bottom: 1.5rem; font-family: 'Georgia', serif;">🎯 The ₹1 → ₹1.92 Magic Formula</h3>
        <p style="color: #555; line-height: 1.8; font-size: 1.1rem; margin: 0;">
            Tourism isn't just about visitors and monuments - it's about <strong>economic multiplication</strong>.
            When a tourist spends ₹1 directly on tourism, it generates an additional ₹0.92 through indirect and induced effects,
            creating a <strong>total economic impact of ₹1.92</strong>. This multiplier effect ripples through hotels, restaurants,
            transportation, handicrafts, and countless other sectors, making tourism one of India's most powerful economic engines.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # GDP Contribution Analysis
    if not tourism_gdp_df.empty:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #2E8B57, #3CB371, #90EE90); padding: 1rem; border-radius: 25px; margin: 1.5rem 0; text-align: center; box-shadow: 0 15px 35px rgba(46,139,87,0.3); position: relative; overflow: hidden;">
            <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.3;"></div>
            <div style="position: relative; z-index: 1;">
                <h1 style="color: white; font-size: 1.6rem; margin-bottom: 1rem; text-shadow: 3px 3px 6px rgba(0,0,0,0.4); font-family: 'Georgia', serif;">
                    📈 Tourism's GDP Contribution: The Growth Engine
                </h1>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Key metrics from latest year
        latest_year = tourism_gdp_df['YEAR'].iloc[-1]
        latest_data = tourism_gdp_df.iloc[-1]

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            direct_gdp = latest_data['DIRECT_CONTRIBUTION_GDP_PERCENT']
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #2E8B57, #3CB371); padding: 1.5rem; border-radius: 12px; text-align: center; color: white; margin-bottom: 1rem;">
                <h3 style="margin: 0; font-size: 2rem;">{direct_gdp:.1f}%</h3>
                <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.9;">Direct GDP Share</p>
                <p style="margin: 0; font-size: 0.8rem; background: rgba(255,255,255,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; display: inline-block;">
                    {latest_year}
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            total_gdp = latest_data['TOTAL_CONTRIBUTION_GDP_PERCENT']
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #3CB371, #90EE90); padding: 1.5rem; border-radius: 12px; text-align: center; color: white; margin-bottom: 1rem;">
                <h3 style="margin: 0; font-size: 2rem;">{total_gdp:.1f}%</h3>
                <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.9;">Total GDP Impact</p>
                <p style="margin: 0; font-size: 0.8rem; background: rgba(255,255,255,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; display: inline-block;">
                    With Multiplier
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            multiplier = latest_data['GVA_MULTIPLIER']
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #90EE90, #98FB98); padding: 1.5rem; border-radius: 12px; text-align: center; color: #2E8B57; margin-bottom: 1rem;">
                <h3 style="margin: 0; font-size: 2rem;">{multiplier:.2f}x</h3>
                <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.9;">Economic Multiplier</p>
                <p style="margin: 0; font-size: 0.8rem; background: rgba(46,139,87,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; display: inline-block;">
                    Magic Formula
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col4:
            tourism_gdp_crore = latest_data['TOURISM_DIRECT_GDP_CRORE']
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #98FB98, #F0FFF0); padding: 1.5rem; border-radius: 12px; text-align: center; color: #2E8B57; margin-bottom: 1rem;">
                <h3 style="margin: 0; font-size: 1.5rem;">₹{tourism_gdp_crore:,.0f}</h3>
                <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.9;">Crores Direct GDP</p>
                <p style="margin: 0; font-size: 0.8rem; background: rgba(46,139,87,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; display: inline-block;">
                    {latest_year}
                </p>
            </div>
            """, unsafe_allow_html=True)

        # GDP Trend Analysis
        col1, col2 = st.columns(2)

        with col1:
            # Direct vs Total GDP Contribution
            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=tourism_gdp_df['YEAR'],
                y=tourism_gdp_df['DIRECT_CONTRIBUTION_GDP_PERCENT'],
                mode='lines+markers',
                name='Direct Contribution',
                line=dict(color='#2E8B57', width=4),
                marker=dict(size=10, color='#2E8B57'),
                hovertemplate='<b>Direct GDP:</b> %{y:.2f}%<br><b>Year:</b> %{x}<extra></extra>'
            ))

            fig.add_trace(go.Scatter(
                x=tourism_gdp_df['YEAR'],
                y=tourism_gdp_df['TOTAL_CONTRIBUTION_GDP_PERCENT'],
                mode='lines+markers',
                name='Total Impact (with Multiplier)',
                line=dict(color='#90EE90', width=4),
                marker=dict(size=10, color='#90EE90'),
                hovertemplate='<b>Total GDP:</b> %{y:.2f}%<br><b>Year:</b> %{x}<extra></extra>'
            ))

            fig.update_layout(
                title=dict(
                    text="📊 Tourism's GDP Contribution: Direct vs Total Impact",
                    font=dict(size=16, color='#2E8B57'),
                    x=0.5,
                    xanchor='center'
                ),
                xaxis=dict(
                    title=dict(text="Year", font=dict(color='black')),
                    tickfont=dict(color='black')
                ),
                yaxis=dict(
                    title=dict(text="GDP Contribution (%)", font=dict(color='black')),
                    tickfont=dict(color='black')
                ),
                plot_bgcolor='rgba(248,249,250,0.8)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#333'),
                height=400,
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(color='black'))
            )

            st.plotly_chart(fig, use_container_width=True)

        with col2:
            # GDP Value in Crores - Area Chart with Gradient
            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=tourism_gdp_df['YEAR'],
                y=tourism_gdp_df['TOURISM_DIRECT_GDP_CRORE'],
                mode='lines+markers',
                name='Direct GDP (₹ Crores)',
                line=dict(color='#2E8B57', width=4),
                marker=dict(size=12, color='#3CB371', line=dict(width=2, color='white')),
                fill='tozeroy',
                fillcolor='rgba(46,139,87,0.3)',
                hovertemplate='<b>Direct GDP:</b> ₹%{y:,.0f} crores<br><b>Year:</b> %{x}<extra></extra>'
            ))

            fig.update_layout(
                title=dict(
                    text="💰 Tourism's Direct GDP Growth Journey",
                    font=dict(size=16, color='#2E8B57'),
                    x=0.5,
                    xanchor='center'
                ),
                xaxis=dict(
                    title=dict(text="Year", font=dict(color='black')),
                    tickfont=dict(color='black')
                ),
                yaxis=dict(
                    title=dict(text="GDP Value (₹ Crores)", font=dict(color='black')),
                    tickfont=dict(color='black')
                ),
                plot_bgcolor='rgba(248,249,250,0.8)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#333'),
                height=400,
                showlegend=False
            )

            st.plotly_chart(fig, use_container_width=True)

    # Employment Impact
    if not tourism_employment_df.empty:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #2E8B57, #3CB371, #90EE90); padding: 1rem; border-radius: 25px; margin: 1.5rem 0; text-align: center; box-shadow: 0 15px 35px rgba(46,139,87,0.3); position: relative; overflow: hidden;">
            <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.3;"></div>
            <div style="position: relative; z-index: 1;">
                <h1 style="color: white; font-size: 1.6rem; text-shadow: 3px 3px 6px rgba(0,0,0,0.4); font-family: 'Georgia', serif;">
                    👥 Employment Engine: Millions of Livelihoods
                </h1>
                <p style="color: rgba(255,255,255,0.95); font-size: 1.0rem; margin: 0; line-height: 1.6; text-shadow: 1px 1px 3px rgba(0,0,0,0.3);">
                    Tourism doesn't just generate revenue - it creates jobs across the entire economy
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

        latest_emp_data = tourism_employment_df.iloc[-1]

        col1, col2, col3 = st.columns(3)

        with col1:
            direct_emp = latest_emp_data['TOURISM_CHARACTERISTIC_INDUSTRIES_MILLION']
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #2E8B57, #3CB371); padding: 2rem; border-radius: 15px; text-align: center; color: white;">
                <h3 style="margin: 0; font-size: 2.5rem;">{direct_emp:.1f}M</h3>
                <p style="margin: 0.5rem 0; font-size: 1rem; opacity: 0.9;">Direct Employment</p>
                <small style="opacity: 0.8;">Tourism Industries</small>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            total_emp = latest_emp_data['DIRECT_INDIRECT_EMPLOYMENT_MILLION']
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #3CB371, #90EE90); padding: 2rem; border-radius: 15px; text-align: center; color: white;">
                <h3 style="margin: 0; font-size: 2.5rem;">{total_emp:.1f}M</h3>
                <p style="margin: 0.5rem 0; font-size: 1rem; opacity: 0.9;">Total Employment</p>
                <small style="opacity: 0.8;">Direct + Indirect</small>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            emp_share = latest_emp_data['DIRECT_INDIRECT_SHARE_PERCENT']
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #90EE90, #98FB98); padding: 2rem; border-radius: 15px; text-align: center; color: #2E8B57;">
                <h3 style="margin: 0; font-size: 2.5rem;">{emp_share:.1f}%</h3>
                <p style="margin: 0.5rem 0; font-size: 1rem; opacity: 0.9;">of Total Employment</p>
                <small style="opacity: 0.8;">National Share</small>
            </div>
            """, unsafe_allow_html=True)

        # Employment Trend - Stacked Area Chart
        col1, col2 = st.columns(2)

        with col1:
            # Employment Growth - Waterfall Chart Style
            fig = go.Figure()

            # Calculate indirect employment
            indirect_employment = (tourism_employment_df['DIRECT_INDIRECT_EMPLOYMENT_MILLION'] -
                                 tourism_employment_df['TOURISM_CHARACTERISTIC_INDUSTRIES_MILLION'])

            fig.add_trace(go.Scatter(
                x=tourism_employment_df['YEAR'],
                y=tourism_employment_df['TOURISM_CHARACTERISTIC_INDUSTRIES_MILLION'],
                mode='lines+markers',
                name='Direct Employment',
                line=dict(color='#2E8B57', width=3),
                marker=dict(size=10, color='#2E8B57'),
                fill='tozeroy',
                fillcolor='rgba(46,139,87,0.4)',
                hovertemplate='<b>Direct:</b> %{y:.1f}M jobs<br><b>Year:</b> %{x}<extra></extra>'
            ))

            fig.add_trace(go.Scatter(
                x=tourism_employment_df['YEAR'],
                y=indirect_employment,
                mode='lines+markers',
                name='Indirect Employment',
                line=dict(color='#90EE90', width=3),
                marker=dict(size=10, color='#90EE90'),
                fill='tonexty',
                fillcolor='rgba(144,238,144,0.4)',
                hovertemplate='<b>Indirect:</b> %{y:.1f}M jobs<br><b>Year:</b> %{x}<extra></extra>'
            ))

            fig.update_layout(
                title=dict(
                    text="👥 Employment Breakdown: Direct vs Indirect",
                    font=dict(size=16, color='#2E8B57'),
                    x=0.5,
                    xanchor='center'
                ),
                xaxis=dict(
                    title=dict(text="Year", font=dict(color='black')),
                    tickfont=dict(color='black')
                ),
                yaxis=dict(
                    title=dict(text="Employment (Millions)", font=dict(color='black')),
                    tickfont=dict(color='black')
                ),
                plot_bgcolor='rgba(248,249,250,0.8)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#333'),
                height=400,
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(color='black'))
            )

            st.plotly_chart(fig, use_container_width=True)

        with col2:
            # Employment Share - Donut Chart
            latest_emp_data = tourism_employment_df.iloc[-1]
            direct_emp = latest_emp_data['TOURISM_CHARACTERISTIC_INDUSTRIES_MILLION']
            total_emp = latest_emp_data['DIRECT_INDIRECT_EMPLOYMENT_MILLION']
            indirect_emp = total_emp - direct_emp

            fig = go.Figure(data=[go.Pie(
                labels=['Direct Employment', 'Indirect Employment'],
                values=[direct_emp, indirect_emp],
                hole=0.6,
                marker_colors=['#2E8B57', '#90EE90'],
                textinfo='label+percent',
                textposition='outside',
                hovertemplate='<b>%{label}</b><br>%{value:.1f}M jobs<br>%{percent}<extra></extra>'
            )])

            fig.update_layout(
                title=dict(
                    text=f"🎯 Employment Distribution ({latest_emp_data['YEAR']})",
                    font=dict(size=16, color='#2E8B57'),
                    x=0.5,
                    xanchor='center'
                ),
                plot_bgcolor='rgba(248,249,250,0.8)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#333'),
                height=400,
                showlegend=True,
                legend=dict(font=dict(color='black')),
                annotations=[dict(text=f'{total_emp:.1f}M<br>Total Jobs', x=0.5, y=0.5,
                                font_size=20, showarrow=False, font_color='#2E8B57')]
            )

            st.plotly_chart(fig, use_container_width=True)

    # Revenue and Global Position
    if not fee_earnings_df.empty and not india_world_share_df.empty:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #2E8B57, #3CB371, #90EE90); padding: 1rem; border-radius: 25px; margin: 1rem 0; text-align: center; box-shadow: 0 15px 35px rgba(46,139,87,0.3); position: relative; overflow: hidden;">
            <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.3;"></div>
            <div style="position: relative; z-index: 1;">
                <h1 style="color: white; font-size: 1.6rem; margin-bottom: 1rem; text-shadow: 3px 3px 6px rgba(0,0,0,0.4); font-family: 'Georgia', serif;">
                    🌍 Global Tourism Revenue & India's Rising Rank
                </h1>
            </div>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            # Revenue Growth - Candlestick Style with Growth Indicators
            fig = go.Figure()

            # Calculate year-over-year growth
            revenue_growth = fee_earnings_df['FEE_CRORE'].pct_change() * 100

            # Create bar chart with color coding for growth
            colors = ['#FF6B6B' if x < 0 else '#2E8B57' for x in revenue_growth]

            fig.add_trace(go.Bar(
                x=fee_earnings_df['YEAR'],
                y=fee_earnings_df['FEE_CRORE'],
                name='Revenue (₹ Crores)',
                marker_color=colors,
                text=[f"₹{x:,.0f}" for x in fee_earnings_df['FEE_CRORE']],
                textposition='outside',
                hovertemplate='<b>Revenue:</b> ₹%{y:,.0f} crores<br><b>Year:</b> %{x}<br><b>Growth:</b> %{customdata:.1f}%<extra></extra>',
                customdata=revenue_growth.fillna(0)
            ))

            fig.update_layout(
                title=dict(
                    text="💰 Tourism Revenue: Growth Trajectory",
                    font=dict(size=16, color='#2E8B57'),
                    x=0.5
                ),
                xaxis=dict(
                    title=dict(text="Year", font=dict(color='black')),
                    tickfont=dict(color='black')
                ),
                yaxis=dict(
                    title=dict(text="Revenue (₹ Crores)", font=dict(color='black')),
                    tickfont=dict(color='black')
                ),
                plot_bgcolor='rgba(248,249,250,0.8)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#333'),
                height=400,
                showlegend=False
            )

            st.plotly_chart(fig, use_container_width=True)

        with col2:
            # Global Position Trend - Dual Axis Chart
            fig = go.Figure()

            # Convert rank to numeric (remove 'th', 'st', 'nd', 'rd')
            ranks = india_world_share_df['INDIA_WORLD_RANK'].str.extract(r'(\d+)')[0].astype(int)
            latest_rank = ranks.iloc[-1]
            latest_share = india_world_share_df['INDIA_WORLD_SHARE_PERCENT'].iloc[-1]

            # Add ranking trend (inverted so lower rank = higher on chart)
            fig.add_trace(go.Scatter(
                x=india_world_share_df['YEAR'],
                y=51 - ranks,  # Invert ranking so improvement goes up
                mode='lines+markers',
                name='Global Ranking (Inverted)',
                line=dict(color='#FF6B6B', width=4),
                marker=dict(size=12, color='#FF6B6B',
                           line=dict(width=2, color='white')),
                yaxis='y',
                hovertemplate='<b>Rank:</b> #%{customdata}<br><b>Year:</b> %{x}<extra></extra>',
                customdata=ranks
            ))

            # Add market share trend on secondary axis
            fig.add_trace(go.Scatter(
                x=india_world_share_df['YEAR'],
                y=india_world_share_df['INDIA_WORLD_SHARE_PERCENT'],
                mode='lines+markers',
                name='Market Share (%)',
                line=dict(color='#2E8B57', width=4),
                marker=dict(size=12, color='#3CB371',
                           line=dict(width=2, color='white')),
                yaxis='y2',
                fill='tozeroy',
                fillcolor='rgba(46,139,87,0.2)',
                hovertemplate='<b>Market Share:</b> %{y:.2f}%<br><b>Year:</b> %{x}<extra></extra>'
            ))

            # Update layout with dual y-axes
            fig.update_layout(
                title=dict(
                    text="🌍 India's Global Tourism Journey",
                    font=dict(size=16, color='#2E8B57'),
                    x=0.5
                ),
                xaxis=dict(
                    title=dict(text="Year", font=dict(color='black')),
                    tickfont=dict(color='black')
                ),
                yaxis=dict(
                    title=dict(text="Ranking Performance", font=dict(color='#FF6B6B')),
                    tickfont=dict(color='black'),
                    side='left',
                    tickvals=[51-50, 51-40, 51-30, 51-20, 51-10, 51-1],
                    ticktext=['50th', '40th', '30th', '20th', '10th', '1st']
                ),
                yaxis2=dict(
                    title=dict(text="Market Share (%)", font=dict(color='#2E8B57')),
                    tickfont=dict(color='black'),
                    overlaying='y',
                    side='right'
                ),
                plot_bgcolor='rgba(248,249,250,0.8)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='black'),
                height=400,
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1,
                    font=dict(color='black')
                ),
            )

            st.plotly_chart(fig, use_container_width=True)

    # Add Multiplier Effect Visualization
    if not tourism_gdp_df.empty:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #2E8B57, #3CB371, #90EE90); padding: 1rem; border-radius: 25px; margin: 1rem 0; text-align: center; box-shadow: 0 15px 35px rgba(46,139,87,0.3); position: relative; overflow: hidden;">
            <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.3;"></div>
            <div style="position: relative; z-index: 1;">
                <h1 style="color: white; font-size: 1.6rem; margin-bottom: 1rem; text-shadow: 3px 3px 6px rgba(0,0,0,0.4); font-family: 'Georgia', serif;">
                    🔄 The Economic Multiplier Effect in Action
                </h1>
            </div>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            # Multiplier Effect - Funnel Chart
            latest_data = tourism_gdp_df.iloc[-1]
            direct_gdp = latest_data['TOURISM_DIRECT_GDP_CRORE']
            multiplier = latest_data['GVA_MULTIPLIER']
            total_impact = direct_gdp * multiplier

            fig = go.Figure(go.Funnel(
                y = ["💰 Direct Tourism Spending", "🔄 Multiplier Effect", "📈 Total Economic Impact"],
                x = [direct_gdp, direct_gdp * 0.92, total_impact],
                textinfo = "value+percent initial",
                texttemplate = "₹%{value:,.0f} Cr<br>%{percentInitial}",
                textfont = {"color": "white", "size": 12},
                outsidetextfont = {"color": "black", "size": 12},
                marker = {"color": ["#2E8B57", "#3CB371", "#90EE90"],
                         "line": {"width": [2, 2, 2], "color": ["white", "white", "white"]}},
                connector = {"line": {"color": "rgb(63, 63, 63)", "dash": "dot", "width": 3}},
                hovertemplate='<b>%{label}</b><br>₹%{value:,.0f} crores<extra></extra>'
            ))

            fig.update_layout(
                title=dict(
                    text="💫 The ₹1 → ₹1.92 Magic Formula",
                    font=dict(size=16, color='#2E8B57'),
                    x=0.5
                ),
                yaxis=dict(
                    tickfont=dict(color='black', size=12),
                    showticklabels=True
                ),
                plot_bgcolor='rgba(248,249,250,0.8)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='black'),
                height=400
            )

            st.plotly_chart(fig, use_container_width=True)

        with col2:
            # Multiplier Trend Over Time - Radar Chart
            fig = go.Figure()

            # Create a radar chart showing different economic indicators
            categories = ['GDP Impact', 'Employment', 'Revenue Growth', 'Global Position', 'Multiplier Effect']

            # Normalize values for radar chart (0-100 scale)
            latest_gdp_pct = latest_data['TOTAL_CONTRIBUTION_GDP_PERCENT']
            latest_emp_data = tourism_employment_df.iloc[-1]
            latest_emp_pct = latest_emp_data['DIRECT_INDIRECT_SHARE_PERCENT']
            latest_revenue = fee_earnings_df.iloc[-1]['FEE_CRORE']
            revenue_growth = ((latest_revenue / fee_earnings_df.iloc[0]['FEE_CRORE']) - 1) * 100

            values = [
                min(latest_gdp_pct * 10, 100),  # GDP impact scaled
                min(latest_emp_pct, 100),       # Employment share
                min(revenue_growth / 10, 100),  # Revenue growth scaled
                max(100 - latest_rank * 2, 0),  # Global position (inverted)
                min(multiplier * 50, 100)       # Multiplier scaled
            ]

            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=categories,
                fill='toself',
                fillcolor='rgba(46,139,87,0.3)',
                line=dict(color='#2E8B57', width=3),
                marker=dict(size=8, color='#3CB371'),
                name='Tourism Impact Score'
            ))

            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 100],
                        tickfont=dict(size=10, color='black'),
                        gridcolor='rgba(46,139,87,0.3)'
                    ),
                    angularaxis=dict(
                        tickfont=dict(size=12, color='black')
                    )
                ),
                title=dict(
                    text="🎯 Tourism Impact Scorecard",
                    font=dict(size=16, color='#2E8B57'),
                    x=0.5
                ),
                plot_bgcolor='rgba(248,249,250,0.8)',
                paper_bgcolor='rgba(0,0,0,0)',
                height=400,
                showlegend=False
            )

            st.plotly_chart(fig, use_container_width=True)

    # Economic Impact Summary
    st.markdown("""
    <div style="background: linear-gradient(135deg, #2E8B57, #3CB371); padding: 2.5rem; border-radius: 20px; margin: 3rem 0; color: white; text-align: center;">
        <h3 style="margin-bottom: 1.5rem; font-size: 1.8rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
            🎯 The Economic Multiplier in Action
        </h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; margin: 2rem 0;">
            <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h4 style="margin: 0 0 0.5rem 0; color: #FFD700;">💰 Revenue Impact</h4>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">₹2.3+ Lakh Crores (2023)</p>
            </div>
            <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h4 style="margin: 0 0 0.5rem 0; color: #98FB98;">👥 Employment</h4>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">76+ Million Jobs</p>
            </div>
            <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h4 style="margin: 0 0 0.5rem 0; color: #87CEEB;">🌍 Global Rank</h4>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">13th Position Worldwide</p>
            </div>
        </div>
        <p style="margin: 2rem 0 0 0; font-size: 1.1rem; line-height: 1.6; opacity: 0.9;">
            The <strong>₹1 → ₹1.92 multiplier effect</strong> demonstrates tourism's power as an economic catalyst,
            creating ripple effects across industries and transforming India into a global tourism powerhouse.
        </p>
    </div>
    """, unsafe_allow_html=True)
