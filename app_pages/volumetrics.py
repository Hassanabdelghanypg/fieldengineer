import streamlit as st

def show():

    st.title("Volumetrics, Hole Fill, and Metal Displacement Calculations")

    col1, col2 = st.columns(2)

    with col1:
        # Headers Top
        st.markdown("Volumetric calculations represent some of the most critical concepts in drilling operations. A wide range of essential wellsite calculations\
                     - such as determining the volume of cement slurry required to fill the annulus, rely directly on these principles.")
        st.markdown("###### Remarkably, all of these scenarios are derived from a single fundamental engineering formula:")



    # Main Formula ||
        st.latex(r"\text{Volume (bbl)} = \frac{\text{OD}^2 - \text{ID}^2}{1029.4} \times \text{Length (ft)}")
        st.markdown("###### Where :")
        st.markdown("- ***OD*** = Outer Diameter (inches) \n\n - ***ID*** = Inner Diameter (inches) \n\n - ***1029.4*** = The standard conversion constant for oilfield units (barrels per foot).")
        st.markdown("###### Instead of memorizing dozens of individual formulas, you can easily manipulate this core equation for any scenario simply by in-mind visualizing the cross-sectional area of the geometry you are calculating.")
        st.divider()



        # 1- Hole Fill Calculations
        st.markdown("#### 1. Hole Fill Calculations")
        st.markdown("**Overview:** Hole fill determines the volume of drilling fluid required to fill a given section of the open or cased hole. This calculation is vital when setting cement plugs or monitoring fluid loss rates while drilling.")
        st.markdown("###### Because an open hole has no inner pipe, the (ID) in the core formula becomes zero, leaving only the Hole Diameter (HD).")
        st.markdown("")
        st.markdown("##### • Hole Fill Rate:")
        st.latex(r"\text{Hole Fill (bbl/ft)} = \frac{\text{HD}^2}{1029.4}")
        st.markdown("")
        st.markdown("##### • Total Hole Volume:")
        st.latex(r"\text{Hole Fill (bbl)} = \frac{\text{HD}^2}{1029.4} \times \text{Hole Length (ft)}")
        st.markdown("")
        st.markdown("###### Where (HD) = Hole Diameter or Casing Inner Diameter")
        st.divider()


        # 2- Annular Volume Calculations
        st.markdown("#### 2. Annular Volume Calculations")
        st.markdown("**Overview:** Annular volume determines the amount of fluid contained in the space (the annulus) between the outside of the drillstring (or casing) and the wall of the open hole (or outer casing).\
                    This calculation is essential for determining the volume of cement slurry required for a casing job, or for calculating bottoms-up displacement volumes during circulating operations.")
        st.markdown("###### To find this volume, you take the total hole volume and subtract the space occupied by the outside of the pipe string:")
        st.markdown("")
        st.markdown("##### • Annular Volume Rate:")
        st.latex(r"\text{Annular Volume (bbl/ft)} = \frac{\text{HD}^2 - \text{OD}^2}{1029.4}")
        st.markdown("##### • Total Annular Volume:")
        st.latex(r"\text{Annular Volume (bbl)} = \frac{\text{HD}^2 - \text{OD}^2}{1029.4} \times \text{Hole Length (ft)}")
        st.markdown("")
        st.markdown("###### Where:\n\n • **HD** = Hole Diameter (or Inner Diameter of the outer casing)\n\n • **OD** = Outer Diameter of the inner drillstring or casing string")
        st.divider()


        # 3- Pipe Capacity Calculations
        st.markdown("#### 3. Pipe Capacity Calculations")
        st.markdown("**Overview:** This calculation determines the internal volume of a drillstring, a single stand, or any casing/tubing section (i.e., how much mud is required to completely fill the inside of the pipe).")
        st.markdown("###### Just like calculating an open hole, you are evaluating a hollow cylinder, so you only look at the pipe's internal boundary.")
        st.markdown("")
        st.markdown("##### • Pipe Capacity:")
        st.latex(r"\text{Pipe Capacity (bbl)} = \frac{\text{ID}^2}{1029.4} \times \text{Pipe Length (ft)}")
        st.markdown("")
        st.markdown("###### Where (ID) = Inner Diameter of the Pipe")
        st.divider()


        # 4- Metal Displacement Calculations
        st.markdown("#### 4. Metal Displacement Calculations")
        st.markdown("**Overview:** This calculation determines the volume of drilling fluid displaced by the drillstring or casing during operations.")
        st.markdown("###### Accurate displacement tracking is critical during tripping operations (tripping in or out of the hole) to correctly evaluate the volumetric gains or losses observed in the trip tank.")
        st.markdown("")
        # Open-End Metal Displacement
        st.markdown("##### • Scenario A: Open-End Metal Displacement")
        st.markdown("Used when tripping a pipe string that is open at the bottom, allowing fluid to pass through the inside of the steel. In this case, you are calculating only the actual volume of the steel wall itself.")
        st.latex(r"\text{Open-End Metal Displacement (bbl/ft)} = \frac{\text{OD}^2 - \text{ID}^2}{1029.4}")
        st.markdown("")
        # Closed-End Metal Displacement
        st.markdown("##### • Scenario B: Closed-End Metal Displacement")
        st.markdown("Used when tripping a pipe string equipped with a float valve, a plugged bit, or a closed casing shoe that prevents mud from entering the string. Because the fluid cannot enter, the pipe acts as a solid cylinder, displacing mud equal to its entire outer volume.")
        st.latex(r"\text{Closed-End Metal Displacement (bbl/ft)} = \frac{\text{OD}^2}{1029.4}")
        st.markdown("")
        st.markdown("###### Where (ID) and (ID) represent the Outer and Inner Diameters of the pipe respectively")


