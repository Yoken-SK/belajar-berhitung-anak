import streamlit as st
import random

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Petualangan PiMa", page_icon="🚀", layout="wide") # Menggunakan wide layout untuk menampung sidebar

# --- KUSTOMISASI CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #F0FDF4; }
    .card { background-color: #FFFFFF; padding: 25px; border-radius: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-top: 8px solid #818CF8; margin-bottom: 20px; }
    .main-title { color: #4F46E5; font-size: 2.5rem; font-weight: 900; text-align: center; margin-bottom: 5px; }
    .score-badge { background-color: #DBEAFE; color: #1E40AF; padding: 10px; border-radius: 12px; font-weight: bold; font-size: 1.2rem; text-align: center; }
    .level-badge { background-color: #FEF3C7; color: #92400E; padding: 10px; border-radius: 12px; font-weight: bold; font-size: 1.2rem; text-align: center; }
    .question-text { font-size: 1.4rem; color: #1E293B; font-weight: 700; margin-bottom: 15px; text-align: center; }
    .emoji-box { font-size: 3.5rem; text-align: center; padding: 20px; border-radius: 15px; margin-bottom: 20px; background-color: #F8FAFC; border: 2px dashed #CBD5E1; }
    .hint-box { background-color: #FFFBEB; color: #B45309; padding: 15px; border-radius: 12px; border-left: 5px solid #F59E0B; margin-top: 20px; font-size: 1.1rem; }
    
    /* Tombol Navigasi Sidebar */
    .css-1d391kg p { font-size: 1.1rem; }
    </style>
""", unsafe_allow_html=True)

# --- INISIALISASI STATE (Memori Data) ---
if 'score' not in st.session_state: st.session_state.score = 0
if 'level_soal' not in st.session_state: st.session_state.level_soal = 1
# Memori Analitik untuk Orang Tua
if 'total_benar' not in st.session_state: st.session_state.total_benar = 0
if 'total_salah' not in st.session_state: st.session_state.total_salah = 0

# --- FUNGSI PEMBUAT SOAL DINAMIS (TAMBAH & KURANG) ---
def generate_soal():
    # Menentukan jenis operasi secara acak
    st.session_state.operasi = random.choice(['tambah', 'kurang'])
    
    if st.session_state.operasi == 'tambah':
        st.session_state.angka1 = random.randint(1, 5)
        st.session_state.angka2 = random.randint(1, 5)
        st.session_state.jawaban_benar = st.session_state.angka1 + st.session_state.angka2
    else:
        # Untuk pengurangan, pastikan angka1 lebih besar dari angka2
        st.session_state.angka1 = random.randint(3, 9)
        st.session_state.angka2 = random.randint(1, st.session_state.angka1 - 1)
        st.session_state.jawaban_benar = st.session_state.angka1 - st.session_state.angka2
        
    # Pilihan Ganda Logis
    opsi = [
        st.session_state.jawaban_benar, 
        abs(st.session_state.jawaban_benar + random.randint(1, 2)), 
        abs(st.session_state.jawaban_benar - random.randint(1, 2))
    ]
    # Pastikan opsi unik
    opsi = list(set(opsi))
    while len(opsi) < 3:
        opsi.append(opsi[-1] + 1)
        opsi = list(set(opsi))
        
    random.shuffle(opsi)
    st.session_state.opsi_jawaban = opsi
    st.session_state.salah_menebak = 0
    st.session_state.status_jawaban = None

# Panggil fungsi pertama kali
if 'angka1' not in st.session_state: generate_soal()

# ==========================================
# BAGIAN 1: DASHBOARD ORANG TUA (SIDEBAR)
# ==========================================
with st.sidebar:
    st.markdown("## 🔐 Ruang Orang Tua")
    st.write("Masukkan PIN untuk melihat laporan belajar anak.")
    
    pin_input = st.text_input("PIN (Ketik: 1234)", type="password")
    
    if pin_input == "1234":
        st.success("Akses Dibuka!")
        st.markdown("### 📊 Laporan Perkembangan")
        
        # Kalkulasi Akurasi
        total_jawab = st.session_state.total_benar + st.session_state.total_salah
        akurasi = (st.session_state.total_benar / total_jawab * 100) if total_jawab > 0 else 0
        
        # Menampilkan Metrik dengan gaya Dashboard profesional
        c_met1, c_met2 = st.columns(2)
        c_met1.metric(label="✅ Jawaban Benar", value=st.session_state.total_benar)
        c_met2.metric(label="❌ Kesalahan", value=st.session_state.total_salah)
        
        st.metric(label="🎯 Tingkat Akurasi", value=f"{akurasi:.0f}%")
        
        st.markdown("### 💡 Analisis AI:")
        if total_jawab == 0:
            st.info("Anak belum mulai bermain. Pantau terus ya!")
        elif akurasi >= 80:
            st.success("Luar biasa! Anak sangat menguasai konsep dasar. Berikan pujian atas usahanya!")
        elif akurasi >= 50:
            st.warning("Pemahaman sudah baik, namun butuh sedikit ketelitian. Temani saat ia bermain.")
        else:
            st.error("Sepertinya anak kesulitan membayangkan konsepnya. Gunakan benda nyata (seperti sendok/kelereng) di rumah untuk membantunya.")
            
        if st.button("Reset Laporan Data"):
            st.session_state.total_benar = 0
            st.session_state.total_salah = 0
            st.session_state.score = 0
            st.session_state.level_soal = 1
            st.rerun()

# ==========================================
# BAGIAN 2: ANTARMUKA ANAK (MAIN AREA)
# ==========================================
st.markdown('<div class="main-title">🚀 Petualangan PiMa</div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1: st.markdown(f'<div class="score-badge">⭐ Poin: {st.session_state.score}</div>', unsafe_allow_html=True)
with c2: st.markdown(f'<div class="level-badge">🎯 Misi ke: {st.session_state.level_soal}</div>', unsafe_allow_html=True)
st.write("---")

st.markdown('<div class="card">', unsafe_allow_html=True)

# Render Visual Sesuai Jenis Operasi
if st.session_state.operasi == 'tambah':
    teks_soal = f"Berapa hasil dari {st.session_state.angka1} apel ditambah {st.session_state.angka2} apel?"
    visual = ("🍎" * st.session_state.angka1) + " ➕ " + ("🍏" * st.session_state.angka2)
else:
    teks_soal = f"Ada {st.session_state.angka1} burung, lalu {st.session_state.angka2} ekor terbang. Berapa sisanya?"
    visual = ("🐦" * st.session_state.angka1) + " ➖ " + ("💨🐦" * st.session_state.angka2)

st.markdown(f'<div class="emoji-box">{visual}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="question-text">{teks_soal}</div>', unsafe_allow_html=True)

# Logika Tombol Jawaban
def cek_jawaban(jawaban_user):
    if jawaban_user == st.session_state.jawaban_benar:
        st.session_state.status_jawaban = 'benar'
