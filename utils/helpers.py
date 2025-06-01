import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PIL import Image
import os

def display_image_safely(image_path, caption="", width=None):
    """Safely display image with error handling"""
    try:
        if os.path.exists(image_path):
            img = Image.open(image_path)
            st.image(img, caption=caption, width=width)
        else:
            st.warning(f"Image not found: {image_path}")
    except Exception as e:
        st.error(f"Error loading image: {e}")

def create_india_map(state_tourism_df):
    """Create an interactive choropleth map of India with tourism data"""

    # State name mapping for GeoJSON compatibility
    state_name_mapping = {
        'Andhra Pradesh': 'Andhra Pradesh',
        'Arunachal Pradesh': 'Arunachal Pradesh',
        'Assam': 'Assam',
        'Bihar': 'Bihar',
        'Chhattisgarh': 'Chhattisgarh',
        'Goa': 'Goa',
        'Gujarat': 'Gujarat',
        'Haryana': 'Haryana',
        'Himachal Pradesh': 'Himachal Pradesh',
        'Jharkhand': 'Jharkhand',
        'Karnataka': 'Karnataka',
        'Kerala': 'Kerala',
        'Madhya Pradesh': 'Madhya Pradesh',
        'Maharashtra': 'Maharashtra',
        'Manipur': 'Manipur',
        'Meghalaya': 'Meghalaya',
        'Mizoram': 'Mizoram',
        'Nagaland': 'Nagaland',
        'Odisha': 'Odisha',
        'Punjab': 'Punjab',
        'Rajasthan': 'Rajasthan',
        'Sikkim': 'Sikkim',
        'Tamil Nadu': 'Tamil Nadu',
        'Telangana': 'Telangana',
        'Tripura': 'Tripura',
        'Uttar Pradesh': 'Uttar Pradesh',
        'Uttarakhand': 'Uttarakhand',
        'West Bengal': 'West Bengal',
        'Andaman & Nicobar Island': 'Andaman & Nicobar',
        'Chandigarh': 'Chandigarh',
        'Dadra & Nagar Haveli': 'Dadra and Nagar Haveli and Daman and Diu',
        'Delhi': 'Delhi',
        'Jammu & Kashmir': 'Jammu & Kashmir',
        'Ladakh': 'Ladakh',
        'Lakshadweep': 'Lakshadweep',
        'Puducherry': 'Puducherry'
    }

    # Prepare map data with total tourism across all years (2017-2023)
    map_data = []
    year_columns = ['YEAR_2017', 'YEAR_2018', 'YEAR_2019', 'YEAR_2020', 'YEAR_2021', 'YEAR_2022', 'YEAR_2023']

    for idx, row in state_tourism_df.iterrows():
        state_name = row['STATE']

        # Calculate total across all years
        total_all_years = sum([row[col] for col in year_columns if col in row and pd.notna(row[col])])

        # Calculate recent growth (2022 to 2023)
        growth = ((row['YEAR_2023'] - row['YEAR_2022']) / row['YEAR_2022']) * 100 if row['YEAR_2022'] > 0 else 0

        # Calculate average per year
        avg_per_year = total_all_years / len(year_columns)

        map_data.append({
            'State': state_name,
            'State_Mapped': state_name_mapping.get(state_name, state_name),
            'Tourism_2023': row['YEAR_2023'],
            'Tourism_2022': row['YEAR_2022'],
            'Total_All_Years': total_all_years,
            'Avg_Per_Year': avg_per_year,
            'Growth_2022_23': growth,
            'Region': row['REGION']
        })

    if map_data:
        map_df = pd.DataFrame(map_data)

        # Use scatter map for Snowflake compatibility
        create_fallback_scatter_map(map_df)


    else:
        st.warning("Unable to create map - tourism data not available")

