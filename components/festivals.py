import streamlit as st
import pandas as pd
import plotly.express as px
import base64
import io
from snowflake.snowpark.context import get_active_session

def get_snowflake_session():
    """Get active Snowflake session for Snowflake native apps"""
    return get_active_session()

@st.cache_data
def get_festival_image_from_stage(stage_name, file_path):
    """Get festival image binary data from Snowflake stage"""
    try:
        session = get_snowflake_session()

        # Map stage name to full qualified name
        if stage_name == "FESTIVAL_IMAGES":
            full_stage_name = '"CULTURE_TOURISM_DB"."ASSETS"."FESTIVAL_IMAGES_STAGE"'
        else:
            full_stage_name = f'"CULTURE_TOURISM_DB"."ASSETS"."{stage_name}_STAGE"'

        # Use session.file.get_stream() for Snowflake Native Apps
        stage_path = f"@{full_stage_name}/{file_path}"
        image_data = session.file.get_stream(stage_path, decompress=False).read()

        if image_data:
            return image_data
        else:
            return None

    except Exception as e:
        return None

@st.cache_data
def get_festival_image_info(stage_name, file_path):
    """Cache festival image existence info from Snowflake stage"""
    try:
        session = get_snowflake_session()

        # Map stage name to full qualified name
        if stage_name == "FESTIVAL_IMAGES":
            full_stage_name = '"CULTURE_TOURISM_DB"."ASSETS"."FESTIVAL_IMAGES_STAGE"'
        else:
            full_stage_name = f'"CULTURE_TOURISM_DB"."ASSETS"."{stage_name}_STAGE"'

        query = f"LIST '@{full_stage_name}' PATTERN='.*{file_path}.*'"
        result = session.sql(query).to_pandas()
        return {"exists": not result.empty}
    except:
        return {"exists": False}

# Exact mapping between festival names and their image files
FESTIVAL_IMAGE_MAPPING = {
    # National Festivals
    "Diwali": "diwali-national.jpg",
    "Holi": "holi-national.jpg",
    "Dussehra": "dussehra-national.jpg",
    "Eid ul-Fitr": "eid-national.jpg",
    "Christmas": "chirstmas-national.jpg",
    "Ganesh Chaturthi": "ganesh-national.jpg",
    "Navratri": "navratri-national.jpg",
    "Janmashtami": "janmashtami-national.jpeg",
    "Raksha Bandhan": "raksha-national.jpg",
    "Karva Chauth": "KarvaChauthMoon2-national.jpg",
    "Makar Sankranti": "makar-national.jpg",

    # State Festivals
    "Ugadi": "Ugadi_Festival.jpeg",
    "Losar": "losar.jpeg",
    "Rongali Bihu": "bihu.jpg",
    "Chhath Puja": "Chhath_Puja.jpg",
    "Hareli": "Hareli.jpeg",
    "Carnival": "Carnival.jpg",
    "Rann Utsav": "Rann_Utsav.jpeg",
    "Teej": "Teej.jpg",
    "Shimla Summer Festival": "shimla-summer-festival.jpg",
    "Sarhul": "Sarhul.jpg",
    "Karaga": "Karaga.jpeg",
    "Onam": "onam.jpg",
    "Khajuraho Dance Festival": "Khajuraho.jpg",
    "Gudi Padwa": "Gudi_Padwa.jpg",
    "Yaoshang": "yaoshang.jpg",
    "Shad Suk Mynsiem": "Shad_Suk_Mynsiem.jpg",
    "Chapchar Kut": "ChapChar_Kut.jpg",
    "Hornbill Festival": "Hornbill.png",
    "Jagannath Rath Yatra": "Rath_Yatra.jpg",
    "Baisakhi": "Baisakhi.jpg",
    "Pushkar Fair": "pushkar.jpg",
    "Saga Dawa": "saga_dawa.jpg",
    "Thaipusam": "Thaipusam.jpg",
    "Kharchi Puja": "Kharachi_Puja.jpg",
    "Kumbh Mela": "Kumbh_mela.jpg",
    "Nanda Devi Raj Jat": "Nanda_Devi_Raj.jpg",
    "Durga Puja": "Durga_Puja.jpg",
    "Hemis Festival": "Hemis.jpg",
    "Bonalu": "bonalu.jpg",
    "Mopin": "mopin.jpg",
    "Teeja": "teeja.jpg",
    "Shigmo": "shigmo.png",
    "Karma": "karma.jpg",
    "Thrissur Pooram": "thrissur_pooram.jpeg",
    "Lai Haraoba": "lai_haraoba.jpg",
    "Kali Puja": "kali-puja.jpg",
    "Lohri": "lohri.jpg",
    "Gangaur": "gangaur.jpg",
    "Pang Lhabsol": "pang_lhabsol.jpg",
    "Pongal": "pongal.jpg",
    "Garia Puja": "garia_puja.jpeg",
    "Kartik Purnima": "kartik_purnima.jpg",
    "Egoss": "egas.jpeg",
    "Poila Boishakh": "poila_boishakh.jpg"
}

