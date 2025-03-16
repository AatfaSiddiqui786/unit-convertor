import streamlit as st
import pandas as pd
import base64
from PIL import Image
import io

# Set page configuration
st.set_page_config(
    page_title="VIP Ultimate Unit Converter",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def add_custom_css():
    st.markdown("""
    <style>
    /* Main container styling */
    .main {
    color: #FFD700;
    font-family: 'Arial', sans-serif;
    padding: 20px;
    border-radius: 10px;
    position: relative;
    overflow: hidden;
}

.main::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.7);
    z-index: 1;
}

.main > * {
    position: relative;
    z-index: 2;
}

#background-video {
    position: fixed;
    right: 0;
    bottom: 0;
    min-width: 100%;
    min-height: 100%;
    width: auto;
    height: auto;
    z-index: 0;
}
    
    /* Header styling */
    .header {
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #1c1c1c 0%, #2c2c2c 100%);
        color: #FFD700;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(255, 215, 0, 0.1);
    }
    
    .header h1 {
        font-size: 2.5rem;
        font-weight: 700;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
    }
    
    /* Card styling */
    .card {
        background-color: #1c1c1c;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(255, 215, 0, 0.1);
        margin-bottom: 20px;
        transition: transform 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
        color: #000000;
        border: none;
        padding: 10px 24px;
        border-radius: 5px;
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        padding: 10px;
        background-color: #1c1c1c;
        border-radius: 10px;
        margin-top: 20px;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .header h1 {
            font-size: 24px;
        }
        .card {
            padding: 15px;
        }
    }
    
    /* Category title styling */
    .category-title {
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
        color: #000000;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 15px;
        text-align: center;
    }
    
    /* Result styling */
    .result {
        background-color: #2c2c2c;
        padding: 15px;
        border-radius: 5px;
        font-weight: bold;
        text-align: center;
        margin-top: 15px;
        color: #FFD700;
    }
    
    /* Developer credit */
    .developer {
        font-style: italic;
        text-align: center;
        margin-top: 10px;
        color: #FFD700;
    }

    /* Input fields styling */
    .stNumberInput input, .stSelectbox div[data-baseweb="select"] div {
        background-color: #2c2c2c !important;
        color: #FFD700 !important;
        border-color: #FFD700 !important;
    }

    /* Label styling */
    .stNumberInput label, .stSelectbox label {
        color: #FFD700 !important;
    }

    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #1c1c1c !important;
    }

    .stTabs [data-baseweb="tab"] {
        color: #FFD700 !important;
    }

    .stTabs [aria-selected="true"] {
        background-color: #2c2c2c !important;
        color: #FFD700 !important;
    }

    /* Table styling */
    .stDataFrame {
        background-color: #1c1c1c !important;
    }

    .stDataFrame th {
        background-color: #2c2c2c !important;
        color: #FFD700 !important;
    }

    .stDataFrame td {
        color: #FFD700 !important;
    }

    /* Content wrapper for better readability */
    .content-wrapper {
        background-color: rgba(0, 0, 0, 0.7);
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

def add_background_video():
    st.markdown("""
    <video autoplay muted loop id="background-video">
        <source src="https://example.com/your-background-video.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    """, unsafe_allow_html=True)

# Conversion functions for different units
def convert_length(value, from_unit, to_unit):
    # Conversion to meters (base unit)
    length_to_meters = {
        "Nanometer (nm)": 1e-9,
        "Micrometer (μm)": 1e-6,
        "Millimeter (mm)": 1e-3,
        "Centimeter (cm)": 1e-2,
        "Decimeter (dm)": 1e-1,
        "Meter (m)": 1,
        "Kilometer (km)": 1e3,
        "Inch (in)": 0.0254,
        "Foot (ft)": 0.3048,
        "Yard (yd)": 0.9144,
        "Mile (mi)": 1609.344,
        "Nautical mile (nmi)": 1852
    }
    
    # Convert from input unit to meters, then to output unit
    meters = value * length_to_meters[from_unit]
    return meters / length_to_meters[to_unit]

def convert_weight(value, from_unit, to_unit):
    # Conversion to grams (base unit)
    weight_to_grams = {
        "Microgram (μg)": 1e-6,
        "Milligram (mg)": 1e-3,
        "Gram (g)": 1,
        "Kilogram (kg)": 1e3,
        "Metric ton (t)": 1e6,
        "Ounce (oz)": 28.34952,
        "Pound (lb)": 453.59237,
        "Stone (st)": 6350.29318,
        "US ton (short)": 907184.74,
        "Imperial ton (long)": 1016046.9088
    }
    
    # Convert from input unit to grams, then to output unit
    grams = value * weight_to_grams[from_unit]
    return grams / weight_to_grams[to_unit]

def convert_temperature(value, from_unit, to_unit):
    # Direct conversion formulas for temperature
    if from_unit == "Celsius (°C)":
        if to_unit == "Fahrenheit (°F)":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin (K)":
            return value + 273.15
        else:
            return value
    elif from_unit == "Fahrenheit (°F)":
        if to_unit == "Celsius (°C)":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin (K)":
            return (value - 32) * 5/9 + 273.15
        else:
            return value
    elif from_unit == "Kelvin (K)":
        if to_unit == "Celsius (°C)":
            return value - 273.15
        elif to_unit == "Fahrenheit (°F)":
            return (value - 273.15) * 9/5 + 32
        else:
            return value

def convert_area(value, from_unit, to_unit):
    # Conversion to square meters (base unit)
    area_to_sq_meters = {
        "Square millimeter (mm²)": 1e-6,
        "Square centimeter (cm²)": 1e-4,
        "Square meter (m²)": 1,
        "Hectare (ha)": 1e4,
        "Square kilometer (km²)": 1e6,
        "Square inch (in²)": 0.00064516,
        "Square foot (ft²)": 0.09290304,
        "Square yard (yd²)": 0.83612736,
        "Acre": 4046.8564224,
        "Square mile (mi²)": 2589988.110336
    }
    
    # Convert from input unit to square meters, then to output unit
    sq_meters = value * area_to_sq_meters[from_unit]
    return sq_meters / area_to_sq_meters[to_unit]

def convert_volume(value, from_unit, to_unit):
    # Conversion to liters (base unit)
    volume_to_liters = {
        "Milliliter (ml)": 1e-3,
        "Cubic centimeter (cm³)": 1e-3,
        "Liter (L)": 1,
        "Cubic meter (m³)": 1e3,
        "US teaspoon": 0.00492892,
        "US tablespoon": 0.01478676,
        "US fluid ounce (fl oz)": 0.02957353,
        "US cup": 0.2365882,
        "US pint": 0.4731765,
        "US quart": 0.9463529,
        "US gallon": 3.78541,
        "Imperial fluid ounce": 0.0284131,
        "Imperial pint": 0.56826125,
        "Imperial quart": 1.1365225,
        "Imperial gallon": 4.54609
    }
    
    # Convert from input unit to liters, then to output unit
    liters = value * volume_to_liters[from_unit]
    return liters / volume_to_liters[to_unit]

def convert_time(value, from_unit, to_unit):
    # Conversion to seconds (base unit)
    time_to_seconds = {
        "Nanosecond (ns)": 1e-9,
        "Microsecond (μs)": 1e-6,
        "Millisecond (ms)": 1e-3,
        "Second (s)": 1,
        "Minute (min)": 60,
        "Hour (h)": 3600,
        "Day (d)": 86400,
        "Week (wk)": 604800,
        "Month (avg)": 2629746,
        "Year (365 days)": 31536000,
        "Decade": 315360000,
        "Century": 3153600000
    }
    
    # Convert from input unit to seconds, then to output unit
    seconds = value * time_to_seconds[from_unit]
    return seconds / time_to_seconds[to_unit]

def convert_speed(value, from_unit, to_unit):
    # Conversion to meters per second (base unit)
    speed_to_mps = {
        "Meter per second (m/s)": 1,
        "Kilometer per hour (km/h)": 0.277778,
        "Mile per hour (mph)": 0.44704,
        "Foot per second (ft/s)": 0.3048,
        "Knot (kn)": 0.514444,
        "Mach (at sea level)": 340.29
    }
    
    # Convert from input unit to meters per second, then to output unit
    mps = value * speed_to_mps[from_unit]
    return mps / speed_to_mps[to_unit]

def convert_digital(value, from_unit, to_unit):
    # Conversion to bytes (base unit)
    digital_to_bytes = {
        "Bit": 0.125,
        "Byte": 1,
        "Kilobyte (KB)": 1e3,
        "Megabyte (MB)": 1e6,
        "Gigabyte (GB)": 1e9,
        "Terabyte (TB)": 1e12,
        "Petabyte (PB)": 1e15,
        "Kibibyte (KiB)": 1024,
        "Mebibyte (MiB)": 1048576,
        "Gibibyte (GiB)": 1073741824,
        "Tebibyte (TiB)": 1099511627776,
        "Pebibyte (PiB)": 1125899906842624
    }
    
    # Convert from input unit to bytes, then to output unit
    bytes_val = value * digital_to_bytes[from_unit]
    return bytes_val / digital_to_bytes[to_unit]

def convert_pressure(value, from_unit, to_unit):
    # Conversion to pascals (base unit)
    pressure_to_pascals = {
        "Pascal (Pa)": 1,
        "Kilopascal (kPa)": 1e3,
        "Megapascal (MPa)": 1e6,
        "Bar": 1e5,
        "Atmosphere (atm)": 101325,
        "Torr": 133.322,
        "Pound per square inch (psi)": 6894.76,
        "Millimeter of mercury (mmHg)": 133.322
    }
    
    # Convert from input unit to pascals, then to output unit
    pascals = value * pressure_to_pascals[from_unit]
    return pascals / pressure_to_pascals[to_unit]

def convert_energy(value, from_unit, to_unit):
    # Conversion to joules (base unit)
    energy_to_joules = {
        "Joule (J)": 1,
        "Kilojoule (kJ)": 1e3,
        "Calorie (cal)": 4.184,
        "Kilocalorie (kcal)": 4184,
        "Watt-hour (Wh)": 3600,
        "Kilowatt-hour (kWh)": 3.6e6,
        "Electronvolt (eV)": 1.602176634e-19,
        "British Thermal Unit (BTU)": 1055.06,
        "Foot-pound (ft⋅lb)": 1.355818
    }
    
    # Convert from input unit to joules, then to output unit
    joules = value * energy_to_joules[from_unit]
    return joules / energy_to_joules[to_unit]

def convert_fuel_economy(value, from_unit, to_unit):
    # For fuel economy, we'll convert everything to kilometers per liter
    fuel_economy_to_kpl = {
        "Miles per gallon (US)": 0.425144,
        "Miles per gallon (Imperial)": 0.354006,
        "Kilometers per liter (km/L)": 1,
        "Liters per 100 kilometers (L/100km)": lambda x: 100/x
    }
    
    # Special handling for L/100km which is inversely related to other units
    if from_unit == "Liters per 100 kilometers (L/100km)":
        kpl = 100 / value
    else:
        kpl = value * fuel_economy_to_kpl[from_unit]
    
    if to_unit == "Liters per 100 kilometers (L/100km)":
        return 100 / kpl
    else:
        return kpl / fuel_economy_to_kpl[to_unit]

def convert_angle(value, from_unit, to_unit):
    # Conversion to radians (base unit)
    angle_to_radians = {
        "Degree (°)": 0.0174533,
        "Radian (rad)": 1,
        "Gradian (grad)": 0.015708,
        "Arcminute (′)": 0.000290888,
        "Arcsecond (″)": 4.84814e-6,
        "Turn/Cycle": 6.28319
    }
    
    # Convert from input unit to radians, then to output unit
    radians = value * angle_to_radians[from_unit]
    return radians / angle_to_radians[to_unit]

# Define unit categories and their units
unit_categories = {
    "Length": {
        "units": [
            "Nanometer (nm)", "Micrometer (μm)", "Millimeter (mm)", "Centimeter (cm)", 
            "Decimeter (dm)", "Meter (m)", "Kilometer (km)", "Inch (in)", "Foot (ft)", 
            "Yard (yd)", "Mile (mi)", "Nautical mile (nmi)"
        ],
        "convert_function": convert_length,
        "icon": "📏"
    },
    "Weight/Mass": {
        "units": [
            "Microgram (μg)", "Milligram (mg)", "Gram (g)", "Kilogram (kg)", 
            "Metric ton (t)", "Ounce (oz)", "Pound (lb)", "Stone (st)", 
            "US ton (short)", "Imperial ton (long)"
        ],
        "convert_function": convert_weight,
        "icon": "⚖️"
    },
    "Temperature": {
        "units": ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"],
        "convert_function": convert_temperature,
        "icon": "🌡️"
    },
    "Area": {
        "units": [
            "Square millimeter (mm²)", "Square centimeter (cm²)", "Square meter (m²)", 
            "Hectare (ha)", "Square kilometer (km²)", "Square inch (in²)", 
            "Square foot (ft²)", "Square yard (yd²)", "Acre", "Square mile (mi²)"
        ],
        "convert_function": convert_area,
        "icon": "📐"
    },
    "Volume": {
        "units": [
            "Milliliter (ml)", "Cubic centimeter (cm³)", "Liter (L)", "Cubic meter (m³)", 
            "US teaspoon", "US tablespoon", "US fluid ounce (fl oz)", "US cup", 
            "US pint", "US quart", "US gallon", "Imperial fluid ounce", 
            "Imperial pint", "Imperial quart", "Imperial gallon"
        ],
        "convert_function": convert_volume,
        "icon": "🧪"
    },
    "Time": {
        "units": [
            "Nanosecond (ns)", "Microsecond (μs)", "Millisecond (ms)", "Second (s)", 
            "Minute (min)", "Hour (h)", "Day (d)", "Week (wk)", "Month (avg)", 
            "Year (365 days)", "Decade", "Century"
        ],
        "convert_function": convert_time,
        "icon": "⏱️"
    },
    "Speed": {
        "units": [
            "Meter per second (m/s)", "Kilometer per hour (km/h)", "Mile per hour (mph)", 
            "Foot per second (ft/s)", "Knot (kn)", "Mach (at sea level)"
        ],
        "convert_function": convert_speed,
        "icon": "🚀"
    },
    "Digital Storage": {
        "units": [
            "Bit", "Byte", "Kilobyte (KB)", "Megabyte (MB)", "Gigabyte (GB)", 
            "Terabyte (TB)", "Petabyte (PB)", "Kibibyte (KiB)", "Mebibyte (MiB)", 
            "Gibibyte (GiB)", "Tebibyte (TiB)", "Pebibyte (PiB)"
        ],
        "convert_function": convert_digital,
        "icon": "💾"
    },
    "Pressure": {
        "units": [
            "Pascal (Pa)", "Kilopascal (kPa)", "Megapascal (MPa)", "Bar", 
            "Atmosphere (atm)", "Torr", "Pound per square inch (psi)", 
            "Millimeter of mercury (mmHg)"
        ],
        "convert_function": convert_pressure,
        "icon": "🔄"
    },
    "Energy": {
        "units": [
            "Joule (J)", "Kilojoule (kJ)", "Calorie (cal)", "Kilocalorie (kcal)", 
            "Watt-hour (Wh)", "Kilowatt-hour (kWh)", "Electronvolt (eV)", 
            "British Thermal Unit (BTU)", "Foot-pound (ft⋅lb)"
        ],
        "convert_function": convert_energy,
        "icon": "⚡"
    },
    "Fuel Economy": {
        "units": [
            "Miles per gallon (US)", "Miles per gallon (Imperial)", 
            "Kilometers per liter (km/L)", "Liters per 100 kilometers (L/100km)"
        ],
        "convert_function": convert_fuel_economy,
        "icon": "🚗"
    },
    "Angle": {
        "units": [
            "Degree (°)", "Radian (rad)", "Gradian (grad)", 
            "Arcminute (′)", "Arcsecond (″)", "Turn/Cycle"
        ],
        "convert_function": convert_angle,
        "icon": "📐"
    }
}

# Function to create the home page
def home_page():
    st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
    st.markdown('<div class="header"><h1>VIP Ultimate Unit Converter</h1></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("""
        <h2 style="text-align: center; color: #FFD700;">Welcome to the VIP Unit Converter</h2>
        <p style="text-align: center; color: #FFD700;">A luxury tool for converting between different units of measurement.</p>
        <p style="text-align: center; color: #FFD700;">Explore our premium conversion categories:</p>
        """, unsafe_allow_html=True)
        
        cols = st.columns(3)
        for i, (category, info) in enumerate(unit_categories.items()):
            with cols[i % 3]:
                st.markdown(f"""
                <div style="text-align: center; margin-bottom: 15px;">
                    <div style="font-size: 24px;">{info['icon']}</div>
                    <div style="color: #FFD700;">{category}</div>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("✨ OPEN LUXURY CONVERTER ✨", key="open_converter"):
            st.session_state.page = "converter"
            st.rerun()
        
        st.markdown('<div class="developer">Developed by Aatfa Siddiqui</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Function to create the converter page
def converter_page():
    st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
    st.markdown('<div class="header"><h1>VIP Ultimate Unit Converter</h1></div>', unsafe_allow_html=True)
    
    if st.button("← Back to Home", key="back_home"):
        st.session_state.page = "home"
        st.rerun()
    
    tabs = st.tabs([f"{info['icon']} {category}" for category, info in unit_categories.items()])
    
    for i, (category, info) in enumerate(unit_categories.items()):
        with tabs[i]:
            st.markdown(f'<div class="category-title"><h3>{category} Converter</h3></div>', unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                value = st.number_input(f"Enter {category} value:", value=1.0, key=f"value_{category}")
                from_unit = st.selectbox("From unit:", options=info["units"], index=0, key=f"from_{category}")
            
            with col2:
                st.text(" ")
                st.text(" ")
                to_unit = st.selectbox("To unit:", options=info["units"], index=1 if len(info["units"]) > 1 else 0, key=f"to_{category}")
            
            if from_unit and to_unit:
                try:
                    result = info["convert_function"](value, from_unit, to_unit)
                    result_str = f"{result:.6e}" if abs(result) >= 1e6 or abs(result) <= 1e-6 and result != 0 else f"{result:.6g}"
                    
                    st.markdown(f"""
                    <div class="result">
                        {value} {from_unit} = {result_str} {to_unit}
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown("<h4 style='color: #FFD700; margin-top: 20px;'>VIP Conversion Table</h4>", unsafe_allow_html=True)
                    
                    if value != 0:
                        multipliers = [0.01, 0.1, 0.5, 1, 2, 5, 10, 100]
                        values = [value * m for m in multipliers]
                    else:
                        values = [0, 1, 2, 5, 10, 100]
                    
                    df = pd.DataFrame({
                        f"{from_unit}": values,
                        f"{to_unit}": [info["convert_function"](v, from_unit, to_unit) for v in values]
                    })
                    
                    for col in df.columns:
                        df[col] = df[col].apply(lambda x: f"{x:.6g}" if abs(x) >= 1e-6 and abs(x) < 1e6 else f"{x:.6e}")
                    
                    st.dataframe(df, use_container_width=True)
                    
                except Exception as e:
                    st.error(f"Error in conversion: {e}")
            
            st.markdown("<h4 style='color: #FFD700; margin-top: 20px;'>Conversion Formula</h4>", unsafe_allow_html=True)
            
            if category == "Temperature":
                formula = get_temperature_formula(from_unit, to_unit)
            else:
                formula = f"Conversion factor: 1 {from_unit} = {info['convert_function'](1, from_unit, to_unit):.6g} {to_unit}"
            
            st.markdown(f"<div style='background-color: #2c2c2c; padding: 10px; border-radius: 5px; color: #FFD700;'>{formula}</div>", unsafe_allow_html=True)
    
    st.markdown('<div class="developer">Developed by Aatfa Siddiqui</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def get_temperature_formula(from_unit, to_unit):
    formulas = {
        ("Celsius (°C)", "Fahrenheit (°F)"): "°F = (°C × 9/5) + 32",
        ("Fahrenheit (°F)", "Celsius (°C)"): "°C = (°F - 32) × 5/9",
        ("Celsius (°C)", "Kelvin (K)"): "K = °C + 273.15",
        ("Kelvin (K)", "Celsius (°C)"): "°C = K - 273.15",
        ("Fahrenheit (°F)", "Kelvin (K)"): "K = (°F - 32) × 5/9 + 273.15",
        ("Kelvin (K)", "Fahrenheit (°F)"): "°F = (K - 273.15) × 9/5 + 32"
    }
    return formulas.get((from_unit, to_unit), "Direct conversion (same unit)")

# Main function
def main():
    # Add custom CSS
    add_custom_css()
    
    # Add background video
    add_background_video()
    
    # Initialize session state for page navigation if not already set
    if 'page' not in st.session_state:
        st.session_state.page = "home"
    
    # Display the appropriate page based on session state
    if st.session_state.page == "home":
        home_page()
    else:
        converter_page()

if __name__ == "__main__":
    main()

