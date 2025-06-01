import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show_regional_tapestry(state_total_df, state_domestic_df, state_foreign_df):
    """Chapter 4: The Regional Tapestry - State-wise Tourism Analysis"""

    # Chapter Header
    st.markdown("""
    <div style="background: linear-gradient(135deg, #FF6347, #FF7F50, #FFA07A); padding: 3rem; border-radius: 25px; margin: 2rem 0; text-align: center; box-shadow: 0 15px 35px rgba(255,99,71,0.3);">
        <h1 style="color: white; font-size: 2.9rem; margin-bottom: 1rem; text-shadow: 3px 3px 6px rgba(0,0,0,0.4); font-family: 'Georgia', serif;">
            🗺️ Chapter 4: The Regional Tapestry
        </h1>
        <p style="color: rgba(255,255,255,0.95); font-size: 1.3rem; margin: 0; line-height: 1.6; text-shadow: 1px 1px 3px rgba(0,0,0,0.3);">
            From Himalayan Heights to Coastal Delights - India's Diverse Tourism Landscape
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Regional Introduction
    st.markdown("""
    <div style="background: white; padding: 2.5rem; border-radius: 20px; margin: 2rem 0; border-left: 6px solid #FF6347;">
        <h3 style="color: #FF6347; margin-bottom: 1.5rem; font-family: 'Georgia', serif;">🌈 India's Cultural Kaleidoscope</h3>
        <p style="color: #555; line-height: 1.8; font-size: 1.1rem; margin: 0;">
            India's tourism isn't just about numbers - it's about the <strong>incredible diversity</strong> across regions.
            From the <strong>snow-capped Himalayas of the North</strong> to the <strong>tropical backwaters of the South</strong>,
            from the <strong>desert kingdoms of the West</strong> to the <strong>tribal cultures of the Northeast</strong>,
            each region offers unique experiences. With countless festivals and dance forms,
            India presents a living museum of human culture and tradition.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Regional Tourism Distribution
    if not state_total_df.empty:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #FF6347, #FF7F50, #FFA07A); border-radius: 15px; margin: 1rem; padding: 2rem;">
            <h4 style="color: white; text-align: center; font-family: 'Georgia', serif;">
                🎯 Regional Tourism Distribution: Where India Shines
            </h4>
        </div>
        """, unsafe_allow_html=True)

        # Create a copy of the dataframe to avoid modifying the original
        state_df_copy = state_total_df.copy()

        # Remap regions to exactly 5 regions: EAST, WEST, NORTH, SOUTH, CENTER
        def remap_regions(region):
            if region == 'EAST':
                return 'EAST'
            elif region == 'NORTH':
                return 'NORTH'
            elif region == 'NORTH EAST':
                return 'EAST'  # Merge Northeast with East
            elif region == 'SOUTH':
                return 'SOUTH'
            elif region == 'WEST & CENTRAL':
                return 'CENTER'  # Split West & Central into Center
            else:
                return 'CENTER'  # Default fallback

        # Apply the remapping
        state_df_copy['NEW_REGION'] = state_df_copy['REGION'].apply(remap_regions)

        # Separate West states from Central states in WEST & CENTRAL
        west_states = ['Goa', 'Gujarat', 'Maharashtra', 'Dadra & Nagar Haveli']
        central_states = ['Chhattisgarh', 'Madhya Pradesh']

        # Update mapping for West states
        state_df_copy.loc[state_df_copy['STATE'].isin(west_states), 'NEW_REGION'] = 'WEST'
        state_df_copy.loc[state_df_copy['STATE'].isin(central_states), 'NEW_REGION'] = 'CENTER'

        # Calculate regional totals for latest year using new regions (apply correction: divide by 10, convert to millions)
        regional_totals = state_df_copy.groupby('NEW_REGION')['YEAR_2023'].sum().reset_index()
        regional_totals = regional_totals.rename(columns={'NEW_REGION': 'REGION'})
        regional_totals['YEAR_2023'] = regional_totals['YEAR_2023'] / 10 / 1_000_000  # Apply correction and convert to millions
        regional_totals = regional_totals.sort_values('YEAR_2023', ascending=False)

        col1, col2 = st.columns([1, 2])

        with col1:
            # Regional insights - compact header
            st.markdown("""
            <div style="background: white; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-bottom: 0.3rem">
                <h6 style="color: #FF6347; text-align: center; font-size: 1.8rem;">🏆 Regional Champions</h6>
            </div>
            """, unsafe_allow_html=True)

            # Darker, more intense colors for better contrast
            colors = ['#DC2626', '#B91C1C', '#EA580C', '#D97706', '#059669']

            for i, (_, row) in enumerate(regional_totals.iterrows()):
                region = row['REGION']
                visitors = row['YEAR_2023']
                percentage = (visitors / regional_totals['YEAR_2023'].sum()) * 100

                # Regional descriptions for new 5-region structure
                descriptions = {
                    'SOUTH': '🌴 Temples & Tech Hubs',
                    'WEST': '🏖️ Beaches & Business',
                    'NORTH': '🏔️ Heritage & Hills',
                    'EAST': '🎭 Culture & Tribes',
                    'CENTER': '🏛️ Heart of India'
                }

                desc = descriptions.get(region, '🌟 Unique Experiences')

                st.markdown(f"""
                <div style="background: {colors[i]}; padding: 0.5rem; border-radius: 6px; margin: 0.25rem 0; color: white; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-weight: bold; font-size: 1.2rem;">{region}</span>
                        <span style="font-size: 0.85rem; font-weight: bold;">{visitors:.1f}M</span>
                    </div>
                    <div style="font-size: 0.85rem; margin-top: 0.15rem; opacity: 0.95;">{desc}</div>
                    <div style="background: rgba(255,255,255,0.4); height: 3px; border-radius: 2px; margin-top: 0.3rem;">
                        <div style="background: white; height: 100%; width: {percentage}%; border-radius: 2px;"></div>
                    </div>
                    <small style="opacity: 0.95; font-size: 1rem;">{percentage:.1f}% of total</small>
                </div>
                """, unsafe_allow_html=True)

        with col2:
            # Regional distribution donut chart
            fig = go.Figure(data=[
                go.Pie(
                    labels=regional_totals['REGION'],
                    values=regional_totals['YEAR_2023'],
                    hole=0.6,
                    marker_colors=colors[:len(regional_totals)],
                    textinfo='label+percent',
                    textposition='outside',
                    hovertemplate='<b>%{label}</b><br>Visitors: %{value:.1f}M<br>Share: %{percent}<extra></extra>',
                    textfont_size=12,
                    marker=dict(
                        line=dict(color='white', width=3)
                    )
                )
            ])

            # Add center text
            fig.add_annotation(
                text=f"<b>{regional_totals['YEAR_2023'].sum():.1f}M</b><br><span style='font-size:14px'>Total Visitors</span>",
                x=0.5, y=0.5,
                font_size=20,
                font_color='#FF6347',
                showarrow=False
            )

            fig.update_layout(
                title=dict(
                    text="🌟 Regional Tourism Distribution (2023)",
                    font=dict(size=22, color='#FF6347'),
                    x=0.15
                ),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#333'),
                height=650,
                showlegend=True,
                legend=dict(
                    orientation="v",
                    yanchor="middle",
                    y=0.5,
                    xanchor="left",
                    x=1.05,
                    font=dict(color='black', size=12)
                )
            )

            st.plotly_chart(fig, use_container_width=True)

    # Top Performing States
    if not state_total_df.empty:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #FF6347, #FF7F50, #FFA07A); border-radius: 15px; margin: 1rem 0; padding: 2rem;">
            <h3 style="color: white; text-align: center; font-family: 'Georgia', serif;">
                🏆 State Champions: Tourism Powerhouses
            </h3>
        </div>
        """, unsafe_allow_html=True)

        # Top 10 states by total visitors with new regional mapping (apply correction: divide by 10, convert to millions)
        top_states = state_df_copy.nlargest(10, 'YEAR_2023').copy()
        top_states['REGION'] = top_states['NEW_REGION']  # Use the new regional mapping
        top_states['YEAR_2023'] = top_states['YEAR_2023'] / 10 / 1_000_000  # Apply correction and convert to millions

        col1, col2 = st.columns([1.2, 0.8])

        with col1:
            # Top states treemap with better contrast using discrete colors
            # Create discrete color mapping for better visibility
            discrete_colors = [
                '#8B0000',  # Dark red
                '#B22222',  # Fire brick
                '#DC143C',  # Crimson
                '#FF4500',  # Orange red
                '#FF6347',  # Tomato
                '#FF7F50',  # Coral
                '#FFA07A',  # Light salmon
                '#CD5C5C',  # Indian red
                '#F08080',  # Light coral
                '#FA8072'   # Salmon
            ]

            # Assign colors based on ranking (largest gets darkest)
            top_states_sorted = top_states.sort_values('YEAR_2023', ascending=False).reset_index(drop=True)
            color_mapping = {state: discrete_colors[i] for i, state in enumerate(top_states_sorted['STATE'])}
            colors = [color_mapping[state] for state in top_states['STATE']]

            fig = go.Figure(go.Treemap(
                labels=top_states['STATE'],
                values=top_states['YEAR_2023'],
                parents=[""] * len(top_states),
                textinfo="label+value",
                texttemplate="<b>%{label}</b><br>%{value:.1f}M",
                hovertemplate='<b>%{label}</b><br>Visitors: %{value:.1f}M<br>Region: %{customdata}<extra></extra>',
                customdata=top_states['REGION'],
                marker_colors=colors,  # Use marker_colors instead of marker dict
                marker_line_width=3,
                marker_line_color='white',
                textfont_size=11,
                textfont_color='white'
            ))

            fig.update_layout(
                title=dict(
                    text="🌟 Top 10 States by Visitors (2023)",
                    font=dict(size=16, color="#FDF2F1", family='Arial Black'),
                    x=0.25
                ),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='black',
                font=dict(color='#333', family='Arial'),
                height=500,
                margin=dict(t=50, l=25, r=25, b=25),
                # Add annotations for better text visibility on smaller segments
                annotations=[
                    dict(
                        text="<i>Hover over segments for detailed information</i>",
                        x=0.5, y=-0.1,
                        xref="paper", yref="paper",
                        showarrow=False,
                        font=dict(size=10, color='#666')
                    )
                ]
            )

            st.plotly_chart(fig, use_container_width=True)

        with col2:
            # Tourism Champions Story
            st.markdown("""
            <div style="background: white; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); height: 40px;margin-bottom: 0.5rem;">
                <h5 style="color: #FF6347; text-align: center; font-family: 'Georgia', serif;">📖 Insights</h5>
            </div>
            """, unsafe_allow_html=True)

            # Generate dynamic stories based on top states data
            if not top_states.empty:
                # Get top 3 states for detailed stories
                champion_states = top_states.head(3)

                # Create stories for each champion
                stories = []
                for i, (_, state_row) in enumerate(champion_states.iterrows()):
                    state_name = state_row['STATE']
                    visitors = state_row['YEAR_2023']
                    region = state_row['REGION']

                    # Define state-specific stories
                    state_stories = {
                        'Uttar Pradesh': {
                            'icon': '🕌',
                            'title': 'Heritage Capital',
                            'story': f'Home to the iconic Taj Mahal and Agra Fort, UP dominates with {visitors:.1f}M visitors. The Golden Triangle circuit makes it India\'s tourism crown jewel.',
                            'highlight': 'Taj Mahal alone attracts 6-8M visitors annually'
                        },
                        'Tamil Nadu': {
                            'icon': '🏛️',
                            'title': 'Temple Trail Leader',
                            'story': f'With {visitors:.1f}M visitors, TN showcases Dravidian architecture and cultural heritage. From Meenakshi Temple to Marina Beach, it\'s a complete experience.',
                            'highlight': 'Over 30,000 temples across the state'
                        },
                        'Karnataka': {
                            'icon': '🏰',
                            'title': 'Tech & Heritage Hub',
                            'story': f'Attracting {visitors:.1f}M visitors, Karnataka blends IT capital Bangalore with Mysore\'s royal heritage and Hampi\'s ruins.',
                            'highlight': 'Mysore Palace receives 6M+ visitors yearly'
                        },
                        'Andhra Pradesh': {
                            'icon': '⛰️',
                            'title': 'Spiritual Destination',
                            'story': f'With {visitors:.1f}M visitors, AP offers Tirupati\'s spiritual magnetism and Araku Valley\'s natural beauty.',
                            'highlight': 'Tirupati temple sees 50,000+ daily visitors'
                        },
                        'Rajasthan': {
                            'icon': '🏜️',
                            'title': 'Desert Kingdom',
                            'story': f'The royal state welcomes {visitors:.1f}M visitors to its palaces, forts, and desert experiences across Jaipur, Udaipur, and Jodhpur.',
                            'highlight': 'Hawa Mahal and City Palace are iconic draws'
                        }
                    }

                    # Get story or create default
                    story_data = state_stories.get(state_name, {
                        'icon': '🌟',
                        'title': f'{region} Gem',
                        'story': f'This {region.lower()} region champion attracts {visitors:.1f}M visitors with its unique cultural and natural offerings.',
                        'highlight': 'A rising star in Indian tourism'
                    })

                    stories.append(f"""
                    <div style="background: linear-gradient(135deg, #FF6347, #FF7F50); padding: 0.7rem; border-radius: 10px; margin: 0.2rem 0; color: white;">
                        <div style="display: flex; align-items: center; margin-bottom: 0.2rem;">
                            <span style="font-size: 1.3rem; margin-right: 0.5rem;">{story_data['icon']}</span>
                            <div>
                                <h6 style="margin: 0; font-size: 1rem; font-weight: bold;">{state_name}</h6>
                                <small style="opacity: 0.9; font-size: 0.8rem;">{story_data['title']}</small>
                            </div>
                        </div>
                        <p style="margin: 0.5rem 0; font-size: 0.85rem; line-height: 1.2;">{story_data['story']}</p>
                        <div style="background: rgba(255,255,255,0.2); padding: 0.1rem; border-radius: 5px; margin-top: 0.2rem;">
                            <small style="font-size: 0.65rem; font-style: italic;">💡 {story_data['highlight']}</small>
                        </div>
                    </div>
                    """)

                # Display stories
                for story in stories:
                    st.markdown(story, unsafe_allow_html=True)



    # Tourism trends line chart (moved below market analysis, full width)
    if 'YEAR_2017' in state_total_df.columns:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #FF6347, #FF7F50, #FFA07A); border-radius: 15px; margin: 1rem 0; padding: 2rem;">
            <h4 style="color: white; text-align: center; font-family: 'Georgia', serif;">
                📈 Tourism Growth Trends: Top 5 States Journey (2017-2023)
            </h4>
        </div>
        """, unsafe_allow_html=True)

        # Get top 5 states for trend analysis
        top_5_states = state_total_df.nlargest(5, 'YEAR_2023').copy()

        fig = go.Figure()

        # Create line for each top state
        years = ['YEAR_2017', 'YEAR_2018', 'YEAR_2019', 'YEAR_2020', 'YEAR_2021', 'YEAR_2022', 'YEAR_2023']
        year_labels = ['2017', '2018', '2019', '2020', '2021', '2022', '2023']

        colors_line = ['#FF6347', '#FF7F50', '#FFA07A', '#FFB6C1', '#FFC0CB']

        for i, (_, state_row) in enumerate(top_5_states.iterrows()):
            # Apply correction: divide by 10 and convert to millions, trim decimals
            values = [int(state_row[year] / 10 / 1_000_000) for year in years if year in state_row and pd.notna(state_row[year])]
            valid_years = [year_labels[j] for j, year in enumerate(years) if year in state_row and pd.notna(state_row[year])]

            fig.add_trace(go.Scatter(
                x=valid_years,
                y=values,
                mode='lines+markers',
                name=state_row['STATE'],
                line=dict(color=colors_line[i], width=3),
                marker=dict(size=8, color=colors_line[i]),
                hovertemplate='<b>%{fullData.name}</b><br>Year: %{x}<br>Visitors: %{y}M<extra></extra>'
            ))

        fig.update_layout(
            title=dict(
                text="📊 State-wise Tourism Evolution: The Champions' Journey",
                font=dict(size=18, color='#FF6347'),
                x=0.3
            ),
            xaxis_title="Year",
            yaxis_title="Visitors (Millions)",
            plot_bgcolor='rgba(248,249,250,0.8)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#333'),
            height=550,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="center",
                x=0.5
            ),
            hovermode='x unified'
        )

        st.plotly_chart(fig, use_container_width=True)



    # Calculate recovery metrics for storytelling
    if not state_total_df.empty and 'YEAR_2019' in state_total_df.columns and 'YEAR_2020' in state_total_df.columns:
        # Calculate recovery rate (2023 vs 2019 - pre-COVID)
        state_total_df['Recovery_Rate'] = ((state_total_df['YEAR_2023'] - state_total_df['YEAR_2019']) / state_total_df['YEAR_2019']) * 100
        state_total_df['Recovery_Rate'] = state_total_df['Recovery_Rate'].fillna(0)

        # Calculate pandemic impact (2020 vs 2019)
        state_total_df['Pandemic_Impact'] = ((state_total_df['YEAR_2020'] - state_total_df['YEAR_2019']) / state_total_df['YEAR_2019']) * 100
        state_total_df['Pandemic_Impact'] = state_total_df['Pandemic_Impact'].fillna(0)

        # Recovery Champions Section - Full Width for Better Visibility
        st.markdown("""
        <div style="background: linear-gradient(135deg, #FF6347, #FF7F50, #FFA07A); border-radius: 15px; margin: 1rem 0; padding: 2rem;">
            <h4 style="color: white; text-align: center; font-family: 'Georgia', serif;">
                🏆 Recovery Champions: States Leading the Tourism Comeback
            </h4>
        </div>
        """, unsafe_allow_html=True)

        # Recovery Champions vs Strugglers - Full width for better visibility
        top_recoverers = state_total_df.nlargest(12, 'Recovery_Rate')[['STATE', 'Recovery_Rate', 'YEAR_2019', 'YEAR_2023']].copy()
        top_recoverers['YEAR_2019_M'] = top_recoverers['YEAR_2019'] / 10 / 1_000_000  # Apply correction
        top_recoverers['YEAR_2023_M'] = top_recoverers['YEAR_2023'] / 10 / 1_000_000  # Apply correction

        # Create recovery champions chart
        fig = go.Figure()

        # Add bars for recovery rate
        fig.add_trace(go.Bar(
            x=top_recoverers['Recovery_Rate'],
            y=top_recoverers['STATE'],
            orientation='h',
            name='Recovery Rate (%)',
            marker=dict(
                color=top_recoverers['Recovery_Rate'],
                colorscale='RdYlGn',
                colorbar=dict(title="Recovery %"),
                line=dict(color='white', width=1)
            ),
            text=[f"+{x:.0f}%" if x > 0 else f"{x:.0f}%" for x in top_recoverers['Recovery_Rate']],
            textposition='outside',
            hovertemplate='<b>%{y}</b><br>Recovery: %{x:.1f}%<br>2019: %{customdata[0]:.1f}M<br>2023: %{customdata[1]:.1f}M<extra></extra>',
            customdata=top_recoverers[['YEAR_2019_M', 'YEAR_2023_M']].values
        ))

        fig.update_layout(
            title=dict(
                text="Recovery Performance: Growth vs Pre-Pandemic Levels",
                font=dict(size=18, color='#FF6347'),
                x=0.3
            ),
            xaxis_title="Recovery Rate vs 2019 (%)",
            yaxis_title="",
            plot_bgcolor='rgba(248,249,250,0.8)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='black'),
            height=600,
            showlegend=False,
            yaxis={'categoryorder':'total ascending'},
            margin=dict(l=150, r=100, t=80, b=60)
        )

        st.plotly_chart(fig, use_container_width=True)

        # COVID Impact and Recovery Analysis - Simplified View
        st.markdown("""
        <div style="background: linear-gradient(135deg, #FF6347, #FF7F50, #FFA07A); border-radius: 15px; margin: 1rem 0; padding: 2rem;">
            <h4 style="color: white; text-align: center; font-family: 'Georgia', serif;">
                🎯 COVID Impact and Recovery: Before, During, and After
            </h4>
        </div>
        """, unsafe_allow_html=True)

        # Create side-by-side comparison charts
        col1, col2 = st.columns(2)

        with col1:
            # Most affected states during pandemic (2020 vs 2019)
            if 'Pandemic_Impact' in state_total_df.columns:
                worst_hit = state_total_df.nsmallest(10, 'Pandemic_Impact')[['STATE', 'Pandemic_Impact']].copy()

                fig = go.Figure()
                fig.add_trace(go.Bar(
                    x=worst_hit['Pandemic_Impact'],
                    y=worst_hit['STATE'],
                    orientation='h',
                    marker=dict(
                        color=worst_hit['Pandemic_Impact'],
                        colorscale='Reds_r',  # Reverse red scale so darker = worse impact
                        line=dict(width=1, color='white')
                    ),
                    text=[f"{x:.1f}%" for x in worst_hit['Pandemic_Impact']],
                    textposition='outside',
                    textfont=dict(color='black', size=12),  # Black font for better contrast
                    hovertemplate='<b>%{y}</b><br>Impact: %{x:.1f}%<extra></extra>',
                    showlegend=False
                ))

                fig.update_layout(
                    title=dict(
                        text="📉 Most Affected States (2020)",
                        font=dict(size=16, color='#DC143C'),
                        x=0.5
                    ),
                    xaxis_title="Impact (%)",
                    yaxis_title="",
                    plot_bgcolor='rgba(248,249,250,0.8)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='black'),
                    height=400,
                    yaxis={'categoryorder':'total ascending'},
                    margin=dict(l=100, r=50, t=60, b=40)
                )

                st.plotly_chart(fig, use_container_width=True)

        with col2:
            # Best recovery states (2023 vs 2019)
            if 'Recovery_Rate' in state_total_df.columns:
                best_recovery = state_total_df.nlargest(10, 'Recovery_Rate')[['STATE', 'Recovery_Rate']].copy()

                fig = go.Figure()
                fig.add_trace(go.Bar(
                    x=best_recovery['Recovery_Rate'],
                    y=best_recovery['STATE'],
                    orientation='h',
                    marker=dict(
                        color=best_recovery['Recovery_Rate'],
                        colorscale='Greens',
                        line=dict(width=1, color='white')
                    ),
                    text=[f"{x:.1f}%" for x in best_recovery['Recovery_Rate']],
                    textposition='outside',
                    textfont=dict(color='black', size=12),  # Black font for better contrast
                    hovertemplate='<b>%{y}</b><br>Recovery: %{x:.1f}%<extra></extra>',
                    showlegend=False
                ))

                fig.update_layout(
                    title=dict(
                        text="📈 Best Recovery States (2023)",
                        font=dict(size=16, color='#228B22'),
                        x=0.5
                    ),
                    xaxis_title="Recovery (%)",
                    yaxis_title="",
                    plot_bgcolor='rgba(248,249,250,0.8)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='black'),
                    xaxis=dict(
                        title_font=dict(color='#006400', size=14),
                        tickfont=dict(color='#006400', size=12)
                    ),
                    yaxis=dict(
                        title_font=dict(color='#006400', size=14),
                        tickfont=dict(color='#006400', size=12),
                        categoryorder='total ascending'
                    ),
                    height=400,
                    margin=dict(l=100, r=50, t=60, b=40)
                )

                st.plotly_chart(fig, use_container_width=True)

        # Recovery Story Narrative
        if not state_total_df.empty:
            # Calculate key insights with error handling
            try:
                recovered_states = len(state_total_df[state_total_df['Recovery_Rate'] > 0])
                total_states = len(state_total_df.dropna(subset=['Recovery_Rate']))
                avg_recovery = state_total_df['Recovery_Rate'].mean()
                best_recovery_state = state_total_df.loc[state_total_df['Recovery_Rate'].idxmax(), 'STATE']
                best_recovery_rate = state_total_df['Recovery_Rate'].max()
                worst_impact_state = state_total_df.loc[state_total_df['Pandemic_Impact'].idxmin(), 'STATE']
                worst_impact_rate = state_total_df['Pandemic_Impact'].min()

                # Create the narrative section
                st.markdown("""
                <div style="background: linear-gradient(135deg, #FF6347, #FF7F50, #FFA07A); border-radius: 20px; color: white; margin: 2rem 0; padding: 2rem;">
                    <h4 style="text-align: center; font-size: 1.5rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
                        📖 The Great Recovery Story: Insights from the Data
                    </h4>
                </div>
                """, unsafe_allow_html=True)

                # Create metrics cards
                col1, col2, col3 = st.columns(3)

                with col1:
                    st.markdown(f"""
                    <div style="background: rgba(0,128,128,0.4); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px); text-align: center; color: white; border: 1px solid rgba(255,255,255,0.3); box-shadow: 3px 3px 10px rgba(0,0,0,0.3);">
                        <h5 style="margin: 0 0 0.5rem 0; color: #FFD700; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">🎯 Recovery Success Rate</h5>
                        <p style="margin: 0; font-size: 1.2rem; font-weight: bold; color: white; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">{recovered_states}/{total_states} states</p>
                        <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; color: white; opacity: 0.9; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">({(recovered_states/total_states)*100:.1f}%) exceeded 2019 levels</p>
                    </div>
                    """, unsafe_allow_html=True)

                with col2:
                    st.markdown(f"""
                    <div style="background: rgba(0,128,128,0.4); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px); text-align: center; color: white; border: 1px solid rgba(255,255,255,0.3); box-shadow: 3px 3px 10px rgba(0,0,0,0.3);">
                        <h5 style="margin: 0 0 0.5rem 0; color: #FFD700; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">📈 Average Recovery</h5>
                        <p style="margin: 0; font-size: 1.2rem; font-weight: bold; color: white; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">{avg_recovery:.1f}%</p>
                        <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; color: white; opacity: 0.9; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">growth vs pre-pandemic</p>
                    </div>
                    """, unsafe_allow_html=True)

                with col3:
                    st.markdown(f"""
                    <div style="background: rgba(0,128,128,0.4); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px); text-align: center; color: white; border: 1px solid rgba(255,255,255,0.3); box-shadow: 3px 3px 10px rgba(0,0,0,0.3);">
                        <h5 style="margin: 0 0 0.5rem 0; color: #FFD700; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">🏆 Recovery Champion</h5>
                        <p style="margin: 0; font-size: 1.1rem; font-weight: bold; color: white; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">{best_recovery_state}</p>
                        <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; color: white; opacity: 0.9; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">+{best_recovery_rate:.1f}% growth</p>
                    </div>
                    """, unsafe_allow_html=True)

                # Narrative text
                st.markdown(f"""
                <div style="background: rgba(0,128,128,0.4); padding: 2rem; border-radius: 15px; margin: 2rem 0; color: white; border: 1px solid rgba(255,255,255,0.3); box-shadow: 3px 3px 15px rgba(0,0,0,0.3);">
                    <p style="margin: 0; font-size: 1.1rem; line-height: 1.8; text-align: left; color: white; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">
                        <strong style="color: #FFD700;">The Resilience Narrative:</strong> India's tourism sector has shown remarkable resilience in its post-COVID recovery.
                        While <strong>{worst_impact_state}</strong> faced the steepest decline during 2020 ({worst_impact_rate:.1f}%),
                        states like <strong>{best_recovery_state}</strong> have not just recovered but thrived, showing {best_recovery_rate:.1f}% growth above pre-pandemic levels.
                        <br><br>
                        The data reveals a tale of two recoveries: <strong>heritage and spiritual destinations</strong> bounced back faster due to
                        domestic tourism surge, while <strong>international gateway states</strong> took longer to recover as global travel normalized.
                        This shift has democratized tourism, spreading benefits to previously underexplored regions.
                    </p>
                </div>
                """, unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Error in recovery analysis: {e}")
                st.info("Recovery analysis data is being processed...")

    # Domestic vs Foreign Tourism Trends (2017-2023)
    if not state_domestic_df.empty and not state_foreign_df.empty:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #FF6347, #FF7F50, #FFA07A); border-radius: 15px; margin: 1rem 0; padding: 2rem;">
            <h4 style="color: white; text-align: center; font-family: 'Georgia', serif;">
                📈 Domestic vs International Tourism Trends (2017-2023)
            </h4>
        </div>
        """, unsafe_allow_html=True)

        # Calculate total domestic and foreign visitors by year
        years = ['YEAR_2017', 'YEAR_2018', 'YEAR_2019', 'YEAR_2020', 'YEAR_2021', 'YEAR_2022', 'YEAR_2023']
        year_labels = ['2017', '2018', '2019', '2020', '2021', '2022', '2023']

        # Calculate totals for each year (convert to millions)
        domestic_totals = []
        foreign_totals = []

        for year in years:
            if year in state_domestic_df.columns:
                domestic_total = state_domestic_df[year].sum() / 10 / 1_000_000  # Apply correction and convert to millions
                domestic_totals.append(domestic_total)
            else:
                domestic_totals.append(0)

            if year in state_foreign_df.columns:
                foreign_total = state_foreign_df[year].sum() / 10 / 1_000_000  # Apply correction and convert to millions
                foreign_totals.append(foreign_total)
            else:
                foreign_totals.append(0)

        # Create the trend comparison chart
        fig = go.Figure()

        # Add domestic tourism line
        fig.add_trace(go.Scatter(
            x=year_labels,
            y=domestic_totals,
            mode='lines+markers+text',
            name='🇮🇳 Domestic Tourism',
            line=dict(color='#FF6347', width=4),
            marker=dict(size=10, color='#FF6347', line=dict(width=2, color='white')),
            text=[f"{x:.0f}M" for x in domestic_totals],
            textposition='top center',
            textfont=dict(color='black', size=12),
            hovertemplate='<b>Domestic Tourism</b><br>Year: %{x}<br>Visitors: %{y:.1f}M<extra></extra>'
        ))

        # Add foreign tourism line
        fig.add_trace(go.Scatter(
            x=year_labels,
            y=foreign_totals,
            mode='lines+markers+text',
            name='🌍 International Tourism',
            line=dict(color='#4169E1', width=4),
            marker=dict(size=10, color='#4169E1', line=dict(width=2, color='white')),
            text=[f"{x:.1f}M" for x in foreign_totals],
            textposition='bottom center',
            textfont=dict(color='black', size=12),
            hovertemplate='<b>International Tourism</b><br>Year: %{x}<br>Visitors: %{y:.1f}M<extra></extra>'
        ))

        # Add COVID-19 impact annotation
        fig.add_annotation(
            x='2020',
            y=max(max(domestic_totals), max(foreign_totals)) * 0.8,
            text="🦠 COVID-19<br>Impact",
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor="red",
            font=dict(size=12, color='red'),
            bgcolor="rgba(255,255,255,0.8)",
            bordercolor="red",
            borderwidth=1
        )

        fig.update_layout(
            title=dict(
                text="Tourism Trends: Domestic vs International Visitors (2017-2023)",
                font=dict(size=20, color='#FF6347'),
                x=0.25
            ),
            xaxis_title="Year",
            yaxis_title="Visitors (Millions)",
            plot_bgcolor='rgba(248,249,250,0.8)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='black'),
            height=500,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="center",
                x=0.5,
                font=dict(size=14)
            ),
            margin=dict(l=80, r=80, t=100, b=60),
            hovermode='x unified'
        )

        st.plotly_chart(fig, use_container_width=True)

        # Tourism Trends Analysis Narrative
        if domestic_totals and foreign_totals:
            # Calculate key insights
            try:
                pre_covid_domestic = domestic_totals[2] if len(domestic_totals) > 2 else 0  # 2019
                covid_domestic = domestic_totals[3] if len(domestic_totals) > 3 else 0      # 2020
                latest_domestic = domestic_totals[-1] if domestic_totals else 0             # 2023

                pre_covid_foreign = foreign_totals[2] if len(foreign_totals) > 2 else 0     # 2019
                covid_foreign = foreign_totals[3] if len(foreign_totals) > 3 else 0         # 2020
                latest_foreign = foreign_totals[-1] if foreign_totals else 0               # 2023

                domestic_covid_impact = ((covid_domestic - pre_covid_domestic) / pre_covid_domestic * 100) if pre_covid_domestic > 0 else 0
                foreign_covid_impact = ((covid_foreign - pre_covid_foreign) / pre_covid_foreign * 100) if pre_covid_foreign > 0 else 0

                domestic_recovery = ((latest_domestic - pre_covid_domestic) / pre_covid_domestic * 100) if pre_covid_domestic > 0 else 0
                foreign_recovery = ((latest_foreign - pre_covid_foreign) / pre_covid_foreign * 100) if pre_covid_foreign > 0 else 0

                # Create insights section
                st.markdown("""
                <div style="background: linear-gradient(135deg, #FF6347, #FF7F50, #FFA07A); border-radius: 20px; margin: 1rem 0; color: white; padding: 2rem;">
                    <h4 style="text-align: center; font-size: 1.5rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
                        📊 Tourism Trends: Key Insights from the Data
                    </h4>
                </div>
                """, unsafe_allow_html=True)

                # Create metrics cards
                col1, col2, col3 = st.columns(3)

                with col1:
                    st.markdown(f"""
                    <div style="background: white; padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px); text-align: center; color: black;">
                        <h5 style="margin: 0 0 0.5rem 0; color: #FF6347;">🇮🇳 Domestic Tourism (2023)</h5>
                        <p style="margin: 0; font-size: 1.4rem; font-weight: bold; color: #FF6347;">{latest_domestic:.0f}M</p>
                        <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; color: {'green' if domestic_recovery > 0 else 'red'};">
                            {domestic_recovery:+.1f}% vs 2019
                        </p>
                    </div>
                    """, unsafe_allow_html=True)

                with col2:
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #FF6347, #FF7F50, #FFA07A); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px); text-align: center; color: black;">
                        <h5 style="margin: 0 0 0.5rem 0; color: white;">🌍 World Tourism (2023)</h5>
                        <p style="margin: 0; font-size: 1.4rem; font-weight: bold; color: white;">{latest_foreign:.1f}M</p>
                        <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; color: {'white' if foreign_recovery > 0 else 'white'};">
                            {foreign_recovery:+.1f}% vs 2019
                        </p>
                    </div>
                    """, unsafe_allow_html=True)

                with col3:
                    ratio_2023 = (latest_domestic / latest_foreign) if latest_foreign > 0 else 0
                    st.markdown(f"""
                    <div style="background: white; padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px); text-align: center; color: black;">
                        <h5 style="margin: 0 0 0.5rem 0; color: #FF6347;">⚖️ Domestic:World Ratio</h5>
                        <p style="margin: 0; font-size: 1.4rem; font-weight: bold; color: #FF6347;">{ratio_2023:.1f}:1</p>
                        <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; color: green;">
                            Domestic dominance
                        </p>
                    </div>
                    """, unsafe_allow_html=True)

                # Narrative analysis
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.7); padding: 2rem; border-radius: 15px; margin: 2rem 0; color: black;">
                    <p style="margin: 0; font-size: 1.1rem; line-height: 1.8; text-align: left;">
                        <strong>The Great Tourism Shift:</strong> The 2017-2023 period reveals a fascinating transformation in India's tourism landscape.
                        While <strong>domestic tourism</strong> showed remarkable resilience, bouncing back to {latest_domestic:.0f}M visitors
                        ({domestic_recovery:+.1f}% vs pre-pandemic), <strong>international tourism</strong> faced a steeper challenge,
                        reaching {latest_foreign:.1f}M visitors ({foreign_recovery:+.1f}% vs 2019).
                        <br><br>
                        <strong>COVID-19 Impact Analysis:</strong> The pandemic hit international tourism harder ({foreign_covid_impact:.1f}% decline in 2020)
                        compared to domestic tourism ({domestic_covid_impact:.1f}% decline), highlighting India's growing self-reliance in tourism.
                        This shift has <strong>democratized travel</strong>, with Indians exploring their own country like never before,
                        creating new opportunities for regional destinations and local economies.
                    </p>
                </div>
                """, unsafe_allow_html=True)

            except Exception as e:
                st.info("Tourism trends analysis is being processed...")

    # Regional Tourism Summary
    if not state_total_df.empty:
        # Calculate summary statistics using new regional mapping (apply correction: divide by 10, convert to millions)
        total_visitors_all = state_total_df['YEAR_2023'].sum() / 10 / 1_000_000  # Apply correction and convert to millions
        total_regions = 5  # Exactly 5 regions: EAST, WEST, NORTH, SOUTH, CENTER
        total_states = len(state_total_df)

        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #FF6347, #FF7F50); padding: 2.5rem; border-radius: 20px; margin: 3rem 0; color: white; text-align: center;">
            <h3 style="margin-bottom: 1.5rem; font-size: 1.8rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
                🌈 India's Regional Tourism Tapestry: Data-Driven Insights
            </h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; margin: 2rem 0;">
                <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                    <h4 style="margin: 0 0 0.5rem 0; color: #FFD700;">🗺️ Regional Coverage</h4>
                    <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">{total_regions} tourism regions</p>
                </div>
                <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                    <h4 style="margin: 0 0 0.5rem 0; color: #98FF99;">📊 Total Visitors (2023)</h4>
                    <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">{total_visitors_all:.1f}M tourists</p>
                </div>
                <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                    <h4 style="margin: 0 0 0.5rem 0; color: cyan;">🏛️ Active Destinations</h4>
                    <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">{total_states} states & UTs</p>
                </div>
            </div>
            <p style="margin: 2rem 0 0 0; font-size: 1.1rem; line-height: 1.6; opacity: 0.9;">
                From <strong>Uttar Pradesh's heritage circuits</strong> to <strong>Tamil Nadu's temple trails</strong>,
                from <strong>Gujarat's business tourism</strong> to <strong>Kerala's backwaters</strong>,
                India's regional tourism landscape showcases remarkable diversity in visitor preferences,
                growth patterns, and market dynamics across the subcontinent.
            </p>
        </div>
        """, unsafe_allow_html=True)
