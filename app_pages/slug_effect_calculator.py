import streamlit as st

def show():

    st.title("Slug Effect Calculator")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### What is Slug Effect?")
        st.markdown("###### When pumping a heavy slug prior to tripping pipe out of the hole, the goal is to lower the fluid level inside the drillstring. This creates a dry length of pipe, preventing mud from spilling onto the rig floor. This dry length inside the drill pipe results in an additional mud return at the surface (pit gain) after the slug is pumped.")
        st.markdown("###### This calculator is designed to help you determine the required slug volume to achieve a desired length of dry pipe, as well as the expected pit gain after pumping the slug.")
        st.header("Steps of Calculation \"Theoritically\"")


    # Phase 1 ( Calculating Required Slug Volume for a Set Length of Dry Pipe )
        st.markdown("####")
        st.markdown("### 1. Calculating Required Slug Volume for a Set Length of Dry Pipe")
        st.markdown("######")

        # Step 1 ===============================================================================
        st.markdown("##### Step 1: Calculate the required Hydrostatic Pressure (HP)")
        st.latex(r"""
                HP = \text{Current Mud Weight (ppg)} \times 0.052 \times \text{Desired Length of Dry Pipe (ft)}
                """)

        # Step 2 ===============================================================================
        st.markdown("##### Step 2: Calculate the Pressure Gradient Change (ΔG)")
        st.latex(r"""\Delta G = (\text{Slug Weight (ppg)} - \text{Current Mud Weight (ppg)}) \times 0.052
                """)

        # Step 3 ===============================================================================
        st.markdown("##### Step 3: Determine Slug Length in the Drill Pipe")
        st.latex(r"""\text{Slug Length (ft)} = \frac{HP}{\Delta G}
                """)

        # Step 4 ===============================================================================
        st.markdown("##### Step 4: Calculate the Required Slug Volume")
        st.latex(r"""\text{Slug Volume (bbl)} = \text{Slug Length (ft)} \times \text{Drill Pipe Capacity (bbl/ft)}
                """)
        

    # Phase 2 ( Calculating the Pit Gain (Mud Returned) )
        st.markdown("####")
        st.markdown("#### 2. Calculating the Pit Gain (Mud Returned)")
        st.markdown("######")


        # Step 1 ===============================================================================
        st.markdown("Step 1: Calculate the total mud volume returned after pumping the slug")
        st.latex(r"""
                \text{Total Mud Returned (bbl)} = \frac{\text{Slug Weight (ppg)}}{\text{Mud Weight (ppg)}} \times \text{Slug Volume (bbl)}
                """)

        # Step 2 ===============================================================================
        st.markdown("Step 2: Calculate the Additional Mud Returned (Pit Gain)")
        st.latex(r"""\text{Additional Mud Returned (bbl)} = \left( \frac{\text{Slug Weight (ppg)}}{\text{Mud Weight (ppg)}} - 1 \right) \times \text{Slug Volume (bbl)}
                """)

        # Step 3 ===============================================================================
        st.markdown("Step 3: Determine the Level Drop (Length of Dry Pipe)")
        st.latex(r"""\text{Level Drop (ft)} = \frac{\text{Additional Mud Returned (bbl)}}{\text{Drill Pipe Capacity (bbl/ft)}}
                """)
        
            
    with col2:
        st.image(".\images\Slug_Effect.jpg", caption="Slug Effect Illustration")
        st.header("The Calculator")

        # Phase 1 ( Calculating Required Slug Volume )
        with st.expander("1. Calculating Required Slug Volume for a Set Length of Dry Pipe"):

            # Input Fields
            current_mud_weight = st.number_input("Current Mud Weight (ppg)", min_value=0.0, value=10.0, step=0.1)
            desired_length_dry_pipe = st.number_input("Desired Length of Dry Pipe (ft)", min_value=0.0, value=100.0, step=1.0)
            slug_weight = st.number_input("Slug Weight (ppg)", min_value=0.0, value=12.0, step=0.1)
            drill_pipe_capacity = st.number_input("Drill Pipe Capacity (bbl/ft)", min_value=0.0, value=0.0178, step=0.0001, format="%.4f")

            # Calculate Required Slug Volume
            hp = current_mud_weight * 0.052 * desired_length_dry_pipe
            delta_g = (slug_weight - current_mud_weight) * 0.052
            slug_length = hp / delta_g if delta_g != 0 else 0
            slug_volume = slug_length * drill_pipe_capacity

            st.markdown(f"**1. HP:** {hp:.0f} psi")
            st.markdown(f"**2. ΔG:** {delta_g:.2f} psi/ft")
            st.markdown(f"**3. Slug Length:** {slug_length:.2f} ft")
            st.markdown(f"**4. Required Slug Volume:** {slug_volume:.2f} bbl")

        # Phase 2 ( Calculating the Pit Gain )
        with st.expander("2. Calculating the Pit Gain (Mud Returned)"):

            # Input Fields
            slug_weight_pg = st.number_input("Slug Weight (ppg) for Pit Gain Calculation", min_value=0.0, value=12.0, step=0.1)
            mud_weight_pg = st.number_input("Mud Weight (ppg) for Pit Gain Calculation", min_value=0.0, value=10.0, step=0.1)
            slug_volume_pg = st.number_input("Slug Volume (bbl) for Pit Gain Calculation", min_value=0.0, value=slug_volume, step=0.01)
            drill_pipe_capacity = st.number_input("Drill Pipe Capacity (bbl/ft) for Pit Gain Calculation", min_value=0.0, value=0.0178, step=0.0001, format="%.4f")

            # Calculate Pit Gain
            total_mud_returned = (slug_weight_pg / mud_weight_pg) * slug_volume_pg if mud_weight_pg != 0 else 0
            additional_mud_returned = ((slug_weight_pg / mud_weight_pg) - 1) * slug_volume_pg if mud_weight_pg != 0 else 0
            level_drop = additional_mud_returned / drill_pipe_capacity if drill_pipe_capacity != 0 else 0

            st.markdown(f"**1. Total Mud Returned:** {total_mud_returned:.2f} bbl")
            st.markdown(f"**2. Additional Mud Returned (Pit Gain):** {additional_mud_returned:.2f} bbl")
            st.markdown(f"**3. Level Drop (Length of Dry Pipe):** {level_drop:.2f} ft") 