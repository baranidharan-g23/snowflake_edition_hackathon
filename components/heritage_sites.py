import streamlit as st
import pandas as pd
from snowflake.snowpark.context import get_active_session

def get_snowflake_session():
    """Get active Snowflake session for Snowflake native apps"""
    return get_active_session()

@st.cache_data
def get_heritage_image_from_stage(stage_name, file_path):
    """Get heritage image binary data from Snowflake stage"""
    try:
        session = get_snowflake_session()

        # Map stage name to full qualified name
        if stage_name == "HERITAGE_IMAGES":
            full_stage_name = '"CULTURE_TOURISM_DB"."ASSETS"."HERITAGE_IMAGES_STAGE"'
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
def get_heritage_image_info(stage_name, file_path):
    """Cache heritage image existence info from Snowflake stage"""
    try:
        session = get_snowflake_session()

        # Map stage name to full qualified name
        if stage_name == "HERITAGE_IMAGES":
            full_stage_name = '"CULTURE_TOURISM_DB"."ASSETS"."HERITAGE_IMAGES_STAGE"'
        else:
            full_stage_name = f'"CULTURE_TOURISM_DB"."ASSETS"."{stage_name}_STAGE"'

        query = f"LIST '@{full_stage_name}' PATTERN='.*{file_path}.*'"
        result = session.sql(query).to_pandas()
        return {"exists": not result.empty}
    except:
        return {"exists": False}

def load_heritage_data():
    """Load heritage sites data from Snowflake tables"""
    try:
        session = get_snowflake_session()

        # Load heritage sites data from correct location
        heritage_df = session.table("CULTURE_TOURISM_DB.CULTURAL_DATA.HERITAGE_SITES").to_pandas()

        # Load top monuments data
        protected_df = session.table("CULTURE_TOURISM_DB.TOURISM_DATA.TOP_MONUMENTS_FOREIGN_VISITS").to_pandas()

        return heritage_df, protected_df
    except Exception as e:
        st.error(f"Error loading heritage data: {e}")
        return pd.DataFrame(), pd.DataFrame()

