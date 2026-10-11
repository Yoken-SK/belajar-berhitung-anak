import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Petualangan PiMa", page_icon="🚀", layout="centered")

# --- KUSTOMISASI CSS (Warna Pastel yang Adem di Mata) ---
st.markdown("""
    <style>
    /* Background utama aplikasi: Soft Mint / Hijau sangat muda */
    .stApp { background-color: #F0FDF4; }
    
    /* Kartu Soal */
    .card {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border-top: 8px solid #818CF8; /* Aksen Lavender/Ungu lembut */
        margin-bottom: 20px;
    }
    
    /* Teks dan Judul */
    .main-title { color: #4F46E5; font-size: 2.8rem; font-weight: 900; text-align: center; }
    .subtitle { color: #6366F1; font-size: 1.2rem; text-align: center; margin-bottom: 30px; }
    .score-badge { background-color: #DBEAFE; color: #1E40AF; padding: 10px 20px; border-radius: 12px; font-weight: bold; font-size: 1.2rem; text-align: center; }
    .level-badge { background-color: #FEF3C7; color: #92400E; padding: 10px 20px; border-radius: 12px; font-weight: bold; font-size: 1.2rem; text-align: center; }
    .question-text { font-size: 1.4rem; color: #1E293B; font-weight: 600; margin-bottom: 15px; }
    
    /* Kotak Penjelasan */
    .explanation-box { background-color: #D1FAE5; color: #065F46; padding: 15px; border-radius: 12px; border-left: 5px solid #10B981; margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)

# --- BANK SOAL MISI 1 (10 Soal Pecahan) ---
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
        "opsi": ["4/8", "4/4 (atau 1 utuh)", "2/8"],
        "jawaban": "4/4 (atau 1 utuh)",
        "pesan": "Super! 2/4 ditambah 2/4 jadi 4/4. 4 dibagi 4 = 1 (utuh)."
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
    st.session_state.status_jawaban = None # None, 'benar', atau 'salah'

# --- HEADER APLIKASI ---
st.markdown('<div class="main-title">Petualangan PiMa 🚀</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Belajar Matematika Jadi Semudah Bermain Game!</div>', unsafe_allow_html=True)

# Papan Skor
c1, c2 = st.columns(2)
with c1:
    st.markdown(f'<div class="score-badge">⭐ Total Poin: {st.session_state.score}</div>', unsafe_allow_html=True)
with c2:
    q_tampil = min(st.session_state.q_index + 1, len(misi_1))
    st.markdown(f'<div class="level-badge">🎯 Soal: {q_tampil} dari {len(misi_1)}</div>', unsafe_allow_html=True)

st.write("---")

# --- LOGIKA GAME ---
if st.session_state.q_index < len(misi_1):
    # Ambil data soal saat ini
    soal_sekarang = misi_1[st.session_state.q_index]
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f'<div class="question-text">{soal_sekarang["soal"]}</div>', unsafe_allow_html=True)
    
    # Area tombol pilihan ganda
    st.write("Pilih jawabanmu:")
    col1, col2, col3 = st.columns(3)
    
    # Fungsi untuk mengecek jawaban
    def cek_jawaban(jawaban_user):
        if jawaban_user == soal_sekarang["jawaban"]:
            st.session_state.status_jawaban = 'benar'
            st.session_state.score += 10
        else:
            st.session_state.status_jawaban = 'salah'

    # Tombol Opsi A
    with col1:
        if st.button(soal_sekarang["opsi"][0], use_container_width=True, key=f"btn1_{st.session_state.q_index}"):
            cek_jawaban(soal_sekarang["opsi"][0])
    # Tombol Opsi B
    with col2:
        if st.button(soal_sekarang["opsi"][1], use_container_width=True, key=f"btn2_{st.session_state.q_index}"):
            cek_jawaban(soal_sekarang["opsi"][1])
    # Tombol Opsi C
    with col3:
        if st.button(soal_sekarang["opsi"][2], use_container_width=True, key=f"btn3_{st.session_state.q_index}"):
            cek_jawaban(soal_sekarang["opsi"][2])

    st.markdown('</div>', unsafe_allow_html=True) # Tutup card

    # Menampilkan hasil setelah tombol ditekan
    if st.session_state.status_jawaban == 'benar':
        st.balloons()
        st.success("Tepat Sekali! 🎉")
        st.markdown(f'<div class="explanation-box">💡 <b>Penjelasan:</b><br>{soal_sekarang["pesan"]}</div>', unsafe_allow_html=True)
        
        if st.button("Lanjut Soal Berikutnya ➡️", type="primary"):
            st.session_state.q_index += 1
            st.session_state.status_jawaban = None
            st.rerun()
            
    elif st.session_state.status_jawaban == 'salah':
        st.error("Waduh, jawabanmu belum tepat. Yuk coba dihitung ulang pelan-pelan! 🕵️‍♂️")
        if st.button("Coba Lagi 🔄"):
            st.session_state.status_jawaban = None
            st.rerun()

else:
    # --- JIKA SEMUA SOAL SELESAI ---
    st.markdown('<div class="card" style="text-align:center;">', unsafe_allow_html=True)
    st.markdown('<div class="question-text" style="font-size: 2rem;">🏆 MISI SELESAI! 🏆</div>', unsafe_allow_html=True)
    st.write(f"Kamu luar biasa! Total skormu adalah **{st.session_state.score}**.")
    st.image("https://cdn-icons-png.flaticon.com/512/3113/3113054.png", width=150) # Ikon piala
    
    if st.button("Ulangi Petualangan dari Awal 🔄", use_container_width=True):
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.session_state.status_jawaban = None
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
