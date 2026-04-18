import streamlit as st
import random
import time
from fpdf import FPDF

st.set_page_config(page_title="SERKAN HOCA İLE", page_icon="📘", layout="centered")

# ====================== SORU HAVUZU ======================
questions_pool = [
    {"id": 1, "q": "Yer kabuğundan çekirdeğe doğru inildikçe sıcaklık, yoğunluk ve basınç artar. Dünya’nın en yoğun, en basınçlı ve en kalın katmanı hangisidir?", "options": ["A) Yer kabuğu", "B) Manto", "C) Çekirdek", "D) Astenosfer", "E) SIAL"], "correct": "C"},
    {"id": 2, "q": "Yer kabuğunun alt katmanında silisyum ve magnezyum yoğunluğu artar. Bu katmana ne ad verilir?", "options": ["A) SIAL", "B) SIMA", "C) Manto", "D) Barisfer", "E) Litosfer"], "correct": "B"},
    {"id": 3, "q": "Dünya’nın toplam hacminin yaklaşık %84’ünü oluşturan, 70-2900 km derinliğinde yer alan ve sıvı-akışkan yapıdaki katman aşağıdakilerden hangisidir?", "options": ["A) Yer kabuğu", "B) Çekirdek", "C) Manto", "D) SIAL", "E) Sima"], "correct": "C"},
    {"id": 4, "q": "1915 yılında Alfred Wegener tarafından ortaya atılan ve kıtaların tek parça halinde olduğunu savunan teori hangisidir?", "options": ["A) Levha Tektoniği Teorisi", "B) Deprem Teorisi", "C) Volkanizma Teorisi", "D) Kıtaların Kayma Teorisi", "E) Epirojenez Teorisi"], "correct": "D"},
    {"id": 5, "q": "Levha hareketleri kaç farklı şekilde gerçekleşir ve ülkemiz hangi iki levha arasında yer alır?", "options": ["A) 2 şekilde – Avrasya ve Pasifik", "B) 4 şekilde – Afrika ve Antarktika", "C) 1 şekilde – Sadece yaklaşma", "D) 5 şekilde – Pasifik ve İzlanda", "E) 3 şekilde – Yaklaşma, uzaklaşma ve yanal yer değiştirme"], "correct": "E"},
    {"id": 6, "q": "Ülkemizin büyük bir kısmı 3. Jeolojik zamanda (Senozoyik) oluşmuştur. Bu durum ülkemizi hangi açıdan etkilemektedir?", "options": ["A) Deprem riski yüksek ve genç oluşumlu bir ülkeyiz", "B) Masif araziler bakımından zenginiz", "C) Taş kömürü yatakları çok fazladır", "D) Dinazor fosilleri yaygındır", "E) Prekambriyen kayaçlar hâkimdir"], "correct": "A"},
    {"id": 7, "q": "Dünya yaklaşık 4,5 milyar yıl önce yaratılmıştır. ... Mezozoyik (2. zaman) devrinde gerçekleşen olay hangisidir?", "options": ["A) İnsan yaratılmıştır", "B) Dinazorlar ortaya çıkmıştır", "C) Ege Denizi oluşmuştur", "D) Toros Dağları oluşmuştur", "E) Taş kömürü yatakları oluşmuştur"], "correct": "B"},
    {"id": 8, "q": "Yer kabuğu parçalarının (levhaların) yükselmesi veya alçalması şeklinde gerçekleşen iç kuvvet hangisidir?", "options": ["A) Orojenez", "B) Volkanizma", "C) Epirojenez", "D) Deprem", "E) Tsunami"], "correct": "C"},
    {"id": 9, "q": "Karaların ağırlaşarak çökmesi sonucu denizin karaya doğru ilerlemesine ne ad verilir?", "options": ["A) Regresyon", "B) Orojenez", "C) Konveksiyonel akım", "D) Transgresyon", "E) Aşınma"], "correct": "D"},
    {"id": 10, "q": "Okyanus ve deniz tabanındaki tortul tabakaların kıtaların hareketiyle yan basınca uğraması sonucu oluşan dağ türü hangisidir?", "options": ["A) Volkanik dağlar", "B) Masif dağlar", "C) Epirojenez dağları", "D) Kırıklı dağlar", "E) Kıvrımlı ve kırıklı dağlar"], "correct": "E"},
    {"id": 11, "q": "Kıvrımlı dağlarda yüksekte kalan yerlere ne denir?", "options": ["A) Antiklinal", "B) Senklinal", "C) Horst", "D) Graben", "E) Dayk"], "correct": "A"},
    {"id": 12, "q": "Kırıklı dağlarda alçakta kalan yerlere ne denir? Ülkemizde bu tür ovaların en çok bulunduğu bölge hangisidir?", "options": ["A) Antiklinal – Doğu Anadolu", "B) Graben – Ege Bölgesi", "C) Senklinal – Karadeniz", "D) Horst – Akdeniz", "E) Kaldera – İç Anadolu"], "correct": "B"},
    {"id": 13, "q": "Ülkemizde aktif volkan bulunmadığı için hangi deprem türü görülmez?", "options": ["A) Tektonik depremler", "B) Çöküntü depremleri", "C) Volkanik depremler", "D) Tsunami depremleri", "E) Epirojenez depremleri"], "correct": "C"},
    {"id": 14, "q": "Depremi inceleyen bilim dalının adı nedir?", "options": ["A) Jeoloji", "B) Volkanoloji", "C) Petrografi", "D) Sismoloji", "E) Orojenez"], "correct": "D"},
    {"id": 15, "q": "Magmanın yer yüzüne çıkıp soğuyarak katılaşmasına ne denir?", "options": ["A) Derinlik volkanizması", "B) Konveksiyonel akım", "C) Epirojenez", "D) Orojenez", "E) Yüzey volkanizması"], "correct": "E"},
    {"id": 16, "q": "Derinlik volkanizmasında magmanın yerkabuğunun içine sokularak oluşan çok büyük volkanik kütleye ne ad verilir?", "options": ["A) Batolit", "B) Lakolit", "C) Sill", "D) Dayk", "E) Krater"], "correct": "A"},
    {"id": 17, "q": "Magmanın yerin derinliklerinde yavaş soğuyup katılaşmasıyla oluşan püskürük kayalara ne denir?", "options": ["A) Dış püskürük kayalar", "B) İç püskürük (plütonik) kayalar", "C) Tortul kayalar", "D) Metamorfik kayalar", "E) Organik tortul kayalar"], "correct": "B"},
    {"id": 18, "q": "Bitkisel ve hayvansal artıkların uzun süre toprak altında kalmasıyla oluşan tortul kayaç türü hangisidir?", "options": ["A) Fiziksel tortul", "B) Kimyasal tortul", "C) Organik tortul", "D) Püskürük kayaç", "E) Başkalaşım kayaç"], "correct": "C"},
    {"id": 19, "q": "Kayaç döngüsünde tortul kayaçların oluşumunda etkili olan temel süreç hangisidir?", "options": ["A) Erime-soğuma", "B) Yüksek sıcaklık ve basınç", "C) Kristalleşme", "D) Aşınma-taşıma-biriktirme", "E) Magmanın sokulması"], "correct": "D"},
    {"id": 20, "q": "Türkiye bugünkü görünümünü hangi jeolojik zamanda almıştır?", "options": ["A) 1. jeolojik zamanda", "B) 2. jeolojik zamanda", "C) Prekambriyen dönemde", "D) Mezozoyik dönemde", "E) 3. jeolojik zamanda"], "correct": "E"},
    {"id": 21, "q": "Türkiye en çok hangi orojenezden etkilenmiştir ve bu dönemde hangi dağlar oluşmuştur?", "options": ["A) Alp orojenezinden – Kuzey Anadolu ve Toros Dağları", "B) Kaledoniyen orojenezinden – İskandinavya Dağları", "C) Hersiniyen orojenezinden – Appalaş Dağları", "D) Epirojenezden – Ege grabenleri", "E) Volkanizmadan – Kula tepeleri"], "correct": "A"},
    {"id": 22, "q": "Türkiye’de deprem riski en az olan yöre aşağıdakilerden hangisidir?", "options": ["A) İstanbul", "B) Konya - Karapınar", "C) İzmir", "D) Van", "E) Hatay"], "correct": "B"},
    {"id": 23, "q": "Okyanus ve deniz tabanında biriken tortul tabakalar... kıvrımlı dağ örneği hangisidir?", "options": ["A) Ege bölgesindeki dağlar", "B) Kaz Dağı", "C) Toroslar", "D) Madra Dağı", "E) Aydın Dağları"], "correct": "C"},
    {"id": 24, "q": "Yüzey volkanizması magmanın yer yüzüne çıkıp soğuyarak katılaşmasıdır. Derinlik volkanizması örneği aşağıdakilerden hangisidir?", "options": ["A) Volkan konisi", "B) Krater", "C) Kaldera", "D) Batolit", "E) Maar"], "correct": "D"},
    {"id": 25, "q": "Kayaç döngüsünde ... Aşağıdakilerden hangisi metamorfik kayaç örneğidir?", "options": ["A) Bazalt", "B) Kumtaşı", "C) Kalker", "D) Linyit", "E) Mermer"], "correct": "E"}
]

