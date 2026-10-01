import streamlit as st

# Datos del servicio 277
tren_277 = [
    {"estacion": "Retiro", "horario": "19:55"},
    {"estacion": "Villa Ballester", "horario": "20:37 - 20:38"},
    {"estacion": "Campana", "horario": "21:45 - 21:48"},
    {"estacion": "Zarate", "horario": "22:03 - 22:06"},
    {"estacion": "Lima", "horario": "22:27 - 22:29"},
    {"estacion": "Baradero", "horario": "23:13 - 23:18"},
    {"estacion": "San Pedro", "horario": "00:06 - 00:11"},
    {"estacion": "Gobernador Castro", "horario": "00:31 - 00:33"},
    {"estacion": "Ramallo", "horario": "00:59 - 01:01"},
    {"estacion": "San Nicolas", "horario": "01:24 - 01:29"},
    {"estacion": "E.V.C", "horario": "01:54 - 01:56"},
    {"estacion": "Arroyo Seco", "horario": "02:14 - 02:16"},
    {"estacion": "Rosario Sur", "horario": "02:42 - 02:45"},
    {"estacion": "Rosario Norte", "horario": "03:29"},
]

# Datos del servicio 278 (invertido en recorrido con sus horarios reales)
tren_278a = [
    {"estacion": "Retiro", "horario": "12:22"},
    {"estacion": "Villa Ballester", "horario": "11:38 - 11:39"},
    {"estacion": "Campana", "horario": "10:24 - 10:27"},
    {"estacion": "Zarate", "horario": "10:11 - 10:14"},
    {"estacion": "Lima", "horario": "09:49 - 09:51"},
    {"estacion": "Baradero", "horario": "09:00 - 09:05"},
    {"estacion": "San Pedro", "horario": "08:04 - 08:09"},
    {"estacion": "Gobernador Castro", "horario": "07:44 - 07:46"},
    {"estacion": "Ramallo", "horario": "07:17 - 07:19"},
    {"estacion": "San Nicolas", "horario": "06:44 - 06:49"},
    {"estacion": "E.V.C", "horario": "06:20 - 06:22"},
    {"estacion": "Arroyo Seco", "horario": "06:01 - 06:03"},
    {"estacion": "Rosario Sur", "horario": "05:32 - 05:35"},
    {"estacion": "Rosario Norte", "horario": "04:48"},
]

tren_278 = tren_278a[::-1]

servicios = {"Servicio 277 (A Rosario)": tren_277, "Servicio 278 (A Retiro)": tren_278}

# --- INTERFAZ GRAFICA ---
st.title("Consulta de Itinerarios")

# Menú para elegir el tren
opcion_servicio = st.selectbox("Seleccione el servicio:", list(servicios.keys()))
servicio_seleccionado = servicios[opcion_servicio]

# Pestañas para ver todo o buscar una estación
tab1, tab2 = st.tabs(["Lista Completa", "Buscar Estación"])

with tab1:
    st.subheader("Itinerario Completo")
    st.dataframe(servicio_seleccionado, use_container_width=True)

with tab2:
    estaciones = [item["estacion"] for item in servicio_seleccionado]
    estacion_elegida = st.selectbox("Seleccione estación:", estaciones)

    for item in servicio_seleccionado:
        if item["estacion"] == estacion_elegida:
            st.info(
                f"**Estación:** {item['estacion']}\n\n**Horario:** {item['horario']}"
            )