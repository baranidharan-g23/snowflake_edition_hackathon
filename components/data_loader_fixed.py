import streamlit as st
import pandas as pd

def get_snowflake_connection():
    """Get Snowflake connection"""
    return st.connection("snowflake")

def safe_query(query, description="data"):
    """Safely execute a query with proper error handling"""
    try:
        conn = get_snowflake_connection()
        return conn.query(query)
    except Exception as e:
        st.warning(f"Could not load {description}. Table may not exist or not be accessible.")
        print(f"Error executing query '{query}': {e}")
        return pd.DataFrame()

@st.cache_data
def load_festivals_data():
    """Load festivals data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.CULTURAL_DATA.FESTIVAL", "festivals data")

@st.cache_data
def load_dance_data():
    """Load dance forms data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.CULTURAL_DATA.DANCE_FORMS", "dance data")

@st.cache_data
def load_heritage_sites_data():
    """Load heritage sites data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.CULTURAL_DATA.HERITAGE_SITES", "heritage sites data")

@st.cache_data
def load_ita_data():
    """Load International Tourist Arrivals data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.ITA_YEARLY", "ITA data")

@st.cache_data
def load_ita_monthly_data():
    """Load monthly ITA data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.ITA_MONTHLY", "monthly ITA data")

@st.cache_data
def load_state_tourism_data():
    """Load state-wise tourism data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.STATE_WISE_TOURIST", "state tourism data")

@st.cache_data
def load_centrally_protected_data():
    """Load centrally protected monuments data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.CENTRALLY_PROTECTED", "centrally protected data")

@st.cache_data
def load_duration_stay_data():
    """Load tourist duration stay data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.DURATION_STAY", "duration stay data")

@st.cache_data
def load_fee_earnings_data():
    """Load foreign exchange earnings data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.FEE_EARNINGS", "fee earnings data")

@st.cache_data
def load_india_world_share_data():
    """Load India's world tourism share data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.INDIA_WORLD_SHARE", "India world share data")

@st.cache_data
def load_lean_peak_data():
    """Load lean and peak month data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.LEAN_PEAK_MONTH", "lean peak data")

@st.cache_data
def load_monthly_foreigners_data():
    """Load monthly foreigners arrival data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.MONTHLY_FOREIGNERS", "monthly foreigners data")

@st.cache_data
def load_state_footfall_data():
    """Load state-wise footfall data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.STATE_FOOTFALL", "state footfall data")

@st.cache_data
def load_top_monuments_data():
    """Load top 10 monuments data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.TOP_MONUMENTS", "top monuments data")

@st.cache_data
def load_age_statistics_data():
    """Load age-wise tourism statistics data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.AGE_STATISTICS", "age statistics data")

@st.cache_data
def load_tourism_gdp_data():
    """Load tourism GDP contribution data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.TOURISM_GDP", "tourism GDP data")

@st.cache_data
def load_tourism_employment_data():
    """Load tourism employment data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.TOURISM_EMPLOYMENT", "tourism employment data")

@st.cache_data
def load_unesco_sites_data():
    """Load UNESCO sites data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.CULTURAL_DATA.UNESCO_SITES", "UNESCO sites data")

# Image loading functions for Snowflake stages
@st.cache_data
def get_image_url_from_stage(stage_name, file_path):
    """Get presigned URL for image in Snowflake stage"""
    try:
        conn = get_snowflake_connection()
        query = f"SELECT GET_PRESIGNED_URL('@{stage_name}', '{file_path}') as image_url"
        result = conn.query(query)
        if not result.empty:
            return result.iloc[0]['IMAGE_URL']
        return None
    except Exception as e:
        st.error(f"Error getting image URL: {e}")
        return None

@st.cache_data
def get_available_images(stage_name):
    """Get list of all images in a stage"""
    try:
        conn = get_snowflake_connection()
        query = f"LIST '@{stage_name}'"
        result = conn.query(query)
        if not result.empty:
            return result['name'].tolist()
        return []
    except Exception as e:
        st.error(f"Error listing images: {e}")
        return []

