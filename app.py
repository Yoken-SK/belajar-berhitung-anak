import streamlit as st
import random

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Petualangan PiMa", page_icon="🚀", layout="centered")

# --- KUSTOMISASI CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #F0FDF4; }
    .card { background-color: #FFFFFF; padding: 25px; border-radius: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-top: 8px solid #818CF8; margin-bottom: 20px; }
    .main-title { color: #4F46E5; font-size: 2.5rem; font-weight: 900; text-align: center; margin-bottom: 5px; }
    .score-badge { background-color: #DBEAFE; color: #1E40AF; padding: 10px; border-radius: 12px; font-weight: bold; font-size: 1.2rem; text-align: center; }
    .level-badge { background-color: #FEF3C7; color: #92400E; padding: 10px; border-radius: 12px; font-weight: bold; font-size: 1.2rem; text-align: center; }
    .question-text { font-size: 1.4rem; color: #1E293B; font-weight: 700; margin-bottom: 15px; text-align: center; }
    .emoji-box { font-size: 4rem; text-align: center; padding: 20px; border-radius: 15px; margin-bottom: 20px; background-color: #FFE4E6; }
    .hint-box { background-color: #FFFBEB; color: #B45309; padding: 15px; border-radius: 12px; border-left: 5px solid #F59E0B; margin-top: 20px; font-size: 1.1rem; }
    
    @media (max-width: 768px) {
        .emoji-box { font-size: 2.5rem; }
        .question-text { font-size: 1.2rem; }
    }
    </style>
""", unsafe_allow_html=True)

# --- FUNGSI PEMBUAT SOAL DINAMIS ---
def generate_soal():
    # Menghasilkan angka acak 1 sampai 5
    st.session_state.angka1 = random.randint(1, 5)
    st.session_state.angka2 = random.randint(1, 5)
    st.session_state.jawaban_benar = st.session_state.angka1 + st.session_state.angka2
    
    # Membuat pilihan ganda yang mengecoh tapi logis
    opsi = [
        st.session_state.jawaban_benar, 
        st.session_state.jawaban_benar + random.randint(1, 2), 
        abs(st.session_state.jawaban_benar - random.randint(1, 2))
    ]
    # Memastikan tidak ada opsi yang sama
    opsi = list(set(opsi))
    while len(opsi) < 3:
        opsi.append(opsi[-1] + 1)
        opsi = list(set(opsi))
        
    random.shuffle(opsi)
    st.session_state.opsi_jawaban = opsi
    st.session_state.salah_menebak = 0 # Reset hitungan salah
    st.session_state.status_jawaban = None

# --- INISIALISASI STATE (Memori) ---
if 'score' not in st.session_state: st.session_state.score = 0
if 'level_soal' not in st.session_state: st.session_state.level_soal = 1
if 'angka1' not in st.session_state: generate_soal()

# --- HEADER APLIKASI ---
st.markdown('<div class="main-title">🚀 Petualangan PiMa</div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1: st.markdown(f'<div class="score-badge">⭐ Poin: {st.session_state.score}</div>', unsafe_allow_html=True)
with c2: st.markdown(f'<div class="level-badge">🎯 Soal ke: {st.session_state.level_soal}</div>', unsafe_allow_html=True)
st.write("---")

# --- AREA KARTU SOAL ---
st.markdown('<div class="card">', unsafe_allow_html=True)

# Menampilkan Emoji Sesuai Jumlah Angka
apel_kiri = "🍎" * st.session_state.angka1
apel_kanan = "🍏" * st.session_state.angka2

st.markdown(f'<div class="emoji-box">{apel_kiri} ➕ {apel_kanan}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="question-text">Berapa hasil dari {st.session_state.angka1} + {st.session_state.angka2}?</div>', unsafe_allow_html=True)

# --- LOGIKA PENGECEKAN JAWABAN ---
def cek_jawaban(jawaban_user):
    if jawaban_user == st.session_state.jawaban_benar:
        st.session_state.status_jawaban = 'benar'
        if st.session_state.salah_menebak == 0:
            st.session_state.score += 10 # Poin penuh jika langsung benar
        else:
            st.session_state.score += 5  # Poin setengah jika pakai bantuan
    else:
        st.session_state.status_jawaban = 'salah'
        st.session_state.salah_menebak += 1

# Tombol Opsi Jawaban
col1, col2, col3 = st.columns(3)
with col1:
    if st.button(f"{st.session_state.opsi_jawaban[0]}", use_container_width=True): cek_jawaban(st.session_state.opsi_jawaban[0])
with col2:
    if st.button(f"{st.session_state.opsi_jawaban[1]}", use_container_width=True): cek_jawaban(st.session_state.opsi_jawaban[1])
with col3:
    if st.button(f"{st.session_state.opsi_jawaban[2]}", use_container_width=True): cek_jawaban(st.session_state.opsi_jawaban[2])

st.markdown('</div>', unsafe_allow_html=True)

# --- SISTEM FEEDBACK (SCAFFOLDING) & AUDIO ---
if st.session_state.status_jawaban == 'benar':
    st.markdown('<audio autoplay style="display:none;"><source src="https://assets.mixkit.co/active_storage/sfx/2013/2013-preview.mp3" type="audio/mpeg"></audio>', unsafe_allow_html=True)
    st.balloons()
    st.success("🎉 Tepat Sekali! Kamu Hebat karena pantang menyerah!")
    
    if st.button("Lanjut Soal Berikutnya ➡️", type="primary", use_container_width=True):
        st.session_state.level_soal += 1
        generate_soal() # Memanggil soal baru
        st.rerun()

elif st.session_state.status_jawaban == 'salah':
    st.markdown('<audio autoplay style="display:none;"><source src="https://assets.mixkit.co/active_storage/sfx/2658/2658-preview.mp3" type="audio/mpeg"></audio>', unsafe_allow_html=True)
    
    # Scaffolding: Bantuan Bertingkat
    if st.session_state.salah_menebak == 1:
        st.warning("Hihi, hampir benar! Yuk hitung lagi semua apelnya satu per satu! 🕵️‍♂️")
    elif st.session_state.salah_menebak >= 2:
        st.markdown(f'<div class="hint-box">💡 <b>Petunjuk PiMa:</b><br>Simpan angka <b>{st.session_state.angka1}</b> di mulutmu, lalu siapkan <b>{st.session_state.angka2}</b> jari di tanganmu. Lanjutkan menghitungnya!</div>', unsafe_allow_html=True)
        
    if st.button("Coba Lagi 🔄", use_container_width=True):
        st.session_state.status_jawaban = None
        st.rerun()