@st.cache_data
def verify_festival_images(stage_name="FESTIVAL_IMAGES"):
    """Verify that all festival images exist in Snowflake stage (cached)"""
    missing_images = []
    for festival_name, image_file in FESTIVAL_IMAGE_MAPPING.items():
        image_info = get_festival_image_info(stage_name, image_file)
        if not image_info["exists"]:
            missing_images.append(f"{festival_name} -> {image_file}")

    if missing_images:
        print("Missing festival images:")
        for missing in missing_images:
            print(f"  - {missing}")
    else:
        print("✅ All festival images are properly mapped and exist!")

    return len(missing_images) == 0

def show_monthly_festival_chart(festivals_df):
    """Display a beautiful chart showing festival count by month"""

    # Create month mapping for better analysis
    month_mapping = {
        'January': ['January', 'Jan'],
        'February': ['February', 'Feb'],
        'March': ['March', 'Mar', 'March-April'],
        'April': ['April', 'Apr', 'March-April', 'April-May'],
        'May': ['May', 'April-May', 'May-June'],
        'June': ['June', 'Jun', 'May-June', 'June-July'],
        'July': ['July', 'Jul', 'June-July', 'July-August'],
        'August': ['August', 'Aug', 'July-August', 'August-September'],
        'September': ['September', 'Sep', 'August-September', 'September-October'],
        'October': ['October', 'Oct', 'September-October', 'October-November'],
        'November': ['November', 'Nov', 'October-November'],
        'December': ['December', 'Dec']
    }

    # Count festivals by month
    monthly_counts = {}
    for month in month_mapping.keys():
        count = 0
        for _, festival in festivals_df.iterrows():
            month_season = festival['MONTH_SEASON']
            if any(keyword in month_season for keyword in month_mapping[month]):
                count += 1
        monthly_counts[month] = count

    # Create DataFrame for plotting
    chart_data = pd.DataFrame({
        'Month': list(monthly_counts.keys()),
        'Festival Count': list(monthly_counts.values())
    })

    # Create a beautiful bar chart with better gradient colors
    fig = px.bar(
        chart_data,
        x='Month',
        y='Festival Count',
        title="📊 Festival Calendar - Monthly Distribution",
        color='Festival Count',
        color_continuous_scale=["#8D2207", "#FF0000", "#FF6200", "#E19909", "#FFE600"],
        text='Festival Count'
    )

    # Customize the chart
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#033D3C', family='Poppins'),
        xaxis=dict(
            title=dict(text="Month", font=dict(size=14, color="#033D3C")),
            tickfont=dict(size=12, color='#303')
        ),
        yaxis=dict(
            title=dict(text="Number of Festivals", font=dict(size=14, color='#033D3C')),
            tickfont=dict(size=12, color='#303')
        ),
        showlegend=False,
        margin=dict(l=50, r=50, t=50, b=50)
    )

    # Update bar appearance
    fig.update_traces(
        texttemplate='%{text}',
        textposition='outside',
        textfont=dict(size=12, color='#008080'),
        marker=dict(
            line=dict(color='#008080', width=2),
            opacity=0.8
        )
    )

    # Display the chart
    st.plotly_chart(fig, use_container_width=True)

    # Add some insights with better contrasting colors
    max_month = max(monthly_counts, key=monthly_counts.get)
    max_count = monthly_counts[max_month]

    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #FF6B6B, #FECDC4);
                padding: 1rem; border-radius: 15px; margin: 1rem 0;
                text-align: center; color: white; box-shadow: 0 5px 15px rgba(0,0,0,0.2);">
        <strong>🎉 Peak Festival Season: {max_month} with {max_count} festivals!</strong>
    </div>
    """, unsafe_allow_html=True)

def show_festivals_section(festivals_df):
    """Display festivals information with beautiful card layout"""
    st.markdown('<h2 class="section-header" style="color: white;">🎪 Indian Festivals</h2>', unsafe_allow_html=True)

    if festivals_df.empty:
        st.warning("No festival data available")
        return

    # Add monthly festival distribution chart first
    show_monthly_festival_chart(festivals_df)

    # Add a visual divider to separate sections
    st.markdown("""
    <div style="margin: 3rem 0 2rem 0;">
        <hr style="border: none; height: 3px;
                   background: linear-gradient(90deg, white, #FF6B6B);
                   border-radius: 2px; margin: 2rem 0;">
        <div style="text-align: center; margin: 1rem 0;">
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #008080, #20B2AA);
                padding: 1rem; border-radius: 15px; margin: 1rem 0;
                border: 1px solid white;
                text-align: center; color: white; box-shadow: 0 5px 15px rgba(0,0,0,0.2);">
        <h3><strong>🗺️ Explore Festivals by State and Month</strong></h3>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        selected_state = st.selectbox(
            "🏛️ Select State:",
            ["All States"] + sorted(list(festivals_df['STATE'].unique()))
        )

    with col2:
        # Extract months from festival data for filtering
        months = ["All Months", "January", "February", "March", "April", "May", "June",
                 "July", "August", "September", "October", "November", "December"]
        selected_month = st.selectbox("📅 Select Month/Season:", months)

    # Filter data based on selection
    filtered_df = festivals_df.copy()

    if selected_state != "All States":
        filtered_df = filtered_df[filtered_df['STATE'] == selected_state]

    if selected_month != "All Months":
        filtered_df = filtered_df[filtered_df['MONTH_SEASON'].str.contains(selected_month, case=False, na=False)]

    # Pagination logic for "All States" and "All Months" selection
    festivals_per_page = 10
    show_pagination = (selected_state == "All States" and selected_month == "All Months")

    # Reset pagination when filters change
    current_filter_key = f"{selected_state}_{selected_month}"
    if 'last_festival_filter' not in st.session_state or st.session_state.last_festival_filter != current_filter_key:
        st.session_state.current_page = 0  # Reset to first page
        st.session_state.last_festival_filter = current_filter_key

    # Initialize session state for festivals pagination
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 0

    # Apply pagination if showing all festivals
    total_festivals = len(filtered_df)
    if show_pagination and total_festivals > festivals_per_page:
        start_idx = st.session_state.current_page * festivals_per_page
        end_idx = start_idx + festivals_per_page
        display_df = filtered_df.iloc[start_idx:end_idx]
        festivals_displayed = len(display_df)
        current_page_num = st.session_state.current_page + 1
        total_pages = (total_festivals + festivals_per_page - 1) // festivals_per_page
    else:
        display_df = filtered_df
        festivals_displayed = total_festivals
        current_page_num = 1
        total_pages = 1

    # Count festivals with images
    festivals_with_images = sum(1 for _, festival in display_df.iterrows()
                               if festival['FESTIVAL_NAME'] in FESTIVAL_IMAGE_MAPPING)

    # Display count with beautiful styling
    if show_pagination and total_festivals > festivals_per_page:
        count_text = f"🎭 Page {current_page_num} of {total_pages} - Showing {festivals_displayed} Amazing Festivals"
    else:
        count_text = f"🎭 Discovered {festivals_displayed} Amazing Festivals"

    st.markdown(f"""
    <div style="text-align: center; margin: 2rem 0; padding: 1.5rem;
                background: linear-gradient(135deg, #008080, #20B2AA);
                border-radius: 15px; color: white; font-weight: bold;
                font-family: 'Poppins', sans-serif; font-size: 1.1rem;
                box-shadow: 0 5px 15px rgba(0,128,128,0.3);">
        {count_text}
        <br><small style="opacity: 0.9;">📸 {festivals_with_images} festivals with beautiful images!</small>
    </div>
    """, unsafe_allow_html=True)

    # Display festivals in beautiful cards
    if not display_df.empty:
        for _, festival in display_df.iterrows():
            display_festival_card(festival)

        # Add pagination navigation
        if show_pagination and total_pages > 1:
            # Create a vertically centered container for pagination
            st.markdown("""
            <div style="display: flex; justify-content: center; align-items: center;
                        min-height: 120px; margin: 3rem 0;">
            """, unsafe_allow_html=True)

            # Center the navigation
            _, center_col, _ = st.columns([1, 2, 1])

            with center_col:
                # Show current page info
                st.markdown(f"""
                <div style="text-align: center; margin-bottom: 1rem; color: #008080; font-weight: bold;">
                    📄 Page {current_page_num} of {total_pages}
                </div>
                """, unsafe_allow_html=True)

                # Navigation buttons
                nav_col1, nav_col2 = st.columns(2)

                with nav_col1:
                    if current_page_num > 1:
                        if st.button("⬅️ Previous", key="prev_festivals", use_container_width=True):
                            st.session_state.current_page -= 1
                            st.rerun()

                with nav_col2:
                    if current_page_num < total_pages:
                        if st.button("Next ➡️", key="next_festivals", use_container_width=True):
                            st.session_state.current_page += 1
                            st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)

    else:
        st.markdown("""
        <div style="text-align: center; margin: 3rem 0; padding: 2rem;
                    background: rgba(255,255,255,0.9); border-radius: 20px;
                    border: 2px dashed #008080; color: #008080;">
            <h3>🔍 No festivals found</h3>
            <p>Try adjusting your filters to discover more festivals!</p>
        </div>
        """, unsafe_allow_html=True)


