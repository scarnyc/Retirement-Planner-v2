import streamlit as st
from constants import COLORS

def apply_custom_styles():
    """Apply custom styles to the Streamlit application"""
    
    # Define CSS styles
    st.markdown("""
        <style>
        /* Main styles */
        .stApp {
            background-color: #F5F7FA;
            color: #333333;
            font-family: 'Roboto', 'Inter', sans-serif;
        }
        
        /* Headers */
        h1, h2, h3, h4, h5, h6 {
            color: #006D75;
            font-weight: 600;
        }
        
        /* Metric styles */
        .stMetric label {
            color: #2E5E82;
            font-weight: 500;
        }
        
        /* Comprehensive metric value styling to ensure visibility */
        .stMetric .css-1xarl3l,
        .stMetric div[data-testid="stMetricValue"],
        .stMetric [data-testid="stMetricValue"] > div,
        .css-1649tca-annotationValue,
        .css-10trblm,
        .css-1qg75gu,
        .css-81oif8,
        .stMetric > div > div > div > div,
        .stMetric span,
        div[data-testid="stMetricLabel"] ~ div,
        div[data-testid="stMetricValue"] {
            color: #333333 !important;
            font-weight: 700 !important;
        }
        
        /* Fix text visibility in tabs and projection sections */
        .stTabs [data-baseweb="tab-panel"] p,
        .stTabs [data-baseweb="tab-panel"] div,
        .stTabs [data-baseweb="tab-panel"] span,
        .stTabs [data-baseweb="tab-list"] button,
        .block-container p,
        .block-container li,
        .block-container div:not([class*="st"]),
        .dataframe th,
        .dataframe td {
            color: #333333 !important;
        }
        
        /* Fix tab panel visibility */
        [data-baseweb="tab-panel"] {
            color: #333333 !important;
        }
        
        /* Fix table text colors */
        .stDataFrame tbody tr td {
            color: #333333 !important;
        }
        
        /* Make tab labels more visible */
        .stTabs [role="tab"][aria-selected="true"] {
            background-color: rgba(0, 109, 117, 0.1);
            font-weight: 600;
        }
        
        /* Sidebar styles */
        .sidebar .sidebar-content,
        [data-testid="stSidebar"],
        [data-testid="stSidebar"] > div:first-child,
        [data-testid="stSidebar"] .sidebar-content {
            background-color: #FFFFFF !important;
        }
        
        /* Improve sidebar text visibility */
        .sidebar .block-container {
            color: #333333;
        }
        
        /* Override dark mode settings in sidebar */
        [data-testid="stSidebar"],
        [data-testid="stSidebar"] > div,
        [data-testid="stSidebar"] .stExpander,
        [data-testid="stSidebar"] stExpanderContent {
            background-color: #FFFFFF !important;
        }
        
        /* Ensure all sidebar text elements are visible */
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] .stMarkdown,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] span,
        [data-testid="stSidebar"] div:not([class*="st"]),
        [data-testid="stSidebar"] .stExpander label,
        [data-testid="stSidebar"] .stNumberInput label,
        [data-testid="stSidebar"] .stSelectbox label,
        [data-testid="stSidebar"] .streamlit-expanderHeader {
            color: #333333 !important;
            font-weight: 500 !important;
        }
        
        /* Make sidebar header text visible and prominent */
        [data-testid="stSidebar"] .sidebar-content h1,
        [data-testid="stSidebar"] .sidebar-content h2,
        [data-testid="stSidebar"] .sidebar-content h3,
        [data-testid="stSidebar"] .sidebar-content h4 {
            color: #006D75 !important;
            font-weight: 600 !important;
        }
        
        /* Improve number input visibility */
        [data-testid="stSidebar"] input[type="number"] {
            color: #333333 !important;
            background-color: #FFFFFF !important;
            border: 1px solid #E0E0E0 !important;
        }
        
        /* Make sidebar input labels more visible */
        [data-testid="stSidebar"] .stNumberInput label,
        [data-testid="stSidebar"] .stSelectbox label {
            color: #333333 !important;
            font-weight: 600 !important;
        }
        
        /* Style expander background */
        [data-testid="stSidebar"] .streamlit-expanderContent,
        [data-testid="stSidebar"] [data-baseweb="input"],
        [data-testid="stSidebar"] [data-baseweb="select"] {
            background-color: #FFFFFF !important;
            border-radius: 4px;
            padding: 8px !important;
        }
        
        /* Fix form elements in sidebar */
        [data-testid="stSidebar"] input,
        [data-testid="stSidebar"] select,
        [data-testid="stSidebar"] .st-bq,
        [data-testid="stSidebar"] .st-br, 
        [data-testid="stSidebar"] .st-bs,
        [data-testid="stSidebar"] [data-baseweb] {
            background-color: #FFFFFF !important;
            color: #333333 !important;
            border-color: #E0E0E0 !important;
        }
        
        /* Style info boxes in sidebar */
        [data-testid="stSidebar"] .stAlert {
            background-color: rgba(0, 109, 117, 0.1) !important;
            color: #333333 !important;
        }
        
        /* Expander styles */
        .streamlit-expanderHeader {
            background-color: #F5F7FA;
            color: #2E5E82;
            font-weight: 600;
        }
        
        /* Button styles */
        .stButton button {
            background-color: #006D75;
            color: white;
            border-radius: 4px;
            border: none;
            padding: 0.5rem 1rem;
            font-weight: 600;
        }
        
        .stButton button:hover {
            background-color: #2E5E82;
        }
        
        /* Info box styling */
        .stAlert {
            background-color: rgba(0, 109, 117, 0.1);
            border-color: #006D75;
        }
        
        /* Success styles */
        .element-container div[data-testid="stAlert"][aria-label="Success"] {
            background-color: rgba(76, 175, 80, 0.1);
            border-color: #4CAF50;
        }
        
        /* Warning styles */
        .element-container div[data-testid="stAlert"][aria-label="Warning"] {
            background-color: rgba(255, 183, 77, 0.1);
            border-color: #FFB74D;
        }
        
        /* Input field styles */
        .stTextInput input, .stNumberInput input, .stSelectbox, .stMultiselect {
            border-radius: 4px;
            border: 1px solid #E0E0E0;
        }
        
        .stTextInput input:focus, .stNumberInput input:focus {
            border-color: #006D75;
            box-shadow: 0 0 0 2px rgba(0, 109, 117, 0.2);
        }
        
        /* Table styles */
        .stTable td, .stDataFrame td {
            color: #333333;
        }
        
        .stTable th, .stDataFrame th {
            background-color: #2E5E82;
            color: white;
            font-weight: 600;
        }
        
        /* Slider styles */
        .stSlider div[data-baseweb="slider"] div {
            background-color: #006D75 !important;
        }
        
        /* Progress bar */
        .stProgress div {
            background-color: #006D75;
        }
        
        /* Footer styles */
        footer {
            visibility: hidden;
        }
        
        /* Customize the sidebar width */
        [data-testid="stSidebar"] {
            min-width: 350px;
            max-width: 450px;
        }
        </style>
    """, unsafe_allow_html=True)
