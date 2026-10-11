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
    .question-text { font-size: 1.3rem; color: #1E293B; font-weight: 600; margin-bottom: 15px; line-height: 1.4; }
    .kelas-badge { display: inline-block; background-color: #4F46E5; color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.9rem; font-weight: bold; margin-bottom: 15px; }
    .explanation-box { background-color: #D1FAE5; color: #065F46; padding: 15px; border-radius: 12px; border-left: 5px solid #10B981; margin-top: 20px; font-size: 1.1rem; }
    
    /* Box Visual Emoji Besar */
    .emoji-box { font-size: 3.5rem; text-align: center; padding: 20px; border-radius: 15px; margin-bottom: 20px; line-height: 1.3; }
    
    @media (max-width: 768px) {
        .main-title { font-size: 2.2rem; }
        .subtitle { font-size: 1.1rem; margin-bottom: 20px; }
        .card { padding: 20px; }
        .question-text { font-size: 1.15rem; }
        .emoji-box { font-size: 2.2rem; padding: 15px; }
    }
    </style>
""", unsafe_allow_html=True)

# --- BANK SOAL (Total 25 Soal: Tambah, Kurang, Kali, Bagi, Pecahan) ---
misi_1 = [
    # --- TAHAP 1: PENJUMLAHAN (5 Soal) ---
    {
        "kelas": "Level 1: Penjumlahan", "bg": "#FFE4E6",
        "soal": "1. Di meja ada 3 apel merah, lalu ibu menaruh 2 apel hijau. Berapa total apel sekarang?",
        "visual": "🍎🍎🍎 ➕ 🍏🍏",
        "opsi": ["4 Apel", "5 Apel", "6 Apel"], "jawaban": "5 Apel",
        "pesan": "Hebat! 3 + 2 = 5."
    },
    {
        "kelas": "Level 1: Penjumlahan", "bg": "#FEF3C7",
        "soal": "2. Budi punya 4 mobil mainan. Ayah membelikan 3 mobil lagi. Berapa jumlah mobil Budi?",
        "visual": "🚗🚗🚗🚗 <br> ➕ 🚙🚙🚙",
        "opsi": ["6 Mobil", "7 Mobil", "8 Mobil"], "jawaban": "7 Mobil",
        "pesan": "Betul! 4 + 3 = 7."
    },
    {
        "kelas": "Level 1: Penjumlahan", "bg": "#E0E7FF",
        "soal": "3. Ani melihat 5 kupu-kupu di taman. Lalu datang lagi 4 kupu-kupu. Berapa kupu-kupu sekarang?",
        "visual": "🦋🦋🦋🦋🦋 ➕ 🦋🦋🦋🦋",
        "opsi": ["9 Kupu-kupu", "8 Kupu-kupu", "10 Kupu-kupu"], "jawaban": "9 Kupu-kupu",
        "pesan": "Pintar! 5 + 4 = 9."
    },
    {
        "kelas": "Level 1: Penjumlahan", "bg": "#DCFCE7",
        "soal": "4. Kakak memanggang 6 kue cokelat dan 4 kue stroberi. Berapa total kue kakak?",
        "visual": "🍪🍪🍪🍪🍪🍪 <br> ➕ 🧁🧁🧁🧁",
        "opsi": ["10 Kue", "9 Kue", "11 Kue"], "jawaban": "10 Kue",
        "pesan": "Luar biasa! 6 + 4 = 10."
    },
    {
        "kelas": "Level 1: Penjumlahan", "bg": "#FAE8FF",
        "soal": "5. Di kolam ada 7 ikan emas. Dimasukkan lagi 5 ikan koi. Berapa jumlah ikannya?",
        "visual": "🐟🐟🐟🐟🐟🐟🐟 ➕ 🐠🐠🐠🐠🐠",
        "opsi": ["11 Ikan", "12 Ikan", "13 Ikan"], "jawaban": "12 Ikan",
        "pesan": "Mantap! 7 + 5 = 12."
    },

    # --- TAHAP 2: PENGURANGAN (5 Soal) ---
    {
        "kelas": "Level 2: Pengurangan", "bg": "#E0F2FE",
        "soal": "6. Di dahan pohon ada 5 ekor burung. Tiba-tiba 2 ekor terbang tertiup angin. Sisa burung di dahan adalah...",
        "visual": "🌳 🐦🐦🐦🐦🐦 <br> ➖ 💨🐦🐦",
        "opsi": ["2 Ekor", "3 Ekor", "4 Ekor"], "jawaban": "3 Ekor",
        "pesan": "Tepat sekali! Dari 5 burung, 2 terbang, sisanya 3. (5 - 2 = 3)"
    },
    {
        "kelas": "Level 2: Pengurangan", "bg": "#FFEDD5",
        "soal": "7. Paman punya 8 potong semangka. Dimakan oleh adik 3 potong. Berapa sisa semangka paman?",
        "visual": "🍉🍉🍉🍉🍉🍉🍉🍉 <br> ➖ 😋🍉🍉🍉",
        "opsi": ["4 Potong", "5 Potong", "6 Potong"], "jawaban": "5 Potong",
        "pesan": "Benar! 8 - 3 = 5."
    },
    {
        "kelas": "Level 2: Pengurangan", "bg": "#F3E8FF",
        "soal": "8. Siti membeli 10 balon, tapi di jalan 4 balon meletus! Sisa balon Siti yang masih utuh adalah...",
        "visual": "🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈 <br> ➖ 💥💥💥💥",
        "opsi": ["6 Balon", "5 Balon", "7 Balon"], "jawaban": "6 Balon",
        "pesan": "Super! 10 - 4 = 6."
    },
    {
        "kelas": "Level 2: Pengurangan", "bg": "#FFE4E6",
        "soal": "9. Di kotak ada 7 pensil. Doni meminjam 2 pensil. Sisa pensil di kotak adalah...",
        "visual": "✏️✏️✏️✏️✏️✏️✏️ <br> ➖ 🤲✏️✏️",
        "opsi": ["4 Pensil", "5 Pensil", "6 Pensil"], "jawaban": "5 Pensil",
        "pesan": "Tepat! 7 - 2 = 5."
    },
    {
        "kelas": "Level 2: Pengurangan", "bg": "#FEF3C7",
        "soal": "10. Ibu merebus 6 butir telur. Sayangnya 1 butir pecah. Sisa telur yang utuh adalah...",
        "visual": "🥚🥚🥚🥚🥚🥚 <br> ➖ 🍳 (pecah 1)",
        "opsi": ["4 Telur", "5 Telur", "6 Telur"], "jawaban": "5 Telur",
        "pesan": "Pintar! 6 - 1 = 5."
    },

    # --- TAHAP 3: PERKALIAN (5 Soal) ---
    {
        "kelas": "Level 3: Perkalian", "bg": "#FFEDD5",
        "soal": "11. Ada 3 kelompok. Masing-masing kelompok punya 4 buah jeruk. Berapa total jeruk semuanya?",
        "visual": "🍊🍊🍊🍊 ➕ 🍊🍊🍊🍊 ➕ 🍊🍊🍊🍊",
        "opsi": ["10 Jeruk", "12 Jeruk", "7 Jeruk"], "jawaban": "12 Jeruk",
        "pesan": "Hebat! 4 jeruk diulang 3 kali sama dengan 3 x 4 = 12."
    },
    {
        "kelas": "Level 3: Perkalian", "bg": "#DCFCE7",
        "soal": "12. Terdapat 4 kotak donat. Setiap kotak berisi 2 donat. Berapa jumlah semua donat?",
        "visual": "📦🍩🍩 + 📦🍩🍩 <br> + 📦🍩🍩 + 📦🍩🍩",
        "opsi": ["6 Donat", "8 Donat", "10 Donat"], "jawaban": "8 Donat",
        "pesan": "Benar! 4 kotak dikali 2 donat = 8. (4 x 2 = 8)"
    },
    {
        "kelas": "Level 3: Perkalian", "bg": "#E0E7FF",
        "soal": "13. Pak guru membagikan permen kepada 5 anak. Masing-masing anak dapat 3 permen. Berapa total permen yang dibagikan?",
        "visual": "👦🍬🍬🍬 (x5 Anak)",
        "opsi": ["15 Permen", "12 Permen", "8 Permen"], "jawaban": "15 Permen",
        "pesan": "Keren! 5 anak x 3 permen = 15."
    },
    {
        "kelas": "Level 3: Perkalian", "bg": "#FCE7F3",
        "soal": "14. Di parkiran ada 6 sepeda motor. Setiap motor punya 2 roda. Berapa total jumlah roda motor di sana?",
        "visual": "🏍️ (2 Roda) <br> Ada 6 Motor",
        "opsi": ["10 Roda", "12 Roda", "8 Roda"], "jawaban": "12 Roda",
        "pesan": "Pintar! 6 motor dikali 2 roda = 12 roda. (6 x 2 = 12)"
    },
    {
        "kelas": "Level 3: Perkalian", "bg": "#FEF3C7",
        "soal": "15. Ibu menyusun gelas menjadi 2 baris. Setiap baris berisi 5 gelas. Berapa jumlah semua gelas?",
        "visual": "🥛🥛🥛🥛🥛 <br> 🥛🥛🥛🥛🥛",
        "opsi": ["10 Gelas", "7 Gelas", "12 Gelas"], "jawaban": "10 Gelas",
        "pesan": "Betul! 2 baris x 5 gelas = 10 gelas."
    },

    # --- TAHAP 4: PEMBAGIAN (5 Soal) ---
    {
        "kelas": "Level 4: Pembagian", "bg": "#E0F2FE",
        "soal": "16. Ada 10 permen manis. Ingin dibagikan sama rata kepada 2 anak. Tiap anak dapat berapa?",
        "visual": "🍬🍬🍬🍬🍬🍬🍬🍬🍬🍬 <br> ➗ 👦 👧",
        "opsi": ["4 Permen", "5 Permen", "6 Permen"], "jawaban": "5 Permen",
        "pesan": "Tepat sekali! 10 dibagi 2 sama dengan 5 permen untuk masing-masing anak."
    },
    {
        "kelas": "Level 4: Pembagian", "bg": "#FFEDD5",
        "soal": "17. Ibu punya 12 buah stroberi. Akan diletakkan ke dalam 3 piring sama banyak. Satu piring isinya berapa?",
        "visual": "🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓 <br> ➗ 🍽️ 🍽️ 🍽️",
        "opsi": ["3 Stroberi", "4 Stroberi", "5 Stroberi"], "jawaban": "4 Stroberi",
        "pesan": "Benar! 12 dibagi 3 adalah 4."
    },
    {
        "kelas": "Level 4: Pembagian", "bg": "#DCFCE7",
        "soal": "18. Pak Tani memanen 8 buah wortel. Ia mengikatnya menjadi 4 ikatan. Tiap ikat ada berapa wortel?",
        "visual": "🥕🥕🥕🥕🥕🥕🥕🥕 <br> ➗ 🎀🎀🎀🎀",
        "opsi": ["2 Wortel", "3 Wortel", "4 Wortel"], "jawaban": "2 Wortel",
        "pesan": "Hebat! 8 dibagi 4 = 2 wortel per ikat."
    },
    {
        "kelas": "Level 4: Pembagian", "bg": "#F3E8FF",
        "soal": "19. Ada 15 bola ditata ke dalam 5 keranjang. Tiap keranjang diisi sama banyak. Berapa isi tiap keranjangnya?",
        "visual": "⚽ (15 Bola) ➗ 🧺🧺🧺🧺🧺",
        "opsi": ["5 Bola", "4 Bola", "3 Bola"], "jawaban": "3 Bola",
        "pesan": "Mantap! 15 dibagi 5 sama dengan 3."
    },
    {
        "kelas": "Level 4: Pembagian", "bg": "#FFE4E6",
        "soal": "20. Rina punya 6 potong pizza. Ia membaginya sama rata dengan adiknya (berdua). Berapa potong yang didapat Rina?",
        "visual": "🍕🍕🍕🍕🍕🍕 <br> ➗ 👩 👦",
        "opsi": ["2 Potong", "3 Potong", "4 Potong"], "jawaban": "3 Potong",
        "pesan": "Pintar! 6 dibagi 2 orang = 3 potong."
    },

    # --- TAHAP 5: PECAHAN (5 Soal) ---
    {
        "kelas": "Level 5: Pecahan", "bg": "#FEF2F2",
        "soal": "21. Ibu memotong kue menjadi 4 bagian. Adik makan 1 potong. Berapa nilai pecahan kue yang dimakan adik?",
        "visual": "🍰 dibagi 4",
        "opsi": ["1/4", "1/2", "3/4"], "jawaban": "1/4",
        "pesan": "Pintar! 1 potong dari total 4 potongan ditulis sebagai 1/4 (seperempat)."
    },
    {
        "kelas": "Level 5: Pecahan", "bg": "#F3E8FF",
        "soal": "22. Siti punya 1/2 potong cokelat. Pecahan mana yang besarnya SAMA PERSIS dengan 1/2?",
        "visual": "🍫 1/2 = ...?",
        "opsi": ["1/3", "2/4", "1/4"], "jawaban": "2/4",
        "pesan": "Luar biasa! Jika 1/2 dipotong lagi tengahnya, ia akan menjadi 2 potong dari 4 bagian (2/4)."
    },
    {
        "kelas": "Level 5: Pecahan", "bg": "#E0E7FF",
        "soal": "23. Budi minum 1/3 gelas jus, lalu minum lagi 1/3 gelas. Berapa total jus yang diminum?",
        "visual": "🧃 1/3 ➕ 🧃 1/3",
        "opsi": ["2/6", "1/3", "2/3"], "jawaban": "2/3",
        "pesan": "Keren! Jika angka di bawah (penyebut) sama, cukup jumlahkan angka yang atas: 1+1 = 2. Jadi 2/3."
    },
    {
        "kelas": "Level 5: Pecahan", "bg": "#DCFCE7",
        "soal": "24. Satu gelas penuh berisi susu (1 utuh). Diminum ayah 1/4 bagian. Sisa susu adalah...",
        "visual": "🥛 1 Utuh (4/4) ➖ 1/4",
        "opsi": ["2/4", "3/4", "4/4"], "jawaban": "3/4",
        "pesan": "Benar! 1 utuh itu sama dengan 4/4. Jadi 4/4 dikurangi 1/4 sisanya 3/4."
    },
    {
        "kelas": "Level 5: Pecahan", "bg": "#FFEDD5",
        "soal": "25. Manakah potongan pizza yang ukuran aslinya paling BESAR?",
        "visual": "🍕 1/2  vs  🍕 1/4  vs  🍕 1/8",
        "opsi": ["1/8", "1/4", "1/2"], "jawaban": "1/2",
        "pesan": "Betul sekali! Semakin sedikit kue itu dipotong (angka penyebutnya kecil), semakin BESAR potongan yang kita dapat!"
    }
]

# --- STATE ---
if 'score' not in st.session_state: st.session_state.score = 0
if 'q_index' not in st.session_state: st.session_state.q_index = 0
if 'status_jawaban' not in st.session_state: st.session_state.status_jawaban = None 

# --- HEADER ---
st.markdown('<div class="main-title">Petualangan PiMa 🚀</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Belajar Matematika Seru Kelas 1 - 6</div>', unsafe_allow_html=True)

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
    
    # VISUAL EMOJI CERIA
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
        if st.button("Lanjut ke Tantangan Berikutnya ➡️", type="primary", use_container_width=True):
            st.session_state.q_index += 1
            st.session_state.status_jawaban = None
            st.rerun()
            
    elif st.session_state.status_jawaban == 'salah':
        st.markdown('<audio autoplay style="display:none;"><source src="https://assets.mixkit.co/active_storage/sfx/2658/2658-preview.mp3" type="audio/mpeg"></audio>', unsafe_allow_html=True)
        st.warning("Hihi, hampir benar! Yuk perhatikan lagi gambarnya dan hitung pelan-pelan! 🕵️‍♂️")
        if st.button("Coba Lagi 🔄", use_container_width=True):
            st.session_state.status_jawaban = None
            st.rerun()
else:
    st.markdown('<audio autoplay style="display:none;"><source src="https://assets.mixkit.co/active_storage/sfx/2018/2018-preview.mp3" type="audio/mpeg"></audio>', unsafe_allow_html=True)
    st.markdown('<div class="card" style="text-align:center;">', unsafe_allow_html=True)
    st.markdown('<div class="question-text" style="font-size: 2.5rem; color: #4F46E5;">🏆 TAMAT! 🏆</div>', unsafe_allow_html=True)
    st.write(f"Kamu adalah Ahli Matematika sejati! Total skormu adalah **{st.session_state.score}** dari 250 maksimal poin.")
    st.markdown('<div class="emoji-box" style="background-color: #FEF08A;">🎓🥇🎉</div>', unsafe_allow_html=True)
    if st.button("Mainkan Lagi dari Level 1 🔄", use_container_width=True):
        st.session_state.q_index = 0; st.session_state.score = 0; st.session_state.status_jawaban = None; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