def create_fallback_scatter_map(map_df):
    """Create interactive scatter map for tourism data"""

    # State coordinates for scatter map
    state_coordinates = {
        'Andhra Pradesh': [15.9129, 79.7400],
        'Arunachal Pradesh': [28.2180, 94.7278],
        'Assam': [26.2006, 92.9376],
        'Bihar': [25.0961, 85.3131],
        'Chhattisgarh': [21.2787, 81.8661],
        'Goa': [15.2993, 74.1240],
        'Gujarat': [23.0225, 72.5714],
        'Haryana': [29.0588, 76.0856],
        'Himachal Pradesh': [31.1048, 77.1734],
        'Jharkhand': [23.6102, 85.2799],
        'Karnataka': [15.3173, 75.7139],
        'Kerala': [10.8505, 76.2711],
        'Madhya Pradesh': [22.9734, 78.6569],
        'Maharashtra': [19.7515, 75.7139],
        'Manipur': [24.6637, 93.9063],
        'Meghalaya': [25.4670, 91.3662],
        'Mizoram': [23.1645, 92.9376],
        'Nagaland': [26.1584, 94.5624],
        'Odisha': [20.9517, 85.0985],
        'Punjab': [31.1471, 75.3412],
        'Rajasthan': [27.0238, 74.2179],
        'Sikkim': [27.5330, 88.5122],
        'Tamil Nadu': [11.1271, 78.6569],
        'Telangana': [18.1124, 79.0193],
        'Tripura': [23.9408, 91.9882],
        'Uttar Pradesh': [26.8467, 80.9462],
        'Uttarakhand': [30.0668, 79.0193],
        'West Bengal': [22.9868, 87.8550],
        'Andaman and Nicobar Islands': [11.7401, 92.6586],
        'Chandigarh': [30.7333, 76.7794],
        'Dadra and Nagar Haveli and Daman and Diu': [20.1809, 73.0169],
        'Delhi': [28.7041, 77.1025],
        'Jammu and Kashmir': [34.0837, 74.7973],
        'Ladakh': [34.1526, 77.5771],
        'Lakshadweep': [10.5667, 72.6417],
        'Puducherry': [11.9416, 79.8083]
    }

    # Add coordinates to map data
    for idx, row in map_df.iterrows():
        state_name = row['State']
        if state_name in state_coordinates:
            map_df.at[idx, 'lat'] = state_coordinates[state_name][0]
            map_df.at[idx, 'lon'] = state_coordinates[state_name][1]

    # Filter out states without coordinates
    map_df = map_df.dropna(subset=['lat', 'lon'])

    if not map_df.empty:
        fig = px.scatter_map(
            map_df,
            lat='lat',
            lon='lon',
            size='Total_All_Years',
            color='Total_All_Years',
            hover_name='State',
            hover_data={
                'Total_All_Years': ':,.1f',
                'Region': True,
                'lat': False,
                'lon': False,
                'Tourism_2023': False,
                'Tourism_2022': False,
                'Avg_Per_Year': False,
                'Growth_2022_23': False
            },
            color_continuous_scale=[[0, '#E8F5E8'], [0.2, '#B8E6B8'], [0.4, '#7DD87D'], [0.6, '#4CAF50'], [0.8, '#2E7D32'], [1, '#1B5E20']],
            size_max=30,
            zoom=4,
            center={'lat': 20.5937, 'lon': 78.9629},
            title='🗺️ India Tourism Map - Total Tourist Arrivals (2017-2023)',
            labels={
                'Total_All_Years': 'Total Tourists (M)'
            }
        )

        fig.update_layout(
            height=600,
            font=dict(size=12),
            title=dict(
                text='🗺️ India Tourism Map - Total Tourist Arrivals (2017-2023)',
                font=dict(size=18, color='#008080', family="Arial Black"),
                x=0.5,
                y=0.95
            ),
            margin={"r":0,"t":60,"l":0,"b":0},
            coloraxis_colorbar=dict(
                title=dict(
                    text="Total Tourists<br>2017-2023 (Million)",
                    font=dict(size=14, color='#008080', family="Arial Black")
                ),
                tickfont=dict(size=11, color='#008080', family="Arial"),
                thickness=15,
                len=0.7,
                x=1.02
            )
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        <div style="background-color: #f0f0f0; padding: 6px; border-radius: 5px; margin: 8px 0;">
            <p style="font-size: 0.8rem; color: black; text-align: center; margin: 0; font-weight: bold;">
                <strong>🔵 Circle Guide:</strong> Larger & darker circles = Higher tourist arrivals (2017-2023) | <strong>🖱️ Interactive:</strong> Click for details
            </p>
        </div>
        """, unsafe_allow_html=True)

def create_enhanced_tourism_chart(ita_df):
    """Create an enhanced tourism growth chart"""

    # Create subplots with increased spacing
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Tourism Growth Trend', 'Year-over-Year Growth',
                       'Decade Comparison', 'Recovery Analysis'),
        specs=[[{"colspan": 2}, None],
               [{"type": "bar"}, {"type": "bar"}]],
        vertical_spacing=0.25
    )

    # Main trend line - minimalist style
    fig.add_trace(
        go.Scatter(
            x=ita_df['YEAR'],
            y=ita_df['INDIA_ARRIVALS_MILLION'],
            mode='lines+markers',
            name='Tourist Arrivals',
            line=dict(color='#008080', width=2),
            marker=dict(size=6, color='#008080'),
            fill=None
        ),
        row=1, col=1
    )

    # Add COVID impact annotation - minimalist style
    fig.add_annotation(
        x=2020, y=ita_df[ita_df['YEAR'] == 2020]['INDIA_ARRIVALS_MILLION'].iloc[0],
        text="COVID-19",
        showarrow=True,
        arrowhead=1,
        arrowcolor="#666",
        bgcolor="rgba(255,255,255,0.9)",
        bordercolor="#ccc",
        borderwidth=1,
        font=dict(size=10, color="#666"),
        row=1, col=1
    )

    # Growth rate chart - minimalist colors
    ita_df_growth = ita_df.copy()
    ita_df_growth['Growth Rate'] = ita_df_growth['INDIA_ARRIVALS_MILLION'].pct_change() * 100

    colors = ['#008080' if x > 0 else '#999' for x in ita_df_growth['Growth Rate'].fillna(0)]

    fig.add_trace(
        go.Bar(
            x=ita_df_growth['YEAR'][1:],
            y=ita_df_growth['Growth Rate'][1:],
            name='Growth Rate',
            marker_color=colors[1:],
            opacity=0.6
        ),
        row=2, col=1
    )

    # Decade comparison - minimalist colors
    decades = {
        '2001-2010': ita_df[(ita_df['YEAR'] >= 2001) & (ita_df['YEAR'] <= 2010)]['INDIA_ARRIVALS_MILLION'].mean(),
        '2011-2020': ita_df[(ita_df['YEAR'] >= 2011) & (ita_df['YEAR'] <= 2020)]['INDIA_ARRIVALS_MILLION'].mean(),
        '2021-2023': ita_df[(ita_df['YEAR'] >= 2021) & (ita_df['YEAR'] <= 2023)]['INDIA_ARRIVALS_MILLION'].mean()
    }

    fig.add_trace(
        go.Bar(
            x=list(decades.keys()),
            y=list(decades.values()),
            name='Decade Average',
            marker_color=['#008080', '#20B2AA', '#66CDAA'],
            opacity=0.6
        ),
        row=2, col=2
    )

    # Add horizontal separator line between top and bottom sections
    fig.add_shape(
        type="line",
        x0=0, x1=1,
        y0=0.50, y1=0.50,
        xref="paper", yref="paper",
        line=dict(color="black", width=3)
    )

    # Update layout - minimalist style
    fig.update_layout(
        height=500,
        showlegend=False,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color='#666', size=11),
        title_text="",
        margin=dict(l=40, r=40, t=40, b=40)
    )

    # Update axes - minimal grid with black bold labels
    fig.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(200,200,200,0.3)',
        showline=True,
        linewidth=1,
        linecolor='rgba(200,200,200,0.5)',
        tickfont=dict(color='black', size=11),
        title_font=dict(color='black', size=12)
    )
    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(200,200,200,0.3)',
        showline=True,
        linewidth=1,
        linecolor='rgba(200,200,200,0.5)',
        tickfont=dict(color='black', size=11),
        title_font=dict(color='black', size=12)
    )

    return fig

def create_tourism_growth_trend_chart(ita_df):
    """Create enhanced tourism growth trend chart with attractive styling"""

    fig = go.Figure()

    # Add area fill first (behind the line)
    fig.add_trace(
        go.Scatter(
            x=ita_df['YEAR'],
            y=ita_df['INDIA_ARRIVALS_MILLION'],
            mode='lines',
            name='Tourist Arrivals',
            line=dict(color='rgba(0,128,128,0)', width=0),
            fill='tozeroy',
            fillcolor='rgba(0,128,128,0.1)',
            showlegend=False
        )
    )

    # Main trend line with enhanced styling
    fig.add_trace(
        go.Scatter(
            x=ita_df['YEAR'],
            y=ita_df['INDIA_ARRIVALS_MILLION'],
            mode='lines+markers',
            name='Tourist Arrivals',
            line=dict(color='#008080', width=4, shape='spline'),
            marker=dict(
                size=8,
                color='#008080',
                line=dict(color='white', width=2),
                symbol='circle'
            ),
            hovertemplate='<b>Year:</b> %{x}<br><b>Arrivals:</b> %{y:.2f}M<extra></extra>'
        )
    )

    # Add milestone markers for significant years
    milestones = {
        2001: "Tourism Year",
        2008: "Global Crisis",
        2020: "COVID-19 Impact",
        2023: "Recovery"
    }

    for year, label in milestones.items():
        if year in ita_df['YEAR'].values:
            y_val = ita_df[ita_df['YEAR'] == year]['INDIA_ARRIVALS_MILLION'].iloc[0]
            color = '#FF6B6B' if year in [2008, 2020] else '#4ECDC4'

            fig.add_annotation(
                x=year, y=y_val,
                text=f"<b>{label}</b>",
                showarrow=True,
                arrowhead=2,
                arrowcolor=color,
                arrowwidth=2,
                bgcolor=f"rgba{(*[int(color[i:i+2], 16) for i in (1, 3, 5)], 0.9)}",
                bordercolor=color,
                borderwidth=2,
                font=dict(size=10, color='white'),
                ax=0, ay=-40 if year != 2020 else 40
            )

    # Update layout with enhanced styling
    fig.update_layout(
        height=350,
        showlegend=False,
        plot_bgcolor='rgba(248,249,250,0.8)',
        paper_bgcolor='white',
        font=dict(color='#2C3E50', size=12),
        title_text="",
        margin=dict(l=50, r=50, t=30, b=50),
        xaxis_title="<b>Year</b>",
        yaxis_title="<b>Tourist Arrivals (Million)</b>",
        hovermode='x unified'
    )

    # Enhanced axes styling
    fig.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(200,200,200,0.4)',
        showline=True,
        linewidth=2,
        linecolor='#34495E',
        tickfont=dict(color='#2C3E50', size=11, family='Arial Black'),
        title_font=dict(color='#2C3E50', size=13, family='Arial Black'),
        zeroline=False
    )
    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(200,200,200,0.4)',
        showline=True,
        linewidth=2,
        linecolor='#34495E',
        tickfont=dict(color='#2C3E50', size=11, family='Arial Black'),
        title_font=dict(color='#2C3E50', size=13, family='Arial Black'),
        zeroline=False
    )

    return fig

def create_year_over_year_growth_chart(ita_df):
    """Create year-over-year growth chart"""

    fig = go.Figure()

    # Growth rate chart - minimalist colors
    ita_df_growth = ita_df.copy()
    ita_df_growth['Growth Rate'] = ita_df_growth['INDIA_ARRIVALS_MILLION'].pct_change() * 100

    colors = ['#008080' if x > 0 else '#999' for x in ita_df_growth['Growth Rate'].fillna(0)]

    fig.add_trace(
        go.Bar(
            x=ita_df_growth['YEAR'][1:],
            y=ita_df_growth['Growth Rate'][1:],
            name='Growth Rate',
            marker_color=colors[1:],
            opacity=0.6
        )
    )

    # Update layout - minimalist style
    fig.update_layout(
        height=300,
        showlegend=False,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color='black', size=11),
        title_text="",
        margin=dict(l=40, r=40, t=20, b=40),
        xaxis_title="Year",
        yaxis_title="Growth Rate (%)"
    )

    # Update axes - minimal grid with black bold labels
    fig.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(200,200,200,0.3)',
        showline=True,
        linewidth=1,
        linecolor='rgba(200,200,200,0.5)',
        tickfont=dict(color='black', size=11),
        title_font=dict(color='black', size=12)
    )
    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(200,200,200,0.3)',
        showline=True,
        linewidth=1,
        linecolor='rgba(200,200,200,0.5)',
        tickfont=dict(color='black', size=11),
        title_font=dict(color='black', size=12)
    )

    return fig

def create_decade_comparison_chart(ita_df):
    """Create decade comparison chart"""

    fig = go.Figure()

    # Decade comparison - minimalist colors
    decades = {
        '2001-2010': ita_df[(ita_df['YEAR'] >= 2001) & (ita_df['YEAR'] <= 2010)]['INDIA_ARRIVALS_MILLION'].mean(),
        '2011-2020': ita_df[(ita_df['YEAR'] >= 2011) & (ita_df['YEAR'] <= 2020)]['INDIA_ARRIVALS_MILLION'].mean(),
        '2021-2023': ita_df[(ita_df['YEAR'] >= 2021) & (ita_df['YEAR'] <= 2023)]['INDIA_ARRIVALS_MILLION'].mean()
    }

    fig.add_trace(
        go.Bar(
            x=list(decades.keys()),
            y=list(decades.values()),
            name='Decade Average',
            marker_color=['#008080', '#20B2AA', '#66CDAA'],
            opacity=0.6
        )
    )

    # Update layout - minimalist style
    fig.update_layout(
        height=300,
        showlegend=False,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color='black', size=11),
        title_text="",
        margin=dict(l=40, r=40, t=20, b=40),
        xaxis_title="Decade",
        yaxis_title="Average Arrivals (Million)"
    )

    # Update axes - minimal grid with black bold labels
    fig.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(200,200,200,0.3)',
        showline=True,
        linewidth=1,
        linecolor='rgba(200,200,200,0.5)',
        tickfont=dict(color='black', size=11),
        title_font=dict(color='black', size=12)
    )
    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(200,200,200,0.3)',
        showline=True,
        linewidth=1,
        linecolor='rgba(200,200,200,0.5)',
        tickfont=dict(color='black', size=11),
        title_font=dict(color='black', size=12)
    )

    return fig

def create_gdp_contribution_chart(tourism_gdp_df):
    """Create GDP contribution chart"""

    fig = go.Figure()

    # Add direct contribution line
    fig.add_trace(
        go.Scatter(
            x=tourism_gdp_df['YEAR'],
            y=tourism_gdp_df['DIRECT_CONTRIBUTION_GDP_PERCENT'],
            mode='lines+markers',
            name='Direct Contribution',
            line=dict(color='#008080', width=3),
            marker=dict(size=8, color='#008080'),
            fill='tonexty',
            fillcolor='rgba(0,128,128,0.1)'
        )
    )

    # Add total contribution line
    fig.add_trace(
        go.Scatter(
            x=tourism_gdp_df['YEAR'],
            y=tourism_gdp_df['TOTAL_CONTRIBUTION_GDP_PERCENT'],
            mode='lines+markers',
            name='Total Contribution (Direct + Indirect)',
            line=dict(color='#20B2AA', width=3),
            marker=dict(size=8, color='#20B2AA'),
            fill='tonexty',
            fillcolor='rgba(32,178,170,0.1)'
        )
    )

    # Add COVID impact annotation
    fig.add_annotation(
        x='2020-21',
        y=tourism_gdp_df[tourism_gdp_df['YEAR'] == '2020-21']['DIRECT_CONTRIBUTION_GDP_PERCENT'].iloc[0],
        text="COVID-19 Impact",
        showarrow=True,
        arrowhead=2,
        arrowcolor="red",
        bgcolor="rgba(255,0,0,0.1)",
        bordercolor="red"
    )

    fig.update_layout(
        title='Tourism Contribution to India\'s GDP',
        xaxis_title='Year',
        yaxis_title='Contribution (%)',
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#333', size=11),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')

    return fig

def create_employment_trends_chart(tourism_employment_df):
    """Create employment trends chart"""

    fig = go.Figure()

    # Add direct employment
    fig.add_trace(
        go.Scatter(
            x=tourism_employment_df['YEAR'],
            y=tourism_employment_df['TOURISM_CHARACTERISTIC_INDUSTRIES_MILLION'],
            mode='lines+markers',
            name='Direct Tourism Jobs',
            line=dict(color='#FF6B35', width=3),
            marker=dict(size=8, color='#FF6B35'),
            fill='tonexty',
            fillcolor='rgba(255,107,53,0.1)'
        )
    )

    # Add total employment
    fig.add_trace(
        go.Scatter(
            x=tourism_employment_df['YEAR'],
            y=tourism_employment_df['DIRECT_INDIRECT_EMPLOYMENT_MILLION'],
            mode='lines+markers',
            name='Total Tourism Employment',
            line=dict(color='#F18F01', width=3),
            marker=dict(size=8, color='#F18F01'),
            fill='tonexty',
            fillcolor='rgba(241,143,1,0.1)'
        )
    )

    # Add employment share percentage as secondary y-axis
    fig.add_trace(
        go.Scatter(
            x=tourism_employment_df['YEAR'],
            y=tourism_employment_df['DIRECT_INDIRECT_SHARE_PERCENT'],
            mode='lines+markers',
            name='Employment Share (%)',
            line=dict(color='#A23B72', width=2, dash='dash'),
            marker=dict(size=6, color='#A23B72'),
            yaxis='y2'
        )
    )

    fig.update_layout(
        title='Tourism Employment in India',
        xaxis_title='Year',
        yaxis_title='Employment (Million)',
        yaxis2=dict(
            title='Share of Total Employment (%)',
            overlaying='y',
            side='right',
            range=[10, 16]
        ),
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#333', size=11),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')

    return fig

def get_embedded_india_geojson():
    """Return embedded India GeoJSON data for choropleth maps (Snowflake-compatible)"""
    # Simplified India states GeoJSON - key states for tourism data
    return {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {"ST_NM": "Andhra Pradesh"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[77.5, 12.5], [84.5, 12.5], [84.5, 19.5], [77.5, 19.5], [77.5, 12.5]]]
                }
            },
            {
                "type": "Feature",
                "properties": {"ST_NM": "Assam"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[89.5, 24.0], [96.0, 24.0], [96.0, 28.0], [89.5, 28.0], [89.5, 24.0]]]
                }
            },
            {
                "type": "Feature",
                "properties": {"ST_NM": "Bihar"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[83.0, 24.0], [88.5, 24.0], [88.5, 27.5], [83.0, 27.5], [83.0, 24.0]]]
                }
            },
            {
                "type": "Feature",
                "properties": {"ST_NM": "Goa"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[73.5, 14.8], [74.5, 14.8], [74.5, 15.8], [73.5, 15.8], [73.5, 14.8]]]
                }
            },
            {
                "type": "Feature",
                "properties": {"ST_NM": "Gujarat"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[68.0, 20.0], [74.5, 20.0], [74.5, 24.5], [68.0, 24.5], [68.0, 20.0]]]
                }
            },
            {
                "type": "Feature",
                "properties": {"ST_NM": "Haryana"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[74.5, 27.5], [77.5, 27.5], [77.5, 30.5], [74.5, 30.5], [74.5, 27.5]]]
                }
            },
            {
                "type": "Feature",
                "properties": {"ST_NM": "Himachal Pradesh"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[75.5, 30.5], [79.0, 30.5], [79.0, 33.0], [75.5, 33.0], [75.5, 30.5]]]
                }
            },
            {
                "type": "Feature",
                "properties": {"ST_NM": "Karnataka"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[74.0, 11.5], [78.5, 11.5], [78.5, 18.5], [74.0, 18.5], [74.0, 11.5]]]
                }
            },
            {
                "type": "Feature",
                "properties": {"ST_NM": "Kerala"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[74.5, 8.0], [77.5, 8.0], [77.5, 12.5], [74.5, 12.5], [74.5, 8.0]]]
                }
            },
            {
                "type": "Feature",
                "properties": {"ST_NM": "Madhya Pradesh"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[74.0, 21.0], [82.5, 21.0], [82.5, 26.5], [74.0, 26.5], [74.0, 21.0]]]
                }
            },
            {
                "type": "Feature",
                "properties": {"ST_NM": "Maharashtra"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[72.5, 15.5], [80.5, 15.5], [80.5, 22.0], [72.5, 22.0], [72.5, 15.5]]]
                }
            },
            {
                "type": "Feature",
                "properties": {"ST_NM": "Odisha"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[81.5, 17.5], [87.5, 17.5], [87.5, 22.5], [81.5, 22.5], [81.5, 17.5]]]
                }
            },
            {
                "type": "Feature",
                "properties": {"ST_NM": "Punjab"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[73.5, 29.5], [76.5, 29.5], [76.5, 32.5], [73.5, 32.5], [73.5, 29.5]]]
                }
            },
            {
                "type": "Feature",
                "properties": {"ST_NM": "Rajasthan"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[69.0, 23.0], [78.0, 23.0], [78.0, 30.0], [69.0, 30.0], [69.0, 23.0]]]
                }
            },
            {
                "type": "Feature",
                "properties": {"ST_NM": "Tamil Nadu"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[76.0, 8.0], [80.5, 8.0], [80.5, 13.5], [76.0, 13.5], [76.0, 8.0]]]
                }
            },
            {
                "type": "Feature",
                "properties": {"ST_NM": "Telangana"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[77.0, 15.5], [81.0, 15.5], [81.0, 19.5], [77.0, 19.5], [77.0, 15.5]]]
                }
            },
            {
                "type": "Feature",
                "properties": {"ST_NM": "Uttar Pradesh"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[77.0, 24.0], [84.5, 24.0], [84.5, 30.5], [77.0, 30.5], [77.0, 24.0]]]
                }
            },
            {
                "type": "Feature",
                "properties": {"ST_NM": "West Bengal"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[85.5, 21.5], [89.5, 21.5], [89.5, 27.5], [85.5, 27.5], [85.5, 21.5]]]
                }
            },
            {
                "type": "Feature",
                "properties": {"ST_NM": "Delhi"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[76.8, 28.4], [77.3, 28.4], [77.3, 28.9], [76.8, 28.9], [76.8, 28.4]]]
                }
            },
            {
                "type": "Feature",
                "properties": {"ST_NM": "Jammu and Kashmir"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[73.0, 32.0], [80.0, 32.0], [80.0, 37.0], [73.0, 37.0], [73.0, 32.0]]]
                }
            }
        ]
    }
