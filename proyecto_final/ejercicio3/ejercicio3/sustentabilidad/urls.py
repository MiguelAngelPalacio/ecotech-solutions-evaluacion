<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>EcoTech - Sustentabilidad</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f9f4; color: #2c3e50; }
        h1, h2, h3 { color: #1e824c; }
        .card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px; }
        table { width: 100%; border-collapse: collapse; margin-top: 15px; background: white; }
        th, td { padding: 12px; border: 1px solid #e0e0e0; text-align: left; }
        th { background-color: #2e7d32; color: white; }
        tr:nth-child(even) { background-color: #f1f8e9; }
    </style>
</head>
<body>

    <h1>{{ titulo_panel }}</h1>
    
    <div class="card">
        <h2>Resumen Ejecutivo de Emisiones</h2>
        <p><strong>Emisiones Totales Globales:</strong> {{ emisiones_totales_kg }} kg CO₂</p>
        <p><strong>Planta de Mayor Consumo:</strong> {{ planta_mayor_consumo }}</p>
    </div>

    <div class="card">
        <h3>Desglose por Planta Industrial</h3>
        <table>
            <thead>
                <tr>
                    <th>Planta</th>
                    <th>Consumo (kWh)</th>
                    <th>Emisiones (kg CO₂)</th>
                </tr>
            </thead>
            <tbody>
                {% for item in desglose_plantas %}
                <tr>
                    <td>{{ item.planta }}</td>
                    <td>{{ item.consumo_kwh }}</td>
                    <td>{{ item.emisiones_kg }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>

</body>
</html>
