import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Modern Unit Converter",
    page_icon="🔄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Add heading with your name
st.markdown("## Developed by Aatfa Siddiqui", unsafe_allow_html=True)

# st.markdown("<h2 style='text-align: center;'>Developed by Aatfa Siddiqui</h2>", unsafe_allow_html=True)

# Custom CSS
def add_custom_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    
    body {
        font-family: 'Roboto', sans-serif;
        background-color: #1a1a1a;
        color: #ffffff;
    }
    
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    
    h1, h2, h3 {
        color: #00ffff;
        text-align: center;
    }
    
    .stButton > button {
        background-color: #00ffff;
        color: #1a1a1a;
        font-weight: bold;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #ff00ff;
        color: #ffffff;
    }
    
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input {
        background-color: #2a2a2a;
        color: #ffffff;
        border: 1px solid #00ffff;
        border-radius: 5px;
    }
    
    .stSelectbox > div > div > div {
        background-color: #2a2a2a;
        color: #ffffff;
        border: 1px solid #00ffff;
        border-radius: 5px;
    }
    
    .result {
        background-color: #2a2a2a;
        color: #00ffff;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 24px;
        margin-top: 20px;
        box-shadow: 0 0 10px #00ffff;
    }
    
    .category-card {
        background-color: #2a2a2a;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .category-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 15px rgba(0, 255, 255, 0.3);
    }
    
    .category-icon {
        font-size: 48px;
        margin-bottom: 10px;
    }
    
    .footer {
        text-align: center;
        margin-top: 50px;
        color: #888888;
    }
    
    /* Neon text effect */
    .neon-text {
        color: #fff;
        text-shadow:
            0 0 7px #fff,
            0 0 10px #fff,
            0 0 21px #fff,
            0 0 42px #0fa,
            0 0 82px #0fa,
            0 0 92px #0fa,
            0 0 102px #0fa,
            0 0 151px #0fa;
    }
    </style>
    """, unsafe_allow_html=True)

# Conversion functions
def convert_length(value, from_unit, to_unit):
    # Conversion factors to meters
    length_to_meters = {
        "Millimeter": 0.001,
        "Centimeter": 0.01,
        "Meter": 1,
        "Kilometer": 1000,
        "Inch": 0.0254,
        "Foot": 0.3048,
        "Yard": 0.9144,
        "Mile": 1609.34,
        "Nanometer": 1e-9,
        "Micrometer": 1e-6,
        "Decimeter": 0.1,
        "Nautical Mile": 1852,
        "Light Year": 9.461e+15,
        "Parsec": 3.086e+16,
        "Astronomical Unit": 1.496e+11,
        "Hand": 0.1016,
        "Fathom": 1.8288,
        "Furlong": 201.168,
        "League": 4828.03
    }
    return value * length_to_meters[from_unit] / length_to_meters[to_unit]

def convert_weight(value, from_unit, to_unit):
    # Conversion factors to grams
    weight_to_grams = {
        "Milligram": 0.001,
        "Gram": 1,
        "Kilogram": 1000,
        "Ounce": 28.3495,
        "Pound": 453.592,
        "Stone": 6350.29,
        "Ton (Metric)": 1e+6,
        "Ton (US)": 907185,
        "Ton (UK)": 1016050,
        "Carat": 0.2,
        "Grain": 0.0648,
        "Dram": 1.772,
        "Hundredweight (US)": 45359.2,
        "Hundredweight (UK)": 50802.3,
        "Microgram": 1e-6,
        "Atomic Mass Unit": 1.66053886e-24
    }
    return value * weight_to_grams[from_unit] / weight_to_grams[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
        elif to_unit == "Rankine":
            return (value + 273.15) * 9/5
        elif to_unit == "Réaumur":
            return value * 4/5
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif to_unit == "Rankine":
            return value + 459.67
        elif to_unit == "Réaumur":
            return (value - 32) * 4/9
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        elif to_unit == "Rankine":
            return value * 9/5
        elif to_unit == "Réaumur":
            return (value - 273.15) * 4/5
    elif from_unit == "Rankine":
        if to_unit == "Celsius":
            return (value - 491.67) * 5/9
        elif to_unit == "Fahrenheit":
            return value - 459.67
        elif to_unit == "Kelvin":
            return value * 5/9
        elif to_unit == "Réaumur":
            return (value - 491.67) * 4/9
    elif from_unit == "Réaumur":
        if to_unit == "Celsius":
            return value * 5/4
        elif to_unit == "Fahrenheit":
            return value * 9/4 + 32
        elif to_unit == "Kelvin":
            return value * 5/4 + 273.15
        elif to_unit == "Rankine":
            return value * 9/4 + 491.67
    return value

def convert_volume(value, from_unit, to_unit):
    # Conversion factors to liters
    volume_to_liters = {
        "Milliliter": 0.001,
        "Liter": 1,
        "Cubic Meter": 1000,
        "Fluid Ounce (US)": 0.0295735,
        "Cup (US)": 0.236588,
        "Pint (US)": 0.473176,
        "Quart (US)": 0.946353,
        "Gallon (US)": 3.78541,
        "Cubic Centimeter": 0.001,
        "Cubic Inch": 0.0163871,
        "Cubic Foot": 28.3168,
        "Cubic Yard": 764.555,
        "Teaspoon (US)": 0.00492892,
        "Tablespoon (US)": 0.0147868,
        "Fluid Ounce (UK)": 0.0284131,
        "Pint (UK)": 0.568261,
        "Quart (UK)": 1.13652,
        "Gallon (UK)": 4.54609,
        "Barrel (Oil)": 158.987,
        "Barrel (US)": 119.240,
        "Barrel (UK)": 163.659
    }
    return value * volume_to_liters[from_unit] / volume_to_liters[to_unit]

def convert_time(value, from_unit, to_unit):
    # Conversion factors to seconds
    time_to_seconds = {
        "Second": 1,
        "Minute": 60,
        "Hour": 3600,
        "Day": 86400,
        "Week": 604800,
        "Month (30 days)": 2592000,
        "Year (365 days)": 31536000,
        "Millisecond": 0.001,
        "Microsecond": 1e-6,
        "Nanosecond": 1e-9,
        "Picosecond": 1e-12,
        "Decade": 315360000,
        "Century": 3153600000,
        "Millennium": 31536000000,
        "Fortnight": 1209600
    }
    return value * time_to_seconds[from_unit] / time_to_seconds[to_unit]

def convert_area(value, from_unit, to_unit):
    # Conversion factors to square meters
    area_to_sq_meters = {
        "Square Millimeter": 1e-6,
        "Square Centimeter": 1e-4,
        "Square Meter": 1,
        "Square Kilometer": 1e+6,
        "Square Inch": 0.00064516,
        "Square Foot": 0.092903,
        "Square Yard": 0.836127,
        "Square Mile": 2.59e+6,
        "Acre": 4046.86,
        "Hectare": 10000,
        "Are": 100,
        "Barn": 1e-28,
        "Homestead": 647497.027584
    }
    return value * area_to_sq_meters[from_unit] / area_to_sq_meters[to_unit]

def convert_speed(value, from_unit, to_unit):
    # Conversion factors to meters per second
    speed_to_mps = {
        "Meter per Second": 1,
        "Kilometer per Hour": 0.277778,
        "Mile per Hour": 0.44704,
        "Knot": 0.514444,
        "Foot per Second": 0.3048,
        "Inch per Second": 0.0254,
        "Speed of Light": 299792458,
        "Speed of Sound (Air)": 343,
        "Mach (at std. atmosphere)": 343
    }
    return value * speed_to_mps[from_unit] / speed_to_mps[to_unit]

def convert_pressure(value, from_unit, to_unit):
    # Conversion factors to pascals
    pressure_to_pascal = {
        "Pascal": 1,
        "Kilopascal": 1000,
        "Megapascal": 1e+6,
        "Bar": 1e+5,
        "Atmosphere": 101325,
        "Torr": 133.322,
        "Pound per Square Inch": 6894.76,
        "Pound per Square Foot": 47.8803,
        "Millimeter of Mercury": 133.322
    }
    return value * pressure_to_pascal[from_unit] / pressure_to_pascal[to_unit]

def convert_energy(value, from_unit, to_unit):
    # Conversion factors to joules
    energy_to_joules = {
        "Joule": 1,
        "Kilojoule": 1000,
        "Calorie": 4.184,
        "Kilocalorie": 4184,
        "Watt Hour": 3600,
        "Kilowatt Hour": 3.6e+6,
        "Electron Volt": 1.602e-19,
        "British Thermal Unit": 1055.06,
        "US Therm": 1.055e+8,
        "Foot-Pound": 1.35582
    }
    return value * energy_to_joules[from_unit] / energy_to_joules[to_unit]

def convert_power(value, from_unit, to_unit):
    # Conversion factors to watts
    power_to_watts = {
        "Watt": 1,
        "Kilowatt": 1000,
        "Megawatt": 1e+6,
        "Horsepower (Mechanical)": 745.7,
        "Horsepower (Metric)": 735.5,
        "Foot-Pound per Second": 1.35582,
        "BTU per Hour": 0.293071,
        "Calorie per Second": 4.184
    }
    return value * power_to_watts[from_unit] / power_to_watts[to_unit]

def convert_data(value, from_unit, to_unit):
    # Conversion factors to bytes
    data_to_bytes = {
        "Bit": 0.125,
        "Byte": 1,
        "Kilobit": 125,
        "Kilobyte": 1000,
        "Megabit": 125000,
        "Megabyte": 1e+6,
        "Gigabit": 1.25e+8,
        "Gigabyte": 1e+9,
        "Terabit": 1.25e+11,
        "Terabyte": 1e+12,
        "Petabit": 1.25e+14,
        "Petabyte": 1e+15
    }
    return value * data_to_bytes[from_unit] / data_to_bytes[to_unit]

def convert_fuel_economy(value, from_unit, to_unit):
    # Conversion to kilometers per liter
    fuel_to_kpl = {
        "Miles per Gallon (US)": 0.425144,
        "Miles per Gallon (UK)": 0.354006,
        "Kilometers per Liter": 1,
        "Liters per 100 Kilometers": lambda x: 100 / x if x != 0 else float('inf')
    }
    
    # Special case for L/100km which is inverse
    if from_unit == "Liters per 100 Kilometers":
        kpl = 100 / value if value != 0 else float('inf')
    else:
        kpl = value * fuel_to_kpl[from_unit] if isinstance(fuel_to_kpl[from_unit], (int, float)) else fuel_to_kpl[from_unit](value)
    
    if to_unit == "Liters per 100 Kilometers":
        return 100 / kpl if kpl != 0 else float('inf')
    else:
        return kpl / (fuel_to_kpl[to_unit] if isinstance(fuel_to_kpl[to_unit], (int, float)) else 1)

def convert_angle(value, from_unit, to_unit):
    # Conversion factors to radians
    angle_to_radians = {
        "Degree": 0.0174533,
        "Radian": 1,
        "Gradian": 0.015708,
        "Minute of Arc": 0.000290888,
        "Second of Arc": 4.84814e-6,
        "Turn": 6.28319
    }
    return value * angle_to_radians[from_unit] / angle_to_radians[to_unit]

def convert_frequency(value, from_unit, to_unit):
    # Conversion factors to hertz
    frequency_to_hertz = {
        "Hertz": 1,
        "Kilohertz": 1000,
        "Megahertz": 1e+6,
        "Gigahertz": 1e+9,
        "Cycle per Second": 1,
        "RPM": 1/60,
        "Degree per Second": 1/360
    }
    return value * frequency_to_hertz[from_unit] / frequency_to_hertz[to_unit]

def convert_currency(value, from_unit, to_unit):
    # Example rates (would need to be updated with real-time data in a real app)
    currency_to_usd = {
        "USD": 1,
        "EUR": 1.09,
        "GBP": 1.27,
        "JPY": 0.0067,
        "CAD": 0.74,
        "AUD": 0.66,
        "CHF": 1.13,
        "CNY": 0.14,
        "INR": 0.012,
        "BRL": 0.18,
        "PKR": 0.00357588,
    }
    return value * currency_to_usd[from_unit] / currency_to_usd[to_unit]

# Unit categories
unit_categories = {
    "Length": {
        "units": ["Millimeter", "Centimeter", "Meter", "Kilometer", "Inch", "Foot", "Yard", "Mile", 
                 "Nanometer", "Micrometer", "Decimeter", "Nautical Mile", "Light Year", "Parsec", 
                 "Astronomical Unit", "Hand", "Fathom", "Furlong", "League"],
        "convert_function": convert_length,
        "icon": "📏"
    },
    "Weight": {
        "units": ["Milligram", "Gram", "Kilogram", "Ounce", "Pound", "Stone", "Ton (Metric)", 
                 "Ton (US)", "Ton (UK)", "Carat", "Grain", "Dram", "Hundredweight (US)", 
                 "Hundredweight (UK)", "Microgram", "Atomic Mass Unit"],
        "convert_function": convert_weight,
        "icon": "⚖️"
    },
    "Temperature": {
        "units": ["Celsius", "Fahrenheit", "Kelvin", "Rankine", "Réaumur"],
        "convert_function": convert_temperature,
        "icon": "🌡️"
    },
    "Volume": {
        "units": ["Milliliter", "Liter", "Cubic Meter", "Fluid Ounce (US)", "Cup (US)", "Pint (US)", 
                 "Quart (US)", "Gallon (US)", "Cubic Centimeter", "Cubic Inch", "Cubic Foot", 
                 "Cubic Yard", "Teaspoon (US)", "Tablespoon (US)", "Fluid Ounce (UK)", "Pint (UK)", 
                 "Quart (UK)", "Gallon (UK)", "Barrel (Oil)", "Barrel (US)", "Barrel (UK)"],
        "convert_function": convert_volume,
        "icon": "🧪"
    },
    "Time": {
        "units": ["Second", "Minute", "Hour", "Day", "Week", "Month (30 days)", "Year (365 days)",
                 "Millisecond", "Microsecond", "Nanosecond", "Picosecond", "Decade", "Century", 
                 "Millennium", "Fortnight"],
        "convert_function": convert_time,
        "icon": "⏱️"
    },
    "Area": {
        "units": ["Square Millimeter", "Square Centimeter", "Square Meter", "Square Kilometer", 
                 "Square Inch", "Square Foot", "Square Yard", "Square Mile", "Acre", "Hectare", 
                 "Are", "Barn", "Homestead"],
        "convert_function": convert_area,
        "icon": "📐"
    },
    "Speed": {
        "units": ["Meter per Second", "Kilometer per Hour", "Mile per Hour", "Knot", "Foot per Second", 
                 "Inch per Second", "Speed of Light", "Speed of Sound (Air)", "Mach (at std. atmosphere)"],
        "convert_function": convert_speed,
        "icon": "🚀"
    },
    "Pressure": {
        "units": ["Pascal", "Kilopascal", "Megapascal", "Bar", "Atmosphere", "Torr", 
                 "Pound per Square Inch", "Pound per Square Foot", "Millimeter of Mercury"],
        "convert_function": convert_pressure,
        "icon": "🔄"
    },
    "Energy": {
        "units": ["Joule", "Kilojoule", "Calorie", "Kilocalorie", "Watt Hour", "Kilowatt Hour", 
                 "Electron Volt", "British Thermal Unit", "US Therm", "Foot-Pound"],
        "convert_function": convert_energy,
        "icon": "⚡"
    },
    "Power": {
        "units": ["Watt", "Kilowatt", "Megawatt", "Horsepower (Mechanical)", "Horsepower (Metric)", 
                 "Foot-Pound per Second", "BTU per Hour", "Calorie per Second"],
        "convert_function": convert_power,
        "icon": "💪"
    },
    "Data": {
        "units": ["Bit", "Byte", "Kilobit", "Kilobyte", "Megabit", "Megabyte", "Gigabit", 
                 "Gigabyte", "Terabit", "Terabyte", "Petabit", "Petabyte"],
        "convert_function": convert_data,
        "icon": "💾"
    },
    "Fuel Economy": {
        "units": ["Miles per Gallon (US)", "Miles per Gallon (UK)", "Kilometers per Liter", 
                 "Liters per 100 Kilometers"],
        "convert_function": convert_fuel_economy,
        "icon": "⛽"
    },
    "Angle": {
        "units": ["Degree", "Radian", "Gradian", "Minute of Arc", "Second of Arc", "Turn"],
        "convert_function": convert_angle,
        "icon": "📐"
    },
    "Frequency": {
        "units": ["Hertz", "Kilohertz", "Megahertz", "Gigahertz", "Cycle per Second", 
                 "RPM", "Degree per Second"],
        "convert_function": convert_frequency,
        "icon": "🔊"
    },
    "Currency": {
        "units": ["USD", "EUR", "GBP", "JPY", "CAD", "AUD", "CHF", "CNY", "INR", "BRL", "PKR"],
        "convert_function": convert_currency,
        "icon": "💰"
    }
}

def home_page():
    st.markdown('<h1 class="neon-text"> Unit Converter</h1>', unsafe_allow_html=True)
    st.write("Welcome to the  Unit Converter. Choose a category to start converting!")

    # Create rows of categories (3 per row)
    categories = list(unit_categories.items())
    num_rows = (len(categories) + 2) // 3  # Calculate number of rows needed
    
    for i in range(num_rows):
        cols = st.columns(3)
        for j in range(3):
            idx = i * 3 + j
            if idx < len(categories):
                category, info = categories[idx]
                with cols[j]:
                    st.markdown(f"""
                    <div class="category-card">
                        <div class="category-icon">{info['icon']}</div>
                        <h3>{category}</h3>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"Convert {category}", key=f"btn_{category}"):
                        st.session_state.page = category
                        st.rerun()

