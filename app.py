import streamlit as st
import pandas as pd
import plotly.express as px


from src.analytics import get_summary
from src.recommendation_engine import get_recommendation
from src.intent_engine import add_intent

from src.customer_health import add_health_metrics

from src.customer_scoring import add_customer_scoring
from src.ai_ad_generator import generate_ai_ad


from src.channel_intelligence import (
    recommend_channel,
    recommend_time
)

from src.campaign_generator import (
    generate_campaign
)

from src.performance_predictor import (
    predict_conversion,
    predict_roi
)

from src.forecasting import (
    revenue_forecast
)

from src.marketing_assistant import (
    answer_query
)
from src.behavior_intent import (
    detect_intent,
    get_strategy
)
from src.customer_age import add_age_group
from src.explainable_ai import (
    explain_customer
)
from src.ai_ad_generator import (
    generate_ai_ad
)



# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

h1 {
    text-align: center;
    color: #00C9A7;
}

div[data-testid="metric-container"] {
    background-color: #1E1E1E;
    border: 1px solid #333;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
}

section[data-testid="stSidebar"] {
    background-color: #111827;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# LOAD DATA
# =====================================

df = pd.read_csv(
    "data/segmented_customers.csv"
)

df = add_intent(df)

df = add_age_group(df)

df = add_health_metrics(df)

df = add_customer_scoring(df)

df["RecommendedChannel"] = df.apply(

    lambda row:
    recommend_channel(

        row["AgeGroup"],
        row["Intent"],
        row["Segment"]

    ),

    axis=1
)

df["CampaignTime"] = (
    df["AgeGroup"]
    .apply(recommend_time)
)

df["ExpectedConversion"] = (
    df["Segment"]
    .apply(predict_conversion)
)

df["ExpectedROI"] = (
    df["Segment"]
    .apply(predict_roi)
)


# =====================================
# RISK LEVEL
# =====================================

def risk_level(recency):

    if recency < 30:
        return "🟢 Low"

    elif recency < 90:
        return "🟡 Medium"

    else:
        return "🔴 High"

df["Risk"] = df["Recency"].apply(
    risk_level
)

# =====================================
# CUSTOMER RANK
# =====================================

df["Rank"] = (
    df["TotalSpent"]
    .rank(
        ascending=False,
        method="dense"
    )
    .astype(int)
)

# =====================================
# SIDEBAR
# =====================================

st.sidebar.title(
    "🎯 Customer Intelligence Hub"
)

selected_segment = st.sidebar.multiselect(
    "Select Segment",
    options=df["Segment"].unique(),
    default=df["Segment"].unique()
)

df = df[
    df["Segment"].isin(
        selected_segment
    )
]

summary = get_summary(df)

st.sidebar.markdown("---")

st.sidebar.metric(
    "Customers",
    len(df)
)

st.sidebar.metric(
    "Revenue",
    round(
        df["TotalSpent"].sum(),
        2
    )
)

st.sidebar.metric(
    "Segments",
    df["Segment"].nunique()
)

# =====================================
# TITLE
# =====================================

st.title(
    "🚀 IntentReach AI"
)

st.caption(
    "Predict Intent • Understand Customers • Optimize Campaigns"
)

# =====================================
# TABS
# =====================================

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11 = st.tabs(
[
    "📈 Overview",
    "📊 Analytics",
    "👤 Customers",
    "📄 Reports",
    "🎯 Intent Radar",
    "❤️ Customer Health",
    "⭐ Customer Scoring",
    "📢 Campaign Intelligence",
    "🤖 AI Assistant",
    "🧠 Behavioral Intent",
    "📈 Revenue Forecast"
]
)


# =====================================
# OVERVIEW TAB
# =====================================

with tab1:

    st.header(
        "📈 Executive Dashboard"
    )

    premium_count = len(
        df[
            df["Segment"] ==
            "Premium Customers"
        ]
    )

    at_risk_count = len(
        df[
            df["Segment"] ==
            "At Risk Customers"
        ]
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "👥 Total Customers",
        summary["total_customers"]
    )

    col2.metric(
        "🛒 Avg Orders",
        summary["average_orders"]
    )

    col3.metric(
        "💰 Avg Spending",
        summary["average_spending"]
    )

    col4, col5, col6 = st.columns(3)

    col4.metric(
        "⏳ Avg Recency",
        summary["average_recency"]
    )

    col5.metric(
        "⭐ Premium Customers",
        premium_count
    )

    col6.metric(
        "⚠️ At Risk Customers",
        at_risk_count
    )

    st.markdown("---")

    if not df.empty:

        largest_segment = (
            df["Segment"]
            .value_counts()
            .idxmax()
        )

        highest_spending_segment = (
            df.groupby("Segment")
            ["TotalSpent"]
            .mean()
            .idxmax()
        )

        st.info(
            f"""
📈 Largest Segment: {largest_segment}

💰 Highest Spending Segment: {highest_spending_segment}

👥 Customers Analysed: {len(df)}
"""
        )

    st.subheader(
        "Customer Segment Distribution"
    )

    fig = px.pie(
        df,
        names="Segment",
        hole=0.4
    )

    fig.update_layout(
        template="plotly_dark",
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader(
        "Customers Per Segment"
    )

    segment_count = (
        df.groupby("Segment")
        .size()
        .reset_index(
            name="Customers"
        )
    )

    fig_bar = px.bar(
        segment_count,
        x="Segment",
        y="Customers",
        color="Segment",
        text_auto=True
    )

    fig_bar.update_layout(
        template="plotly_dark",
        height=500
    )

    st.plotly_chart(
        fig_bar,
        use_container_width=True
    )
    # =====================================
# ANALYTICS TAB
# =====================================

with tab2:

    st.header(
        "📊 Customer Analytics"
    )

    # ==========================
    # REVENUE BY SEGMENT
    # ==========================

    st.subheader(
        "💰 Revenue By Segment"
    )

    revenue = (
        df.groupby("Segment")
        ["TotalSpent"]
        .sum()
        .reset_index()
    )

    fig_rev = px.bar(
        revenue,
        x="Segment",
        y="TotalSpent",
        color="Segment",
        text_auto=True
    )

    fig_rev.update_layout(
        template="plotly_dark",
        height=500
    )

    st.plotly_chart(
        fig_rev,
        use_container_width=True
    )

    # ==========================
    # ORDERS VS SPENDING
    # ==========================

    st.subheader(
        "🛒 Orders vs Spending"
    )

    fig2 = px.scatter(
        df,
        x="TotalOrders",
        y="TotalSpent",
        color="Segment",
        hover_data=[
            "CustomerID"
        ]
    )

    fig2.update_layout(
        template="plotly_dark",
        height=500
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    

# =====================================
# CUSTOMERS TAB


        
# =====================================
# CUSTOMERS TAB
# =====================================

with tab3:

    st.header(
        "👤 Customer Intelligence"
    )

    st.subheader(
        "🔍 Customer Search"
    )

    customer_id = st.number_input(
        "Enter Customer ID",
        min_value=int(df["CustomerID"].min()),
        max_value=int(df["CustomerID"].max()),
        step=1
    )

    if st.button("Search Customer"):

        customer = df[
            df["CustomerID"] == customer_id
        ]

        if not customer.empty:

            customer = customer.iloc[0]

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Customer ID",
                int(customer["CustomerID"])
            )

            c2.metric(
                "Orders",
                int(customer["TotalOrders"])
            )

            c3.metric(
                "Total Spent",
                round(customer["TotalSpent"], 2)
            )

            c4, c5, c6 = st.columns(3)

            c4.metric(
                "Segment",
                customer["Segment"]
            )

            c5.metric(
                "Risk",
                customer["Risk"]
            )

            c6.metric(
                "Rank",
                int(customer["Rank"])
            )

            st.success(
                get_recommendation(
                    customer["Segment"]
                )
            )

            st.subheader(
                "🧠 Explainable AI"
            )

            explanation = explain_customer(
                customer
            )

            st.info(explanation)

        else:

            st.error(
                "Customer Not Found"
            )

    st.subheader(
        "🏆 Top 10 Customers"
    )

    top_customers = (
        df.sort_values(
            "TotalSpent",
            ascending=False
        )
        .head(10)
    )

    st.dataframe(
        top_customers,
        use_container_width=True
    )

    st.subheader(
        "📂 Cluster Wise Customer Details"
    )

    for segment in sorted(
        df["Segment"].unique()
    ):

        segment_df = df[
            df["Segment"] == segment
        ]

        with st.expander(
            f"{segment} ({len(segment_df)} Customers)"
        ):

            st.dataframe(
                segment_df,
                use_container_width=True
            )

       

   

    # ==========================
    # TOP CUSTOMERS
    # ==========================

    st.subheader(
        "🏆 Top 10 Customers"
    )

    top_customers = (
        df.sort_values(
            "TotalSpent",
            ascending=False
        )
        .head(10)
    )

    st.dataframe(
        top_customers,
        use_container_width=True
    )

  

# =====================================
# REPORTS TAB
# =====================================

with tab4:

    st.header(
        "📄 Reports & Insights"
    )

    # ==========================
    # SEGMENT COMPARISON
    # ==========================

    st.subheader(
        "📊 Segment Comparison"
    )

    comparison = (
        df.groupby("Segment")
        [
            [
                "TotalOrders",
                "TotalSpent",
                "Recency"
            ]
        ]
        .mean()
        .round(2)
    )

    st.dataframe(
        comparison,
        use_container_width=True
    )

    # ==========================
    # RISK ANALYSIS
    # ==========================

    st.subheader(
        "⚠️ Customer Risk Analysis"
    )

    risk_summary = (
        df.groupby("Risk")
        .size()
        .reset_index(
            name="Customers"
        )
    )

    st.dataframe(
        risk_summary,
        use_container_width=True
    )

    # ==========================
    # RECOMMENDATIONS
    # ==========================

    st.subheader(
        "🎯 Business Recommendations"
    )

    for segment in sorted(
        df["Segment"].unique()
    ):

        st.success(
            f"{segment}: {get_recommendation(segment)}"
        )

    # ==========================
    # DOWNLOAD REPORT
    # ==========================

    st.subheader(
        "📥 Export Report"
    )

    csv = df.to_csv(
        index=False
    )

    st.download_button(
        label="Download Segmentation Report",
        data=csv,
        file_name="segmentation_report.csv",
        mime="text/csv"
    )

# =====================================
# FOOTER
# =====================================

st.markdown("---")
# =====================================
# INTENTREACH AI TAB
# =====================================

with tab5:

    st.header(
        "🎯 IntentReach AI"
    )

    st.subheader(
        "Customer Intent Distribution"
    )

    intent_count = (
        df["Intent"]
        .value_counts()
        .reset_index()
    )

    intent_count.columns = [
        "Intent",
        "Customers"
    ]

    fig = px.bar(

        intent_count,

        x="Intent",

        y="Customers",

        color="Intent",

        text_auto=True
    )

    fig.update_layout(
        template="plotly_dark"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader(
        "AI Campaign Generator"
    )

    customer = st.selectbox(
        "Select Customer",
        df["CustomerID"]
    )

    selected = df[
        df["CustomerID"]
        ==
        customer
    ].iloc[0]

    st.info(
        f"Intent: {selected['Intent']}"
    )

# =====================================
# CUSTOMER HEALTH TAB
# =====================================

with tab6:

    st.header(
        "❤️ Customer Health"
    )

    st.dataframe(

        df[
            [
                "CustomerID",
                "HealthScore",
                "HealthStatus"
            ]
        ],

        use_container_width=True
    )

    fig = px.histogram(

        df,

        x="HealthStatus",

        color="HealthStatus"

    )

    fig.update_layout(
        template="plotly_dark"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
  # =====================================
# CUSTOMER SCORING TAB
# =====================================

with tab7:

    st.header(
        "⭐ Customer Scoring"
    )

    st.dataframe(

        df[
            [
                "CustomerID",
                "CustomerScore",
                "Tier"
            ]
        ],

        use_container_width=True
    )

    fig = px.histogram(

        df,

        x="Tier",

        color="Tier"

    )

    fig.update_layout(
        template="plotly_dark"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
# =====================================
# CAMPAIGN INTELLIGENCE TAB
# =====================================
with tab8:

    st.header("📢 Campaign Intelligence")

    customer = st.selectbox(
        "Select Customer",
        df["CustomerID"],
        key="campaign_customer"
    )

    row = df[
        df["CustomerID"] == customer
    ].iloc[0]

    campaign = generate_campaign(
        row["Intent"]
    )

    st.info(...)

    st.metric(
        "Recommended Channel",
        row["RecommendedChannel"]
    )

    st.metric(
        "Best Campaign Time",
        row["CampaignTime"]
    )

    st.metric(
        "Expected Conversion",
        f"{row['ExpectedConversion']}%"
    )

    st.metric(
        "Expected ROI",
        f"{row['ExpectedROI']}%"
    )

    # ADD THE AI AD SECTION HERE

    st.subheader(
        "🎨 AI Generated Advertisement"
    )

    if st.button(
        "Generate Personalized Ad",
        key="generate_ad_btn"
    ):

        ad = generate_ai_ad(row)

        st.markdown(
            ad,
            unsafe_allow_html=True
        )

        st.download_button(
            "📥 Download Advertisement",
            data=ad,
            file_name="Personalized_Ad.html",
            mime="text/html"
        )
 
 # =====================================
# AI ASSISTANT TAB
# =====================================

with tab9:

    st.header(
        "🤖 AI Marketing Assistant"
    )

    question = st.text_input(
        "Ask IntentReach AI"
    )

    if question:

        answer = answer_query(
            question,
            df
        )

        st.success(
            answer
        )
# =====================================
# BEHAVIORAL INTENT ANALYZER
# =====================================

with tab10:

    st.header(
        "🧠 Behavioral Intent Analyzer"
    )

    st.write(
        "Enter customer behavior or interests to predict intent."
    )

    user_text = st.text_area(
        "Customer Behavior"
    )

    if st.button(
        "Analyze Intent"
    ):

        intent = detect_intent(
            user_text
        )

        st.success(
            f"Predicted Intent: {intent}"
        )

        strategy = get_strategy(
            intent
        )

        if strategy:

            st.subheader(
                "Recommended Products"
            )

            for product in strategy["Products"]:

                st.write(
                    f"✅ {product}"
                )

            st.subheader(
                "Recommended Marketing Strategy"
            )

            st.info(
                strategy["Strategy"]
            )
# =====================================
# REVENUE FORECAST TAB
# =====================================

with tab11:

    st.header(
        "📈 Revenue Forecast"
    )

    forecast = revenue_forecast(df)

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "30 Days Revenue",
        f"₹{forecast['30 Days']:,.2f}"
    )

    col2.metric(
        "60 Days Revenue",
        f"₹{forecast['60 Days']:,.2f}"
    )

    col3.metric(
        "90 Days Revenue",
        f"₹{forecast['90 Days']:,.2f}"
    )

    forecast_df = pd.DataFrame(
        {
            "Period": [
                "30 Days",
                "60 Days",
                "90 Days"
            ],
            "Revenue": [
                forecast["30 Days"],
                forecast["60 Days"],
                forecast["90 Days"]
            ]
        }
    )

    fig = px.line(
        forecast_df,
        x="Period",
        y="Revenue",
        markers=True,
        title="Revenue Forecast Trend"
    )

    fig.update_layout(
        template="plotly_dark"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.caption(
    "🚀 Built with Streamlit • Plotly • Pandas • Scikit-Learn"
)