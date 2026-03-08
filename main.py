import streamlit as st

# Настройка страницы
st.set_page_config(page_title="A GUARD", page_icon="🛡️")
st.title("🛡️ A GUARD: Smart Fire Detection")

# 1. Датчики (Симуляция)
st.sidebar.header("🕹️ Датчики")
temp = st.sidebar.slider("Температура (°C)", 10, 100, 25)
smoke = st.sidebar.slider("Уровень дыма", 0, 500, 20)

# 2. Логика тревоги (RED CODE)
is_danger = temp > 60 or smoke > 200

if is_danger:
    st.error("🚨 RED CODE: ОБНАРУЖЕНА ОПАСНОСТЬ!")
    st.warning("Внимание: Возможен пожар. Покиньте здание!")
    
    # Кнопки экстренного вызова
    col1, col2 = st.columns(2)
    with col1:
        st.button("📞 Вызвать 112", type="primary", use_container_width=True)
    with col2:
        st.button("👨‍👩‍👧 Семья", use_container_width=True)
else:
    st.success("✅ СИСТЕМА: Всё в норме.")

# 3. Карточки данных
st.divider()
c1, c2 = st.columns(2)
c1.metric("Темп.", f"{temp} °C")
c2.metric("Дым", f"{smoke} ppm")

# 4. Режим Away
st.toggle("🔔 Режим 'Не дома'")
