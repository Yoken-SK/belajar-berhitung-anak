import streamlit as st
import time

# Konfigurasi Halaman
st.set_page_config(
    page_title="Petualangan PiMa",
    page_icon="🧮",
    layout="centered"
)

# Kustomisasi CSS untuk mempercantik tampilan
st.markdown("""
    <style>
    .main-title {
        color: #4f46e5;
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
    }
    .score-board {
        background-color: #f3f4f6;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        border: 2px solid #e5e7eb;
    }
    .story-box {
        background-color: #eff6ff;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #3b82f6;
        font-size: 1.2rem;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Inisialisasi Session State (Menyimpan Skor dan Status Misi)
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'level' not in st.session_state:
    st.session_state.level = 1
if 'mission_status' not in st.session_state:
    st.session_state.mission_status = 'playing' # 'playing' atau 'success'

# --- Header & Score Board ---
st.markdown('<div class="main-title">Petualangan PiMa 🚀</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown(f'<div class="score-board"><h4>⭐ Poin: {st.session_state.score}</h4></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="score-board"><h4>🎯 Misi ke: {st.session_state.level}</h4></div>', unsafe_allow_html=True)

st.divider()

# --- Misi 1: Pecahan (1/2 + 1/4) ---
if st.session_state.level == 1:
    st.subheader("Misi 1: Menggabungkan Martabak 🥞")
    
    # Area Cerita
    st.markdown("""
        <div class="story-box">
        Budi punya <strong>1/2 (setengah)</strong> loyang martabak cokelat.<br>
        Siti membawa <strong>1/4 (seperempat)</strong> martabak keju.<br>
        Berapa jumlah martabak mereka jika digabungkan?
        </div>
    """, unsafe_allow_html=True)

    # Visualisasi Sederhana menggunakan kolom
    st.write("Bayangkan loyang martabak dibagi menjadi 4 bagian yang sama besar:")
    
    c1, c2, c3 = st.columns([1, 0.5, 1])
    with c1:
        st.write("**Loyang Budi (1/2)**")
        # Visualisasi 1/2 sebagai 2 dari 4 bagian (menggunakan warna)
        st.markdown("""
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 5px; width: 100px; height: 100px; border: 2px solid gray; border-radius: 50%; overflow: hidden;">
                <div style="background-color: #8B4513;"></div> <!-- Cokelat -->
                <div style="background-color: #8B4513;"></div> <!-- Cokelat -->
                <div style="background-color: transparent;"></div>
                <div style="background-color: transparent;"></div>
            </div>
        """, unsafe_allow_html=True)
        st.caption("2 dari 4 bagian terisi")

    with c2:
        st.write("")
        st.write("")
        st.write("")
        st.markdown("<h2 style='text-align:center;'>+</h2>", unsafe_allow_html=True)

    with c3:
        st.write("**Martabak Siti (1/4)**")
        # Visualisasi 1/4 sebagai 1 dari 4 bagian
        st.markdown("""
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 5px; width: 100px; height: 100px; border: 2px dashed gray; border-radius: 50%; overflow: hidden;">
                <div style="background-color: transparent;"></div>
                <div style="background-color: transparent;"></div>
                <div style="background-color: transparent;"></div>
                <div style="background-color: #FBBF24;"></div> <!-- Keju -->
            </div>
        """, unsafe_allow_html=True)
        st.caption("1 dari 4 bagian terisi")

    st.write("---")
    
    # Area Interaksi Jawaban
    if st.session_state.mission_status == 'playing':
        st.write("Jika martabak Siti digabungkan ke loyang Budi, berapa total bagian yang terisi?")
        
        # Pilihan Jawaban
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        
        with col_btn1:
            if st.button("2/6 Bagian", use_container_width=True):
                st.error("Waduh, loyangnya kan cuma dibagi 4. Coba hitung lagi kotaknya!")
        
        with col_btn2:
            if st.button("3/4 Bagian", use_container_width=True):
                st.success("🎉 Hebat! Jawabanmu Benar!")
                st.session_state.score += 10
                st.session_state.mission_status = 'success'
                st.rerun() # Refresh halaman untuk menampilkan tombol Lanjut
        
        with col_btn3:
            if st.button("4/4 Bagian", use_container_width=True):
                st.warning("Hampir! Tapi belum penuh satu loyang tuh.")

    # Jika Berhasil
    elif st.session_state.mission_status == 'success':
        st.balloons()
        st.success("Luar biasa! 1/2 (atau 2/4) ditambah 1/4 menjadi 3/4. Kamu mendapatkan 10 Poin!")
        
        if st.button("Lanjut ke Misi Berikutnya ➡️"):
            st.session_state.level += 1
            st.session_state.mission_status = 'playing'
            st.rerun()

# --- Misi 2: Perkalian (Level Selanjutnya) ---
elif st.session_state.level == 2:
    st.subheader("Misi 2: Harta Karun Bajak Laut 🏴‍☠️")
    st.write("Misi perkalian sedang dalam pengembangan...")
    
    if st.button("Kembali ke Misi 1"):
        st.session_state.level = 1
        st.rerun()
