import streamlit as st

def show():

    st.title("Pump Output Calculator")

    col1, col2 = st.columns(2)

    with col1:
        # Headers Top
        st.markdown("#### Pump Output")
        st.markdown("Normally expressed in bbl/stk, Pump output is the volume of drilling fluid delivered by the mud pump per stroke. It is used to calculate flow rate and is a key parameter for drilling hydraulics, circulation, and well control calculations.")
        st.markdown("###### This calculator is designed to help you calculate pump output for both triplex pump and duplex pump.")



    # Triplex Pump || Overview
        st.header("Triplex Pump Oerview ||")
        st.markdown("A triplex pump is a single-acting reciprocating mud pump with three pistons. Each piston displaces drilling fluid on only one side during its forward stroke. Because there is no piston rod reducing the pumping area, the pump output depends only on the liner diameter and stroke length.")
        st.markdown("###### Today, triplex pumps are the industry standard and are used on nearly all modern land and offshore drilling rigs.")
        st.markdown("#### Why it's widely used:")
        st.markdown("""- *Produces smoother and more continuous flow.*
                    \n - *Lower pressure fluctuations compared to duplex pumps.*
                    \n - *More compact and efficient.*
                    \n - *Requires less maintenance and operates with lower vibration.*""")

        # Triplex Pump Output Calculations ===============================================================================
        st.markdown("######")
        st.markdown("##### Triplex Pump Output Formula :")
        st.latex(r"""\text{Triplex Pump Output (bbl/stk)} = 0.000243 \times (\text{Liner Diameter})^{2} \times (\text{Stroke Length})""")
        st.latex(r"""\text{Actual Pump Output (bbl/stk)} = \text{Triplex Pump Output (bbl/stk)} \times \text{Actual Pump Efficiency \%}""")



    # Duplex Pump || Overview
        st.markdown("######")
        st.header("Duplex Pump Overview ||")
        st.markdown("A duplex pump is a double-acting reciprocating mud pump with two pistons. Unlike a triplex pump, each piston pumps fluid during both the forward and return strokes. However, one side of the piston contains a piston rod, which reduces the effective pumping area on that side.")
        st.markdown("###### Duplex pumps are now rarely used and are mostly found on older drilling rigs or legacy equipment, having been largely replaced by triplex pumps due to their superior performance and reliability.")
        st.markdown("#### Characteristics:")
        st.markdown("""- *Two double-acting pistons.*
                    \n - *Pump output depends on liner diameter, stroke length, and rod diameter.*
                    \n - *Produces more pulsating flow and higher vibration than triplex pumps.*
                    \n - *Larger, heavier, and generally less efficient.*""")

        # Duplex Pump Output Calculations ===============================================================================
        st.markdown("######")
        st.markdown("##### Duplex Pump Output Formula :")
        st.latex(r"""\text{Duplex Pump Output (bbl/stk)} = 0.000162 \times \text{(Stroke Length)} \times\left[2 \times \left(\text{Liner Diameter}\right)^2-\left(\text{Rod Diameter}\right)^2\right]""")
        st.latex(r"""\text{Actual Pump Output (bbl/stk)} = \text{Duplex Pump Output (bbl/stk)} \times \text{Actual Pump Efficiency \%}""")



# The Calculations
    with col2:
        st.image("./images/pump_triplex.jpg", caption="Triplex Pump")
        st.image("./images/duplex.jpg", caption="Duplex Pump")
        st.header("The Calculator")

        # ( Triplex Pump Output Calculation )
        with st.expander("Triplex Pump Output Calculation"):

            # Input Fields
            liner_diameter = st.number_input("Liner Diameter (inches)", min_value=0.0, value=5.0, step=0.1)
            stroke_length = st.number_input("Stroke Length (inches)", min_value=0.0, value=10.0, step=0.1)
            pump_efficiency = st.number_input("Pump Efficiency (%)", min_value=0.0, max_value=100.0, value=90.0, step=1.0)

            # Calculate Triplex Pump Output
            triplex_pump_output = 0.000243 * (liner_diameter ** 2) * stroke_length
            st.markdown(f"**Triplex Pump Output (100% Efficiency):** {triplex_pump_output:.4f} bbl/stk")
            st.markdown(f"**Actual Triplex Pump Output:** {triplex_pump_output * (pump_efficiency / 100):.4f} bbl/stk")


        # ( Duplex Pump Output Calculation )
        with st.expander("Duplex Pump Output Calculation"):

            # Input Fields
            liner_diameter = st.number_input("Liner Diameter (inches)", min_value=0.0, value=6.0, step=0.1, key="duplex_liner_diameter")
            stroke_length = st.number_input("Stroke Length (inches)", min_value=0.0, value=10.0, step=0.1, key="duplex_stroke_length")
            rod_diameter = st.number_input("Rod Diameter (inches)", min_value=0.0, value=2.0, step=0.1, key="duplex_rod_diameter")
            pump_efficiency = st.number_input("Pump Efficiency (%)", min_value=0.0, max_value=100.0, value=90.0, step=1.0, key="duplex_pump_efficiency")

            # Calculate Duplex Pump Output
            duplex_pump_output = 0.000162 * stroke_length * (2 * (liner_diameter ** 2) - (rod_diameter ** 2))
            st.markdown(f"**Duplex Pump Output (100% Efficiency):** {duplex_pump_output:.4f} bbl/stk")
            st.markdown(f"**Actual Duplex Pump Output:** {duplex_pump_output * (pump_efficiency / 100):.4f} bbl/stk")