def get_festival_image_url(festival_name):
    """Get festival image URL from Snowflake stage"""
    try:
        # Try different image formats
        for ext in ['.jpg', '.jpeg', '.png']:
            file_name = f"{festival_name.replace(' ', '_')}{ext}"
            image_url = get_image_url_from_stage('CULTURE_TOURISM_DB.ASSETS.FESTIVAL_IMAGES', file_name)
            if image_url:
                return image_url
        return None
    except Exception as e:
        return None

def get_dance_image_url(state_name, dance_name):
    """Get dance image URL from Snowflake stage"""
    try:
        # Try different naming conventions
        for ext in ['.jpg', '.jpeg', '.png']:
            file_name = f"{state_name.lower().replace(' ', '_')}_{dance_name.lower().replace(' ', '_')}{ext}"
            image_url = get_image_url_from_stage('CULTURE_TOURISM_DB.ASSETS.DANCE_IMAGES', file_name)
            if image_url:
                return image_url
        return None
    except Exception as e:
        return None

def get_heritage_image_url(city_name, heritage_name):
    """Get heritage image URL from Snowflake stage"""
    try:
        # Try different naming conventions
        for ext in ['.jpg', '.jpeg', '.png']:
            file_name = f"{city_name.upper()}_{heritage_name.replace(' ', '_')}{ext}"
            image_url = get_image_url_from_stage('CULTURE_TOURISM_DB.ASSETS.HERITAGE_IMAGES', file_name)
            if image_url:
                return image_url
        return None
    except Exception as e:
        return None

def clear_dance_cache():
    """Clear the cache for dance data"""
    load_dance_data.clear()

def clear_all_cache():
    """Clear all cached data"""
    load_festivals_data.clear()
    load_dance_data.clear()
    load_heritage_sites_data.clear()
    load_ita_data.clear()
    load_ita_monthly_data.clear()
    load_state_tourism_data.clear()
    load_centrally_protected_data.clear()
    load_duration_stay_data.clear()
    load_fee_earnings_data.clear()
    load_india_world_share_data.clear()
    load_lean_peak_data.clear()
    load_monthly_foreigners_data.clear()
    load_state_footfall_data.clear()
    load_top_monuments_data.clear()
    load_age_statistics_data.clear()
    load_tourism_gdp_data.clear()
    load_tourism_employment_data.clear()
    load_unesco_sites_data.clear()

# Additional functions for compatibility with existing code
def load_unesco_data():
    """Alias for load_unesco_sites_data for compatibility"""
    return load_unesco_sites_data()

def load_top_monuments_domestic_data():
    """Load top monuments domestic data - alias for compatibility"""
    return load_top_monuments_data()

def load_top_monuments_foreign_data():
    """Load top monuments foreign data - alias for compatibility"""
    return load_top_monuments_data()

def load_centrally_protected_domestic_data():
    """Load centrally protected domestic data - alias for compatibility"""
    return load_centrally_protected_data()

def load_centrally_protected_foreign_data():
    """Load centrally protected foreign data - alias for compatibility"""
    return load_centrally_protected_data()

def load_state_foreign_tourism_data():
    """Load state foreign tourism data - alias for compatibility"""
    return load_state_tourism_data()

def load_all_lean_peak_data():
    """Load all lean peak data - alias for compatibility"""
    return {'combined': load_lean_peak_data()}

def load_all_data():
    """Load all data and return as a dictionary"""
    return {
        'festivals_df': load_festivals_data(),
        'dance_df': load_dance_data(),
        'heritage_sites_df': load_heritage_sites_data(),
        'ita_df': load_ita_data(),
        'ita_monthly_df': load_ita_monthly_data(),
        'state_tourism_df': load_state_tourism_data(),
        'centrally_protected_df': load_centrally_protected_data(),
        'duration_stay_df': load_duration_stay_data(),
        'fee_earnings_df': load_fee_earnings_data(),
        'india_world_share_df': load_india_world_share_data(),
        'lean_peak_df': load_lean_peak_data(),
        'monthly_foreigners_df': load_monthly_foreigners_data(),
        'state_footfall_df': load_state_footfall_data(),
        'top_monuments_df': load_top_monuments_data(),
        'age_statistics_df': load_age_statistics_data(),
        'tourism_gdp_df': load_tourism_gdp_data(),
        'tourism_employment_df': load_tourism_employment_data(),
        'unesco_sites_df': load_unesco_sites_data()
    }
