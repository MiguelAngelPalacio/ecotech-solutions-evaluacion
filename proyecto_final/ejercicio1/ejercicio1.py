def limpiar_registro_sensor(registro_raw):
    """
    Punto A: Normaliza y sanitiza los datos crudos de un sensor.
    - Limpia espacios sobrantes en sensor_id.
    - Convierte la temperatura a tipo float eliminando sufijos de unidad.
    - Asigna una ubicación por defecto si no fue registrada o está vacía.
    """
    # 1. Normalizar ID del sensor eliminando espacios sobrantes
    sensor_id = str(registro_raw.get("sensor_id", "")).strip()

    # 2. Convertir temperatura a float extrayendo solo caracteres numéricos y signo/decimal
    temp_raw = str(registro_raw.get("temperatura", "0")).strip()
    temp_limpia = "".join(c for c in temp_raw if c.isdigit() or c in [".", "-"])
    temperatura = float(temp_limpia) if temp_limpia else 0.0

    # 3. Valor por defecto seguro para ubicación en caso de estar ausente o vacía
    ubicacion_raw = registro_raw.get("ubicacion")
    if not ubicacion_raw or not str(ubicacion_raw).strip():
        ubicacion = "Ubicación Desconocida"
    else:
        ubicacion = str(ubicacion_raw).strip()

    return {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion
    }

def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    """
    Punto B: Mapea sensores en alerta y calcula el promedio térmico global.
    Retorna una tupla: (lista_sensores_alerta, promedio_temperatura).
    """
    if not lista_sensores_limpios:
        return ([], 0.0)

    # Filtrar IDs de sensores que superan el umbral térmico
    sensores_alerta = [
        sensor["sensor_id"] 
        for sensor in lista_sensores_limpios 
        if sensor["temperatura"] > umbral_temperatura
    ]

    # Calcular promedio global de temperatura
    suma_temperaturas = sum(sensor["temperatura"] for sensor in lista_sensores_limpios)
    promedio_temperatura = suma_temperaturas / len(lista_sensores_limpios)

    # Retornar tupla con los resultados
    return (sensores_alerta, promedio_temperatura)


# ==========================================
# BLOQUE DE EJECUCIÓN Y DEMOSTRACIÓN COMPLETA
# ==========================================
if __name__ == "__main__":
    # Registros crudos heterogéneos de EcoTech Solutions
    datos_crudos = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": "SENSOR-002", "temperatura": "31.2 °C", "ubicacion": ""},
        {"sensor_id": " SENSOR-003", "temperatura": "19.0C"},
        {"sensor_id": "SENSOR-004 ", "temperatura": "28.7C", "ubicacion": "Planta Sur"}
    ]

    # 1. Sanitización de registros
    registros_sanitizados = [limpiar_registro_sensor(reg) for reg in datos_crudos]

    # 2. Definición de umbral y generación de reporte
    UMBRAL = 25.0
    alertas, promedio_global = generar_resumen_sensores(registros_sanitizados, UMBRAL)

    # 3. Impresión formateada del reporte consolidado
    print("=" * 55)
    print(" REPORTE CONSOLIDADO DE MONITOREO TÉRMICO")
    print("=" * 55)
    print(f"Total de sensores procesados : {len(registros_sanitizados)}")
    print(f"Umbral de alerta configurado : {UMBRAL} °C")
    print(f"Promedio térmico global      : {promedio_global:.2f} °C")
    print("-" * 55)
    print(f"Sensores en Estado de Alerta : {', '.join(alertas) if alertas else 'Ninguno'}")
    print("=" * 55)
    print("\nDetalle de Registros Normalizados:")
    for sensor in registros_sanitizados:
        print(f" • ID: {sensor['sensor_id']:<11} | Temp: {sensor['temperatura']:>5.1f} °C | Ubicación: {sensor['ubicacion']}")
    print("=" * 55)