def converter_page(category):
    st.markdown(f'<h1 class="neon-text">{category} Converter</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        value = st.number_input("Enter value:", value=1.0, step=0.1)
        from_unit = st.selectbox("From:", unit_categories[category]["units"], key="from_unit")
    
    with col2:
        to_unit = st.selectbox("To:", unit_categories[category]["units"], key="to_unit")
    
    if st.button("Convert"):
        result = unit_categories[category]["convert_function"](value, from_unit, to_unit)
        st.markdown(f"""
        <div class="result">
            {value} {from_unit} = {result:.4f} {to_unit}
        </div>
        """, unsafe_allow_html=True)
    
    # Conversion table
    st.subheader("Conversion Table")
    table_values = [0.1, 1, 10, 100, 1000]
    df = pd.DataFrame({
        f"{from_unit}": table_values,
        f"{to_unit}": [unit_categories[category]["convert_function"](v, from_unit, to_unit) for v in table_values]
    })
    st.table(df)
    
    if st.button("Back to Home"):
        st.session_state.page = "home"
        st.rerun()

def main():
    add_custom_css()
    
    if "page" not in st.session_state:
        st.session_state.page = "home"
    
    if st.session_state.page == "home":
        home_page()
    elif st.session_state.page in unit_categories:
        converter_page(st.session_state.page)
    
    st.markdown('<div class="footer">DEVELOPED BY AATFA SIDDIQUI</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()