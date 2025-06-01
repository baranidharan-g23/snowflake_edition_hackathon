import streamlit as st

def apply_custom_css():
    """Apply custom CSS styling to the Streamlit app"""
    st.markdown("""
    <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&family=Playfair+Display:wght@400;700&display=swap');

        /* Global Styles */
        .stApp {
            background: linear-gradient(135deg, #008080 0%, #20B2AA 50%, #FFFFFF 100%);
            background-attachment: fixed;
        }

        .main .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            max-width: 1200px;
        }

        /* Hero Section */
        .hero-section {
            background: linear-gradient(135deg, rgba(0,128,128,0.9) 0%, rgba(32,178,170,0.9) 100%);
            padding: 3rem 2rem;
            border-radius: 20px;
            margin-bottom: 2rem;
            text-align: center;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1), 0 0 0 8px rgba(255,255,255,0.3);
            position: relative;
            overflow: hidden;
        }

        .hero-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="25" cy="25" r="1" fill="rgba(255,255,255,0.1)"/><circle cx="75" cy="75" r="1" fill="rgba(255,255,255,0.1)"/><circle cx="50" cy="10" r="0.5" fill="rgba(255,255,255,0.1)"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
            opacity: 0.3;
        }

        .hero-title {
            font-family: 'Playfair Display', serif;
            font-size: 3.5rem;
            font-weight: 700;
            color: white;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            position: relative;
            z-index: 1;
        }

        .hero-subtitle {
            font-family: 'Poppins', sans-serif;
            font-size: 1.3rem;
            color: rgba(255,255,255,0.9);
            margin-bottom: 2rem;
            position: relative;
            z-index: 1;
        }

        .hero-stats {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-top: 2rem;
            position: relative;
            z-index: 1;
        }

        /* Enhanced Metric Cards */
        .metric-card {
            background: rgba(255,255,255,0.95);
            backdrop-filter: blur(10px);
            padding: 1.5rem;
            border-radius: 15px;
            text-align: center;
            margin: 0.5rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            border: 1px solid rgba(255,255,255,0.2);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            min-height: 120px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .metric-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0,0,0,0.15);
        }

        .metric-icon {
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }

        .metric-number {
            font-family: 'Poppins', sans-serif;
            font-size: 2rem;
            font-weight: 700;
            color: #008080;
            margin-bottom: 0.3rem;
        }

        .metric-label {
            font-family: 'Poppins', sans-serif;
            font-size: 0.9rem;
            color: #666;
            font-weight: 500;
        }

        .metric-sublabel {
            font-family: 'Poppins', sans-serif;
            font-size: 0.7rem;
            color: #888;
            font-weight: 400;
            margin-top: 0.3rem;
            opacity: 0.8;
        }

        /* Section Headers */
        .section-header {
            font-family: 'Playfair Display', serif;
            font-size: 2.5rem;
            font-weight: 700;
            color: #008080;
            margin: 2rem 0 1rem 0;
            text-align: center;
            position: relative;
        }

        .section-header::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 100px;
            height: 4px;
            background: linear-gradient(90deg, #20B2AA, #008080);
            border-radius: 2px;
        }

        /* Feature Cards */
        .feature-card {
            background: rgba(255,255,255,0.95);
            backdrop-filter: blur(10px);
            padding: 2rem;
            border-radius: 20px;
            margin: 1rem 0;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            border: 1px solid rgba(255,255,255,0.2);
            transition: transform 0.3s ease;
        }

        .feature-card:hover {
            transform: translateY(-3px);
        }

        .feature-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
            text-align: center;
        }

        .feature-title {
            font-family: 'Poppins', sans-serif;
            font-size: 1.3rem;
            font-weight: 600;
            color: #008080;
            margin-bottom: 1rem;
            text-align: center;
        }

        .feature-description {
            font-family: 'Poppins', sans-serif;
            color: #666;
            line-height: 1.6;
            text-align: center;
        }

        /* Enhanced Cultural Highlights */
        .cultural-highlights-container {
            margin: 2rem 0;
        }

        .highlights-intro {
            text-align: center;
            margin-bottom: 2rem;
        }

        /* Enhanced Festival Cards */
        .enhanced-festival-card {
            background: rgba(255,255,255,0.98);
            backdrop-filter: blur(15px);
            border-radius: 20px;
            margin: 1rem 0;
            box-shadow: 0 15px 35px rgba(0,128,128,0.15);
            border: 2px solid rgba(0,128,128,0.1);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            overflow: hidden;
            position: relative;
        }

        .enhanced-festival-card:hover {
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0 25px 50px rgba(0,128,128,0.25);
            border-color: #008080;
        }

        .festival-card-header {
            position: relative;
            height: 200px;
            overflow: hidden;
        }

        .festival-card-image {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.4s ease;
        }

        .enhanced-festival-card:hover .festival-card-image {
            transform: scale(1.1);
        }

        .festival-card-placeholder {
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #008080, #20B2AA);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: white;
        }

        .placeholder-icon {
            font-size: 4rem;
            margin-bottom: 0.5rem;
        }

        .placeholder-text {
            font-family: 'Poppins', sans-serif;
            font-size: 1rem;
            font-weight: 500;
        }

        .festival-card-overlay {
            position: absolute;
            top: 15px;
            right: 15px;
            background: rgba(0,128,128,0.9);
            backdrop-filter: blur(10px);
            padding: 0.5rem 1rem;
            border-radius: 20px;
            color: white;
            font-size: 0.8rem;
            font-weight: 600;
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .enhanced-festival-card:hover .festival-card-overlay {
            opacity: 1;
        }

        .festival-card-content {
            padding: 1.5rem;
        }

        .festival-card-title {
            font-family: 'Playfair Display', serif;
            font-size: 1.3rem;
            font-weight: 700;
            color: #008080 !important;
            margin-bottom: 1rem;
            text-align: center;
        }

        .festival-card-details {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
            margin-bottom: 1rem;
        }

        .festival-detail-item {
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .detail-icon {
            font-size: 1rem;
            width: 20px;
        }

        .detail-text {
            font-family: 'Poppins', sans-serif;
            font-size: 0.9rem;
            color: #666;
            font-weight: 500;
        }

        .festival-card-description {
            font-family: 'Poppins', sans-serif;
            color: #555;
            line-height: 1.6;
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }



        /* Enhanced Heritage Cards */
        .enhanced-heritage-card {
            background: rgba(255,255,255,0.98);
            backdrop-filter: blur(15px);
            border-radius: 20px;
            margin: 1rem 0;
            box-shadow: 0 15px 35px rgba(139,69,19,0.15);
            border: 2px solid rgba(139,69,19,0.1);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            overflow: hidden;
            position: relative;
        }

        .enhanced-heritage-card:hover {
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0 25px 50px rgba(139,69,19,0.25);
            border-color: #8B4513;
        }

        .heritage-card-header {
            position: relative;
            height: 200px;
            background: linear-gradient(135deg, #8B4513, #CD853F);
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }

        .heritage-card-image {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.4s ease;
        }

        .enhanced-heritage-card:hover .heritage-card-image {
            transform: scale(1.1);
        }

        .heritage-icon-container {
            background: rgba(255,255,255,0.2);
            backdrop-filter: blur(10px);
            border-radius: 50%;
            width: 100px;
            height: 100px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.4s ease;
        }

        .enhanced-heritage-card:hover .heritage-icon-container {
            transform: scale(1.1) rotate(5deg);
        }

        .heritage-icon {
            font-size: 3rem;
            color: white;
        }

        .heritage-card-overlay {
            position: absolute;
            top: 15px;
            right: 15px;
            background: rgba(139,69,19,0.9);
            backdrop-filter: blur(10px);
            padding: 0.5rem 1rem;
            border-radius: 20px;
            color: white;
            font-size: 0.8rem;
            font-weight: 600;
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .enhanced-heritage-card:hover .heritage-card-overlay {
            opacity: 1;
        }

        .heritage-card-content {
            padding: 1.5rem;
        }

        .heritage-card-title {
            font-family: 'Playfair Display', serif;
            font-size: 1.3rem;
            font-weight: 700;
            color: #008080 !important;
            margin-bottom: 1rem;
            text-align: center;
        }

        .heritage-card-details {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
            margin-bottom: 1rem;
        }

        .heritage-detail-item {
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .heritage-card-description {
            font-family: 'Poppins', sans-serif;
            color: #555;
            line-height: 1.6;
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }



        /* Enhanced Dance Cards */
        .enhanced-dance-card {
            background: rgba(255,255,255,0.98);
            backdrop-filter: blur(15px);
            border-radius: 20px;
            margin: 1rem 0;
            box-shadow: 0 15px 35px rgba(255,20,147,0.15);
            border: 2px solid rgba(255,20,147,0.1);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            overflow: hidden;
            position: relative;
        }

        .enhanced-dance-card:hover {
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0 25px 50px rgba(255,20,147,0.25);
            border-color: #FF1493;
        }

        .dance-card-header {
            position: relative;
            height: 200px;
            background: linear-gradient(135deg, #FF1493, #FF69B4);
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }

        .dance-card-image {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.4s ease;
        }

        .enhanced-dance-card:hover .dance-card-image {
            transform: scale(1.1);
        }

        .dance-icon-container {
            background: rgba(255,255,255,0.2);
            backdrop-filter: blur(10px);
            border-radius: 50%;
            width: 100px;
            height: 100px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.4s ease;
        }

        .enhanced-dance-card:hover .dance-icon-container {
            transform: scale(1.1) rotate(-5deg);
        }

        .dance-icon {
            font-size: 3rem;
            color: white;
        }

        .dance-card-overlay {
            position: absolute;
            top: 15px;
            right: 15px;
            background: rgba(255,20,147,0.9);
            backdrop-filter: blur(10px);
            padding: 0.5rem 1rem;
            border-radius: 20px;
            color: white;
            font-size: 0.8rem;
            font-weight: 600;
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .enhanced-dance-card:hover .dance-card-overlay {
            opacity: 1;
        }

        .dance-card-content {
            padding: 1.5rem;
        }

        .dance-card-title {
            font-family: 'Playfair Display', serif;
            font-size: 1.3rem;
            font-weight: 700;
            color: #008080 !important;
            margin-bottom: 1rem;
            text-align: center;
        }

        .dance-card-details {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
            margin-bottom: 1rem;
        }

        .dance-detail-item {
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .dance-card-description {
            font-family: 'Poppins', sans-serif;
            color: #555;
            line-height: 1.6;
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }



        /* Map Container */
        .map-container {
            background: rgba(255,255,255,0.95);
            backdrop-filter: blur(10px);
            padding: 2rem;
            border-radius: 20px;
            margin: 2rem 0;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            text-align: center;
        }

        /* Force teal color for all card titles */
        h4.festival-card-title,
        h4.heritage-card-title,
        h4.dance-card-title {
            color: #008080 !important;
        }

        /* Override any Streamlit default h4 styles */
        .enhanced-festival-card h4,
        .enhanced-heritage-card h4,
        .enhanced-dance-card h4 {
            color: #008080 !important;
        }
    </style>
    """, unsafe_allow_html=True)

