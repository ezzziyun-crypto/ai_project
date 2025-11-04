import streamlit as st

st.set_page_config(page_title="MBTI별 책&영화 추천 💫", page_icon="📖")

st.title("🌈 MBTI별 책 & 영화 추천 🎬")
st.write("안녕! 😊 너의 MBTI를 알려주면, 너한테 딱 어울리는 책이랑 영화 추천해줄게💖")

mbti = st.selectbox("너의 MBTI는 뭐야?", [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
])

# MBTI별 추천 데이터
recommendations = {
    "INTJ": {
        "books": [("데미안 - 헤르만 헤세", "자기 성장과 내면 탐구를 좋아하는 INTJ에게 찰떡!"),
                  ("아몬드 - 손원평", "감정과 논리의 경계를 탐구하는 내용이 딱이야.")],
        "movies": [("인셉션", "복잡한 구조와 철학적인 주제, INTJ 스타일 🎭"),
                   ("인터스텔라", "지적이고 감정적인 우주여행, 완전 취향저격 🚀")]
    },
    "INFP": {
        "books": [("82년생 김지영 - 조남주", "공감력 넘치는 INFP에게 와닿는 이야기 💫"),
                  ("연의 편지 - 조현", "감성 가득한 성장소설, 마음이 따뜻해져 ☕")],
        "movies": [("월터의 상상은 현실이 된다", "꿈과 현실 사이를 여행하는 INFP의 영화 🌍"),
                   ("어바웃 타임", "사랑과 시간에 대한 감성폭발 영화 ⏰💖")]
    },
    "ENFP": {
        "books": [("지금 하지 않으면 언제 하겠는가 - 팀 페리스", "열정 넘치는 ENFP에게 동기부여 팍팍! 💥"),
                  ("달러구트 꿈 백화점 - 이미예", "상상력 가득한 세계관, ENFP 감성에 찰떡 🌙")],
        "movies": [("라라랜드", "꿈과 사랑 사이에서 고민하는 ENFP의 이야기 🎶"),
                   ("인턴", "따뜻하고 활기찬 관계를 그린 영화 ☕💼")]
    },
    "ISTJ": {
        "books": [("공정하다는 착각 - 마이클 샌델", "논리적이고 현실적인 ISTJ에게 딱 맞는 주제 📘"),
                  ("미움받을 용기 - 기시미 이치로", "원칙을 지키는 네가 더 자유로워질 수 있어 💡")],
        "movies": [("셜록 홈즈", "논리적이고 분석적인 추리력, 너랑 잘 어울려 🕵️‍♂️"),
                   ("머니볼", "데이터와 효율을 중시하는 ISTJ에게 추천 ⚾")]
    },
    "ESFP": {
        "books": [("트렌드 코리아 2025 - 김난도", "세상 돌아가는 흐름을 캐치하는 ESFP에게 🎯"),
                  ("죽고 싶지만 떡볶이는 먹고 싶어 - 백세희", "솔직한 감정에 공감할 수 있는 책 🍜")],
        "movies": [("맘마미아!", "에너지 폭발! 노래와 춤으로 가득한 영화 🎤💃"),
                   ("인사이드 아웃", "감정이 주인공인 영화, 완전 너 같아 😍")]
    }
}

if mbti:
    if mbti in recommendations:
        data = recommendations[mbti]
        st.subheader(f"💫 {mbti} 유형을 위한 추천 리스트 💫")

        st.write("📚 **추천 책**")
        for book, reason in data["books"]:
            st.write(f"- **{book}** — {reason}")

        st.write("🎬 **추천 영화**")
        for movie, reason in data["movies"]:
            st.write(f"- **{movie}** — {reason}")

        st.success("읽고 보고 나면, 너만의 생각도 더 깊어질 거야 🌟")
    else:
        st.info("곧 다른 MBTI 유형도 추가될 예정이야! 기다려줘 😆")
