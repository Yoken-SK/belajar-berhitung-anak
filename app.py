import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Petualangan PiMa", page_icon="🚀", layout="centered")

# --- KUSTOMISASI CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #F0FDF4; }
    .card { background-color: #FFFFFF; padding: 25px; border-radius: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-top: 8px solid #818CF8; margin-bottom: 20px; }
    .main-title { color: #4F46E5; font-size: 2.8rem; font-weight: 900; text-align: center; margin-bottom: 5px; }
    .subtitle { color: #6366F1; font-size: 1.2rem; text-align: center; margin-bottom: 30px; font-weight: bold; }
    .score-badge { background-color: #DBEAFE; color: #1E40AF; padding: 10px 20px; border-radius: 12px; font-weight: bold; font-size: 1.2rem; text-align: center; }
    .level-badge { background-color: #FEF3C7; color: #92400E; padding: 10px 20px; border-radius: 12px; font-weight: bold; font-size: 1.2rem; text-align: center; }
    .question-text { font-size: 1.4rem; color: #1E293B; font-weight: 600; margin-bottom: 15px; line-height: 1.4; }
    .kelas-badge { display: inline-block; background-color: #4F46E5; color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.9rem; font-weight: bold; margin-bottom: 15px; }
    .explanation-box { background-color: #D1FAE5; color: #065F46; padding: 15px; border-radius: 12px; border-left: 5px solid #10B981; margin-top: 20px; font-size: 1.1rem; }
    
    /* Box Visual Emoji Besar */
    .emoji-box { font-size: 3.5rem; text-align: center; padding: 20px; border-radius: 15px; margin-bottom: 20px; }
    
    @media (max-width: 768px) {
        .main-title { font-size: 2.2rem; }
        .subtitle { font-size: 1.1rem; margin-bottom: 20px; }
        .card { padding: 20px; }
        .question-text { font-size: 1.2rem; }
        .emoji-box { font-size: 2.5rem; padding: 15px; }
    }
    </style>
""", unsafe_allow_html=True)

# --- BANK SOAL ---
misi_1 = [
    {
        "kelas": "Kelas 1 SD (Penjumlahan)",
        "soal": "1. Di atas meja ada 3 buah apel merah. Lalu ibu menaruh lagi 2 buah apel hijau. Berapa jumlah semua apel di meja sekarang?",
        "visual": "🍎🍎🍎 + 🍏🍏", "bg": "#FFE4E6",
        "opsi": ["4 Apel", "5 Apel", "6 Apel"], "jawaban": "5 Apel",
        "pesan": "Hebat! 3 apel ditambah 2 apel sama dengan 5 apel. (3 + 2 = 5)"
    },
    {
        "kelas": "Kelas 1 SD (Pengurangan)",
        "soal": "2. Di dahan pohon ada 5 ekor burung yang sedang hinggap. Tiba-tiba 2 ekor burung terbang. Sisa burung di pohon adalah...",
        "visual": "🐦🐦🐦🐦🐦 ➖ 🐦🐦", "bg": "#E0F2FE",
        "opsi": ["3 Ekor", "2 Ekor", "4 Ekor"], "jawaban": "3 Ekor",
        "pesan": "Tepat sekali! 5 dikurangi 2 sisanya adalah 3. (5 - 2 = 3)"
    },
    {
        "kelas": "Kelas 2 SD (Bangun Datar)",
        "soal": "3. Perhatikan benda-benda di sekitarmu. Benda manakah yang bentuk permukaannya seperti 'Lingkaran'?",
        "visual": "Bentuk ⭕", "bg": "#FEF3C7",
        "opsi": ["Buku Tulis", "Penggaris Segitiga", "Roda Sepeda"], "jawaban": "Roda Sepeda",
        "pesan": "Betul! Roda sepeda berbentuk lingkaran sempurna sehingga bisa bergelinding."
    },
    {
        "kelas": "Kelas 3 SD (Perkalian Dasar)",
        "soal": "4. Ada 3 buah keranjang di lantai. Setiap keranjang berisi 4 buah jeruk. Berapa total jeruk di semua keranjang?",
        "visual": "🧺(4) ➕ 🧺(4) ➕ 🧺(4)", "bg": "#FFEDD5",
        "opsi": ["7 Jeruk", "12 Jeruk", "10 Jeruk"], "jawaban": "12 Jeruk",
        "pesan": "Keren! Perkalian adalah penjumlahan berulang. 4 + 4 + 4 = 12. Atau 3 x 4 = 12."
    },
    {
        "kelas": "Kelas 3 SD (Pecahan Dasar)",
        "soal": "5. Ibu memotong satu loyang Pizza menjadi 4 bagian yang sama besar. Adik memakan 1 potong. Berapa nilai pecahan untuk Pizza yang dimakan adik?",
        "visual": "🍕 dibagi 4", "bg": "#FEF2F2",
        "opsi": ["1/4", "1/2", "3/4"], "jawaban": "1/4",
        "pesan": "Pintar! 1 potong dari total 4 potongan ditulis sebagai 1/4 (satu per empat)."
    },
    {
        "kelas": "Kelas 4 SD (Pecahan Senilai)",
        "soal": "6. Siti punya 1/2 potong cokelat batang. Pecahan manakah di bawah ini yang besarnya SAMA PERSIS dengan 1/2 cokelat Siti?",
        "visual": "🍫 1/2 = ...?", "bg": "#F3E8FF",
        "opsi": ["1/3", "2/4", "1/4"], "jawaban": "2/4",
        "pesan": "Luar biasa! Jika 1/2 dipotong lagi tengahnya, ia akan menjadi 2 potong dari 4 bagian (2/4)."
    },
    {
        "kelas": "Kelas 4 SD (Luas Bangun Datar)",
        "soal": "7. Sebuah buku tulis berbentuk persegi panjang. Panjangnya 5 cm dan lebarnya 4 cm. Berapakah luas buku tersebut?",
        "visual": "Buku 5cm x 4cm 📘", "bg": "#DCFCE7",
        "opsi": ["9 cm", "20 cm persegi", "10 cm persegi"], "jawaban": "20 cm persegi",
        "pesan": "Benar! Rumus luas persegi panjang adalah Panjang x Lebar. Jadi 5 x 4 = 20."
    },
    {
        "kelas": "Kelas 5 SD (Volume Bangun Ruang)",
        "soal": "8. Sebuah kotak kardus berbentuk kubus. Jika panjang salah satu sisinya adalah 3 meter, berapa volume kardus tersebut?",
        "visual": "📦 Kubus (Sisi=3m)", "bg": "#E0E7FF",
        "opsi": ["9 meter kubik", "12 meter kubik", "27 meter kubik"], "jawaban": "27 meter kubik",
        "pesan": "Super! Volume Kubus = sisi x sisi x sisi. Jadi 3 x 3 x 3 = 27."
    },
    {
        "kelas": "Kelas 5 SD (Kecepatan & Jarak)",
        "soal": "9. Mobil keluarga Budi berjalan dengan kecepatan 50 km/jam menuju Bali. Berapa jarak yang mereka tempuh setelah menyetir selama 2 jam?",
        "visual": "🚗 50 km/jam x 2 jam", "bg": "#F1F5F9",
        "opsi": ["52 km", "100 km", "25 km"], "jawaban": "100 km",
        "pesan": "Mantap! Jarak = Kecepatan x Waktu. Jadi 50 km x 2 jam = 100 km."
    },
    {
        "kelas": "Kelas 6 SD (Pengolahan Data)",
        "soal": "10. Andi mendapat nilai ulangan Matematika sebanyak tiga kali: 8, 7, dan 9. Berapakah nilai rata-rata ulangan Andi?",
        "visual": "📝 Nilai: 8, 7, 9", "bg": "#FAFAF9",
        "opsi": ["8", "24", "7"], "jawaban": "8",
        "pesan": "Wah, kamu siap lulus SD! Rata-rata dicari dengan menjumlahkan semua nilai (8+7+9=24), lalu dibagi jumlah ulangannya (24 dibagi 3 = 8)."
    }
]

# --- STATE ---
if 'score' not in st.session_state: st.session_state.score = 0
if 'q_index' not in st.session_state: st.session_state.q_index = 0
if 'status_jawaban' not in st.session_state: st.session_state.status_jawaban = None 

# --- HEADER ---
st.markdown('<div class="main-title">Petualangan PiMa 🚀</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Misi: Ujian Naik Level (Kelas 1 - 6)</div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1: st.markdown(f'<div class="score-badge">⭐ Poin: {st.session_state.score}</div>', unsafe_allow_html=True)
with c2: 
    q_tampil = min(st.session_state.q_index + 1, len(misi_1))
    st.markdown(f'<div class="level-badge">🎯 Tantangan: {q_tampil} / {len(misi_1)}</div>', unsafe_allow_html=True)
st.write("---")

# --- LOGIKA ---
if st.session_state.q_index < len(misi_1):
    soal_sekarang = misi_1[st.session_state.q_index]
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f'<span class="kelas-badge">{soal_sekarang["kelas"]}</span>', unsafe_allow_html=True)
    
    # VISUAL EMOJI SEBAGAI PENGGANTI GAMBAR
    st.markdown(f'<div class="emoji-box" style="background-color: {soal_sekarang["bg"]};">{soal_sekarang["visual"]}</div>', unsafe_allow_html=True)
    
    st.markdown(f'<div class="question-text">{soal_sekarang["soal"]}</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    def cek_jawaban(jawaban_user):
        if jawaban_user == soal_sekarang["jawaban"]:
            st.session_state.status_jawaban = 'benar'
            st.session_state.score += 10
        else:
            st.session_state.status_jawaban = 'salah'

    with col1:
        if st.button(soal_sekarang["opsi"][0], use_container_width=True, key=f"btn1_{st.session_state.q_index}"): cek_jawaban(soal_sekarang["opsi"][0])
    with col2:
        if st.button(soal_sekarang["opsi"][1], use_container_width=True, key=f"btn2_{st.session_state.q_index}"): cek_jawaban(soal_sekarang["opsi"][1])
    with col3:
        if st.button(soal_sekarang["opsi"][2], use_container_width=True, key=f"btn3_{st.session_state.q_index}"): cek_jawaban(soal_sekarang["opsi"][2])

    st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.status_jawaban == 'benar':
        st.markdown('<audio autoplay style="display:none;"><source src="https://assets.mixkit.co/active_storage/sfx/2013/2013-preview.mp3" type="audio/mpeg"></audio>', unsafe_allow_html=True)
        st.balloons()
        st.success("Tepat Sekali! 🎉")
        st.markdown(f'<div class="explanation-box">💡 <b>Penjelasan:</b><br>{soal_sekarang["pesan"]}</div>', unsafe_allow_html=True)
        if st.button("Lanjut ke Level Berikutnya ➡️", type="primary", use_container_width=True):
            st.session_state.q_index += 1
            st.session_state.status_jawaban = None
            st.rerun()
            
    elif st.session_state.status_jawaban == 'salah':
        st.markdown('<audio autoplay style="display:none;"><source src="https://assets.mixkit.co/active_storage/sfx/2658/2658-preview.mp3" type="audio/mpeg"></audio>', unsafe_allow_html=True)
        st.warning("Hihi, hampir benar! Yuk coba baca dan hitung pelan-pelan lagi! 🕵️‍♂️")
        if st.button("Coba Lagi 🔄", use_container_width=True):
            st.session_state.status_jawaban = None
            st.rerun()
else:
    st.markdown('<audio autoplay style="display:none;"><source src="https://assets.mixkit.co/active_storage/sfx/2018/2018-preview.mp3" type="audio/mpeg"></audio>', unsafe_allow_html=True)
    st.markdown('<div class="card" style="text-align:center;">', unsafe_allow_html=True)
    st.markdown('<div class="question-text" style="font-size: 2.5rem; color: #4F46E5;">🏆 LULUS SD! 🏆</div>', unsafe_allow_html=True)
    st.write(f"Kamu sangat cerdas! Total skormu adalah **{st.session_state.score}**.")
    st.markdown('<div class="emoji-box" style="background-color: #FEF08A;">🎓🥇🎉</div>', unsafe_allow_html=True)
    if st.button("Mainkan Lagi dari Kelas 1 🔄", use_container_width=True):
        st.session_state.q_index = 0; st.session_state.score = 0; st.session_state.status_jawaban = None; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