def apply_heritage_chapter_background():
    """Apply heritage-specific background styling for Chapter 1"""
    st.markdown("""
    <style>
        /* Heritage Chapter Specific Background */
        .stApp {
            background: linear-gradient(135deg, #F5DEB3 0%, #F8E6C8 50%, #FDF5E6 100%) !important;
            background-attachment: fixed;
        }
    </style>
    """, unsafe_allow_html=True)

def apply_economic_chapter_background():
    """Apply economic-specific background styling for Chapter 2"""
    st.markdown("""
    <style>
        /* Economic Chapter Specific Background */
        .stApp {
            background: linear-gradient(135deg, #B8E6B8 0%, #C8EBC8 50%, #D8F0D8 100%) !important;
            background-attachment: fixed;
        }
    </style>
    """, unsafe_allow_html=True)

def apply_dance_styles():
    """Apply dance-specific CSS styling"""
    st.markdown("""
    <style>
        /* Dance Section Specific Styles */
        .dance-main-card {
            background: rgba(255,255,255,0.98);
            backdrop-filter: blur(15px);
            padding: 2rem;
            border-radius: 20px;
            margin: 2rem 0;
            box-shadow: 0 15px 35px rgba(0,128,128,0.2);
            border: 3px solid #008080;
            text-align: center;
        }

        .dance-main-title {
            font-family: 'Playfair Display', serif;
            font-size: 2rem;
            font-weight: 700;
            color: #008080;
            margin-bottom: 1rem;
        }

        .dance-main-image {
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,128,128,0.3);
            margin-bottom: 1.5rem;
            max-width: 100%;
            height: auto;
            border: 2px solid #20B2AA;
        }

        .dance-main-description {
            background: rgba(255,255,255,0.95);
            backdrop-filter: blur(10px);
            padding: 2rem;
            border-radius: 15px;
            margin: 2rem 0;
            border: 2px solid #008080;
            box-shadow: 0 8px 25px rgba(0,128,128,0.15);
            text-align: left;
        }

        .dance-main-description h3 {
            font-family: 'Playfair Display', serif;
            font-size: 1.5rem;
            font-weight: 700;
            color: #008080;
            margin-bottom: 1rem;
            text-align: center;
        }

        .dance-main-description p {
            font-family: 'Poppins', sans-serif;
            color: #333;
            line-height: 1.8;
            font-size: 1rem;
            text-align: justify;
        }

        .dance-description-card {
            background: rgba(255,255,255,0.95);
            backdrop-filter: blur(10px);
            padding: 1.5rem;
            border-radius: 15px;
            margin: 1rem 0;
            border: 2px solid #20B2AA;
            border-left: 6px solid #008080;
            box-shadow: 0 5px 15px rgba(0,128,128,0.1);
        }

        .dance-description-title {
            font-family: 'Poppins', sans-serif;
            font-size: 1.2rem;
            font-weight: 600;
            color: black;
            margin-bottom: 0.5rem;
        }

        .dance-description-text {
            font-family: 'Poppins', sans-serif;
            color: #333;
            line-height: 1.6;
            font-size: 0.95rem;
        }

        .dance-grid-card {
            background: rgba(255,255,255,0.95);
            backdrop-filter: blur(10px);
            padding: 1.5rem;
            border-radius: 15px;
            margin: 1rem 0;
            box-shadow: 0 8px 25px rgba(0,128,128,0.15);
            border: 2px solid #008080;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .dance-grid-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 35px rgba(0,128,128,0.25);
            border-color: #20B2AA;
        }

        .dance-grid-title {
            font-family: 'Poppins', sans-serif;
            font-size: 1.1rem;
            font-weight: 600;
            color: black;
            margin-bottom: 1rem;
            text-align: center;
        }

        .dance-grid-text {
            font-family: 'Poppins', sans-serif;
            color: #333;
            font-size: 0.9rem;
            line-height: 1.4;
            text-align: left;
        }

        /* Slideshow Styles */
        .dance-slideshow-container {
            background: rgba(255,255,255,0.98);
            backdrop-filter: blur(15px);
            padding: 2rem;
            border-radius: 20px;
            margin: 2rem 0;
            box-shadow: 0 15px 35px rgba(0,128,128,0.2);
            border: 2px solid #008080;
            text-align: center;
        }

        .dance-slideshow-title {
            font-family: 'Playfair Display', serif;
            font-size: 2rem;
            font-weight: 700;
            color: black;
            margin-bottom: 1rem;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        }
    </style>
    """, unsafe_allow_html=True)

