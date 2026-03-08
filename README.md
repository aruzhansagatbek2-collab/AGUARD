import streamlit as st

st.set_page_config(page_title="A GUARD", page_icon="🛡️")
st.title("🛡️ A GUARD: Smart Fire Detection")

# Настройки датчиков в боковой панели
st.sidebar.header("🕹️ Симуляция датчиков")
temp = st.sidebar.slider("Температура (°C)", 10, 100, 25)
smoke = st.sidebar.slider("Уровень дыма", 0, 500, 20)
gas = st.sidebar.slider("Уровень газа CO", 0, 500, 10)

# Логика опасности
is_danger = temp > 60 or smoke > 200 or gas > 150

if is_danger:
    st.error("🚨 RED CODE: ОБНАРУЖЕНА УГРОЗА!")
    st.warning("Действуйте быстро! Рекомендация: Покиньте здание.")
    
    # Кнопки экстренного вызова
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("📞 112", type="primary", use_container_width=True)
    with col2:
        st.button("👨‍🚒 Сосед", use_container_width=True)
    with col3:
        st.button("👨‍👩‍👧 Семья", use_container_width=True)
else:
    st.success("✅ Статус: Всё в норме. Воздух чист.")

st.divider()

# Красивые карточки с данными
c1, c2, c3 = st.columns(3)
c1.metric("Темп.", f"{temp}°C", delta=f"{temp-25}°C" if temp > 25 else None)
c2.metric("Дым", smoke, delta=f"{smoke-20}" if smoke > 20 else None)
c3.metric("Газ", gas, delta=f"{gas-10}" if gas > 10 else None)

# Режим "Away Mode"
st.toggle("🔔 Режим 'Не дома' (Away Mode active)")