# ====================== SESSION STATE ======================
if "questions" not in st.session_state:
    st.session_state.questions = random.sample(questions_pool, len(questions_pool))
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "current" not in st.session_state:
    st.session_state.current = 0
if "show_analysis" not in st.session_state:
    st.session_state.show_analysis = False
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if "end_time" not in st.session_state:
    st.session_state.end_time = None

# ====================== YARDIMCI FONKSİYONLAR ======================
def clean_tr(text):
    """Türkçe karakterleri PDF dostu karakterlere çevirir."""
    tr_map = str.maketrans("ığüşöçİĞÜŞÖÇ", "igusocIGUSOC")
    return str(text).translate(tr_map)

def create_pdf(results, correct, total, duration):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(190, 10, txt="SINAV SONUC BELGESI", ln=True, align='C')
        pdf.ln(10)
        
        pdf.set_font("Arial", "", 12)
        pdf.cell(0, 10, txt=clean_tr(f"Basari Orani: %{round((correct/total)*100)}"), ln=True)
        pdf.cell(0, 10, txt=clean_tr(f"Dogru Sayisi: {correct} / {total}"), ln=True)
        pdf.cell(0, 10, txt=clean_tr(f"Tamamlama Suresi: {duration}"), ln=True)
        pdf.ln(10)
        
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, txt="YANLIS YAPILAN SORULAR:", ln=True)
        pdf.set_font("Arial", "", 10)
        pdf.ln(2)
        
        for res in results:
            # Genişliği 190 vererek "horizontal space" hatasını engelliyoruz
            pdf.multi_cell(190, 8, txt=clean_tr(res))
            pdf.ln(2)
            
        return pdf.output(dest='S').encode('latin-1', errors='ignore')
    except:
        return None

