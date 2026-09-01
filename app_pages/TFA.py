import streamlit as st

def show():

    st.title("Total Flow Area (TFA) Calculator")

    col1, col2 = st.columns(2)

    with col1:
        # Headers Top
        st.markdown("#### Mud Circulation and Total Flow Area (TFA)")
        st.markdown("In drilling operations, the mud circulation system functions as a closed loop. The drilling fluid (mud) is pumped from the surface mud tanks, travels down the drillstring, exits into the annulus through the bit nozzles, and finally returns to the surface tanks."
                    " **The Total Flow Area (TFA)** is the cumulative area of all the nozzles through which fluid can pass. When calculating the TFA, every nozzle present in the drill bit must be accounted for.")



    # TFA Calculations ||
        st.header("Nozzle Flow Area (TFA) Formula ||")
        st.markdown("###### To find the flow area of an individual nozzle, use the following formula:")
        st.latex(r"A_{\text{nozzle}} = \frac{N^2}{1303.8}")
        st.markdown("###### Where :")
        st.markdown("- **$A_{nozzle}$** "" =  The flow area of a single nozzle (square inches, $\t{in}^2$)")
        st.markdown("- **$N$** "" =  Nozzle size (expressed in 32nds of an inch; e.g., a 10/32\""" nozzle means $N = 10$)")
        st.markdown("###### To find the Total Flow Area (TFA) of a bit or reamer, simply sum the individual areas of all nozzles:")
        st.latex(r"\text {TFA} = \sum A_{\text{nozzle}}")

        # Example Calculation
        st.markdown("#### Example Calculation :")
        st.markdown("***Example :*** A drill bit has a total of 5 nozzles. Three nozzles have a diameter of 10/32 inch, and the remaining 2 nozzles have a diameter of 12/32 inch. Determine the Total Flow Area (TFA) of the bit.")
        st.markdown("**Solution :** By definition, you must combine the area of every nozzle. You can group them into the formula as follows:")

        st.latex(r"\text{TFA} = \frac{10^2 + 10^2 + 10^2 + 12^2 + 12^2}{1303.8}")
        st.latex(r"\text{TFA} = \frac{100 + 100 + 100 + 144 + 144}{1303.8}")
        st.latex(r"\text{TFA} = \frac{588}{1303.8} \approx \mathbf{0.451\text{ in}^2}")



# The Calculations
    with col2:
        st.image("./images/bit-nozzles.jpg", caption="Bit Nozzles")
        st.header("The Calculator")

        # ( Total Flow Area (TFA) Calculation )
        with st.expander("Total Flow Area (TFA) Calculation"):

            # Input Fields
            st.markdown("### Input Fields :")
            st.markdown("##### Nozzle Numbers and Sizes (in 32nds of an inch) :")
            col1, col2 = st.columns(2)
            
            # Add New Nozzle Button
            if "nozzle_count" not in st.session_state:
                st.session_state.nozzle_count = 2  # Last number of nozzles


            if st.button("Add Nozzle", key="add_nozzle", use_container_width=True):
                st.session_state.nozzle_count += 1

            with col1:
                nozzle_sizes = {}
                for i in range(1, st.session_state.nozzle_count + 1):
                    nozzle_sizes[f"nozzle_{i}_size"] = st.number_input(f"***Nozzle {i} :*** Size (in 32nds of an inch)", min_value=0, value=10, step=1, key=f"nozzle_{i}")


            with col2:
                nozzle_counts = {}
                for i in range(1, st.session_state.nozzle_count + 1):
                    nozzle_counts[f"nozzle_{i}_count"] = st.number_input(f"***Nozzle {i} :*** Count", min_value=0, value=1, step=1, key=f"nozzle_{i}_count")


            # Calculate Total Flow Area (TFA)
            # if st.button("Calculate Total Flow Area (TFA)", key="calculate_tfa", use_container_width=True):
            total_flow_area = 0
            for i in range(1, st.session_state.nozzle_count + 1):
                size = nozzle_sizes[f"nozzle_{i}_size"]
                count = nozzle_counts[f"nozzle_{i}_count"]
                flow_area = (size ** 2) / 1303.8
                total_flow_area += flow_area * count

            st.markdown(f"### Total Flow Area (TFA) : {total_flow_area:.4f} in²")
