from aerocargo import validar_matrices, calcular_ocupacion, evaluar_balance, extraer_submatriz_critica

def main():
    print("=== AeroCargo-Matrix: Sistema de Auditoría de Carga ===")
    
    # 1. Definimos datos de prueba simulando el piso del avión (Matriz 4x4)
    cargas_reales = [
        [500, 450, 480, 510],
        [300, 310, 290, 305],
        [600, 700, 800, 650], # Colocamos un peso de 800 intencionalmente para forzar sobrecarga
        [200, 150, 150, 200]
    ]
    
    capacidades_maximas = [
        [600, 600, 600, 600],
        [400, 400, 400, 400],
        [600, 600, 600, 600],
        [300, 300, 300, 300]
    ]
    
    # Módulo 1: Validación
    es_valido = validar_matrices(cargas_reales, capacidades_maximas)
    print(f"\n1. Validación Dimensional: {'Aprobada ' if es_valido else 'Rechazada '}")
    
    if not es_valido:
        print("Error: Las matrices no son operativamente válidas.")
        return
        
    # Módulo 2: Ocupación y Sobrecarga
    resultado_ocupacion = calcular_ocupacion(cargas_reales, capacidades_maximas)
    criticas = resultado_ocupacion['coordenadas_criticas']
    print(f"\n2. Coordenadas con Sobrecarga Crítica (>100%):")
    if criticas:
        print(f"    Alerta en celdas (Fila, Columna): {criticas}")
    else:
        print("    Ninguna celda supera el límite.")
    
    # Módulo 3: Balance y Simetría (Tolerancia de 300 kg para este vuelo)
    tolerancia_kg = 300.0
    resultado_balance = evaluar_balance(cargas_reales, tolerancia_kg)
    print(f"\n3. Evaluación de Simetría Lateral:")
    print(f"   Estado: {'Aprobado ' if resultado_balance['estado_balance'] else 'Desbalanceado '}")
    print(f"   Desbalance absoluto: {resultado_balance['desbalance_lateral']} kg")
    print(f"   Vector longitudinal de masa: {resultado_balance['pesos_longitudinales']}")
    
    # Módulo 4: Submatriz Crítica (Evaluamos una ventana de 2x2 compartimientos)
    matriz_porcentajes = resultado_ocupacion['matriz_porcentajes']
    submatriz = extraer_submatriz_critica(matriz_porcentajes, 2, 2)
    print(f"\n4. Extracción de Submatriz Crítica (Ventana 2x2):")
    for fila in submatriz:
        print(f"   {[round(val, 1) for val in fila]} %")

if __name__ == '__main__':
    main()
