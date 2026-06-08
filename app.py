import streamlit as st
import pandas as pd
import plotly.express as px

from src.analytics import get_summary
from src.recommendation_engine import get_recommendation

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="AI Customer Segmentation Dashboard",
    page_icon="📊",
    layout="wide"
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
    "📊 AI-Powered Customer Segmentation Dashboard"
)

st.caption(
    "Customer Intelligence • Business Insights • Retention Analytics"
)

# =====================================
# TABS
# =====================================

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📈 Overview",
        "📊 Analytics",
        "👤 Customers",
        "📄 Reports"
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

    # ==========================
    # RECENCY VS SPENDING
    # ==========================

    st.subheader(
        "⏳ Recency vs Spending"
    )

    fig3 = px.scatter(
        df,
        x="Recency",
        y="TotalSpent",
        color="Segment",
        hover_data=[
            "CustomerID"
        ]
    )

    fig3.update_layout(
        template="plotly_dark",
        height=500
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    # ==========================
    # HISTOGRAMS
    # ==========================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "💰 Spending Distribution"
        )

        fig4 = px.histogram(
            df,
            x="TotalSpent",
            color="Segment",
            nbins=30
        )

        fig4.update_layout(
            template="plotly_dark",
            height=450
        )

        st.plotly_chart(
            fig4,
            use_container_width=True
        )

    with col2:

        st.subheader(
            "🛒 Orders Distribution"
        )

        fig5 = px.histogram(
            df,
            x="TotalOrders",
            color="Segment",
            nbins=30
        )

        fig5.update_layout(
            template="plotly_dark",
            height=450
        )

        st.plotly_chart(
            fig5,
            use_container_width=True
        )

    st.subheader(
        "⏳ Recency Distribution"
    )

    fig6 = px.histogram(
        df,
        x="Recency",
        color="Segment",
        nbins=30
    )

    fig6.update_layout(
        template="plotly_dark",
        height=450
    )

    st.plotly_chart(
        fig6,
        use_container_width=True
    )

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
        min_value=int(
            df["CustomerID"].min()
        ),
        max_value=int(
            df["CustomerID"].max()
        ),
        step=1
    )

    if st.button(
        "Search Customer"
    ):

        customer = df[
            df["CustomerID"] ==
            customer_id
        ]

        if not customer.empty:

            customer = (
                customer.iloc[0]
            )

            c1, c2, c3 = (
                st.columns(3)
            )

            c1.metric(
                "Customer ID",
                int(
                    customer["CustomerID"]
                )
            )

            c2.metric(
                "Orders",
                int(
                    customer["TotalOrders"]
                )
            )

            c3.metric(
                "Total Spent",
                round(
                    customer["TotalSpent"],
                    2
                )
            )

            c4, c5, c6 = (
                st.columns(3)
            )

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
                int(
                    customer["Rank"]
                )
            )

            st.success(
                get_recommendation(
                    customer["Segment"]
                )
            )

        else:

            st.error(
                "Customer Not Found"
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

    # ==========================
    # CLUSTER DETAILS
    # ==========================

    st.subheader(
        "📂 Cluster Wise Customer Details"
    )

    for segment in sorted(
        df["Segment"].unique()
    ):

        segment_df = df[
            df["Segment"] ==
            segment
        ]

        with st.expander(
            f"{segment} ({len(segment_df)} Customers)"
        ):

            st.dataframe(
                segment_df,
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

st.caption(
    "🚀 Built with Streamlit • Plotly • Pandas • Scikit-Learn"
)