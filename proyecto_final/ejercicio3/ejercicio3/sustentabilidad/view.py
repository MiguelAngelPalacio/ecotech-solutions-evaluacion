from django.shortcuts import render

def calcular_emisiones_carbono(consumo_kwh: float, factor_emision: float = 0.4) -> float:
    """
    Calcula las emisiones de carbono en kgCO2 basados en el consumo de kWh.
    Eleva un ValueError si el consumo es negativo.
    """
    if consumo_kwh < 0:
        raise ValueError("El consumo en kWh no puede ser negativo.")
    return consumo_kwh * factor_emision

def obtener_metricas_consumo(registros: list) -> dict:
    """
    Procesa el historial de consumos de plantas industriales.
    Determina las emisiones totales globales y la planta de mayor consumo.
    """
    if not registros:
        return {
            "emisiones_totales_kg": 0.0,
            "planta_mayor_consumo": "Sin datos",
            "desglose_plantas": []
        }

    emisiones_totales = 0.0
    planta_max_consumo = None
    max_kwh = -1.0
    desglose = []

    for reg in registros:
        planta = reg.get("planta", "Desconocida")
        consumo = reg.get("consumo_kwh", 0.0)
        factor = reg.get("factor_emision", 0.4)

        # Invocación de la función auditada en Punto A
        emision_planta = calcular_emisiones_carbono(consumo, factor)
        emisiones_totales += emision_planta

        # Determinación de la planta de mayor consumo
        if consumo > max_kwh:
            max_kwh = consumo
            planta_max_consumo = planta

        desglose.append({
            "planta": planta,
            "consumo_kwh": consumo,
            "emisiones_kg": emision_planta
        })

    return {
        "emisiones_totales_kg": emisiones_totales,
        "planta_mayor_consumo": planta_max_consumo,
        "desglose_plantas": desglose
    }

def vista_panel_sustentabilidad(request):
    """
    Vista en Django que procesa las métricas de consumo industrial
    y proporciona el diccionario de contexto a la plantilla sustentabilidad/panel.html.
    """
    # Historial de consumos industriales (simulación de datos recuperados)
    registros_historial = [
        {"planta": "Planta Norte", "consumo_kwh": 12500.0, "factor_emision": 0.4},
        {"planta": "Planta Sur", "consumo_kwh": 18900.0, "factor_emision": 0.4},
        {"planta": "Planta Centro", "consumo_kwh": 9400.0, "factor_emision": 0.35},
        {"planta": "Planta Este", "consumo_kwh": 15200.0, "factor_emision": 0.42}
    ]

    # Procesar métricas globales
    metricas = obtener_metricas_consumo(registros_historial)

    # Diccionario de contexto estructurado para la plantilla HTML
    contexto = {
        "titulo_panel": "Panel de Monitoreo de Sustentabilidad Industrial",
        "emisiones_totales_kg": metricas["emisiones_totales_kg"],
        "planta_mayor_consumo": metricas["planta_mayor_consumo"],
        "desglose_plantas": metricas["desglose_plantas"],
        "total_registros": len(registros_historial)
    }

    # Renderizado hacia la plantilla requerida
    return render(request, "sustentabilidad/panel.html", contexto)
