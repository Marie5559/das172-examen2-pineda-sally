# AeroCargo-Matrix: Auditoria y Balance Matricial

## 1. Explicacion del Problema Operativo
En el transporte aéreo de carga, distribuir bien el peso en la bodega es súper importante por dos factores de seguridad:
* **Capacidad Estructural del Piso:** Cada compartimiento del avión tiene un límite máximo de carga. Si nos pasamos de ese límite, podemos dañar la estructura del fuselaje por sobrecarga.
* **Balance y Simetría Lateral:** Para que el avión sea estable en el aire y fácil de maniobrar, el peso total tiene que estar bien equilibrado entre babor y estribor, o sea, entre los lados izquierdo y derecho.

## 2. Diagrama de Arquitectura Modular
El sistema procesa los datos paso a paso usando funciones puras. Esto asegura que los datos originales nunca se modifiquen.

[ Matrices de Entrada N x M ] 
            │
            ▼
┌─────────────────────────────┐
│ 1. validar_matrices         │ ──> Retorna si las dimensiones son correctas
└─────────────────────────────┘
            │
            ▼
┌─────────────────────────────┐
│ 2. calcular_ocupacion       │ ──> Retorna matriz de porcentajes y alertas
└─────────────────────────────┘
            │
            ▼
┌─────────────────────────────┐
│ 3. evaluar_balance          │ ──> Retorna sumas, desbalance en kg y estado
└─────────────────────────────┘
            │
            ▼
┌─────────────────────────────┐
│ 4. extraer_submatriz_critica│ ──> Retorna el sector k x p con mayor ocupación
└─────────────────────────────┘

## 3. Analisis de Complejidad Computacional
El código está pensado para ser eficiente y no gastar recursos de más:
* **Complejidad de Tiempo $O(N \times M)$:** Como tenemos que revisar la carga y el balance celda por celda, el programa recorre las N filas y las M columnas. El tiempo de procesamiento crece a medida que el piso del avión tiene más compartimientos.
* **Complejidad de Memoria $O(N \times M)$:** Para cumplir la regla de usar funciones puras, el programa nunca altera los datos originales. Lo que hace es crear matrices nuevas del mismo tamaño para guardar los resultados, como la nueva matriz de porcentajes. Por esto, el espacio en memoria siempre es proporcional a las dimensiones N por M.
