import streamlit as st
import pandas as pd
import os
import numpy as np
from scipy import stats
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import io

import warnings
warnings.filterwarnings("ignore", message=".*use_column_width.*")

#######################
# ⚙️ Page Configuration
st.set_page_config(
    page_title="Project RFM Customer Segmentation - Shopping Dataset (Retail Sales Data)",
    page_icon="📊",
    layout="wide"
)

st.sidebar.title('⚙️ Menu Utama')
page = st.sidebar.radio('Pilih halaman:', ['Data Understanding', 'Dashboard', 'Insight', 'About Me'])

if page == 'Data Understanding':

    pd.set_option('display.max_rows', None)  # Menampilkan semua baris
    pd.set_option('display.max_columns', None)  # Jika ada banyak kolom

    st.markdown("<h1 style='text-align: center;'>RFM Customer Segmentation - Shopping Dataset (Retail Sales Data)</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: left;'>Deskripsi:</h2>", unsafe_allow_html=True)
    st.info("Menganalisis Pola Pembelian Konsumen melalui Analisis Pembelian Produk di Kota Istanbul")
    st.markdown("<div style='text-align: justify;'>Proyek ini bertujuan untuk menganalisis perilaku belanja konsumen berdasarkan data transaksi dari 10 pusat perbelanjaan di Istanbul selama tahun 2021 hingga 2023. Dengan menggunakan pendekatan Customer Segmentation, proyek ini berupaya mengelompokkan konsumen berdasarkan usia, jenis kelamin, perilaku belanja, dan metode pembayaran untuk membantu pelaku bisnis memahami preferensi konsumen secara lebih mendalam.</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])  # kolom tengah lebih lebar
    with col2:
        st.image("images/istanbul-thumb.jpg", use_container_width=True)

    with st.expander("📋 About Dataset"):
        st.write('## Dataset : data_cs_shop_Istanbul')
        st.write('99.457 baris : Mewakili jumlah transaksi individu')
        st.write('10 kolom : Mewakili 10 atribut')
        st.write('Periode data dari Tahun 2021 (Awal) sampai Tahun 2023 (Bulan Maret)')
        st.markdown("""
        ### 📄 Deskripsi Dataset

        | **Nama Variabel**   | **Deskripsi**                                                                 |
        |---------------------|-------------------------------------------------------------------------------|
        | `invoice_no`        | Nomor faktur unik untuk setiap transaksi. Format: kombinasi huruf "I" dan 6 digit angka |
        | `customer_id`       | ID unik pelanggan. Format: kombinasi huruf "C" dan 6 digit angka             |
        | `gender`            | Jenis kelamin pelanggan (Laki-laki / Perempuan)                              |
        | `age`               | Usia pelanggan dalam bilangan bulat positif                                  |
        | `category`          | Kategori produk yang dibeli (misalnya: Clothing, Cosmetics, dll)             |
        | `quantity`          | Jumlah unit produk yang dibeli dalam satu transaksi                          |
        | `price`             | Harga satuan produk dalam Lira Turki (TL)                                    |
        | `payment_method`    | Metode pembayaran yang digunakan (Tunai, Kartu Kredit, Kartu Debit)          |
        | `invoice_date`      | Tanggal saat transaksi terjadi                                               |
        | `shopping_mall`     | Nama pusat perbelanjaan tempat transaksi dilakukan                           |
        """)

        df = pd.read_excel('dataset/data_cs_shop_instanbul.xlsx')
        st.markdown("<h2 style='text-align: justify;'>Datasets</h2>", unsafe_allow_html=True)
        st.dataframe(df)
        if 'Unnamed: 0' in df.columns:
            df.drop(columns='Unnamed: 0', inplace=True)
        info_df = pd.DataFrame({
            "Kolom": df.columns,
            "Non-Null Count": df.notnull().sum().values,
            "Tipe Data": df.dtypes.values
            })
        st.subheader("📋 Informasi Struktur Datasets (After Pre Processing)")
        st.dataframe(info_df)

    
    # Fungsi untuk visualisasi outlier
    def check_plot(df_cs, column):
        plt.figure(figsize=(16, 4))

        plt.subplot(1, 3, 1)
        sns.histplot(df_cs[column], bins=30)
        plt.title(f'Histogram - {column}')

        plt.subplot(1, 3, 2)
        stats.probplot(df_cs[column], dist="norm", plot=plt)
        plt.ylabel('Variable quantiles')

        plt.subplot(1, 3, 3)
        sns.boxplot(y=df_cs[column])
        plt.title(f'Boxplot - {column}')

        st.pyplot(plt.gcf())
        plt.clf()

    with st.expander("🧹 Data Pre Processing (Python with Google Colab)"):
        # 1. Duplikat
        st.subheader("✅ Pengecekan Duplikat")
        st.markdown("<div style='text-align: justify;'>Tidak ditemukan duplikat.</div>", unsafe_allow_html=True)
        pilih1 = st.radio("Tampilkan pengecekan?", ["Tidak", "Pengecekan"], key="cek_duplikat")
        if pilih1 == "Pengecekan":
            prop_unique = len(df.drop_duplicates()) / len(df)
            st.write(f"Proporsi data unik: `{prop_unique:.4f}`")
            if prop_unique < 1:
                st.error("⚠️ Ditemukan duplikat dalam data.")
            else:
                st.success("✅ Tidak ditemukan duplikat dalam data.")

        st.markdown("---")

        # 2. Tipe Data
        st.subheader("⚠️ Pengecekan Tipe Data")
        st.markdown("<div style='text-align: justify;'>Merubah format kolom “Invoice Date” ( Object → Datetime )</div>", unsafe_allow_html=True)
        pilih2 = st.radio("Tampilkan setelah sudah diubah?", ["Tidak", "Pengecekan"], key="cek_tipe")
        if pilih2 == "Pengecekan":
            buffer = io.StringIO()
            df.info(buf=buffer)
            info_str = buffer.getvalue()
            st.text(info_str)

        st.markdown("---")

        # 3. Missing Value
        st.subheader("✅ Pengecekan Missing Value")
        st.markdown("<div style='text-align: justify;'>Tidak ditemukan missing value.</div>", unsafe_allow_html=True)
        pilih3 = st.radio("Tampilkan pengecekan?", ["Tidak", "Pengecekan"], key="cek_missing")
        if pilih3 == "Pengecekan":
            st.dataframe(df.isna().sum())

        st.markdown("---")

        # 4. Outlier
        st.subheader("⚠️ Pengecekan Outlier")
        st.markdown("<div style='text-align: justify;'>Terdapat Outlier pada kolom “Price” dimana harga pada kolom “Price” masih masuk akal dan banyak sehingga outlier tidak dihapus</div>", unsafe_allow_html=True)
        pilih4 = st.radio("Tampilkan pengecekan?", ["Tidak", "Pengecekan"], key="cek_outlier")
        if pilih4 == "Pengecekan":
            st.write("🔍 Cek Plot Kolom `age`")
            check_plot(df, 'age')

            st.write("🔍 Cek Plot Kolom `quantity`")
            check_plot(df, 'quantity')

            st.write("🔍 Cek Plot Kolom `price`")
            check_plot(df, 'price')

            st.write("📌 Nilai unik di kolom `price` (diurutkan):")
            uq_price = sorted(df['price'].unique())
            st.write(uq_price)

            # Tampilkan transaksi tertentu (bukti outlier logis)
            for target_price in [5250.0, 4200.0, 3150.0, 3000.85]:
                st.write(f"📄 Transaksi dengan harga {target_price}:")
                df_cs_filter = df[df['price'] == target_price]
                st.dataframe(df_cs_filter)
        
    with st.expander("🎯 Tujuan Proyek & Masalah Bisnis"):
        st.markdown("### 🎯 Tujuan Proyek")
        st.markdown("""
        - Mengelompokkan pelanggan berdasarkan **RFM** waktu terakhir pembelian **(Recency)**, frekuensi transaksi (**Frequency)**, dan nilai pembelian **(Monetary)**.  
        - Mengidentifikasi pelanggan bernilai tinggi dan berisiko hilang untuk menyusun strategi yang lebih tepat.  
        - Memberikan insight untuk pengambilan keputusan pemasaran berbasis data.
        """)

        st.markdown("### 👥 Pihak yang Diuntungkan")
        st.markdown("""
        - **Tim Marketing**: Menargetkan kampanye promosi ke segmen dengan potensi tertinggi.  
        - **Manajemen Pusat Perbelanjaan**: Menentukan strategi retensi pelanggan dan loyalty program.  
        - **Retailer**: Lebih memahami pelanggan aktif vs. pasif untuk penawaran yang disesuaikan.
        """)

        st.markdown("### ❓ Masalah Bisnis")
        st.markdown("""
        **Bagaimana cara mengelompokkan pelanggan berdasarkan perilaku belanja mereka agar strategi pemasaran lebih terarah dan berdampak?**  

        Saat ini, semua pelanggan cenderung diperlakukan sama, padahal kontribusinya berbeda-beda. Tanpa pemetaan pelanggan yang jelas, promosi bisa tidak efektif dan menyebabkan biaya tinggi.
        """)

        st.markdown("### ✅ Manfaat dari Solusi Ini:")
        st.markdown("""
        - Meningkatkan efisiensi anggaran promosi.  
        - Fokus pada retensi pelanggan bernilai tinggi.  
        - Mengurangi churn dari pelanggan yang berisiko hilang.  
        - Mendukung strategi bisnis yang lebih terfokus dan berbasis data.
        """)

    with st.expander("🧠 Customer Segmentation - RFM Score"):
        st.markdown("## 📊 Customer Segmentation")
        st.markdown("Perhitungan RFM ( **R**ecency, **F**requency, **M**onetary ) Score")
        row1, row2, row3 = st.columns([2, 1, 2])

        with row1:
            st.image("../images/rfm1.png", caption="Total Score Formula RFM", use_container_width=True)
        with row2:
            st.image("../images/rfm2.png", caption="Distribution RFM Score", use_container_width=True)
        with row3:
            st.image("../images/rfm3.png", caption="Customer Segmentation Strategy & Action", use_container_width=True)

        st.markdown("---")

        st.markdown("## 📐 Pembagian RFM (Recency, Frequency, Monetary)")
        left_col, right_col = st.columns([2, 2])

        with left_col:
            st.markdown("""
            - **Q1 (25%)**: Batas bawah — 25% data di bawah nilai ini  
            - **Q2 (50%)**: Median — nilai tengah dari seluruh data  
            - **Q3 (75%)**: Batas atas — 75% data di bawah nilai ini
            """)

        with right_col:
            st.image("../images/rfm4.png", caption="RFM Quartile", use_container_width=True)


elif page == 'Dashboard':
    import dashboard
    dashboard.dashboard()

elif page == 'Insight':
    import insight
    insight.insight()

elif page == 'About Me':
    import aboutme
    aboutme.aboutme()