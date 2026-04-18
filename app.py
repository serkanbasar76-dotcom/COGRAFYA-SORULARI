import streamlit as st
import random
from streamlit.components.v1 import html

st.set_page_config(page_title="SERKAN HOCA İLE", page_icon="📘", layout="centered")

# ====================== SORU BANKASI ======================
questions_pool = [ ... ]  # (25 soru aynı kalıyor, yer kaplamasın diye kısalttım)

# ====================== UYGULAMA ======================
if "questions" not in st.session_state:
    st.session_state.questions = random.sample(questions_pool, len(questions_pool))
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "current" not in st.session_state:
    st.session_state.current = 0
if "show_analysis" not in st.session_state:
    st.session_state.show_analysis = False

# Başlık
st.markdown("""
<div style="background: linear-gradient(90deg, #1e3a8a, #3b82f6); color: white; 
            padding: 1.2rem 1rem; border-radius: 16px; text-align: center; 
            margin-bottom: 1.2rem; box-shadow: 0 8px 25px rgba(30,58,138,0.3);">
    <h1 style="font-size: 2.1rem; margin: 0; font-weight: 700;">📘 SERKAN HOCA İLE</h1>
    <h2 style="font-size: 1.25rem; margin: 0.2rem 0 0 0; opacity: 0.95;">
        10. Sınıf Coğrafya • Yer'in Yapısı ve Levha Hareketleri
    </h2>
</div>
""", unsafe_allow_html=True)

if not st.session_state.show_analysis:
    # ... (soru kısmı aynı kalıyor)
    progress = st.session_state.current / len(st.session_state.questions)
    st.progress(progress)
    q = st.session_state.questions[st.session_state.current]
    st.subheader(f"Soru {st.session_state.current + 1} / {len(st.session_state.questions)}")
    st.write(q["q"])

    selected = st.radio(label="", options=q["options"], index=None, 
                        key=f"q{st.session_state.current}", label_visibility="collapsed")

    if selected:
        st.session_state.answers[st.session_state.current] = selected[0]
        if st.session_state.current < len(st.session_state.questions) - 1:
            st.session_state.current += 1
        else:
            st.session_state.show_analysis = True
        st.rerun()

else:
    # ====================== ANALİZ EKRANI ======================
    st.title("📊 Sınav Analizi")
    correct_count = sum(1 for i, q in enumerate(st.session_state.questions) 
                       if st.session_state.answers.get(i) == q["correct"])
    percent = round((correct_count / len(st.session_state.questions)) * 100)

    col1, col2 = st.columns([1, 3])
    with col1:
        st.metric("Başarı Oranı", f"%{percent}")
    
    with col2:
        if percent >= 80:
            st.success("🎉 TEBRİKLER HARİKASIN!")
            
            # GÜÇLENDİRİLMİŞ HAVAI FIŞEK EFEKTİ
            html("""
            <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"></script>
            <script>
                function fireworks() {
                    const count = 300;
                    const defaults = { origin: { y: 0.6 } };
                    function fire(ratio, opts) {
                        confetti(Object.assign({}, defaults, opts, {
                            particleCount: Math.floor(count * ratio)
                        }));
                    }
                    fire(0.3, { spread: 40, startVelocity: 60 });
                    fire(0.25, { spread: 80 });
                    fire(0.35, { spread: 120, decay: 0.88, scalar: 1.1 });
                    fire(0.2, { spread: 150, startVelocity: 30, decay: 0.92 });
                }
                fireworks();
                setTimeout(fireworks, 180);
                setTimeout(fireworks, 380);
                setTimeout(fireworks, 580);
                setTimeout(fireworks, 780);
            </script>
            """, height=180)   # ← Yükseklik artırıldı, daha güvenilir çalışıyor

        else:
            st.info("Daha iyi bir sonuç için tekrar deneyebilirsiniz.")

    # Yanlış sorular kısmı (aynı)
    st.subheader("Yanlış Yapılan Sorular")
    for i, q in enumerate(st.session_state.questions):
        user_letter = st.session_state.answers.get(i, "Boş")
        if user_letter != q["correct"]:
            user_full = next((opt for opt in q["options"] if opt.startswith(user_letter + ")")), user_letter)
            correct_full = next((opt for opt in q["options"] if opt.startswith(q["correct"] + ")")), q["correct"])
            st.error(f"**Soru {i+1}**  \n{q['q'][:140]}...  \n**Sizin cevabınız:** {user_full}  \n**Doğru cevap:** {correct_full}")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Sınavı Yeniden Başlat", type="primary", use_container_width=True):
            for key in list(st.session_state.keys()): del st.session_state[key]
            st.rerun()
    with col2:
        if st.button("🏠 Başa Dön", use_container_width=True):
            st.session_state.current = 0
            st.session_state.show_analysis = False
            st.rerun()
