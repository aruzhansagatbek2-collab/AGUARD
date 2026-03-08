import streamlit as st
st.title("🛡️ A GUARD")
t = st.sidebar.slider("Temp", 10, 100, 25)
s = st.sidebar.slider("Smoke", 0, 500, 20)
if t > 60 or s > 200:
    st.error("🚨 RED CODE!")
    st.button("📞 112", type="primary")
else:
    st.success("✅ Normal")
st.metric("T", f"{t}°C")
st.metric("S", s)
