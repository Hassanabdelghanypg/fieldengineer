import streamlit as st

# Import Pages
from app_pages import TFA, home, slug_effect_calculator, pop, volumetrics
import simulator

# Set Page Configuration
st.set_page_config(page_title="Slug Effect Calculator", page_icon=":oil_drum:", layout="wide")

# Initializing sessions state for page navigations
if "page" not in st.session_state:
    st.session_state.page = "Home"


# Sidebar Navigation

# Buttons to Navigate to Different Calculators
if st.sidebar.button("Home", key="home", use_container_width=True):
    st.session_state.page = "Home"

st.sidebar.markdown("### 🧮 Oil & Gas Calculators", text_alignment="left")

if st.sidebar.button("Slug Effect Calculator", key="slug_effect_calculator", use_container_width=True):
    st.session_state.page = "Slug Effect Calculator"

if st.sidebar.button("Pump Output Calculator", key="pump_output_calculator", use_container_width=True):
    st.session_state.page = "Pump Output Calculator"

if st.sidebar.button("Total Flow Area (TFA) Calculator", key="total_flow_area_calculator", use_container_width=True):
    st.session_state.page = "Total Flow Area (TFA) Calculator"

if st.sidebar.button("Volumetrics, Hole Fill, and Metal Displacement Calculations", key="volumetrics_calculator", use_container_width=True):
    st.session_state.page = "Volumetrics, Hole Fill, and Metal Displacement Calculations"


# Simulator
st.sidebar.markdown("### 🖥️ Drilling Monitoring Simulation", text_alignment="left")
if st.sidebar.button("Hole Simulator", key="simulator_app", use_container_width=True):
    st.session_state.page = "Hole Simulator"

# Notebooks and Topics (No Calculations)

st.sidebar.markdown("### 📚 Knowledge Library", text_alignment="left")


# Courses Title and Link
operationGeologyDictionary = {
    "Full Course Overview": "https://reinvented-shame-da7.notion.site/Operation-Geology-Course-Dr-Ashraf-Elshorbagy-f94db80cca6c82f88c5e0131d9f359c4?source=copy_link",
    "Tendering Processes": "https://www.notion.so/Lecture-1-Tendering-94adb80cca6c8201bdde818cc4d5b2bb?source=copy_link",
    "Sample Collection": "https://www.notion.so/Lecture-2-Sample-Collection-33cdb80cca6c8063ac98e84ae72831b8?source=copy_link",
    "Sample Description": "https://www.notion.so/Lecture-3-Sample-Description-33ddb80cca6c8065b0abe015d2fd8dcb?source=copy_link",
    "Recorded Gases & Gas Ratio": "https://www.notion.so/Lecture-4-Gases-34cdb80cca6c80c1a9dcd5736fbef15c?source=copy_link",
    "Hole Problems": "https://www.notion.so/Lecture-7-Hole-Problems-34cdb80cca6c8021967def49755e684b?source=copy_link",
    "Mud Hydraulics": "https://www.notion.so/Lecture-8-Hydraulics-375db80cca6c80a59eeaf6850d9f360d?source=copy_link",
    }

holeProblemsDictionary = {
    "Full Course Overview": "https://reinvented-shame-da7.notion.site/Hole-problems-Reasons-and-Early-Indicators-34adb80cca6c808abd0ed31824099746?source=copy_link",
    "Well Control Problems": "https://www.notion.so/1-WELL-CONTROL-PROBLEMS-34adb80cca6c803182f1ef7d79b8a1a8?source=copy_link",
    "Wellbore Instability Problems": "https://www.notion.so/2-WELLBORE-STABILITY-PROBLEMS-34bdb80cca6c809c9a40caed14c13189?source=copy_link",
    "Stuck Pipe mechanisms": "https://www.notion.so/3-STUCK-PIPE-MECHANISMS-34bdb80cca6c80d28447c6c3ffd59ad0?source=copy_link",
    "Hole Cleaning Problems": "https://www.notion.so/4-HOLE-CLEANING-PROBLEMS-34bdb80cca6c80b19997fb4626b6d0f6?source=copy_link",
    "Pressure-Related Problems": "https://www.notion.so/5-HYDRAULIC-PRESSURE-PROBLEMS-34bdb80cca6c808a8499c1149b04779f?source=copy_link",
    "Drillstring Failures": "https://www.notion.so/6-DRILLSTRING-FAILURES-34bdb80cca6c80438077d89726ba9291?source=copy_link",
    "Bit Balling": "https://www.notion.so/Torque-behaviour-in-bit-balling-34bdb80cca6c8004a9b2f57891820f92?source=copy_link",
    "Torque & Drag": "https://www.notion.so/How-is-drag-indicated-34bdb80cca6c808799ede14f1210e87d?source=copy_link",
}

# Course 1 || Operation Geology Course

with st.sidebar.expander("Operation Geology", expanded=True):

    for name, url in operationGeologyDictionary.items():
    
        st.link_button(name, url, use_container_width=True)


# Course 2 || Hole Problems

with st.sidebar.expander("Hole Problems", expanded=True):

    for name, url in holeProblemsDictionary.items():
    
        st.link_button(name, url, use_container_width=True)

# Sidebar Footer
st.sidebar.divider()
st.sidebar.caption("All Rights Reserved © 2026", text_alignment="center")
st.sidebar.caption(
    "## Hassan Abdelghany Hussein \n"
    "SDL Field Engineer • Petroleum Geologist • Python Developer\n", text_alignment="center"
)


# Pages to Call and import from pages folder
pages = {
    "Home": home.show,
    "Hole Simulator": simulator.show,
    "Slug Effect Calculator": slug_effect_calculator.show,
    "Pump Output Calculator": pop.show,
    "Total Flow Area (TFA) Calculator": TFA.show,
    "Volumetrics, Hole Fill, and Metal Displacement Calculations": volumetrics.show,
}

# Get into the selected page
pages[st.session_state.page]()