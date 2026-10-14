#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador automático de la Ficha Oficial en Word (.docx)
Caso: JPMorgan Chase (London Whale, 2012) - Versión Simplificada y Clara
"""

import os
import zipfile
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DOCX = os.path.join(BASE_DIR, "Ficha Auditoria Matemática.docx")
OUTPUT_DOCX = os.path.join(BASE_DIR, "Ficha_Auditoria_Matematica_RESUELTA_JPMorgan.docx")

NS_W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
ET.register_namespace('w', NS_W)

def create_p(text: str, bold: bool = False, italic: bool = False, space_after: int = 120) -> ET.Element:
    p = ET.Element(f"{{{NS_W}}}p")
    pPr = ET.SubElement(p, f"{{{NS_W}}}pPr")
    sp = ET.SubElement(pPr, f"{{{NS_W}}}spacing")
    sp.set(f"{{{NS_W}}}after", str(space_after))
    sp.set(f"{{{NS_W}}}line", "276")
    sp.set(f"{{{NS_W}}}lineRule", "auto")
    
    r = ET.SubElement(p, f"{{{NS_W}}}r")
    rPr = ET.SubElement(r, f"{{{NS_W}}}rPr")
    
    rFonts = ET.SubElement(rPr, f"{{{NS_W}}}rFonts")
    rFonts.set(f"{{{NS_W}}}ascii", "Calibri")
    rFonts.set(f"{{{NS_W}}}hAnsi", "Calibri")
    
    sz = ET.SubElement(rPr, f"{{{NS_W}}}sz")
    sz.set(f"{{{NS_W}}}val", "22") # 11pt
    
    if bold:
        ET.SubElement(rPr, f"{{{NS_W}}}b")
    if italic:
        ET.SubElement(rPr, f"{{{NS_W}}}i")
        
    t = ET.SubElement(r, f"{{{NS_W}}}t")
    t.text = text
    t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    return p

def create_heading(text: str, level: int = 1) -> ET.Element:
    p = ET.Element(f"{{{NS_W}}}p")
    pPr = ET.SubElement(p, f"{{{NS_W}}}pPr")
    sp = ET.SubElement(pPr, f"{{{NS_W}}}spacing")
    sp.set(f"{{{NS_W}}}before", "200")
    sp.set(f"{{{NS_W}}}after", "100")
    
    r = ET.SubElement(p, f"{{{NS_W}}}r")
    rPr = ET.SubElement(r, f"{{{NS_W}}}rPr")
    ET.SubElement(rPr, f"{{{NS_W}}}b")
    color = ET.SubElement(rPr, f"{{{NS_W}}}color")
    color.set(f"{{{NS_W}}}val", "1F497D") # Navy blue
    
    sz = ET.SubElement(rPr, f"{{{NS_W}}}sz")
    sz.set(f"{{{NS_W}}}val", "26" if level == 1 else "24") # 13pt / 12pt
    
    t = ET.SubElement(r, f"{{{NS_W}}}t")
    t.text = text
    t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    return p

def generar_documento():
    with zipfile.ZipFile(TEMPLATE_DOCX, 'r') as zin:
        xml_content = zin.read('word/document.xml')
        root = ET.fromstring(xml_content)
        
        body = root.find(f"{{{NS_W}}}body")
        sectPr = body.find(f"{{{NS_W}}}sectPr")
        body.clear()
        
        # Header
        body.append(create_heading("FICHA DEL ALUMNADO — EXPEDIENTE DE AUDITORÍA MATEMÁTICA", level=1))
        body.append(create_p("Nombre y apellidos: Santiago [Graduado en DAM / Estudiante de ADE]", bold=True))
        body.append(create_p("Grupo: Grupo 5 (Turno Tarde)        Fecha: 1 de diciembre de 2026", bold=True))
        body.append(create_p("Asignatura: Matemáticas para la Empresa I (Cód. 2350) — Profesora: Matilde Lafuente Lechuga", italic=True))
        
        # 1. La Evidencia
        body.append(create_heading("1. LA EVIDENCIA", level=2))
        body.append(create_p("Tipo de fuente: [X] Noticia   [ ] Publicidad   [X] Informe Oficial   [ ] Página web   [ ] Documento comercial   [ ] Otro", bold=True))
        body.append(create_p("Título o descripción del caso: El error de cálculo de 6.200 millones de dólares: la fórmula de Excel de JPMorgan que dividió entre la suma en vez de hacer una media aritmética.", bold=True))
        body.append(create_p("Fuente: Informe Oficial del Senado de EE.UU. (Whale Trades Investigation) / Informe de Auditoría Interna de JPMorgan / Financial Times"))
        body.append(create_p("Fecha: 2012 (implementación del modelo en Excel) – 2013 (informe oficial de auditoría)"))
        body.append(create_p("Enlace o referencia: U.S. Senate Hearing on CIO Losses (Exhibit 103) & JPMorgan Management Task Force Report (p. 128)"))
        body.append(create_p("Fragmento transcrito del informe oficial de auditoría:", italic=True))
        body.append(create_p("«El modelo funcionaba mediante hojas de cálculo de Excel que se completaban manualmente, copiando y pegando datos de una hoja a otra... La fórmula utilizada para calcular el riesgo neto cometió un error operativo crítico: en lugar de dividir por el promedio de dos métricas, dividió por su suma. Como resultado, el modelo redujo la volatilidad estimada a la mitad, ocultando el 50% del riesgo real acumulado.» (JPMorgan Task Force Report, p. 128)", italic=True))

        # 2. Qué afirma la fuente
        body.append(create_heading("2. ¿QUÉ AFIRMA LA FUENTE?", level=2))
        body.append(create_p("El departamento de inversión (CIO) de JPMorgan Chase afirmó a la dirección del banco y a los reguladores que el riesgo diario de su cartera de inversión se había reducido notablemente."))
        body.append(create_p("Basándose en este dato erróneo de la hoja de cálculo, los operadores acumularon posiciones gigantescas en derivados crediticios, convencidos de que operaban con total seguridad. En realidad, el riesgo real no había bajado, sino que se había duplicado: la aparente tranquilidad era una ilusión provocada por un simple error de formulación en una celda de Excel."))

        # 3. Término Matemático
        body.append(create_heading("3. TÉRMINO MATEMÁTICO QUE PRESENTA EL PROBLEMA", level=2))
        body.append(create_p("1. Media aritmética simple vs. División por la suma (Aritmética básica - Tema 0): confusión conceptual en el divisor entre el número de observaciones (N=2) y la suma de las propias variables."))
        body.append(create_p("2. Funciones de una variable y signo de la derivada (Tema 1): una función de riesgo debe ser estrictamente creciente respecto a la volatilidad del mercado (derivada positiva: f'(x) > 0). Al poner la variable en el denominador, el error convirtió la función en decreciente (derivada negativa: g'(x) < 0)."))
        body.append(create_p("3. Porcentajes y proporcionalidad directa."))

        # 4. Diagnóstico Matemático
        body.append(create_heading("4. DIAGNÓSTICO MATEMÁTICO: EXPLICACIÓN PASO A PASO CON NÚMEROS REALES", level=2))
        body.append(create_p("A) El cálculo correcto con números claros:", bold=True))
        body.append(create_p("Supongamos dos estimaciones de volatilidad del mercado: x1 = 10% (0,10) y x2 = 10% (0,10)."))
        body.append(create_p("La media aritmética correcta es: Promedio = (0,10 + 0,10) / 2 = 0,20 / 2 = 0,10 (10%)."))
        body.append(create_p("Para una inversión de 1.000 millones de dólares, el riesgo real es: 1.000M$ * 10% = 100 millones de dólares."))
        body.append(create_p("B) El error cometido en la celda de Excel:", bold=True))
        body.append(create_p("En lugar de dividir entre 2, el analista dividió entre la suma (0,10 + 0,10):"))
        body.append(create_p("Fórmula errónea de Excel = (0,10 * 0,10) / (0,10 + 0,10) = 0,01 / 0,20 = 0,05 (5%)."))
        body.append(create_p("Riesgo que mostró Excel en pantalla: 1.000M$ * 5% = 50 millones de dólares."))
        body.append(create_p("¡El fallo hizo desaparecer la mitad del riesgo! La pantalla mostraba 50M$ cuando el riesgo real era de 100M$."))
        body.append(create_p("C) Demostración con la derivada (Tema 1):", bold=True))
        body.append(create_p("Función correcta esperada: f(x) = K * x, cuya derivada es f'(x) = K > 0 (función creciente: a más volatilidad de mercado x, mayor riesgo medido)."))
        body.append(create_p("Función del fallo de Excel: g(x) = K / x = K * x^(-1), cuya derivada es g'(x) = -K / x^2 < 0 (función decreciente). Al subir la volatilidad real, el modelo erróneo reportaba menos riesgo en pantalla."))

        # 5. Gravedad
        body.append(create_heading("5. NIVEL DE GRAVEDAD DEL ERROR", level=2))
        body.append(create_p("[ ] Error menor: apenas modifica la interpretación."))
        body.append(create_p("[ ] Error relevante: puede inducir a una conclusión incorrecta."))
        body.append(create_p("[X] Error grave: puede afectar de forma importante a una decisión económica o empresarial.", bold=True))
        body.append(create_p("Justificación ADE: Es el error de cálculo con mayor impacto económico directo de la historia financiera: pérdida directa de 6.200 millones de dólares en el balance de JPMorgan, sanciones de más de 1.000 millones de dólares impuestas por los reguladores (SEC/FCA), dimisión de los máximos directivos del área de inversión y una caída del 15% del valor en bolsa del banco.", bold=True))

        # 6. Procedimiento Correcto
        body.append(create_heading("6. ENUNCIADO Y PROCEDIMIENTO CORRECTO", level=2))
        body.append(create_p("Fórmula corregida: La media aritmética entre dos estimaciones debe dividir estrictamente entre la constante entera N=2:"))
        body.append(create_p("Volatilidad media = (x1 + x2) / 2 = (0,10 + 0,10) / 2 = 0,10 (10%)."))
        body.append(create_p("Riesgo Diario Real = Inversión * Volatilidad media = 1.000M$ * 0,10 = 100 millones de dólares."))
        body.append(create_p("Al corregir el divisor con la constante 2, la función recupera su derivada estrictamente positiva (f'(x) > 0), garantizando que cuando aumente la inestabilidad del mercado, el modelo alerte del peligro."))

        # 7. Conclusión del Auditor
        body.append(create_heading("7. CONCLUSIÓN DEL AUDITOR: LO QUE HEMOS APRENDIDO", level=2))
        body.append(create_p("Este caso une directamente mis estudios previos en DAM (programación) con mis estudios actuales en ADE:"))
        body.append(create_p("1. Perspectiva DAM (Programación y Calidad de Software): El banco cometió la imprudencia de basar decisiones de miles de millones de dólares en una hoja de Excel artesanal sin control de versiones ni pruebas unitarias (Unit Tests). Con una sola línea de comprobación en código ('assert riesgo_calculado == 100'), el ordenador habría detectado el error al instante y habría impedido su uso."))
        body.append(create_p("2. La alternativa moderna (Palantir Foundry / Data Pipelines): En la actualidad, las grandes empresas y bancos evitan las hojas de cálculo manuales y emplean plataformas de datos donde los cálculos son automáticos, están verificados por programadores y no dependen de que una persona escriba una fórmula en una celda."))
        body.append(create_p("3. Perspectiva ADE (Dirección de Empresas y Control Interno): Los directivos no deben fiarse a ciegas de una cifra solo porque aparezca en una hoja de cálculo o la arroje un ordenador. Quienes gestionan empresas deben auditar y comprender las operaciones elementales de las que dependen sus decisiones estratégicas."))

        if sectPr is not None:
            body.append(sectPr)
            
        new_xml = ET.tostring(root, encoding='utf-8', xml_declaration=True)

    with zipfile.ZipFile(TEMPLATE_DOCX, 'r') as zin:
        with zipfile.ZipFile(OUTPUT_DOCX, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                if item.filename == 'word/document.xml':
                    zout.writestr(item, new_xml)
                else:
                    zout.writestr(item, zin.read(item.filename))
                    
    print(f"[OK] Ficha Word simplificada generada con éxito en: {OUTPUT_DOCX}")

if __name__ == "__main__":
    generar_documento()
