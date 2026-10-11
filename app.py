import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Petualangan PiMa", page_icon="🚀", layout="centered")

# --- KUSTOMISASI CSS (Responsive & Warna Permen Ceria) ---
st.markdown("""
    <style>
    /* Background utama aplikasi: Soft Peach/Pink sangat muda */
    .stApp { background-color: #FFF5F5; }
    
    /* Kartu Soal */
    .card {
        background-color: #FFFFFF;
        padding: 30px;
        border-radius: 25px;
        box-shadow: 0 10px 25px rgba(225, 29, 72, 0.1);
        border-top: 10px solid #F472B6; /* Aksen Soft Pink */
        margin-bottom: 20px;
    }
    
    /* Teks dan Judul Default (Layar Besar/Tablet) */
    .main-title { color: #E11D48; font-size: 3rem; font-weight: 900; text-align: center; margin-bottom: 5px; }
    .subtitle { color: #FB923C; font-size: 1.3rem; text-align: center; margin-bottom: 30px; font-weight: bold; }
    .score-badge { background-color: #FEF08A; color: #854D0E; padding: 12px 20px; border-radius: 15px; font-weight: 900; font-size: 1.3rem; text-align: center; border: 2px solid #FDE047; }
    .level-badge { background-color: #FED7AA; color: #9A3412; padding: 12px 20px; border-radius: 15px; font-weight: 900; font-size: 1.3rem; text-align: center; border: 2px solid #FDBA74; }
    .question-text { font-size: 1.5rem; color: #1F2937; font-weight: 700; margin-bottom: 20px; line-height: 1.4; }
    
    /* Kotak Penjelasan */
    .explanation-box { background-color: #FFEDD5; color: #C2410C; padding: 20px; border-radius: 15px; border-left: 6px solid #F97316; margin-top: 25px; font-size: 1.1rem; }

    /* MEDIA QUERY: Tampilan Khusus HP (iPhone/Android Layar Kecil) */
    @media (max-width: 768px) {
        .main-title { font-size: 2.2rem; }
        .subtitle { font-size: 1.1rem; margin-bottom: 20px; }
        .card { padding: 20px; border-radius: 20px; }
        .question-text { font-size: 1.2rem; }
        .score-badge, .level-badge { font-size: 1.1rem; padding: 10px; margin-bottom: 10px; }
    }
    </style>
""", unsafe_allow_html=True)

# --- BANK SOAL MISI 1 (10 Soal) ---
misi_1 = [
    {
        "soal": "1. Budi punya 1/2 loyang martabak. Siti membawa 1/4 loyang. Jika digabungkan, berapa jumlahnya?",
        "opsi": ["2/6", "3/4", "4/4"],
        "jawaban": "3/4",
        "pesan": "Hebat! 1/2 itu sama besarnya dengan 2/4. Jadi 2/4 + 1/4 = 3/4."
    },
    {
        "soal": "2. Ibu memotong kue ulang tahun menjadi 8 bagian sama besar. Adik memakan 3 bagian. Berapa sisa kue ibu?",
        "opsi": ["5/8", "3/8", "8/8"],
        "jawaban": "5/8",
        "pesan": "Tepat sekali! Kue utuh adalah 8/8. Jika dimakan 3/8, sisanya 8/8 - 3/8 = 5/8."
    },
    {
        "soal": "3. Manakah potongan pizza yang lebih besar untukmu?",
        "opsi": ["1/2 bagian", "1/4 bagian", "Sama besarnya"],
        "jawaban": "1/2 bagian",
        "pesan": "Betul! Ingat, semakin kecil angka di bawah (penyebut), semakin BESAR potongan pizzanya!"
    },
    {
        "soal": "4. Kakak minum 1/3 gelas susu. Adik minum 1/3 gelas susu. Berapa total susu yang diminum?",
        "opsi": ["2/6", "1/3", "2/3"],
        "jawaban": "2/3",
        "pesan": "Keren! Kalau angka di bawahnya (penyebut) sudah sama, kita cukup jumlahkan angka yang atas (pembilang). 1+1 = 2."
    },
    {
        "soal": "5. Pecahan mana yang nilainya SAMA dengan 1/2 (setengah)?",
        "opsi": ["2/4", "1/3", "3/5"],
        "jawaban": "2/4",
        "pesan": "Pintar! 2 potong dari 4 bagian (2/4) itu sama persis dengan setengah (1/2)."
    },
    {
        "soal": "6. Ayah mengecat dinding. Pagi hari selesai 3/5 bagian. Siang hari selesai 1/5 bagian. Berapa bagian yang sudah dicat?",
        "opsi": ["4/5", "4/10", "3/5"],
        "jawaban": "4/5",
        "pesan": "Luar biasa! 3/5 + 1/5 = 4/5."
    },
    {
        "soal": "7. Satu gelas penuh air (1 utuh). Diminum ayah 1/4 bagian. Sisa air di gelas adalah...",
        "opsi": ["2/4", "3/4", "4/4"],
        "jawaban": "3/4",
        "pesan": "Benar! 1 utuh itu sama dengan 4/4. Jadi 4/4 dikurangi 1/4 sisanya 3/4."
    },
    {
        "soal": "8. 2/4 + 2/4 sama dengan...",
        "opsi": ["4/8", "1 utuh", "2/8"],
        "jawaban": "1 utuh",
        "pesan": "Super! 2/4 ditambah 2/4 jadi 4/4. Dan 4/4 itu sama dengan 1 (utuh)."
    },
    {
        "soal": "9. Ani punya tali sepanjang 4/6 meter. Dipotong 2/6 meter. Berapa sisa tali Ani?",
        "opsi": ["2/6", "6/6", "1/6"],
        "jawaban": "2/6",
        "pesan": "Mantap! 4/6 - 2/6 = 2/6."
    },
    {
        "soal": "10. Manakah yang nilainya paling kecil?",
        "opsi": ["1/2", "1/3", "1/8"],
        "jawaban": "1/8",
        "pesan": "Wah, logika matematikamu jalan! Bayangkan kue dibagi 8, potongannya pasti sangat kecil."
    }
]