# The Calculations
    with col2:

        st.header("The Calculator")

        # ( Hole Fill Calculator )
        with st.expander("Hole Fill Calculation"):

            col_a, col_b = st.columns(2)
            with col_a:
                # Input Fields
                st.markdown("### Input Fields :")
                hole_diameter = st.number_input("Hole Diameter (inches)", key="hole_diameter1")
                hole_length = st.number_input("Hole Length (ft)", key="hole_length")

                # Answers
                hole_fill = (hole_diameter ** 2) / 1029.4
                hole_volume = hole_fill * hole_length
                    # Hole Fill Rate                
                st.markdown("#### Hole Fill Rate :")
                st.markdown(f"##### {hole_fill:.4} bbl/ft")
                    # Total Hole Volume
                st.markdown("#### Total Hole Volume :")
                st.markdown(f"##### {hole_volume:.4} bbl")

            with col_b:
                st.image("./images/hole_fill.png", caption="Hole Fill")

        
        # ( Annular Volume Calculations )
        with st.expander("Annular Volume Calculation"):

            col_a, col_b = st.columns(2)
            with col_a:
                # Input Fields
                st.markdown("### Input Fields :")
                hole_diameter = st.number_input("Hole Diameter (inches)", key="hole_diameter2")
                pipe_OD = st.number_input("Pipe Outer Diameter (OD)", key="pipe_outer_annular")
                hole_length = st.number_input("Hole Length (ft)", key="hole_length2")

                # Answers
                annular_volume_rate = ((hole_diameter ** 2) - (pipe_OD ** 2)) / 1029.4
                hole_volume = annular_volume_rate * hole_length
                    # Hole Fill Rate                
                st.markdown("#### Annular Volume Rate :")
                st.markdown(f"##### {annular_volume_rate:.4} bbl/ft")
                    # Total Hole Volume
                st.markdown("#### Total Hole Volume :")
                st.markdown(f"##### {hole_volume:.6} bbl")

            with col_b:
                st.image("./images/annular.png", caption="Annular (Annulus) Section Volume")


        # ( Pipe Volume Calculations )
        with st.expander("Pipe Capacity Calculation"):

            col_a, col_b = st.columns(2)
            with col_a:
                # Input Fields
                st.markdown("### Input Fields :")
                pipe_id = st.number_input("Pipe Inner Diameter (ID) (inches)", key="pipe_id1")
                pipe_length = st.number_input("Pipe Length (ft)", key="pipe_length1")

                # Answers
                pipe_capacity = (pipe_id ** 2) / 1029.4
                pipe_capacity_volume = pipe_capacity * pipe_length
                    # Hole Fill Rate                
                st.markdown("#### Pipe Fill Rate :")
                st.markdown(f"##### {pipe_capacity:.4} bbl/ft")
                    # Total Hole Volume
                st.markdown("#### Total Pipe Volume :")
                st.markdown(f"##### {pipe_capacity_volume:.4} bbl")

            with col_b:
                st.image("./images/pipe_capacity.png", caption="Pipe Inner Capacity (Volume)")


        # ( Metal Displacement Calculations )
        with st.expander("Metal Displacement Calculation"):

            st.image("./images/displacement.png", caption="Pipe Inner Capacity (Volume)")

            # Choose Calculations Mode:
            calculation_mode = st.radio("****Choose Calculation Mode :****",
                                        ["Open-End Metal Displacement", "Closed-End Metal Displacement"]
                                        )

            # Input Fields
            st.markdown("### Input Fields :")

            # Pipe (OD) - Shared
            pipe_od = st.number_input("Pipe Outer Diameter (OD) (inches)", key="pipe_od4")

            # Pipe (ID) - Onl Open-End
            if calculation_mode == "Open-End Metal Displacement":

                pipe_id = st.number_input("Pipe Inner Diameter (ID) (inches)", key="pipe_id4")
            
            # Pipe Length - Shared
            pipe_length = st.number_input("Pipe Length (ft)", key="pipe_length4")


            # Answers ================================================================
            metal_displacement = (pipe_od ** 2) / 1029.4

            # Metal Displacement Rate - Open-End
            if calculation_mode == "Open-End Metal Displacement":

                metal_displacement = ((pipe_od ** 2) - (pipe_id ** 2)) / 1029.4

            # Total Pipe Displacement
            total_pipe_displacement = metal_displacement * pipe_length
                
                       
            st.markdown("#### Metal Displacement Rate :")
            st.markdown(f"##### {metal_displacement:.4} bbl/ft")
            
            st.markdown("#### Total Pipe Displacement :")
            st.markdown(f"##### {total_pipe_displacement:.4} bbl")
