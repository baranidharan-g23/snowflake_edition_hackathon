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

# Cultural Data Tables
@st.cache_data
def load_festivals_data():
    """Load festivals data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.CULTURAL_DATA.FESTIVALS", "festivals data")

@st.cache_data
def load_dance_data():
    """Load dance forms data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.CULTURAL_DATA.DANCE_FORMS", "dance data")

@st.cache_data
def load_heritage_sites_data():
    """Load heritage sites data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.CULTURAL_DATA.HERITAGE_SITES", "heritage sites data")

# Tourism Data Tables
@st.cache_data
def load_age_wise_statistics_data():
    """Load age-wise statistics data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.AGE_WISE_STATISTICS", "age-wise statistics data")

@st.cache_data
def load_centrally_protected_domestic_data():
    """Load centrally protected monuments domestic data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.CENTRALLY_PROTECTED_MONUMENTS_DOMESTIC_VISITS", "centrally protected domestic data")

@st.cache_data
def load_centrally_protected_foreign_data():
    """Load centrally protected monuments foreign data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.CENTRALLY_PROTECTED_MONUMENTS_FOREIGN_VISITS", "centrally protected foreign data")

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
def load_ita_monthwise_data():
    """Load ITA monthwise data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.ITA_MONTHWISE", "ITA monthwise data")

@st.cache_data
def load_ita_yearly_data():
    """Load ITA yearly data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.ITA_YEARLY", "ITA yearly data")

@st.cache_data
def load_state_domestic_tourist_arrivals_data():
    """Load state domestic tourist arrivals data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.STATE_DOMESTIC_TOURIST_ARRIVAL", "state domestic tourist arrivals data")

@st.cache_data
def load_state_foreign_tourist_arrivals_data():
    """Load state foreign tourist arrivals data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.STATE_FOREIGN_TOURIST_ARRIVAL", "state foreign tourist arrivals data")

@st.cache_data
def load_state_total_tourist_arrivals_data():
    """Load state total tourist arrivals data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.STATE_TOTAL_TOURIST_ARRIVAL", "state total tourist arrivals data")

@st.cache_data
def load_top_monuments_domestic_data():
    """Load top monuments domestic data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.TOP_MONUMENTS_DOMESTIC_VISITORS", "top monuments domestic data")

@st.cache_data
def load_top_monuments_foreign_data():
    """Load top monuments foreign data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.TOP_MONUMENTS_FOREIGN_VISITS", "top monuments foreign data")

@st.cache_data
def load_tourism_employment_data():
    """Load tourism employment data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.TOURISM_EMPLOYMENT", "tourism employment data")

@st.cache_data
def load_tourism_gdp_data():
    """Load tourism GDP contribution data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.TOURISM_GDP", "tourism GDP data")

@st.cache_data
def load_unesco_sites_data():
    """Load UNESCO sites data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.UNESCO_SITES", "UNESCO sites data")

# Year-wise Lean Peak Month Data
@st.cache_data
def load_y2017_lean_peak_month_data():
    """Load 2017 lean peak month data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.Y2017_LEAN_PEAK_MONTH", "2017 lean peak month data")

@st.cache_data
def load_y2018_lean_peak_month_data():
    """Load 2018 lean peak month data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.Y2018_LEAN_PEAK_MONTH", "2018 lean peak month data")

@st.cache_data
def load_y2019_lean_peak_month_data():
    """Load 2019 lean peak month data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.Y2019_LEAN_PEAK_MONTH", "2019 lean peak month data")

@st.cache_data
def load_y2020_lean_peak_month_data():
    """Load 2020 lean peak month data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.Y2020_LEAN_PEAK_MONTH", "2020 lean peak month data")

@st.cache_data
def load_y2021_lean_peak_month_data():
    """Load 2021 lean peak month data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.Y2021_LEAN_PEAK_MONTH", "2021 lean peak month data")

@st.cache_data
def load_y2022_lean_peak_month_data():
    """Load 2022 lean peak month data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.Y2022_LEAN_PEAK_MONTH", "2022 lean peak month data")

@st.cache_data
def load_y2023_lean_peak_month_data():
    """Load 2023 lean peak month data from Snowflake"""
    return safe_query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.Y2023_LEAN_PEAK_MONTH", "2023 lean peak month data")