# ====================== TASARIM ======================
st.markdown("""
<style>
    .stApp { max-width: 100%; padding: 0.8rem 1rem; }
    .stSuccess { background-color: #10b981; color: white; border-radius: 16px; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background: linear-gradient(90deg, #1e3a8a, #3b82f6); color: white; 
            padding: 1.1rem; border-radius: 16px; text-align: center; margin-bottom: 1.2rem;">
    <h1 style="margin:0; font-size:2.1rem;">📘 SERKAN HOCA İLE</h1>
    <h2 style="margin:0.3rem 0 0 0; font-size:1.15rem;">10. Sınıf Coğrafya • Yer'in Yapısı ve Levha Hareketleri</h2>
</div>
""", unsafe_allow_html=True)

# ====================== SINAV EKRANI ======================
if not st.session_state.show_analysis:
    st.progress(st.session_state.current / len(st.session_state.questions))
    q = st.session_state.questions[st.session_state.current]
    st.subheader(f"Soru {st.session_state.current + 1} / {len(st.session_state.questions)}")
    st.write(q["q"])

    selected = st.radio("", q["options"], index=None, key=f"q{st.session_state.current}", label_visibility="collapsed")

    if selected:
        st.session_state.answers[st.session_state.current] = selected[0]
        if st.session_state.current < len(st.session_state.questions) - 1:
            st.session_state.current += 1
        else:
            st.session_state.end_time = time.time()
            st.session_state.show_analysis = True
        st.rerun()

# ====================== ANALİZ EKRANI ======================
else:
    # Süre Hesaplama
    total_seconds = int(st.session_state.end_time - st.session_state.start_time)
    min_val, sec_val = divmod(total_seconds, 60)
    sure_metni = f"{min_val} dakika {sec_val} saniye"

    st.title("📊 Sınav Analizi")
    correct_count = sum(1 for i, q in enumerate(st.session_state.questions) if st.session_state.answers.get(i) == q["correct"])
    percent = round((correct_count / len(st.session_state.questions)) * 100)

    st.info(f"⏱️ **Sınavı Tamamlama Süreniz:** {sure_metni}")

    col1, col2 = st.columns([1, 3])
    with col1:
        st.metric("Başarı Oranı", f"%{percent}")
    with col2:
        if percent >= 80:
            st.success("🎉 TEBRİKLER HARİKASIN!")
        else:
            st.warning("Tekrar deneyerek daha iyi sonuçlar alabilirsiniz.")

    # Yanlış soruları listele ve PDF için hazırla
    wrong_list = []
    st.subheader("Yanlış Yapılan Sorular")
    for i, q in enumerate(st.session_state.questions):
        user_letter = st.session_state.answers.get(i, "Boş")
        if user_letter != q["correct"]:
            user_full = next((opt for opt in q["options"] if opt.startswith(user_letter + ")")), user_letter)
            correct_full = next((opt for opt in q["options"] if opt.startswith(q["correct"] + ")")), q["correct"])
            st.error(f"**Soru {i+1}:** {q['q'][:100]}...\n\n**Cevabınız:** {user_full} | **Doğru:** {correct_full}")
            wrong_list.append(f"Soru {i+1}: {q['q'][:50]}... Cevabiniz: {user_letter}, Dogru: {q['correct']}")

    # PDF İNDİRME BUTONU
    pdf_data = create_pdf(wrong_list, correct_count, len(st.session_state.questions), sure_metni)
    if pdf_data:
        st.download_button(
            label="📥 Sonuçları PDF Olarak İndir",
            data=pdf_data,
            file_name="sinav_sonucu.pdf",
            mime="application/pdf",
            use_container_width=True
        )

    # ALT BUTONLAR (Hata olsa bile artık burası hep görünür)
    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🔄 Sınavı Yeniden Başlat", type="primary", use_container_width=True):
            for key in list(st.session_state.keys()): del st.session_state[key]
            st.rerun()
    with c2:
        if st.button("🏠 Başa Dön", use_container_width=True):
            st.session_state.current = 0
            st.session_state.show_analysis = False
            st.session_state.start_time = time.time()
            st.rerun()
