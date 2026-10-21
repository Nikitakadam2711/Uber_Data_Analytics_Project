import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="Uber Data Analytics Dashboard",
    page_icon="🚕",
    layout="wide"
)

# -------------------------
# CUSTOM CSS
# -------------------------
st.markdown("""
<style>

.stApp{
    background-color:#0f172a;
}

h1,h2,h3,h4,h5,h6{
    color:white;
}

.metric-box{
    background:linear-gradient(135deg,#2563eb,#7c3aed);
    padding:20px;
    border-radius:18px;
    text-align:center;
    color:white;
    box-shadow:0px 5px 15px rgba(0,0,0,0.3);
}

.metric-value{
    font-size:32px;
    font-weight:bold;
}

.metric-label{
    font-size:15px;
}

section[data-testid="stSidebar"]{
    background-color:#111827;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# LOAD DATA
# -------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned_uber_data.csv")

try:
    df = load_data()
except:
    st.error("Dataset not found.")
    st.stop()

# -------------------------
# DATE FEATURES
# -------------------------
if "key" in df.columns:

    try:

        df["key"] = pd.to_datetime(df["key"])

        df["year"] = df["key"].dt.year
        df["month"] = df["key"].dt.month
        df["day_name"] = df["key"].dt.day_name()
        df["hour"] = df["key"].dt.hour

    except:
        pass

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.title("🎛 Dashboard Controls")

years = ["All"]

if "year" in df.columns:
    years += sorted(df["year"].dropna().unique().tolist())

selected_year = st.sidebar.selectbox(
    "Select Year",
    years
)

fare_range = st.sidebar.slider(
    "Fare Amount Range",
    float(df["fare_amount"].min()),
    float(df["fare_amount"].max()),
    (
        float(df["fare_amount"].min()),
        float(df["fare_amount"].max())
    )
)

filtered = df[
    (df["fare_amount"] >= fare_range[0]) &
    (df["fare_amount"] <= fare_range[1])
]

if selected_year != "All":
    filtered = filtered[filtered["year"] == selected_year]

# -------------------------
# HEADER
# -------------------------
st.markdown(
"""
<h1 style='text-align:center;color:white'>
🚕 UBER DATA ANALYTICS DASHBOARD
</h1>
""",
unsafe_allow_html=True
)

st.markdown("")

# -------------------------
# KPI CALCULATIONS
# -------------------------
total_trips = len(filtered)
total_revenue = filtered["fare_amount"].sum()
avg_fare = filtered["fare_amount"].mean()

if "passenger_count" in filtered.columns:
    avg_passenger = filtered["passenger_count"].mean()
else:
    avg_passenger = 0

# -------------------------
# KPI CARDS
# -------------------------
c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-value">{total_trips:,}</div>
        <div class="metric-label">🚕 Total Trips</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-value">${total_revenue:,.0f}</div>
        <div class="metric-label">💰 Total Revenue</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-value">${avg_fare:.2f}</div>
        <div class="metric-label">💵 Average Fare</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-value">{avg_passenger:.1f}</div>
        <div class="metric-label">👥 Avg Passengers</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------
# ROW 1
# -------------------------
col1,col2,col3 = st.columns(3)

# Peak Ride Hours
with col1:

    st.subheader("🕒 Peak Ride Hours")

    if "hour" in filtered.columns:

        hourly = (
            filtered
            .groupby("hour")
            .size()
            .reset_index(name="Trips")
        )

        fig1 = px.line(
            hourly,
            x="hour",
            y="Trips",
            markers=True
        )

        fig1.update_layout(
            template="plotly_dark",
            height=350
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

# Monthly Revenue
with col2:

    st.subheader("📈 Monthly Revenue")

    if "month" in filtered.columns:

        monthly = (
            filtered
            .groupby("month")["fare_amount"]
            .sum()
            .reset_index()
        )

        fig2 = px.bar(
            monthly,
            x="month",
            y="fare_amount"
        )

        fig2.update_layout(
            template="plotly_dark",
            height=350
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

# Day Wise Ride Count
with col3:

    st.subheader("📅 Day Wise Ride Count")

    if "day_name" in filtered.columns:

        order = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]

        day_data = (
            filtered["day_name"]
            .value_counts()
            .reindex(order)
            .reset_index()
        )

        day_data.columns = ["Day","Trips"]

        fig3 = px.bar(
            day_data,
            x="Trips",
            y="Day",
            orientation="h"
        )

        fig3.update_layout(
            template="plotly_dark",
            height=350
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

# -------------------------
# ROW 2
# -------------------------
left,right = st.columns(2)

with left:

    st.subheader("👥 Passenger Distribution")

    if "passenger_count" in filtered.columns:

        passenger = (
            filtered["passenger_count"]
            .value_counts()
            .sort_index()
            .reset_index()
        )

        passenger.columns = [
            "Passenger Count",
            "Trips"
        ]

        fig4 = px.bar(
            passenger,
            x="Passenger Count",
            y="Trips"
        )

        fig4.update_layout(
            template="plotly_dark",
            height=400
        )

        st.plotly_chart(
            fig4,
            use_container_width=True
        )

with right:

    st.subheader("💰 Fare Distribution")

    fig5 = px.histogram(
        filtered,
        x="fare_amount",
        nbins=50
    )

    fig5.update_layout(
        template="plotly_dark",
        height=400
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

   
# -------------------------
# DATA PREVIEW
# -------------------------
with st.expander("📄 View Dataset"):

    st.dataframe(
        filtered.head(100),
        use_container_width=True
    )

# -------------------------
# BUSINESS INSIGHTS
# -------------------------

st.subheader("🧠 Key Insights")

try:

    peak_hour = filtered["hour"].mode()[0]

    top_day = (
        filtered["day_name"]
        .value_counts()
        .idxmax()
    )

    top_month = (
        filtered.groupby("month")["fare_amount"]
        .sum()
        .idxmax()
    )

    common_passenger = (
        filtered["passenger_count"]
        .mode()[0]
    )

    st.success(f"""
    ✅ Peak Ride Hour : {peak_hour}:00

    ✅ Highest Ride Demand Day : {top_day}

    ✅ Highest Revenue Month : {top_month}

    ✅ Most Common Passenger Count : {common_passenger}

    ✅ Total Trips : {len(filtered):,}

    ✅ Total Revenue : ${filtered['fare_amount'].sum():,.0f}

    ✅ Average Fare : ${filtered['fare_amount'].mean():.2f}

    ✅ Dashboard successfully analyzes revenue, ride demand, passenger behaviour and pickup locations.
    """)

except:
    st.info("Insights unavailable.")