# Image loading functions for Snowflake stages
@st.cache_data
def get_image_url_from_stage(stage_name, file_path):
    """Get presigned URL for image in Snowflake stage"""
    try:
        conn = get_snowflake_connection()
        # Use the stage name as provided (should include @ prefix)
        query = f"SELECT GET_PRESIGNED_URL('{stage_name}', '{file_path}') as image_url"
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
        # Use the stage name as provided (should include @ prefix)
        query = f"LIST '{stage_name}'"
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
            image_url = get_image_url_from_stage('@"CULTURE_TOURISM_DB"."ASSETS"."FESTIVAL_IMAGES_STAGE"', file_name)
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
            image_url = get_image_url_from_stage('@"CULTURE_TOURISM_DB"."ASSETS"."DANCE_IMAGES_STAGE"', file_name)
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
            image_url = get_image_url_from_stage('@"CULTURE_TOURISM_DB"."ASSETS"."HERITAGE_IMAGES_STAGE"', file_name)
            if image_url:
                return image_url
        return None
    except Exception as e:
        return None

def get_dance_image_from_stage(stage_name, file_name):
    """Get dance image URL from Snowflake stage - compatibility function"""
    try:
        # Map the old stage name to the new full stage name
        if stage_name == "DANCE_IMAGES":
            full_stage_name = '@"CULTURE_TOURISM_DB"."ASSETS"."DANCE_IMAGES_STAGE"'
        elif stage_name == "FESTIVAL_IMAGES":
            full_stage_name = '@"CULTURE_TOURISM_DB"."ASSETS"."FESTIVAL_IMAGES_STAGE"'
        elif stage_name == "HERITAGE_IMAGES":
            full_stage_name = '@"CULTURE_TOURISM_DB"."ASSETS"."HERITAGE_IMAGES_STAGE"'
        else:
            full_stage_name = f'@"CULTURE_TOURISM_DB"."ASSETS"."{stage_name}_STAGE"'

        return get_image_url_from_stage(full_stage_name, file_name)
    except Exception as e:
        st.error(f"Error getting dance image from stage: {e}")
        return None

def clear_dance_cache():
    """Clear the cache for dance data"""
    load_dance_data.clear()

def clear_cultural_cache():
    """Clear cache for cultural data only"""
    load_dance_data.clear()
    load_festivals_data.clear()
    load_heritage_sites_data.clear()

def clear_all_cache():
    """Clear all cached data"""
    # Cultural Data
    load_festivals_data.clear()
    load_dance_data.clear()
    load_heritage_sites_data.clear()

    # Tourism Data
    load_age_wise_statistics_data.clear()
    load_centrally_protected_domestic_data.clear()
    load_centrally_protected_foreign_data.clear()
    load_duration_stay_data.clear()
    load_fee_earnings_data.clear()
    load_india_world_share_data.clear()
    load_ita_monthwise_data.clear()
    load_ita_yearly_data.clear()
    load_state_domestic_tourist_arrivals_data.clear()
    load_state_foreign_tourist_arrivals_data.clear()
    load_state_total_tourist_arrivals_data.clear()
    load_top_monuments_domestic_data.clear()
    load_top_monuments_foreign_data.clear()
    load_tourism_employment_data.clear()
    load_tourism_gdp_data.clear()
    load_unesco_sites_data.clear()

    # Year-wise Lean Peak Data
    load_y2017_lean_peak_month_data.clear()
    load_y2018_lean_peak_month_data.clear()
    load_y2019_lean_peak_month_data.clear()
    load_y2020_lean_peak_month_data.clear()
    load_y2021_lean_peak_month_data.clear()
    load_y2022_lean_peak_month_data.clear()
    load_y2023_lean_peak_month_data.clear()

# Additional functions for compatibility with existing code
def load_unesco_data():
    """Alias for load_unesco_sites_data for compatibility"""
    return load_unesco_sites_data()

def load_ita_data():
    """Alias for load_ita_yearly_data for compatibility"""
    return load_ita_yearly_data()

def load_ita_monthly_data():
    """Alias for load_ita_monthwise_data for compatibility"""
    return load_ita_monthwise_data()

def load_age_statistics_data():
    """Alias for load_age_wise_statistics_data for compatibility"""
    return load_age_wise_statistics_data()

