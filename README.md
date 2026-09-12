# AeroCargo-Matrix: Auditoria y Balance Matricial

## 1. Explicacion del Problema Operativo
En el transporte aéreo de carga, distribuir bien el peso en la bodega es súper importante por dos factores de seguridad:
* **Capacidad Estructural del Piso:** Cada compartimiento del avión tiene un límite máximo de carga. Si nos pasamos de ese límite, podemos dañar la estructura del fuselaje por sobrecarga.
* **Balance y Simetría Lateral:** Para que el avión sea estable en el aire y fácil de maniobrar, el peso total tiene que estar bien equilibrado entre babor y estribor, o sea, entre los lados izquierdo y derecho.

## 2. Diagrama de Arquitectura Modular
El sistema procesa los datos paso a paso usando funciones puras. Esto asegura que los datos originales nunca se modifiquen.

```text
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
