import numpy as np

def validar_matrices(cargas, capacidades):
    cargas_np = np.array(cargas)
    capacidades_np = np.array(capacidades)
    
    if cargas_np.ndim != 2 or capacidades_np.ndim != 2:
        return False
    if cargas_np.shape != capacidades_np.shape:
        return False
        
    N, M = cargas_np.shape
    if N < 2 or M < 2:
        return False
    if np.any(cargas_np < 0) or np.any(capacidades_np <= 0):
        return False
        
    return True

def calcular_ocupacion(cargas, capacidades):
    cargas_np = np.array(cargas)
    capacidades_np = np.array(capacidades)
    
    porcentajes = (cargas_np / capacidades_np) * 100.0
    filas, columnas = np.where(porcentajes > 100.0)
    coordenadas_sobrecarga = list(zip(filas.tolist(), columnas.tolist()))
    
    return {
        "matriz_porcentajes": porcentajes,
        "coordenadas_criticas": coordenadas_sobrecarga
    }

def evaluar_balance(cargas, tolerancia):
    cargas_np = np.array(cargas)
    pesos_longitudinales = np.sum(cargas_np, axis=1).tolist()
    
    M = cargas_np.shape[1]
    mitad = M // 2
    
    if M % 2 == 0:
        suma_izquierda = np.sum(cargas_np[:, :mitad])
        suma_derecha = np.sum(cargas_np[:, mitad:])
    else:
        suma_izquierda = np.sum(cargas_np[:, :mitad])
        suma_derecha = np.sum(cargas_np[:, mitad+1:])
        
    desbalance_lateral = abs(suma_izquierda - suma_derecha)
    estado_balance = bool(desbalance_lateral <= tolerancia)
    
    return {
        "pesos_longitudinales": pesos_longitudinales,
        "desbalance_lateral": float(desbalance_lateral),
        "estado_balance": estado_balance
    }

def extraer_submatriz_critica(porcentajes, k, p):
    porcentajes_np = np.array(porcentajes)
    N, M = porcentajes_np.shape
    
    if k > N or p > M:
        return None
        
    max_promedio = -1.0
    submatriz_critica = None
    
    for i in range(N - k + 1):
        for j in range(M - p + 1):
            submatriz_actual = porcentajes_np[i:i+k, j:j+p]
            promedio_actual = np.mean(submatriz_actual)
            
            if promedio_actual > max_promedio:
                max_promedio = promedio_actual
                submatriz_critica = submatriz_actual
                
    return submatriz_critica.tolist()