def load_centrally_protected_data():
    """Load combined centrally protected data for compatibility"""
    domestic_df = load_centrally_protected_domestic_data()
    foreign_df = load_centrally_protected_foreign_data()
    return pd.concat([domestic_df, foreign_df], ignore_index=True) if not domestic_df.empty and not foreign_df.empty else domestic_df if not domestic_df.empty else foreign_df

def load_top_monuments_data():
    """Load combined top monuments data for compatibility"""
    domestic_df = load_top_monuments_domestic_data()
    foreign_df = load_top_monuments_foreign_data()
    return pd.concat([domestic_df, foreign_df], ignore_index=True) if not domestic_df.empty and not foreign_df.empty else domestic_df if not domestic_df.empty else foreign_df

def load_state_tourism_data():
    """Load combined state tourism data for compatibility"""
    domestic_df = load_state_domestic_tourist_arrivals_data()
    foreign_df = load_state_foreign_tourist_arrivals_data()
    total_df = load_state_total_tourist_arrivals_data()
    return total_df if not total_df.empty else pd.concat([domestic_df, foreign_df], ignore_index=True) if not domestic_df.empty and not foreign_df.empty else domestic_df if not domestic_df.empty else foreign_df

def load_all_lean_peak_data():
    """Load all lean peak data by year"""
    return {
        '2017': load_y2017_lean_peak_month_data(),
        '2018': load_y2018_lean_peak_month_data(),
        '2019': load_y2019_lean_peak_month_data(),
        '2020': load_y2020_lean_peak_month_data(),
        '2021': load_y2021_lean_peak_month_data(),
        '2022': load_y2022_lean_peak_month_data(),
        '2023': load_y2023_lean_peak_month_data()
    }

def load_all_data():
    """Load all data and return as a dictionary"""
    return {
        # Cultural Data
        'festivals_df': load_festivals_data(),
        'dance_df': load_dance_data(),
        'heritage_sites_df': load_heritage_sites_data(),

        # Tourism Data
        'age_wise_statistics_df': load_age_wise_statistics_data(),
        'centrally_protected_domestic_df': load_centrally_protected_domestic_data(),
        'centrally_protected_foreign_df': load_centrally_protected_foreign_data(),
        'duration_stay_df': load_duration_stay_data(),
        'fee_earnings_df': load_fee_earnings_data(),
        'india_world_share_df': load_india_world_share_data(),
        'ita_monthwise_df': load_ita_monthwise_data(),
        'ita_yearly_df': load_ita_yearly_data(),
        'state_domestic_tourist_arrivals_df': load_state_domestic_tourist_arrivals_data(),
        'state_foreign_tourist_arrivals_df': load_state_foreign_tourist_arrivals_data(),
        'state_total_tourist_arrivals_df': load_state_total_tourist_arrivals_data(),
        'top_monuments_domestic_df': load_top_monuments_domestic_data(),
        'top_monuments_foreign_df': load_top_monuments_foreign_data(),
        'tourism_employment_df': load_tourism_employment_data(),
        'tourism_gdp_df': load_tourism_gdp_data(),
        'unesco_sites_df': load_unesco_sites_data(),

        # Year-wise Lean Peak Data
        'y2017_lean_peak_df': load_y2017_lean_peak_month_data(),
        'y2018_lean_peak_df': load_y2018_lean_peak_month_data(),
        'y2019_lean_peak_df': load_y2019_lean_peak_month_data(),
        'y2020_lean_peak_df': load_y2020_lean_peak_month_data(),
        'y2021_lean_peak_df': load_y2021_lean_peak_month_data(),
        'y2022_lean_peak_df': load_y2022_lean_peak_month_data(),
        'y2023_lean_peak_df': load_y2023_lean_peak_month_data(),

        # Combined/Compatibility Data
        'ita_df': load_ita_data(),  # Alias for yearly
        'ita_monthly_df': load_ita_monthly_data(),  # Alias for monthwise
        'state_tourism_df': load_state_tourism_data(),  # Combined state data
        'centrally_protected_df': load_centrally_protected_data(),  # Combined protected data
        'top_monuments_df': load_top_monuments_data(),  # Combined monuments data
        'age_statistics_df': load_age_statistics_data(),  # Alias for age wise
        'lean_peak_all_years': load_all_lean_peak_data()  # All years lean peak data
    }