# --- PENGATURAN STATE (Memori Aplikasi) ---
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'q_index' not in st.session_state:
    st.session_state.q_index = 0
if 'status_jawaban' not in st.session_state:
    st.session_state.status_jawaban = None 

# --- HEADER APLIKASI ---
st.markdown('<div class="main-title">Petualangan PiMa 🚀</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Belajar Matematika Jadi Semudah Bermain Game!</div>', unsafe_allow_html=True)

# Papan Skor (Otomatis ditumpuk ke bawah jika di HP, menyamping di Tablet/PC)
c1, c2 = st.columns(2)
with c1:
    st.markdown(f'<div class="score-badge">⭐ Poin: {st.session_state.score}</div>', unsafe_allow_html=True)
with c2:
    q_tampil = min(st.session_state.q_index + 1, len(misi_1))
    st.markdown(f'<div class="level-badge">🎯 Soal: {q_tampil} / {len(misi_1)}</div>', unsafe_allow_html=True)

st.write("---")

# --- LOGIKA GAME ---
if st.session_state.q_index < len(misi_1):
    soal_sekarang = misi_1[st.session_state.q_index]
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f'<div class="question-text">{soal_sekarang["soal"]}</div>', unsafe_allow_html=True)
    
    # Area tombol pilihan ganda
    col1, col2, col3 = st.columns(3)
    
    def cek_jawaban(jawaban_user):
        if jawaban_user == soal_sekarang["jawaban"]:
            st.session_state.status_jawaban = 'benar'
            st.session_state.score += 10
        else:
            st.session_state.status_jawaban = 'salah'

    with col1:
        if st.button(soal_sekarang["opsi"][0], use_container_width=True, key=f"btn1_{st.session_state.q_index}"):
            cek_jawaban(soal_sekarang["opsi"][0])
    with col2:
        if st.button(soal_sekarang["opsi"][1], use_container_width=True, key=f"btn2_{st.session_state.q_index}"):
            cek_jawaban(soal_sekarang["opsi"][1])
    with col3:
        if st.button(soal_sekarang["opsi"][2], use_container_width=True, key=f"btn3_{st.session_state.q_index}"):
            cek_jawaban(soal_sekarang["opsi"][2])

    st.markdown('</div>', unsafe_allow_html=True)

    # --- PENGATURAN EFEK SUARA DAN VISUAL ---
    if st.session_state.status_jawaban == 'benar':
        # Efek Suara Benar (Suara Koin/Chime ceria)
        st.markdown("""
            <audio autoplay style="display:none;">
                <source src="https://assets.mixkit.co/active_storage/sfx/2013/2013-preview.mp3" type="audio/mpeg">
            </audio>
        """, unsafe_allow_html=True)
        
        st.balloons()
        st.success("Tepat Sekali! 🎉")
        st.markdown(f'<div class="explanation-box">💡 <b>Penjelasan:</b><br>{soal_sekarang["pesan"]}</div>', unsafe_allow_html=True)
        
        if st.button("Lanjut Soal Berikutnya ➡️", type="primary", use_container_width=True):
            st.session_state.q_index += 1
            st.session_state.status_jawaban = None
            st.rerun()
            
    elif st.session_state.status_jawaban == 'salah':
        # Efek Suara Salah (Suara Boing/Kartun lucu, tidak bikin sedih)
        st.markdown("""
            <audio autoplay style="display:none;">
                <source src="https://assets.mixkit.co/active_storage/sfx/2658/2658-preview.mp3" type="audio/mpeg">
            </audio>
        """, unsafe_allow_html=True)
        
        st.warning("Hihi, hampir benar! Yuk coba hitung pelan-pelan lagi! 🕵️‍♂️")
        if st.button("Coba Lagi 🔄", use_container_width=True):
            st.session_state.status_jawaban = None
            st.rerun()

else:
    # --- JIKA SEMUA SOAL SELESAI ---
    # Efek Suara Menang/Selesai
    st.markdown("""
        <audio autoplay style="display:none;">
            <source src="https://assets.mixkit.co/active_storage/sfx/2018/2018-preview.mp3" type="audio/mpeg">
        </audio>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="card" style="text-align:center;">', unsafe_allow_html=True)
    st.markdown('<div class="question-text" style="font-size: 2.5rem; color: #E11D48;">🏆 MISI SELESAI! 🏆</div>', unsafe_allow_html=True)
    st.write(f"Kamu sangat cerdas! Total skormu adalah **{st.session_state.score}**.")
    st.image("https://cdn-icons-png.flaticon.com/512/3113/3113054.png", width=150)
    
    if st.button("Ulangi Petualangan dari Awal 🔄", use_container_width=True):
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.session_state.status_jawaban = None
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
