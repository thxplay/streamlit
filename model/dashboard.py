import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import os

# Disable Plotly Narwhals Warning
os.environ["PLOTLY_DISABLE_NARWHALS"] = "true"

def dashboard():
    #######################
    # 📁 Load Data
    df = pd.read_excel('../dataset/data_cs_shop_instanbul.xlsx')
    df['invoice_date'] = pd.to_datetime(df['invoice_date'], errors='coerce')
    df['revenue'] = df['quantity'] * df['price']

    # 🧮 Hitung RFM Awal
    snapshot_date = pd.Timestamp("2025-04-11")
    rfm = df.groupby('customer_id').agg(
        max_transaction=('invoice_date', 'max'),
        monetary=('revenue', 'sum'),
        frequency=('invoice_no', 'nunique')
    ).reset_index()
    rfm['recency'] = ((snapshot_date - rfm['max_transaction']).dt.days // 30).astype(int)

    q1_m, q3_m = np.percentile(rfm['monetary'], [25, 75])
    q1_f, q3_f = np.percentile(rfm['frequency'], [25, 75])
    q1_r, q3_r = np.percentile(rfm['recency'], [25, 75])

    rfm['monetary_score'] = rfm['monetary'].apply(lambda x: 3 if x >= q3_m else 2 if x >= q1_m else 1)
    rfm['frequency_score'] = rfm['frequency'].apply(lambda x: 3 if x >= q3_f else 2 if x >= q1_f else 1)
    rfm['recency_score'] = rfm['recency'].apply(lambda x: 1 if x >= q3_r else 2 if x >= q1_r else 3)
    rfm['RFM_score'] = rfm['recency_score'] + rfm['frequency_score'] + rfm['monetary_score']

    def segment(row):
        score = row['RFM_score']
        r = row['recency_score']
        if score == 9:
            return "Champion"
        elif score == 8:
            return "Loyal"
        elif score in [6, 7] and r == 3:
            return "Recent Customer"
        elif score in [6, 7] and r == 1:
            return "Cannot Lose Them"
        elif score == 7:
            return "Potential Loyalist"
        elif score == 6:
            return "Average"
        elif score in [4, 5]:
            return "About To Sleep"
        elif score == 3:
            return "Lost Customer"
        else:
            return "Uncategorized"

    rfm['Segment'] = rfm.apply(segment, axis=1)
    df_latest = df[['customer_id', 'gender', 'shopping_mall']].drop_duplicates('customer_id')
    rfm = pd.merge(rfm, df_latest, on='customer_id', how='left')

    #######################
    # 📢 Header
    st.image("../images/istanbul.png", width=250)
    st.title("RFM Customer Segmentation")
    st.info("Menganalisis Pola Pembelian Konsumen melalui Analisis Pembelian Produk di Kota Istanbul")

    #######################
    # 🧭 Sidebar Filters
    with st.sidebar:
        st.title("⚙️ Menu Dashboard")

        with st.expander("📅 Invoice Date", expanded=True):
            df['year'] = df['invoice_date'].dt.year
            min_date = df['invoice_date'].min().date()
            max_date = df['invoice_date'].max().date()
            date_range = st.slider("Pilih rentang tanggal:", min_value=min_date, max_value=max_date, value=(min_date, max_date), format="YYYY-MM-DD")
            df = df[(df['invoice_date'] >= pd.to_datetime(date_range[0])) & (df['invoice_date'] <= pd.to_datetime(date_range[1]))]
            year_list = sorted(df['year'].dropna().unique(), reverse=True)
            year_options = [str(y) for y in year_list]
            selected_years = st.multiselect("Pilih Tahun", options=year_options, default=year_options)

            if selected_years:
                df = df[df['year'].astype(str).isin(selected_years)]

        with st.expander("💰 Revenue"):
            st.write("Total Revenue: ", f"{df['revenue'].sum():,.2f}")
            payment_methods = st.multiselect("Payment Method", options=df['payment_method'].dropna().unique(), default=list(df['payment_method'].dropna().unique()))
            df = df[df['payment_method'].isin(payment_methods)]

        with st.expander("🛍️ Category"):
            categories = st.multiselect("Product Category", options=df['category'].dropna().unique(), default=list(df['category'].dropna().unique()))
            df = df[df['category'].isin(categories)]

        with st.expander("🧑 Customers Personality"):
            genders = st.multiselect("Gender", options=df['gender'].dropna().unique(), default=list(df['gender'].dropna().unique()))
            df = df[df['gender'].isin(genders)]
            age_min, age_max = int(df['age'].min()), int(df['age'].max())
            age_range = st.slider("Age Range", min_value=age_min, max_value=age_max, value=(age_min, age_max))
            df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1])]

        with st.expander("📍 Location"):
            malls = st.multiselect("Shopping Mall", options=df['shopping_mall'].dropna().unique(), default=list(df['shopping_mall'].dropna().unique()))
            df = df[df['shopping_mall'].isin(malls)]

        with st.expander("📈 RFM"):
            recency_min, recency_max = int(rfm['recency_score'].min()), int(rfm['recency_score'].max())
            mon_min, mon_max = int(rfm['monetary_score'].min()), int(rfm['monetary_score'].max())
            rfm_min, rfm_max = int(rfm['RFM_score'].min()), int(rfm['RFM_score'].max())

            recency_range = st.slider("Recency Score", min_value=recency_min, max_value=recency_max, value=(recency_min, recency_max))
            mon_range = st.slider("Monetary Score", min_value=mon_min, max_value=mon_max, value=(mon_min, mon_max))
            rfm_range = st.slider("RFM Score", min_value=rfm_min, max_value=rfm_max, value=(rfm_min, rfm_max))

            rfm = rfm[
                (rfm['recency_score'].between(*recency_range)) &
                (rfm['monetary_score'].between(*mon_range)) &
                (rfm['RFM_score'].between(*rfm_range))
            ]

    #######################
    # 📊 Quick Stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("🧾 Total Orders")
        st.title(f"{df['invoice_no'].nunique():,}")
    with col2:
        st.subheader("💰 Total Revenue")
        st.title(f"{df['revenue'].sum():,.2f}")
    with col3:
        st.subheader("👥 Total Customers")
        st.title(f"{df['customer_id'].nunique():,}")

    #######################
    # 📆 Revenue Over Time
    col1, col2 = st.columns([2, 1])

    with col1:
        df['period'] = df['invoice_date'].dt.to_period('M').astype(str)
        revenue_by_period = df.groupby('period')['revenue'].sum().reset_index()
        revenue_by_period['period'] = pd.to_datetime(revenue_by_period['period'])

        fig_line = px.line(
            revenue_by_period, 
            x='period', y='revenue',
            title='Revenue Growth by Year, Quarter, and Month',
            labels={'period': 'Periode', 'revenue': 'Total Revenue'},
            markers=True
        )
        fig_line.update_traces(line=dict(color='#01ADCD'))
        fig_line.update_layout(
            title_x=0.5,
            xaxis_title="Tanggal (Year-Month)",
            yaxis_title="Revenue",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_line, use_container_width=True)

    with col2:
        mall_seg = rfm.groupby(['shopping_mall', 'Segment'])['customer_id'].nunique().reset_index()
        mall_total = mall_seg.groupby('shopping_mall')['customer_id'].sum().reset_index(name='total')
        mall_seg = pd.merge(mall_seg, mall_total, on='shopping_mall')
        mall_seg = mall_seg.sort_values('total', ascending=False)

        segment_colors = {
        "Loyal": '#0070C0',
        "Potential Loyalist": '#477BE2',
        "Cannot Lose Them": '#CC66FF',
        "Average": '#00B4D7',
        "Champion": '#9444ED',
        "About To Sleep": '#FF66FF',
        "Recent Customer": '#9999FF'
        }

        fig_mall_seg = px.bar(
            mall_seg, x='shopping_mall', y='customer_id', color='Segment', 
            title="Shopping Malls by Revenue",
            color_discrete_map=segment_colors
        )
        fig_mall_seg.update_layout(
            xaxis={'categoryorder': 'total descending'},
            title_x=0.5
        )
        st.plotly_chart(fig_mall_seg, use_container_width=True)

    #######################
    # 📊 Segment Visualizations
    col1, col2, col3 = st.columns(3)

    with col1:
        category_colors = {
            'Clothing': '#9444ED',
            'Costmetics': '#715AE7',
            'Food & Beverages': '#477BE2',
            'Toys': '#10A0DD',
            'Shoes': '#00B4D7',
            'Technology': '#F800B8',
            'Books': '#CE13F0',
            'Souvenir': '#AB32ED'
        }

        category_sales = df.groupby('category')['quantity'].sum().reset_index().sort_values('quantity', ascending=False)
        fig_cat = px.bar(
            category_sales, 
            x='quantity', y='category', orientation='h', 
            title="Best-Selling Categories",
            color='category',
            color_discrete_map=category_colors
        )
        fig_cat.update_layout(title_x=0.5, yaxis={'categoryorder': 'total ascending'})
        st.plotly_chart(fig_cat, use_container_width=True)

    with col2:
        gender_colors = {'Male': '#00B6D8', 'Female': '#F800B8'}
        gender_df = df_latest.groupby('gender')['customer_id'].nunique().reset_index()
        fig_gender = px.pie(
            gender_df, names='gender', values='customer_id', 
            title='User by Gender',
            color='gender',
            color_discrete_map=gender_colors
        )
        fig_gender.update_layout(title_x=0.5)
        st.plotly_chart(fig_gender, use_container_width=True)

    with col3:
        segment_colors = {
            "Loyal": '#0070C0',
            "Potential Loyalist": '#477BE2',
            "Cannot Lose Them": '#CC66FF',
            "Average": '#00B4D7',
            "Champion": '#9444ED',
            "About To Sleep": '#FF66FF',
            "Recent Customer": '#9999FF'
        }
        seg_df = rfm.groupby('Segment')['customer_id'].nunique().reset_index().sort_values('customer_id', ascending=False)
        fig_seg = px.bar(
            seg_df, x='customer_id', y='Segment', orientation='h',
            title='User Count by Segment',
            color='Segment',
            color_discrete_map=segment_colors
        )
        fig_seg.update_layout(title_x=0.5)
        st.plotly_chart(fig_seg, use_container_width=True)
        
    #######################
    # 📋 Segment Table
    st.markdown("### 📋 Customer Segment Table")
    st.dataframe(rfm[['customer_id', 'Segment']].sort_values('customer_id'), use_container_width=True)
