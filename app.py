import streamlit as st
import random

st.set_page_config(page_title="SERKAN HOCA İLE", page_icon="📘", layout="centered")

# SORULAR (25 tane)
questions_pool = [ ... ]  # (Önceki mesajlardan aynı 25 soru burada olacak)

# UYGULAMA
if "questions" not in st.session_state:
    st.session_state.questions = random.sample(questions_pool, len(questions_pool))
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "current" not in st.session_state:
    st.session_state.current = 0
if "show_analysis" not in st.session_state:
    st.session_state.show_analysis = False

st.markdown("""
<div style="background: linear-gradient(90deg, #1e3a8a, #3b82f6); color: white; padding: 1rem; border-radius: 14px; text-align: center; margin-bottom: 1rem;">
    <h1 style="margin:0; font-size:2rem;">📘 SERKAN HOCA İLE</h1>
    <h2 style="margin:0.3rem 0 0 0; font-size:1.1rem;">10. Sınıf Coğrafya • Yer'in Yapısı ve Levha Hareketleri</h2>
</div>
""", unsafe_allow_html=True)

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
            st.session_state.show_analysis = True
        st.rerun()

else:
    st.title("📊 Sınav Analizi")
    correct_count = sum(1 for i, q in enumerate(st.session_state.questions) if st.session_state.answers.get(i) == q["correct"])
    percent = round((correct_count / len(st.session_state.questions)) * 100)

    col1, col2 = st.columns([1, 3])
    with col1:
        st.metric("Başarı Oranı", f"%{percent}")

    with col2:
        if percent >= 80:
            st.success("🎉 TEBRİKLER HARİKASIN!")
            st.balloons()      # Balonlar
            st.snow()          # Kar yağışı (havai fişek havası verir)
        else:
            st.info("Tekrar deneyerek daha iyi sonuçlar alabilirsiniz.")

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
