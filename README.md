# 🧠 Customer Segmentation with RFM Analysis & Dashboard Insights

📊 **RFM (Recency, Frequency, Monetary)** analysis for customer segmentation, backed with actionable business insights from PowerBI & interactive Streamlit dashboard.

---

## 🚀 Tujuan Project
- Mengelompokkan pelanggan berdasarkan RFM waktu terakhir pembelian (Recency), frekuensi transaksi (Frequency), dan nilai pembelian (Monetary).
- Mengidentifikasi pelanggan bernilai tinggi dan berisiko hilang untuk menyusun strategi yang lebih tepat.
- Memberikan insight untuk pengambilan keputusan pemasaran berbasis data.

---

## Dataset Kaggle

Customer Shopping Dataset -  Retail Sales Data
https://www.kaggle.com/datasets/mehmettahiraslan/customer-shopping-dataset

---

## 🚀 Project Overview

Dalam dunia retail modern, memahami perilaku pelanggan adalah kunci untuk meningkatkan loyalitas dan efisiensi pemasaran. Proyek ini menggunakan model **RFM (Recency, Frequency, Monetary)** untuk melakukan **segmentasi pelanggan** secara strategis.

### 🔍 Apa itu RFM?

RFM adalah metode analisis pelanggan berbasis data historis transaksi, yang terdiri dari:

- **Recency** — Seberapa *baru* pelanggan melakukan transaksi terakhir. Semakin baru, semakin aktif pelanggan tersebut.
- **Frequency** — Seberapa *sering* pelanggan bertransaksi dalam periode tertentu. Mewakili loyalitas atau keterlibatan.
- **Monetary** — Seberapa *banyak* uang yang dibelanjakan oleh pelanggan. Mencerminkan nilai finansial pelanggan terhadap bisnis.

Dengan membagi nilai RFM ke dalam kuartil dan skor, kita dapat mengidentifikasi segmen seperti:

- **Champions** 
- **Loyal Customers**
- **Potential Loyalist**
- **Average**
- **Recent Customer**
- **Cannot Lose Them**
- **About To Sleep**
- **Lost Customer**
- **Uncategorized**

### 🎯 Tujuan Proyek

- Mengelompokkan pelanggan berdasarkan RFM waktu terakhir pembelian (Recency), frekuensi transaksi (Frequency), dan nilai pembelian (Monetary).
- Mengidentifikasi pelanggan bernilai tinggi dan berisiko hilang untuk menyusun strategi yang lebih tepat.
- Memberikan insight untuk pengambilan keputusan pemasaran berbasis data.


Dengan dataset transaksi pelanggan di beberapa pusat perbelanjaan besar di Istanbul, analisis RFM ini memberikan gambaran menyeluruh tentang perilaku pelanggan dan peluang pertumbuhan bisnis.


## 👥 Stakeholders

- **Marketing Team** – Menargetkan promosi berdasarkan segmen.
- **Manajemen Mall** – Menyusun strategi retensi dan loyalitas.
- **Retailers** – Memahami pelanggan aktif vs. pasif.

---

## 🧩 Tools & Tech Stack

| Tool            | Keterangan                            |
|------------------|----------------------------------------|
| Python           | Data processing & RFM calculation     |
| Pandas, NumPy    | Data wrangling                        |
| Streamlit        | UI dashboard interaktif               |
| Matplotlib, Seaborn | Visualisasi statistik              |
| PowerBI          | Insight dashboard visualisasi lanjutan |
| scikit-learn     | Clustering dan segmentasi tambahan    |
| Streamlit        | Clustering dan segmentasi tambahan    |

---

## 🧠 Methodology

### 1. Data Preprocessing  
- Membersihkan missing value  
- Analisis distribusi kolom (age, price, quantity)  
- Filtering outliers berdasarkan harga

### 2. RFM Analysis  
- Menghitung nilai **Recency**, **Frequency**, dan **Monetary**  
- Pembagian skor menggunakan kuartil (Q1, Q2, Q3)  
- Menentukan **RFM Score** dan segmentasi pelanggan

### 3. Visualization & Insights  
- Dashboard interaktif Streamlit  
- PowerBI Dashboard untuk eksplorasi lanjutan  
- Insight tertulis berdasarkan:  
  - Segmen pelanggan  
  - Gender  
  - Produk terlaris  
  - Mall paling menguntungkan  
  - Tren revenue per tahun/kuartal/bulan

---

## 📊 Dashboard Preview

🔗 **Streamlit Dashboard**:  
`[lokasi hosting jika ada]`

📈 **PowerBI Dashboard**:  
`[screenshot atau link PowerBI]`

---

## 💡 Key Insights

- **Segmen Loyal dan Potential Loyalist** mendominasi pelanggan (48K+), potensi konversi besar.  
- Produk **Clothing dan Cosmetics** paling laris – cocok untuk kampanye utama.  
- Mall besar seperti **Mall of Istanbul** dan **Kanyon** menyumbang >50% revenue.  
- Penurunan drastis di awal **2023** perlu peninjauan strategi.

---

## ✅ Business Impact

- Meningkatkan efisiensi promosi dan alokasi anggaran.
- Meningkatkan retensi pelanggan bernilai tinggi.
- Menurunkan potensi churn pelanggan pasif.
- Memberikan arah jelas bagi strategi pemasaran berbasis data.

---

## 📂 Folder Structure