def display_festival_card(festival, stage_name="FESTIVAL_IMAGES"):
    """Display festival in a beautiful rectangular card with image on left and description on right"""

    # Get image data using exact mapping with caching
    festival_name = festival['FESTIVAL_NAME']
    image_data = None

    if festival_name in FESTIVAL_IMAGE_MAPPING:
        image_filename = FESTIVAL_IMAGE_MAPPING[festival_name]
        image_info = get_festival_image_info(stage_name, image_filename)
        if image_info["exists"]:
            image_data = get_festival_image_from_stage(stage_name, image_filename)

    # Create the entire card using a different approach - custom CSS with data attributes
    card_id = f"festival-card-{festival_name.replace(' ', '-').lower()}"

    # Add custom CSS for this specific card
    st.markdown(f"""
    <style>
    #{card_id} {{
        background: white !important;
        padding: 2rem !important;
        margin: 2rem 0 !important;
        border-radius: 20px !important;
        box-shadow: 0 15px 35px rgba(0,0,0,0.15) !important;
        border: 3px solid #4ECDC4 !important;
        display: flex !important;
        align-items: flex-start !important;
        gap: 2rem !important;
        min-height: 300px !important;
    }}
    #{card_id} .image-section {{
        flex: 1 !important;
        max-width: 350px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        min-height: 300px !important;
    }}
    #{card_id} .content-section {{
        flex: 2 !important;
        padding-left: 1rem !important;
    }}
    #{card_id} .image-container {{
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        width: 100% !important;
        height: 100% !important;
    }}
    #{card_id} img {{
        border-radius: 15px !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2) !important;
        max-width: 100% !important;
        max-height: 250px !important;
        width: auto !important;
        height: auto !important;
        object-fit: contain !important;
    }}
    </style>
    """, unsafe_allow_html=True)

    # Get image HTML using Snowflake data
    if image_data:
        try:
            # Convert image data to base64 for embedding
            import base64
            img_str = base64.b64encode(image_data).decode()
            image_html = f'<div class="image-container"><img src="data:image/jpeg;base64,{img_str}" alt="{festival_name}"></div>'
        except:
            image_html = f"""
            <div class="image-container">
                <div style="height: 250px; display: flex; align-items: center; justify-content: center;
                            background: linear-gradient(135deg, #FF6B6B, #4ECDC4);
                            border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.2);">
                    <div style="text-align: center; color: white;">
                        <div style="font-size: 3.5rem; margin-bottom: 0.5rem;">🎪</div>
                        <div style="font-size: 1rem; font-weight: bold; opacity: 0.9;">{festival_name}</div>
                    </div>
                </div>
            </div>
            """
    else:
        image_html = f"""
        <div class="image-container">
            <div style="height: 250px; display: flex; align-items: center; justify-content: center;
                        background: linear-gradient(135deg, #FF6B6B, #4ECDC4);
                        border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.2);">
                <div style="text-align: center; color: white;">
                    <div style="font-size: 3.5rem; margin-bottom: 0.5rem;">🎪</div>
                    <div style="font-size: 1rem; font-weight: bold; opacity: 0.9;">{festival_name}</div>
                </div>
            </div>
        </div>
        """

    # Create the complete card as a single HTML block
    st.markdown(f"""
    <div id="{card_id}">
        <div class="image-section">
            {image_html}
        </div>
        <div class="content-section">
            <h2 style="color: #008080; font-family: 'Playfair Display', serif;
                       font-size: 2rem; margin-bottom: 1rem; font-weight: bold;">
                🎭 {festival['FESTIVAL_NAME']}
            </h2>
            <div style="margin-bottom: 1.5rem;">
                <p style="color: #20B2AA; font-weight: bold; font-size: 1.1rem; margin-bottom: 0.5rem;">
                    📍 {festival['STATE']}
                </p>
                <p style="color: #008080; font-weight: bold; font-size: 1rem; margin-bottom: 1rem;">
                    📅 {festival['MONTH_SEASON']}
                </p>
            </div>
            <div style="color: #333; line-height: 1.6; font-family: 'Poppins', sans-serif; font-size: 0.95rem;">
                {festival['DESCRIPTION']}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Add spacing between cards
    st.markdown("<br>", unsafe_allow_html=True)

def show_festival_placeholder(festival_name):
    """Show placeholder for festival images"""
    st.markdown(f"""
    <div style="height: 250px; display: flex; align-items: center; justify-content: center;
                background: linear-gradient(135deg, #FF6B6B, #4ECDC4);
                border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.2);">
        <div style="text-align: center; color: white;">
            <div style="font-size: 3.5rem; margin-bottom: 0.5rem;">🎪</div>
            <div style="font-size: 1rem; font-weight: bold; opacity: 0.9;">{festival_name}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
