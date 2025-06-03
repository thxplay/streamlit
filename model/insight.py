import streamlit as st

def insight():
    st.header('📈 Dashboard Visualisasi PowerBI & Insightnya')
    with st.expander("### Dashboard Visualisasi with PowerBI"):
        st.markdown('<div style="text-align: justify;">Dashboard Visualisasi hanya memiliki 1 halaman dan memiliki 6 kategori untuk slicer dengan total 12 slicers. Warna pada dashboard menyesuaikan gradiasi logo Istanbul.</div>', unsafe_allow_html=True)
        st.image("images/istanbulcs1.png")
        row1, row2, row3 = st.columns([1, 1, 1])
        with row1:
            st.image("images/istanbulcs2.png")
        with row2:
            st.image("images/istanbulcs3.png")
        with row3:
            st.image("images/istanbulcs4.png")
        row1, row2, row3 = st.columns([1, 1, 1])
        with row1:
            st.image("images/istanbulcs5.png")
        with row2:
            st.image("images/istanbulcs6.png")
        with row3:
            st.image("images/istanbulcs7.png")
    # 1. User Count by Segment
    with st.expander("### 👥 User Count by Segment"):
        row1, row2, row3 = st.columns([1, 2, 2])
        with row1:
            st.image("images/11.png")
        with row2:
            st.markdown("""
            **Insight**  
            ---
            - Sebagian besar pelanggan ada di segmen **Loyal (26K)**, **Potential Loyalist (22K)**, dan **Cannot Lose Them (20K)** artinya potensi retensi dan konversi sangat besar.  
            - Segmen **Average (12K)** & **About to Sleep (7K)** berisiko churn bila tidak ditindaklanjuti.  
            - Jumlah **Recent Customer (6K)** dan **Champion (7K)** rendah, menunjukkan pentingnya nurturing pelanggan baru dan top spender.

            **Rekomendasi Aksi**  
            ---
            - **Loyal & Cannot Lose Them** : Pertahankan dengan loyalty program dan penawaran eksklusif.  
            - **Potential Loyalist** : Dorong jadi pelanggan setia dengan edukasi dan promo.  
            - **Average & About to Sleep** : Kirim re-engagement campaign dan diskon berkala.  
            - **Recent Customer** : Aktifkan dengan welcome offer dan promo pembelian pertama.  
            - **Champion** : Berikan apresiasi khusus agar makin loyal.
            """)
        with row3:
            st.image("images/12.png")

    # 2. User by Gender
    with st.expander("### 👤 User by Gender"):
        row1, row2, row3 = st.columns([2, 2, 1])
        with row1:
            st.image("images/21.png")
        with row2:
            st.markdown("""
            **Insight**  
            ---
            - Pengguna **perempuan** mendominasi **(60%)**, menunjukkan kemungkinan keterlibatan atau respons promosi lebih tinggi.  
            - Pengguna **pria (40%)** tetap merupakan segmen signifikan yang perlu diperhatikan, terutama dalam strategi pertumbuhan.

            **Rekomendasi Aksi**  
            ---
            - Fokuskan konten **promosi pada kebutuhan dan preferensi wanita,** seperti campaign produk lifestyle, kecantikan, atau fashion.  
            - Buat **kampanye khusus** yang lebih relevan **untuk pria**, misalnya promosi kategori gadget, hobi, atau sport-related.  
            - Gunakan **influencer marketing** yang relevan dengan masing-masing gender untuk meningkatkan daya tarik dan engagement.
            """)
        with row3:
            st.image("images/22.png")

    # 3. Best-Selling Categories
    with st.expander("### 🛒 Best-Selling Categories"):
        row1, row2, row3 = st.columns([1, 2, 2])
        with row1:
            st.image("images/31.png")
        with row2:
            st.markdown("""
            **Insight**  
            ---
            - Clothing menjadi kategori paling laris (104K), menunjukkan minat tinggi terhadap fashion.  
            - Kosmetik dan makanan menyusul, menunjukkan minat konsisten pada kebutuhan primer dan gaya hidup.  
            - Kategori teknologi, buku, dan souvenir tergolong rendah, tapi bisa dioptimalkan untuk target segmen khusus.

            **Rekomendasi Aksi**  
            ---
            - Fokus promosi, bundling, dan seasonal campaign pada kategori fashion dan beauty, yang relevan bagi pelanggan Loyal dan Champion.  
            - Kembangkan campaign reaktivasi dengan produk best-seller untuk segmen Potential Loyalist dan Cannot Lose Them.  
            - Lakukan kolaborasi brand/konten untuk meningkatkan daya tarik kategori bawah seperti books & tech — arahkan ke segmen niche atau loyalis.
            """)
        with row3:
            st.image("images/32.png")

    # 4. Shopping Malls by Revenue
    with st.expander("### 🏬 Shopping Malls by Revenue"):
        row1, row2, row3 = st.columns([2, 2, 1])
        with row1:
            st.image("images/41.png")
        with row2:
            st.markdown("""
            **Insight**  
            ---
            - Mall of Istanbul dan Kanyon menyumbang pendapatan terbesar (>50M), didominasi oleh segmen Loyal dan Cannot Lose Them.  
            - Segmen Champion juga berperan penting, tapi jumlahnya lebih kecil dari Cannot Lose Them.  
            - Mall-mall lain cenderung hanya didominasi oleh Loyal, menunjukkan potensi penetrasi masih bisa ditingkatkan untuk segmen lainnya.

            **Rekomendasi Aksi**  
            ---
            - Luncurkan kampanye retensi dan penawaran eksklusif bagi segmen Cannot Lose Them, khususnya di mall top-performer seperti Mall of Istanbul dan Kanyon.  
            - Optimalkan nilai Champion dengan pengalaman VIP, untuk mendorong pengeluaran dan referral.  
            - Di mall dengan pendapatan rendah, dorong segmentasi ulang dan inisiatif pemasaran lokal untuk aktifkan segmen Potential Loyalist & Recent Customer.
            """)
        with row3:
            st.image("images/42.png")

    # 5. Revenue Growth by Time
    with st.expander("### 📅 Revenue Growth by Year, Quarter and Month"):
        row1, row2, row3 = st.columns([1, 2, 2])
        with row1:
            st.image("images/51.png")
        with row2:
            st.markdown("""
            **Insight**  
            ---
            - **Revenue cukup stabil** di kisaran 9–10M **sepanjang 2021–2022** dengan sesekali lonjakan hingga 10.3M.  
            - Namun terjadi **penurunan drastis** pada awal **tahun 2023** (dari 9.5M ke 2.5M), menjadi titik terendah dalam 2 tahun terakhir.  
            - Hal ini dapat disebabkan oleh menurunnya aktivitas pelanggan aktif atau perubahan tren musiman/eksternal.

            **Rekomendasi Aksi**  
            ---
            - Lakukan analisis churn dan perilaku segmen Cannot Lose Them, About to Sleep, dan Recent Customer di awal 2023.  
            - Perkuat kampanye reaktivasi dan penawaran spesifik untuk mendorong transaksi di Q1.  
            - Review strategi promosi awal tahun & kanal akuisisi pelanggan untuk memastikan efektivitas.  
            - Kolaborasi dengan kategori terlaris (mis. clothing & cosmetics) untuk penawaran bundling guna menaikkan engagement di masa pemulihan.
            """)
        with row3:
            st.image("images/52.png")

    # Kesimpulan
    with st.expander("### 🧾 Kesimpulan Gabungan"):
        st.markdown("""
        **Insight**  
        ---
        - **Champion & Loyal** adalah segmen paling menguntungkan **:** penting untuk dipertahankan dengan pendekatan personal & program loyalitas.  
        - **Produk Clothing dan Cosmetics paling laris :** jadi prioritas dalam strategi promosi.  
        - **Mall besar seperti Mall of Istanbul dan Kanyon** memberi kontribusi tinggi **:** optimalkan sebagai lokasi promosi/event utama.  
        - **Terjadi penurunan revenue di awal 2023** **:** perlu perhatian terhadap segmen pelanggan pasif.

        **Rekomendasi Aksi**  
        ---
        - Kembangkan **program loyalitas eksklusif** untuk **Champion & Loyal.**  
        - Buat **promosi bundling** berbasis kategori **produk paling laku (Clothing dan Cosmetics).**  
        - Lakukan **aktivasi ulang pelanggan pasif (Cannot Lose Them, About to Sleep)** dengan **kampanye khusus**.  
        - **Fokuskan kampanye pemasaran** di mall dengan kontribusi revenue tertinggi.  
        - **Pantau tren revenue bulanan** untuk deteksi dini penurunan performa.
        """)