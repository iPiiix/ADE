#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
========================================================================================
AUDITORÍA MATEMÁTICA Y DE SOFTWARE: CASO JPMORGAN CHASE (LONDON WHALE, 2012)
Asignatura: Matemáticas para la Empresa I (Facultad de Economía y Empresa - UMU)
Perfil: Graduado en DAM (Programación) · Estudiante de ADE

Este script reproduce de forma sencilla el error de la fórmula de Excel de JPMorgan
y demuestra cómo una prueba unitaria básica de software (DAM / Palantir) habría
evitado la pérdida de 6.200 millones de dólares.
========================================================================================
"""

def calcular_riesgo_correcto(inversion_millones: float, vol1: float, vol2: float) -> float:
    """
    CÁLCULO CORRECTO:
    Calcula la media aritmética de las dos volatilidades: (vol1 + vol2) / 2
    y la multiplica por la inversión total.
    """
    media_volatilidad = (vol1 + vol2) / 2.0
    riesgo = inversion_millones * media_volatilidad
    return riesgo


def calcular_riesgo_erroneo_excel(inversion_millones: float, vol1: float, vol2: float) -> float:
    """
    ERROR HISTÓRICO DE EXCEL DE JPMORGAN:
    En lugar de dividir entre 2, la fórmula dividió entre la suma: (vol1 + vol2).
    Al hacer: (vol1 * vol2) / (vol1 + vol2), el riesgo se reduce artificialmente.
    """
    volatilidad_erronea = (vol1 * vol2) / (vol1 + vol2)
    riesgo = inversion_millones * volatilidad_erronea
    return riesgo


def ejecutar_demostracion():
    inversion = 1000.0  # 1.000 Millones de dólares
    vol1 = 0.10        # 10% de volatilidad estimada
    vol2 = 0.10        # 10% de volatilidad estimada

    riesgo_real = calcular_riesgo_correcto(inversion, vol1, vol2)
    riesgo_excel = calcular_riesgo_erroneo_excel(inversion, vol1, vol2)

    print("=" * 70)
    print("  CASO JPMORGAN CHASE: COMPARACIÓN DE CÁLCULO DE RIESGO")
    print("=" * 70)
    print(f"Inversión total analizada:              ${inversion:,.0f} Millones USD")
    print(f"Volatilidad estimada (estimaciones 1 y 2): 10% y 10%")
    print("-" * 70)
    print(f"1. Cálculo Correcto (Media aritmética):    ${riesgo_real:,.1f} Millones USD (10%)")
    print(f"2. Error de Excel (Dividió entre la suma):  ${riesgo_excel:,.1f} Millones USD (5%)")
    print("-" * 70)
    print(f"DIFERENCIA (Riesgo ocultado por el fallo): -${riesgo_real - riesgo_excel:,.1f} Millones USD (-50.0%)")
    print("=" * 70)
    print("CONCLUSIÓN DE GESTIÓN (ADE):")
    print("Los directivos creyeron que solo arriesgaban $50M cuando en realidad")
    print("se estaban jugando $100M. Esa falsa seguridad les llevó a duplicar sus")
    print("apuestas y perder $6.200 millones de dólares.")
    print("=" * 70)


def test_software_dam():
    """
    EL FACTOR DAM / PALANTIR:
    Una simple prueba unitaria en el código que cualquier programador
    pone antes de desplegar el sistema.
    """
    print("\n>>> Ejecutando comprobación automática de código (Unit Test)...")
    inversion = 1000.0
    vol1, vol2 = 0.10, 0.10
    
    riesgo_calculado = calcular_riesgo_erroneo_excel(inversion, vol1, vol2)
    riesgo_esperado = 100.0  # 1.000 * 10% = 100M

    try:
        assert riesgo_calculado == riesgo_esperado, (
            f"ERROR DETECTADO: El modelo arrojó ${riesgo_calculado}M pero debería dar ${riesgo_esperado}M."
        )
        print("[TEST SUPERADO] El cálculo es correcto.")
    except AssertionError as error:
        print(f"[TEST FALLIDO - ALERTA ROJA]: {error}")
        print(">>> En un entorno profesional con pruebas (DAM / Palantir Foundry),")
        print(">>> este test habría BLOQUEADO el modelo de inmediato, evitando el desastre.")


if __name__ == "__main__":
    ejecutar_demostracion()
    test_software_dam()