def apply_sidebar_styles():
    """Apply sidebar-specific CSS styling"""
    st.markdown("""
    <style>
        /* Sidebar Styling */
        .css-1d391kg {
            background: linear-gradient(180deg, #008080 0%, #20B2AA 100%);
        }

        /* Remove white spaces */
        .css-18e3th9 {
            padding-top: 0;
        }

        .css-1d391kg .css-1v0mbdj {
            margin-top: 0;
        }

        /* Stats Grid */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin: 2rem 0;
        }

        /* Recovery Story Cards - Much Darker for Better Contrast */
        .recovery-metric-card {
            background: rgba(0,0,0,0.85) !important;
            backdrop-filter: blur(10px);
            padding: 1.5rem;
            border-radius: 15px;
            text-align: center;
            color: white !important;
            box-shadow: 0 8px 25px rgba(0,0,0,0.4);
            border: 1px solid rgba(255,255,255,0.3);
        }

        /* Strong override for all light background cards */
        div[style*="rgba(255,255,255,0.2)"],
        div[style*="background: rgba(255,255,255,0.2)"] {
            background: rgba(0,0,0,0.85) !important;
            color: white !important;
            border: 1px solid rgba(255,255,255,0.3) !important;
        }

        /* Ensure ALL text in recovery cards is white with strong specificity */
        div[style*="rgba(255,255,255,0.2)"] h5,
        div[style*="rgba(255,255,255,0.2)"] p,
        div[style*="rgba(255,255,255,0.2)"] h4,
        div[style*="rgba(255,255,255,0.2)"] span,
        div[style*="background: rgba(255,255,255,0.2)"] h5,
        div[style*="background: rgba(255,255,255,0.2)"] p,
        div[style*="background: rgba(255,255,255,0.2)"] h4,
        div[style*="background: rgba(255,255,255,0.2)"] span {
            color: white !important;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
        }

        /* Tourism overview cards - darker */
        div[style*="rgba(255,255,255,0.1)"],
        div[style*="background: rgba(255,255,255,0.1)"] {
            background: rgba(0,0,0,0.8) !important;
            color: white !important;
            border: 1px solid rgba(255,255,255,0.2) !important;
        }

        div[style*="rgba(255,255,255,0.1)"] h4,
        div[style*="rgba(255,255,255,0.1)"] p,
        div[style*="background: rgba(255,255,255,0.1)"] h4,
        div[style*="background: rgba(255,255,255,0.1)"] p {
            color: white !important;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
        }

        /* Additional override for any remaining light cards */
        .stColumn > div > div[style*="rgba(255,255,255"] {
            background: rgba(0,0,0,0.85) !important;
            color: white !important;
        }

        .stColumn > div > div[style*="rgba(255,255,255"] * {
            color: white !important;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .hero-title {
                font-size: 2.5rem;
            }
            .hero-subtitle {
                font-size: 1.1rem;
            }
            .hero-stats {
                flex-direction: column;
                gap: 1rem;
            }
        }
    </style>
    """, unsafe_allow_html=True)