def show_heritage_section():
    """Display enhanced heritage sites information with real data and creative storytelling"""
    st.markdown('<h2 class="section-header">🏛️ Heritage Sites</h2>', unsafe_allow_html=True)

    # Load heritage data
    heritage_df, protected_df = load_heritage_data()

    # Check if data loaded successfully
    if heritage_df.empty:
        st.error("No heritage data available. Please check the database connection and table structure.")
        st.info("Expected table: CULTURE_TOURISM_DB.CULTURAL_DATA.HERITAGE_SITES")
        return

    # Heritage sites overview with improved storytelling
    st.markdown("""
    <div style="background: rgba(255,255,255,0.98); backdrop-filter: blur(15px);
                padding: 3rem; border-radius: 20px; margin: 2rem 0;
                box-shadow: 0 15px 35px rgba(0,128,128,0.2); border: 3px solid #008080;">
        <h3 style="color: #008080; margin-bottom: 2rem; text-align: center;
                   font-family: 'Playfair Display', serif; font-size: 2.5rem; font-weight: 700;">
            🏛️ Chronicles of India's Living Heritage
        </h3>
        <p style="text-align: center; color: #333; font-size: 1.3rem; line-height: 1.8;
                  font-family: 'Poppins', sans-serif; margin-bottom: 1.5rem;">
            Journey through millennia of architectural marvels, sacred temples, royal palaces, and ancient monuments
            that tell the extraordinary story of India's cultural evolution across civilizations.
        </p>
        <p style="text-align: center; color: #666; font-size: 1.1rem; line-height: 1.6;
                  font-family: 'Poppins', sans-serif; margin-bottom: 0;">
            From the mystical caves of Ajanta to the eternal beauty of the Taj Mahal, each heritage site is a
            chapter in humanity's greatest architectural anthology.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Calculate comprehensive statistics
    total_sites = len(heritage_df)
    unique_states = heritage_df['STATE_NAME'].nunique()
    unique_cities = heritage_df['CITY_NAME'].nunique()
    heritage_types = heritage_df['HERITAGE_TYPE'].value_counts()

    # Calculate additional insights
    temple_count = len(heritage_df[heritage_df['HERITAGE_TYPE'].str.contains('Temple|temple', case=False, na=False)])
    monument_count = len(heritage_df[heritage_df['HERITAGE_TYPE'].str.contains('Monument|monument', case=False, na=False)])
    palace_count = len(heritage_df[heritage_df['HERITAGE_TYPE'].str.contains('Palace|palace', case=False, na=False)])

    # Top states by heritage count
    top_states = heritage_df['STATE_NAME'].value_counts().head(3)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div style="background: rgba(255,255,255,0.95); backdrop-filter: blur(10px);
                    padding: 2rem; border-radius: 15px; border-left: 6px solid #008080;
                    margin-bottom: 1rem; text-align: center; box-shadow: 0 8px 25px rgba(0,128,128,0.15);
                    border: 2px solid #20B2AA; transition: transform 0.3s ease;">
            <h5 style="color: #008080; margin-bottom: 1rem; font-size: 1.3rem; font-weight: 600;
                        font-family: 'Poppins', sans-serif;">🏛️ Heritage Treasures</h5>
            <p style="margin: 0; line-height: 1.6; font-size: 2.5rem; color: #008080;
                        font-weight: bold; font-family: 'Poppins', sans-serif;">{total_sites}</p>
            <p style="margin: 0; color: #333; font-size: 1rem; font-weight: 500;">Documented Sites</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="background: rgba(255,255,255,0.95); backdrop-filter: blur(10px);
                    padding: 2rem; border-radius: 15px; border-left: 6px solid #008080;
                    margin-bottom: 1rem; text-align: center; box-shadow: 0 8px 25px rgba(0,128,128,0.15);
                    border: 2px solid #20B2AA; transition: transform 0.3s ease;">
            <h5 style="color: #008080; margin-bottom: 1rem; font-size: 1.3rem; font-weight: 600;
                        font-family: 'Poppins', sans-serif;">🗺️ Cultural Regions</h5>
            <p style="margin: 0; line-height: 1.6; font-size: 2.5rem; color: #008080;
                        font-weight: bold; font-family: 'Poppins', sans-serif;">{unique_states}</p>
            <p style="margin: 0; color: #333; font-size: 1rem; font-weight: 500;">States & Territories</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div style="background: rgba(255,255,255,0.95); backdrop-filter: blur(10px);
                    padding: 2rem; border-radius: 15px; border-left: 6px solid #008080;
                    margin-bottom: 1rem; text-align: center; box-shadow: 0 8px 25px rgba(0,128,128,0.15);
                    border: 2px solid #20B2AA; transition: transform 0.3s ease;">
            <h5 style="color: #008080; margin-bottom: 1rem; font-size: 1.3rem; font-weight: 600;
                        font-family: 'Poppins', sans-serif;">🏙️ Heritage Cities</h5>
            <p style="margin: 0; line-height: 1.6; font-size: 2.5rem; color: #008080;
                        font-weight: bold; font-family: 'Poppins', sans-serif;">{unique_cities}</p>
            <p style="margin: 0; color: #333; font-size: 1rem; font-weight: 500;">Historic Centers</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div style="background: rgba(255,255,255,0.95); backdrop-filter: blur(10px);
                    padding: 2rem; border-radius: 15px; border-left: 6px solid #008080;
                    margin-bottom: 1rem; text-align: center; box-shadow: 0 8px 25px rgba(0,128,128,0.15);
                    border: 2px solid #20B2AA; transition: transform 0.3s ease;">
            <h5 style="color: #008080; margin-bottom: 1rem; font-size: 1.3rem; font-weight: 600;
                        font-family: 'Poppins', sans-serif;">🕉️ Sacred Temples</h5>
            <p style="margin: 0; line-height: 1.6; font-size: 2.5rem; color: #008080;
                        font-weight: bold; font-family: 'Poppins', sans-serif;">{temple_count}</p>
            <p style="margin: 0; color: #333; font-size: 1rem; font-weight: 500;">Divine Architecture</p>
        </div>
        """, unsafe_allow_html=True)
    # Interactive Heritage Slideshow
    show_heritage_slideshow()

    # Regional Heritage Insights
    if not heritage_df.empty:
        show_regional_heritage_insights(heritage_df)

    # Dynamic Heritage Gallery
    if not heritage_df.empty:
        show_heritage_gallery(heritage_df)

    # Enhanced Heritage preservation message
    st.markdown("""
    <div style="background: rgba(255,255,255,0.98); backdrop-filter: blur(15px);
                padding: 3rem; border-radius: 20px; margin-top: 3rem; text-align: center;
                box-shadow: 0 15px 35px rgba(0,128,128,0.2); border: 3px solid #008080;
                border-left: 6px solid #20B2AA;">
        <h3 style="color: #008080; margin-bottom: 2rem; font-family: 'Playfair Display', serif;
                   font-size: 2.2rem; font-weight: 700;">
            🛡️ Preserving Our Heritage for Tomorrow
        </h3>
        <p style="font-size: 1.2rem; margin-bottom: 1.5rem; color: #333; line-height: 1.7;
                  font-family: 'Poppins', sans-serif;">
            India's heritage sites are not just monuments of the past, but living testimonies of our rich cultural legacy.
            Each site tells a unique story of artistic achievement, spiritual devotion, and historical significance that
            connects us to our ancestors and guides us toward the future.
        </p>
        <p style="font-size: 1.1rem; color: #666; line-height: 1.6; font-family: 'Poppins', sans-serif;">
            Through dedicated conservation efforts, scientific preservation techniques, community involvement, and
            responsible tourism, we ensure these irreplaceable treasures remain intact for future generations to
            experience, learn from, and cherish as symbols of human creativity and cultural diversity.
        </p>
        <div style="margin-top: 2rem; padding: 1.5rem; background: rgba(0,128,128,0.05);
                    border-radius: 15px; border: 2px solid #20B2AA;">
            <p style="color: #008080; font-size: 1rem; margin: 0; font-weight: 600;
                      font-family: 'Poppins', sans-serif;">
                🌍 "Heritage is our legacy from the past, what we live with today, and what we pass on to future generations." - UNESCO
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_heritage_slideshow():
    """Display an interactive heritage slideshow with real images"""
    st.markdown("""
    <div style="text-align: center;">
        <br>
        <h3 style="color: white; text-align: center; margin: 3rem 0 2rem 0; font-family: 'Playfair Display', serif;
               font-size: 3.5rem; text-shadow: 3px 3px 6px rgba(0,0,0,0.5); font-weight: 700;">
            🌟 Heritage Highlights
        </h3>
    </div>
    """, unsafe_allow_html=True)

    # Enhanced featured heritage sites with more diverse examples
    featured_sites = [
        {
            "name": "Taj Mahal",
            "location": "Agra, Uttar Pradesh",
            "image": "Images/heritage_images/Agra_TAJ_MAHAL.jpg",
            "description": "The eternal symbol of love, this ivory-white marble mausoleum stands as a testament to Mughal architectural brilliance and eternal devotion. Built by Shah Jahan for his beloved wife Mumtaz Mahal.",
            "significance": "UNESCO World Heritage Site & New Seven Wonders of the World"
        },
        {
            "name": "Red Fort",
            "location": "Agra, Uttar Pradesh",
            "image": "Images/heritage_images/Agra_RED_FORT.jpg",
            "description": "The majestic fortress palace of the Mughal emperors, where India's independence was proclaimed and history was written in red sandstone. A symbol of Mughal power and architectural mastery.",
            "significance": "Symbol of India's sovereignty and Mughal architectural heritage"
        },
        {
            "name": "Gwalior Fort",
            "location": "Madhya Pradesh",
            "image": "Images/heritage_images/Gwalior_Gwalior_Fort.jpg",
            "description": "The 'Pearl among fortresses in Hind', this hilltop citadel has witnessed the rise and fall of dynasties across a millennium of Indian history. Known for its impregnable defenses and musical heritage.",
            "significance": "One of India's most magnificent forts with rich cultural legacy"
        },
        {
            "name": "Brihadeeswarar Temple",
            "location": "Thanjavur, Tamil Nadu",
            "image": "Images/heritage_images/Thanjavur_Bragadeeswarar_Temple.jpg",
            "description": "A thousand-year-old architectural marvel dedicated to Lord Shiva, showcasing the pinnacle of Chola dynasty's artistic and engineering prowess. The temple's towering vimana is a masterpiece of Dravidian architecture.",
            "significance": "UNESCO World Heritage Site and masterpiece of Dravidian architecture"
        },
        {
            "name": "Shaniwarwada Palace",
            "location": "Pune, Maharashtra",
            "image": "Images/heritage_images/Pune_City_Shaniwarwada.jpg",
            "description": "The historic fortified palace of the Peshwas of the Maratha Empire, representing the zenith of Maratha architecture and political power in the 18th century.",
            "significance": "Symbol of Maratha empire and architectural heritage"
        },
        {
            "name": "Fatehpur Sikri",
            "location": "Agra, Uttar Pradesh",
            "image": "Images/heritage_images/Agra_FATEHPURI_SIKRI.jpg",
            "description": "Emperor Akbar's magnificent capital city, a perfect blend of Hindu and Islamic architectural styles. This ghost city tells the story of Mughal grandeur and religious tolerance.",
            "significance": "UNESCO World Heritage Site and architectural fusion masterpiece"
        },
        {
            "name": "Ujjayanta Palace",
            "location": "Agartala, Tripura",
            "image": "Images/heritage_images/Agartala_Ujjayanta_Palace.jpg",
            "description": "The former royal palace of the Kingdom of Tripura, showcasing Indo-Saracenic architecture with beautiful gardens and intricate design elements reflecting royal grandeur.",
            "significance": "Symbol of Tripura's royal heritage and architectural elegance"
        },
        {
            "name": "Akbar's Tomb",
            "location": "Agra, Uttar Pradesh",
            "image": "Images/heritage_images/Agra_AKBARS_TOMB.jpg",
            "description": "The magnificent mausoleum of Emperor Akbar the Great, representing the synthesis of Hindu, Christian, Islamic and Buddhist themes reflecting Akbar's secular philosophy.",
            "significance": "Architectural testament to Akbar's religious tolerance and Mughal grandeur"
        }
    ]

    # Initialize slideshow state
    if 'heritage_slide_index' not in st.session_state:
        st.session_state.heritage_slide_index = 0

    # Navigation buttons
    col1, col2, col3 = st.columns([1, 7, 1])

    with col1:
        if st.button("◀ Previous", key="heritage_prev"):
            st.session_state.heritage_slide_index = (st.session_state.heritage_slide_index - 1) % len(featured_sites)

    with col3:
        if st.button("Next ▶", key="heritage_next"):
            st.session_state.heritage_slide_index = (st.session_state.heritage_slide_index + 1) % len(featured_sites)

    # Display current slide
    current_site = featured_sites[st.session_state.heritage_slide_index]

    # Create slideshow display
    col1, col2 = st.columns([1, 1])

    with col1:
        # Use Snowflake stage for image loading
        # Extract filename from the image path
        image_filename = current_site["image"].split("/")[-1]
        image_data = get_heritage_image_from_stage("HERITAGE_IMAGES", image_filename)
        if image_data:
            try:
                st.image(image_data, use_container_width=True, caption=f"{current_site['name']}, {current_site['location']}")
            except Exception as e:
                st.error(f"Error displaying heritage image: {e}")
                show_heritage_placeholder(current_site['name'])
        else:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #008080, #20B2AA); color: white;
                        padding: 8rem 2rem; border-radius: 15px; text-align: center; margin: 1rem 0;">
                <h2 style="color: white; margin-bottom: 1rem; font-size: 2rem;">🏛️</h2>
                <h3 style="color: white; margin: 0; font-size: 1.5rem;">{current_site['name']}</h3>
                <p style="color: rgba(255,255,255,0.8); margin: 0.5rem 0 0 0;">{current_site['location']}</p>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="background: rgba(255,255,255,0.98); backdrop-filter: blur(15px);
                    padding: 2rem; border-radius: 20px; height: 100%;
                    box-shadow: 0 15px 35px rgba(0,128,128,0.2); border: 3px solid #008080;">
            <h3 style="color: #008080; margin-bottom: 1rem; font-family: 'Playfair Display', serif;
                       font-size: 1.8rem; font-weight: 700;">
                {current_site['name']}
            </h3>
            <p style="color: #666; font-size: 1rem; margin-bottom: 1rem; font-family: 'Poppins', sans-serif;">
                📍 {current_site['location']}
            </p>
            <p style="color: #333; font-size: 1rem; line-height: 1.7; margin-bottom: 1.5rem;
                      font-family: 'Poppins', sans-serif; text-align: justify;">
                {current_site['description']}
            </p>
            <div style="border-top: 2px solid #e0e0e0; padding-top: 1rem;">
                <p style="color: #008080; font-size: 0.9rem; font-weight: 600; margin: 0;
                          font-family: 'Poppins', sans-serif;">
                    ✨ {current_site['significance']}
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Slide indicators with enhanced styling
    st.markdown(f"""
    <div style="text-align: center; margin: 1.5rem 0;">
        <p style="color: white; font-size: 1.1rem; font-family: 'Poppins', sans-serif;
                  text-shadow: 2px 2px 4px rgba(0,0,0,0.5); font-weight: 600;">
            {st.session_state.heritage_slide_index + 1} of {len(featured_sites)} Heritage Treasures
        </p>
    </div>
    """, unsafe_allow_html=True)

def display_heritage_site_card(site):
    """Display an enhanced heritage site card with better styling"""
    # Determine icon based on type
    type_icon = "🏰" if site["type"] == "Cultural" else "🌿" if site["type"] == "Natural" else "🏛️"

    # Get features if available
    features = site.get('features', '')

    st.markdown(f"""
    <div style="background: rgba(255,255,255,0.98); backdrop-filter: blur(15px);
                padding: 2rem; border-radius: 20px; margin: 1.5rem 0;
                box-shadow: 0 15px 35px rgba(0,128,128,0.2); border: 3px solid #008080;
                transition: transform 0.3s ease, box-shadow 0.3s ease; min-height: 400px;
                border-left: 6px solid #20B2AA;">
        <div style="text-align: center; margin-bottom: 1.5rem;">
            <h4 style="color: #008080; margin-bottom: 0.8rem; font-size: 1.5rem; font-weight: 700;
                       font-family: 'Playfair Display', serif;">
                {type_icon} {site['name']}
            </h4>
            <p style="color: #666; font-size: 1rem; margin-bottom: 0.8rem; font-family: 'Poppins', sans-serif;">
                📍 {site['location']} | 🗓️ UNESCO {site['year']}
            </p>
            <span style="background: linear-gradient(135deg, #008080, #20B2AA); color: white;
                         padding: 0.4rem 1rem; border-radius: 20px; font-size: 0.9rem;
                         font-weight: 600; font-family: 'Poppins', sans-serif;">
                {site['type']} Heritage
            </span>
        </div>

        <div style="margin-bottom: 1.5rem;">
            <p style="color: #333; font-size: 1rem; line-height: 1.7; text-align: justify;
                      font-family: 'Poppins', sans-serif;">
                {site['description'][:200]}{'...' if len(site['description']) > 200 else ''}
            </p>
        </div>

        {f'''<div style="margin-bottom: 1.5rem; background: rgba(0,128,128,0.05);
                        padding: 1rem; border-radius: 10px; border-left: 4px solid #20B2AA;">
            <h6 style="color: #008080; margin-bottom: 0.5rem; font-size: 0.9rem; font-weight: 600;
                       font-family: 'Poppins', sans-serif;">🎯 Key Features:</h6>
            <p style="color: #333; font-size: 0.9rem; margin: 0; font-family: 'Poppins', sans-serif;">
                {features}
            </p>
        </div>''' if features else ''}

        <div style="border-top: 2px solid #e0e0e0; padding-top: 1rem;">
            <p style="color: #008080; font-size: 0.95rem; font-weight: 600; margin: 0;
                      font-family: 'Poppins', sans-serif; line-height: 1.5;">
                ✨ {site['significance']}
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_heritage_gallery(heritage_df):
    """Display a Pinterest-style gallery of heritage sites from CSV data"""
    if heritage_df.empty:
        return

    st.markdown("""
    <h3 style="color: white; text-align: center; margin: 3rem 0 2rem 0; font-family: 'Playfair Display', serif;
               font-size: 2.5rem; text-shadow: 3px 3px 6px rgba(0,0,0,0.5); font-weight: 700;">
        🎨 Heritage Gallery - Pinterest Style
    </h3>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        selected_state = st.selectbox(
            "🗺️ Select State",
            ["All States"] + sorted(heritage_df['STATE_NAME'].unique().tolist()),
            key="heritage_state_filter"
        )

    with col2:
        heritage_types = heritage_df['HERITAGE_TYPE'].unique().tolist()
        selected_type = st.selectbox(
            "🏛️ Heritage Type",
            ["All Types"] + sorted([t for t in heritage_types if pd.notna(t)]),
            key="heritage_type_filter"
        )

    with col3:
        cities = heritage_df['CITY_NAME'].unique().tolist() if selected_state == "All States" else heritage_df[heritage_df['STATE_NAME'] == selected_state]['CITY_NAME'].unique().tolist()
        selected_city = st.selectbox(
            "🏙️ Select City",
            ["All Cities"] + sorted([c for c in cities if pd.notna(c)]),
            key="heritage_city_filter"
        )

    # Filter data based on selections
    filtered_df = heritage_df.copy()

    if selected_state != "All States":
        filtered_df = filtered_df[filtered_df['STATE_NAME'] == selected_state]

    if selected_type != "All Types":
        filtered_df = filtered_df[filtered_df['HERITAGE_TYPE'] == selected_type]

    if selected_city != "All Cities":
        filtered_df = filtered_df[filtered_df['CITY_NAME'] == selected_city]

    # Reset pagination when filters change
    current_filter_key = f"{selected_state}_{selected_type}_{selected_city}"
    if 'last_heritage_filter' not in st.session_state or st.session_state.last_heritage_filter != current_filter_key:
        st.session_state.heritage_sites_shown = 20  # Reset to initial page size
        st.session_state.last_heritage_filter = current_filter_key

    # Display filtered results
    if not filtered_df.empty:
        # Results summary with properly sized white box
        st.markdown(f"""
        <div style="background: rgba(255,255,255,0.95); backdrop-filter: blur(10px);
                    padding: 2rem; border-radius: 15px; margin: 1.5rem 0;
                    box-shadow: 0 8px 25px rgba(0,128,128,0.15); border: 2px solid #20B2AA;
                    text-align: center; border-left: 6px solid #008080;">
            <h5 style="color: #008080; margin-bottom: 1rem; font-family: 'Playfair Display', serif;
                       font-size: 1.5rem; font-weight: 700;">
                🎯 Discovered {len(filtered_df)} Heritage Treasures
            </h5>
            <p style="color: #666; margin: 0; font-family: 'Poppins', sans-serif; font-size: 1.1rem; line-height: 1.5;">
                Each site tells a unique story of India's rich cultural tapestry and architectural evolution
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Enhanced Pinterest-style CSS for better responsive design
        st.markdown("""
        <style>
        /* Pinterest-style masonry layout */
        .pinterest-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            grid-gap: 20px;
            margin: 20px 0;
            padding: 0 10px;
        }

        /* Responsive breakpoints */
        @media (max-width: 1400px) {
            .pinterest-container {
                grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            }
        }

        @media (max-width: 1200px) {
            .pinterest-container {
                grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
                grid-gap: 15px;
            }
        }

        @media (max-width: 768px) {
            .pinterest-container {
                grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
                grid-gap: 12px;
                padding: 0 5px;
            }
        }

        @media (max-width: 480px) {
            .pinterest-container {
                grid-template-columns: 1fr;
                grid-gap: 10px;
                padding: 0;
            }
        }

        /* Pinterest card styling */
        .pinterest-card {
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 8px 25px rgba(0,128,128,0.15);
            border: 2px solid #20B2AA;
            transition: all 0.1s ease;
            cursor: pointer;
            position: relative;
        }

        .pinterest-card:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 20px 40px rgba(0,128,128,0.3);
            border-color: #008080;
        }

        .pinterest-card img {
            width: 100%;
            height: auto;
            display: block;
            transition: transform 0.3s ease;
        }

        .pinterest-card:hover img {
            transform: scale(1.05);
        }

        .pinterest-card-content {
            padding: 15px;
            background: white;
        }

        .pinterest-card-title {
            color: #008080;
            font-size: 1.1rem;
            font-weight: 700;
            margin-bottom: 8px;
            font-family: 'Playfair Display', serif;
            line-height: 1.3;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }

        .pinterest-card-location {
            color: #666;
            font-size: 0.9rem;
            margin-bottom: 10px;
            font-family: 'Poppins', sans-serif;
            display: flex;
            align-items: center;
        }

        .pinterest-card-type {
            background: linear-gradient(135deg, #008080, #20B2AA);
            color: white;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
            display: inline-block;
            font-family: 'Poppins', sans-serif;
            text-transform: capitalize;
            box-shadow: 0 2px 8px rgba(0,128,128,0.3);
        }

        .pinterest-placeholder {
            width: 100%;
            height: 200px;
            background: linear-gradient(135deg, #008080, #20B2AA);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.2rem;
            font-family: 'Poppins', sans-serif;
            text-align: center;
            position: relative;
        }

        .pinterest-placeholder::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.1) 50%, transparent 70%);
            animation: shimmer 2s infinite;
        }

        @keyframes shimmer {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
        }

        /* Streamlit column adjustments for Pinterest layout */
        .stColumn > div {
            padding: 0 !important;
        }

        /* Remove default Streamlit margins */
        .element-container {
            margin-bottom: 0 !important;
        }
        </style>
        """, unsafe_allow_html=True)

        # Create Pinterest-style gallery using Streamlit columns for better performance
        total_sites = len(filtered_df)

        # Add pagination for better performance with large datasets
        sites_per_page = 20  # Limit initial load for better performance

        # Add a "Load More" functionality
        if 'heritage_sites_shown' not in st.session_state:
            st.session_state.heritage_sites_shown = sites_per_page

        sites_to_show = min(st.session_state.heritage_sites_shown, total_sites)
        display_df = filtered_df.head(sites_to_show)

        # Display Pinterest-style gallery using Streamlit's native components
        # This approach is more efficient than base64 encoding all images

        # Create a container for the Pinterest layout
        st.markdown('<div class="pinterest-container">', unsafe_allow_html=True)

        # Use Streamlit columns to create a masonry-like effect
        # Responsive column count based on screen size
        # Note: Streamlit doesn't have built-in responsive detection, so we use a reasonable default
        num_columns = 4  # Default for desktop
        cols = st.columns(num_columns, gap="small")

        # Distribute sites across columns for masonry effect
        for idx, (_, site) in enumerate(display_df.iterrows()):
            col_idx = idx % num_columns

            with cols[col_idx]:
                # Create Pinterest-style card
                with st.container():
                    # Custom CSS for this specific card
                    st.markdown(f"""
                    <div class="pinterest-card" style="
                        break-inside: avoid;
                        margin-bottom: 20px;
                        background: white;
                        border-radius: 15px;
                        overflow: hidden;
                        box-shadow: 0 8px 25px rgba(0,128,128,0.15);
                        border: 2px solid #20B2AA;
                        transition: transform 0.3s ease, box-shadow 0.3s ease;
                    ">
                    """, unsafe_allow_html=True)

                    # Display image using Snowflake stage
                    image_filename = site['IMAGE_NAME']
                    image_data = get_heritage_image_from_stage("HERITAGE_IMAGES", image_filename)

                    if image_data:
                        try:
                            st.image(image_data, use_container_width=True, caption="")
                        except Exception as e:
                            show_heritage_placeholder(site['HERITAGE_NAME'])
                    else:
                        st.markdown(f"""
                        <div style="
                            width: 100%;
                            height: 200px;
                            background: linear-gradient(135deg, #008080, #20B2AA);
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            color: white;
                            font-size: 1.2rem;
                            font-family: 'Poppins', sans-serif;
                            text-align: center;
                        ">
                            🏛️<br>{site["HERITAGE_NAME"][:20]}...
                        </div>
                        """, unsafe_allow_html=True)

                    # Card content
                    st.markdown(f"""
                    <div style="padding: 5px;">
                        <div style="
                            background: linear-gradient(135deg, #004d4d);
                            color: white;
                            padding: 4px 10px;
                            border-radius: 8px;
                            font-size: 1rem;
                            font-weight: 600;
                            margin-bottom: 10px;
                            font-family: 'Poppins', sans-serif;
                            line-height: 1.3;
                            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
                        ">{site["HERITAGE_NAME"]}<br>
                        <div style="
                            background: white;
                            color: black;
                            padding: 4px 12px;
                            border-radius: 8px;
                            font-size: 0.8rem;
                            margin-top:10px;
                            margin-bottom: 10px;
                            font-family: 'Poppins', sans-serif;
                            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                        ">📍 {site["CITY_NAME"]}, {site["STATE_NAME"]}</div>
                        <div style="
                            background: white;
                            color: black;
                            padding: 4px 12px;
                            margin-bottom:8px;
                            border-radius: 8px;
                            font-size: 0.8rem;
                            display: inline-block;
                            font-family: 'Poppins', sans-serif;
                            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                        ">{site["HERITAGE_TYPE"]}</div></div>
                    </div>
                    """, unsafe_allow_html=True)

                    st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

        # Status text and Load More button on same line
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            # Create a container with both text and button on same line
            if sites_to_show < total_sites:
                col_text, col_button = st.columns([2, 1])
                with col_text:
                    st.markdown(f"""
                    <div style="text-align: center; padding: 0.5rem;">
                        <span style="color: white; font-family: 'Poppins', sans-serif; font-size: 1.1rem;
                                   text-shadow: 2px 2px 4px rgba(0,0,0,0.5); font-weight: 600;">
                            📊 Showing {sites_to_show} of {total_sites} heritage sites
                        </span>
                    </div>
                    """, unsafe_allow_html=True)
                with col_button:
                    # Add custom CSS for button styling
                    st.markdown("""
                    <style>
                    div.stButton > button[key="load_more_heritage"] {
                        background: linear-gradient(135deg, #008080, #20B2AA) !important;
                        color: white !important;
                        border: none !important;
                        border-radius: 25px !important;
                        padding: 0.5rem 1rem !important;
                        font-weight: 600 !important;
                        font-family: 'Poppins', sans-serif !important;
                        box-shadow: 0 4px 12px rgba(0,128,128,0.3) !important;
                        transition: all 0.3s ease !important;
                    }
                    div.stButton > button[key="load_more_heritage"]:hover {
                        background: linear-gradient(135deg, #20B2AA, #008080) !important;
                        transform: translateY(-2px) !important;
                        box-shadow: 0 6px 16px rgba(0,128,128,0.4) !important;
                    }
                    </style>
                    """, unsafe_allow_html=True)

                    if st.button(f"🔄 Load 20 More",
                               key="load_more_heritage",
                               help="Load more heritage sites"):
                        st.session_state.heritage_sites_shown += sites_per_page
                        st.rerun()
            else:
                st.markdown(f"""
                        <div style="background: linear-gradient(135deg, #008080, #20B2AA);
                            color: white;
                            padding: 0.5rem 0.5rem; border-radius: 15px;
                            text-align: center;
                            font-size: 1.2rem;
                            font-family: 'Poppins', sans-serif;
                            font-weight: 600;
                            margin: 1rem 0;">
                            ✨ Displaying all {total_sites} heritage sites
                        </div>
                        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background: rgba(255,255,255,0.95); backdrop-filter: blur(10px);
                    padding: 3rem; border-radius: 15px; margin: 2rem 0;
                    box-shadow: 0 8px 25px rgba(0,128,128,0.15); border: 2px solid #20B2AA;
                    text-align: center;">
            <h5 style="color: #008080; margin-bottom: 1.5rem; font-family: 'Poppins', sans-serif; font-size: 1.4rem;">
                🔍 No Heritage Sites Found
            </h5>
            <p style="color: #666; margin-bottom: 1rem; font-family: 'Poppins', sans-serif; font-size: 1.1rem;">
                Try adjusting your filters to explore more heritage treasures across India
            </p>
            <p style="color: #999; margin: 0; font-family: 'Poppins', sans-serif; font-size: 0.9rem;">
                💡 Tip: Start with "All States" or "All Types" to see the full collection
            </p>
        </div>
        """, unsafe_allow_html=True)

# Note: display_heritage_gallery_card function removed - now using CSS Grid approach

def show_regional_heritage_insights(heritage_df):
    """Display regional heritage insights and patterns"""
    st.markdown("""
    <h3 style="color: white; text-align: center; margin: 3rem 0 2rem 0; font-family: 'Playfair Display', serif;
               font-size: 2.3rem; text-shadow: 3px 3px 6px rgba(0,0,0,0.5); font-weight: 700;">
        🗺️ Regional Heritage Chronicles
    </h3>
    """, unsafe_allow_html=True)

    # Calculate regional statistics
    state_counts = heritage_df['STATE_NAME'].value_counts().head(5)
    heritage_type_counts = heritage_df['HERITAGE_TYPE'].value_counts().head(6)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="background: rgba(255,255,255,0.95); backdrop-filter: blur(10px);
                    padding: 2rem; border-radius: 15px; border-left: 6px solid #008080;
                    margin-bottom: 1rem; box-shadow: 0 8px 25px rgba(0,128,128,0.15);
                    border: 2px solid #20B2AA;">
            <h5 style="color: #008080; margin-bottom: 1.5rem; font-size: 1.4rem; font-weight: 600;
                       font-family: 'Poppins', sans-serif; text-align: center;">🏆 Heritage Powerhouses</h5>
        </div>
        """, unsafe_allow_html=True)

        for i, (state, count) in enumerate(state_counts.items()):
            rank_emoji = ["🥇", "🥈", "🥉", "🏅", "⭐"][i]
            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.9); padding: 1rem; border-radius: 10px;
                        margin-bottom: 0.5rem; border-left: 4px solid #20B2AA;">
                <p style="margin: 0; color: #333; font-family: 'Poppins', sans-serif;">
                    {rank_emoji} <strong>{state}</strong>: {count} heritage sites
                </p>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background: rgba(255,255,255,0.95); backdrop-filter: blur(10px);
                    padding: 2rem; border-radius: 15px; border-left: 6px solid #008080;
                    margin-bottom: 1rem; box-shadow: 0 8px 25px rgba(0,128,128,0.15);
                    border: 2px solid #20B2AA;">
            <h5 style="color: #008080; margin-bottom: 1.5rem; font-size: 1.4rem; font-weight: 600;
                       font-family: 'Poppins', sans-serif; text-align: center;">🏛️ Heritage Categories</h5>
        </div>
        """, unsafe_allow_html=True)

        type_emojis = {"Temple": "🕉️", "Monument": "🏛️", "Palace": "👑", "Fort": "🏰", "Church": "⛪", "Mosque": "🕌"}

        for heritage_type, count in heritage_type_counts.items():
            emoji = type_emojis.get(heritage_type, "🏛️")
            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.9); padding: 1rem; border-radius: 10px;
                        margin-bottom: 0.5rem; border-left: 4px solid #20B2AA;">
                <p style="margin: 0; color: #333; font-family: 'Poppins', sans-serif;">
                    {emoji} <strong>{heritage_type}</strong>: {count} sites
                </p>
            </div>
            """, unsafe_allow_html=True)

    # Heritage storytelling insights
    st.markdown("""
    <div style="background: rgba(255,255,255,0.98); backdrop-filter: blur(15px);
                padding: 2.5rem; border-radius: 20px; margin: 2rem 0;
                box-shadow: 0 15px 35px rgba(0,128,128,0.2); border: 3px solid #008080;">
        <h4 style="color: #008080; margin-bottom: 1.5rem; text-align: center;
                   font-family: 'Playfair Display', serif; font-size: 1.8rem; font-weight: 700;">
            📖 Stories Written in Stone and Time
        </h4>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-top: 2rem;">
            <div>
                <h6 style="color: #008080; margin-bottom: 1rem; font-size: 1.1rem; font-weight: 600;">
                    🏛️ Architectural Evolution
                </h6>
                <p style="color: #333; font-size: 1rem; line-height: 1.7; margin: 0;">
                    From ancient rock-cut caves to Mughal masterpieces, India's heritage sites chronicle
                    the evolution of architectural styles across millennia, each era leaving its distinctive mark.
                </p>
            </div>
            <div>
                <h6 style="color: #008080; margin-bottom: 1rem; font-size: 1.1rem; font-weight: 600;">
                    🌍 Cultural Confluence
                </h6>
                <p style="color: #333; font-size: 1rem; line-height: 1.7; margin: 0;">
                    These monuments stand as witnesses to India's role as a cultural crossroads, where
                    diverse traditions, religions, and artistic styles merged to create unique masterpieces.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_heritage_placeholder(site_name):
    """Show placeholder for heritage images"""
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #008080, #20B2AA); color: white;
                padding: 8rem 2rem; border-radius: 15px; text-align: center; margin: 1rem 0;">
        <h2 style="color: white; margin-bottom: 1rem; font-size: 2rem;">🏛️</h2>
        <h3 style="color: white; margin-bottom: 0.5rem;">{site_name}</h3>
        <p style="color: white; opacity: 0.9;">Heritage Image</p>
    </div>
    """, unsafe_allow_html=True)
