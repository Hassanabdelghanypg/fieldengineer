import streamlit as st
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import time


def show():
    # ── App Config ──────────────────────────────────────────────
    st.set_page_config(page_title="Real-time Drilling Monitoring Simulation", layout="wide")
    st.title("Real-time Drilling Monitoring Simulation", text_alignment="center")
    st.markdown("---")

    # ── Operation Mode & Scenario Selection ─────────────────────
    col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 2], vertical_alignment="center")

    with col1:
        operation_mode = st.selectbox(
            "Downhole Operation",
            ["Drilling", "Tripping"]
        )

    # ── Dynamic scenario options based on operation mode ────────
    DRILLING_SCENARIOS = ["Normal Drilling", "Well Kick", "Lost of Circulation", "Stuck Pipe"]
    TRIPPING_SCENARIOS = ["POOH", "RIH", "Tight Spot | Pipe Stuck While Tripping", "Overpull"]

    DRILLING_FILES = {
        "Normal Drilling":      "data/Normal.csv",
        "Well Kick":            "data/Kick.csv",
        "Lost of Circulation":  "data/Losses.csv",
        "Stuck Pipe":           "data/Stuck.csv",
    }
    TRIPPING_FILES = {
        "POOH":        "data/Tripping/POOH.csv",
        "RIH":         "data/Tripping/RIH.csv",
        "Tight Spot | Pipe Stuck While Tripping": "data/Tripping/Tight Spots.csv",
        "Overpull":    "data/Tripping/Overpull.csv",
    }

    scenario_options = DRILLING_SCENARIOS if operation_mode == "Drilling" else TRIPPING_SCENARIOS
    file_mapping     = DRILLING_FILES     if operation_mode == "Drilling" else TRIPPING_FILES

    with col2:
        scenario = st.selectbox("Select Scenario", scenario_options)

    with col3:
        st.subheader(scenario, text_alignment="center")

    with col4:
        st.markdown("Simulation Speed", text_alignment="center")
        col_a, col_b, col_c = st.columns([1, 1.5, 1])

        with col_a:
            Slow   = st.button("0.5x", use_container_width=True)

        with col_b:
            Normal = st.button("Normal", use_container_width=True)

        with col_c:
            Fast   = st.button("2x", use_container_width=True)

        # ── Simulation Speed Control ───────────────────────────────
        if "speed" not in st.session_state:
            st.session_state.speed = 0.5  # Default speed

        if Fast:
            st.session_state.speed = 0.3
        elif Slow:
            st.session_state.speed = 0.8
        elif Normal:
            st.session_state.speed = 0.5

    with col5:
        run = st.button("▶️ Start Simulation", use_container_width=True)

    # ── Load & Prepare Data ──────────────────────────────────────
    df = pd.read_csv(file_mapping[scenario])
    df["Time"] = pd.to_datetime(df["Time"])
    df = df.sort_values(by="Time").reset_index(drop=True)

    # ── Master color palette ─────────────────────────────────────
    MASTER_COLORS = {
        "Block Position": "#00FF33",
        "SPP":            "#FF0000",
        "Flow Out":       "#FFFFFF",
        "WOB":            "#FFC800",
        "PVT":            "#0095FF",
        "ROP":            "#FF9244",
        "Torque":         "#FF6BFF",
        "RPM":            "#00E5FF",
        "Hook Load":      "#0000FF",
        "SPM":            "#CA9BF7"
    }
    FALLBACK_COLORS = [
        "#E040FB", "#00BCD4", "#76FF03", "#FF6E40", "#40C4FF",
        "#F06292", "#B2FF59", "#FFD740", "#69F0AE", "#FF4081"
    ]

    # ── Parameters ───────────────────────────────────────────────
    all_params = ["Block Position", "SPP", "Flow Out", "WOB", "PVT", "SPM", "Hook Load", "Torque"]

    # Adjust parameters for Tripping mode
    if operation_mode == "Tripping":
        all_params = [p for p in all_params if p not in ["Flow Out", "WOB"]]

    def get_color(param, fallback_pool):
        if operation_mode == "Tripping" and param == "PVT":
            return "#FFFFFF"  # Trip Tank curve white
        return MASTER_COLORS.get(param, fallback_pool.pop(0))

    fallback_pool = FALLBACK_COLORS.copy()
    param_colors  = {p: get_color(p, fallback_pool) for p in all_params}

    # ── Detect which params have actual data in the loaded CSV ───
    def param_has_data(param, dataframe):
        """Returns True if the column exists and has at least one non-null value."""
        if param not in dataframe.columns:
            return False
        col = dataframe[param].dropna()
        return not col.empty

    # ── Filter checkboxes ────────────────────────────────────────
    selected_params = []
    cols = st.columns(len(all_params) + 1)

    with cols[0]:
        st.markdown("### Filter")

    for i, param in enumerate(all_params):
        color_hex    = param_colors[param]
        display_name = "Trip Tank" if (param == "PVT" and operation_mode == "Tripping") else param
        has_data     = param_has_data(param, df)

        with cols[i + 1]:
            if has_data:
                # Normal, interactive checkbox
                checked = st.checkbox(display_name, value=True, key=f"chk_{param}")
                st.markdown(
                    f"<span style='color:{color_hex}; font-size:11px; "
                    f"margin-top:-18px; display:block; padding-left:26px;'>"
                    f"━━━━━━━━━</span>",
                    unsafe_allow_html=True
                )
                if checked:
                    selected_params.append(param)
            else:
                # Grayed-out, unclickable placeholder — no data in this CSV
                st.markdown(
                    f"""
                    <div style='opacity:0.3; cursor:not-allowed; padding: 4px 0; user-select:none;'>
                        <label style='display:flex; align-items:center; gap:6px;
                                    font-size:14px; color:#888; cursor:not-allowed;'>
                            <input type='checkbox' disabled
                                style='accent-color:{color_hex}; cursor:not-allowed;'/>
                            {display_name}
                        </label>
                        <span style='color:{color_hex}; font-size:11px;
                                    margin-top:2px; display:block; padding-left:22px;'>
                            ━━━━━━━━━
                        </span>
                        <span style='font-size:9px; color:#666; padding-left:22px;'>No data</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    # ── Pretty Names ─────────────────────────────────────────────
    PRETTY_NAMES = {
        "SPP":       "Standpipe Pressure",
        "WOB":       "Weight on Bit",
        "ROP":       "Rate of Penetration",
        "Hook Load": "Hookload",
        "PVT":       "Trip Tank" if operation_mode == "Tripping" else "PVT",
        "SPM": "Pump Strokes",
    }
    def pretty(p): return PRETTY_NAMES.get(p, p)

    # ── X-axis ranges ────────────────────────────────────────────
    X_RANGES = {
        "Block Position": lambda d: [d["Block Position"].min() * 0.95, d["Block Position"].max() * 1.05],
        "SPP":       lambda d: [5000, 20000],
        "Flow Out":  lambda d: [0, 3000],
        "WOB":       lambda d: [-20, 20],
        "PVT":       lambda d: [0, 600],
        "Hook Load": lambda d: [10, 100],
        "Torque":    lambda d: [0, 10000],
        "SPM":       lambda d: [1, 200]
    }
    def get_x_range(param, data):
        if param in X_RANGES:
            return X_RANGES[param](data)
        col_min, col_max = data[param].min(), data[param].max()
        pad = (col_max - col_min) * 0.1 or 1
        return [col_min - pad, col_max + pad]

    # ── Note color logic ─────────────────────────────────────────
    def note_color(Note_Param):
        if "Block Position" in Note_Param: return "#00FF33"
        if "SPP" in Note_Param: return "#FF0000"
        if "Flow Out" in Note_Param: return "#FFFFFF"
        if "PVT" in Note_Param: return "#0095FF"
        if "SPM" in Note_Param: return "#CA9BF7"

        return "#0095FF"

    # # MASTER_COLORS = {
    #     "Block Position": "#00FF33",
    #     "SPP":            "#FF0000",
    #     "Flow Out":       "#FFFFFF",
    #     "WOB":            "#FFC800",
    #     "PVT":            "#0095FF",
    #     "ROP":            "#FF9244",
    #     "Torque":         "#FF6BFF",
    #     "RPM":            "#00E5FF",
    #     "Hook Load":      "#0000FF",
    #     "SPM":            "#CA9BF7"
    # ── Chart Placeholder ────────────────────────────────────────
    st.markdown("---")
    chart_placeholder = st.empty()

    if not selected_params:
        chart_placeholder.warning("⚠️ Please select at least one parameter to display.")
        st.stop()

    param_col_index = {param: idx + 1 for idx, param in enumerate(selected_params)}

    # ── Base figure builder ──────────────────────────────────────
    def build_base_figure(df, params, colors_map):
        y_min, y_max = df["Time"].min(), df["Time"].max()
        fig = make_subplots(
            rows=1, cols=len(params),
            shared_yaxes=True,
            subplot_titles=[pretty(p) for p in params],
            horizontal_spacing=0.04,
        )
        fig.update_annotations(font=dict(size=16, weight="bold"), font_color="white", yshift=20)
        for col_idx, col in enumerate(params):
            fig.add_trace(
                go.Scatter(x=[], y=[], mode="lines",
                        line=dict(color=colors_map[col], width=2), name=col),
                row=1, col=col_idx + 1
            )
            fig.update_xaxes(range=get_x_range(col, df), row=1, col=col_idx + 1,
                            showgrid=True, gridcolor="rgba(255,255,255,0.1)",
                            tickfont=dict(size=9), showticklabels=False)
        fig.update_yaxes(range=[y_max, y_min], autorange=False, showgrid=True,
                        gridcolor="rgba(255,255,255,0.1)", tickformat="%H:%M:%S",
                        row=1, col=1)
        fig.update_layout(
            height=1000, template="plotly_dark", showlegend=False,
            margin=dict(t=40, b=20, l=20, r=20),
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0.3)"
        )
        return fig

    st.caption("All Rights Reserved © 2026 || **Hassan Abdelghany Hussein**", text_alignment="center")
    st.caption("SDL Field Engineer • Petroleum Geologist • Python Developer", text_alignment="center")
    st.caption("Click Here to Visit [My LinkedIn Profile](https://www.linkedin.com/in/hassan-abdelghany-hussein/)", text_alignment="center")

    # ── Simulation ───────────────────────────────────────────────
    if run:
        fig = build_base_figure(df, selected_params, param_colors)
        title_annotations = list(fig.layout.annotations)
        chart_placeholder.plotly_chart(fig, use_container_width=True)

        for i in range(1, len(df) + 1):
            current_df = df.iloc[:i]
            data_annotations, shapes = [], []

            for _, row in current_df.iterrows():
                if pd.notna(row.get("Note")) and str(row["Note"]).strip():
                    target_param = str(row["Note_Param"]).strip()
                    if target_param in param_col_index:
                        col_idx = param_col_index[target_param]
                        x_val, color = row[target_param], note_color(row["Note"])
                        data_annotations.append(dict(
                            x=x_val, y=row["Time"],
                            xref=f"x{col_idx}" if col_idx > 1 else "x", yref="y",
                            text=f"<b>{row['Note']}</b>", showarrow=True,
                            arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor=color,
                            ax=60, ay=0, bgcolor="rgba(0,0,0,0.7)",
                            bordercolor=color, borderwidth=1.5, borderpad=4,
                            font=dict(color=color, size=10), align="left"
                        ))
                if pd.notna(row.get("Zone_Line")) and str(row["Zone_Line"]).strip():
                    zone_label = str(row["Zone_Line"]).strip()
                    shapes.append(dict(
                        type="line", xref="paper", yref="y",
                        x0=0, x1=1, y0=row["Time"], y1=row["Time"],
                        line=dict(color="#FF4444", width=2, dash="dash")
                    ))
                    data_annotations.append(dict(
                        x=0.5, y=row["Time"],
                        xref="paper", yref="y",
                        text=f"<b>▶ {zone_label}</b>",
                        showarrow=False,
                        xanchor="center",
                        yanchor="bottom",
                        bgcolor="rgba(0,0,0,0.6)",
                        bordercolor="#FF4444",
                        borderwidth=1.5,
                        borderpad=4,
                        font=dict(color="#FFFFFF", size=10),
                    ))

            for col_idx, col in enumerate(selected_params):
                fig.data[col_idx].x = current_df[col]
                fig.data[col_idx].y = current_df["Time"]

            fig.update_layout(annotations=title_annotations + data_annotations, shapes=shapes)
            chart_placeholder.plotly_chart(fig, use_container_width=True)
            time.sleep(st.session_state.speed)
    else:
        fig = build_base_figure(df, selected_params, param_colors)
        chart_placeholder.plotly_chart(fig, use_container_width=True)