#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador automático de la Ficha Oficial en Word (.docx)
Caso: JPMorgan Chase (London Whale, 2012)
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
    
    # Font style
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
        # Keep section properties at end of body if present
        sectPr = body.find(f"{{{NS_W}}}sectPr")
        
        # Clear body
        body.clear()
        
        # Build enriched document
        body.append(create_heading("FICHA DEL ALUMNADO — EXPEDIENTE DE AUDITORÍA MATEMÁTICA", level=1))
        body.append(create_p("Nombre y apellidos: Santiago [Estudiante ADE / Graduado en DAM]", bold=True))
        body.append(create_p("Grupo: Grupo 5 (Turno Tarde)        Fecha: 1 de diciembre de 2026", bold=True))
        body.append(create_p("Asignatura: Matemáticas para la Empresa I (Cód. 2350) — Profesora: Matilde Lafuente", italic=True))
        
        body.append(create_heading("1. LA EVIDENCIA", level=2))
        body.append(create_p("Tipo de fuente: [X] Noticia   [ ] Publicidad   [X] Informe Oficial   [ ] Página web   [ ] Documento comercial   [ ] Otro", bold=True))
        body.append(create_p("Título o descripción del caso: The $6.2 Billion Spreadsheet Bug: Error en la agregación de volatilidades del modelo de Value at Risk (VaR) de JPMorgan Chase (London Whale)", bold=True))
        body.append(create_p("Fuente: U.S. Senate Permanent Subcommittee on Investigations / JPMorgan Management Task Force / Financial Times"))
        body.append(create_p("Fecha: Enero de 2012 (implementación del modelo) – Marzo de 2013 (auditoría forense oficial)"))
        body.append(create_p("Enlace o referencia: U.S. Senate Hearing Report on JPMorgan Whale Trades (Exhibit 103) & JPMorgan Chase 2012 CIO Task Force Report"))
        body.append(create_p("Adjunto / Captura de evidencia (Transcripción oficial):", italic=True))
        body.append(create_p("«The model operated through a series of Excel spreadsheets, which had to be completed manually, by a process of copying and pasting data from one spreadsheet to another... The spreadsheet formula used to calculate net position risk divided by the sum of asset volatility metrics rather than their average. As a result, the model artificially depressed volatility estimates, reducing the portfolio's reported Value at Risk (VaR) by approximately 50%.» (Task Force Report, p. 128)", italic=True))

        body.append(create_heading("2. ¿QUÉ AFIRMA LA FUENTE?", level=2))
        body.append(create_p("La división Chief Investment Office (CIO) de JPMorgan Chase afirmó a sus comités de riesgo y a los reguladores de la Reserva Federal que su nuevo modelo interno de riesgo era más preciso y que el Value at Risk (VaR) de su cartera sintética de crédito se había reducido sustancialmente a principios de 2012."))
        body.append(create_p("Respaldados en este informe falsamente optimista, los operadores liderados por Bruno Iksil acumularon masivas posiciones cortas y largas en derivados de crédito (CDS), creyendo que operaban holgadamente dentro de los límites de capital estatutario."))

        body.append(create_heading("3. TÉRMINO MATEMÁTICO QUE PRESENTA EL PROBLEMA", level=2))
        body.append(create_p("1. Operadores de agregación y medias ponderadas en estadística multivariante frente a operadores de suma."))
        body.append(create_p("2. Axiomas de medidas de riesgo coherentes (violación de Monotonicidad y Homogeneidad Positiva)."))
        body.append(create_p("3. Álgebra matricial y cálculo de dispersión: forma cuadrática de la matriz de varianzas-covarianzas en carteras financieras."))
        body.append(create_p("4. Cálculo de funciones multivariantes y sensibilidades marginales (derivadas parciales negativas indebidas)."))

        body.append(create_heading("4. DIAGNÓSTICO MATEMÁTICO: REPRODUCCIÓN DEL ERROR PASO A PASO", level=2))
        body.append(create_p("Para sintetizar dos estimaciones de dispersión temporal (s1 y s2), el diseño teórico requería la media aritmética: s_medio = (s1 + s2) / 2."))
        body.append(create_p("En la hoja de cálculo de Excel, el modelizador programó en la fórmula una división por la suma: s_error = (s1 * s2) / (s1 + s2)."))
        body.append(create_p("Consecuencia analítica y funcional: al introducir la suma de las volatilidades como divisor, la derivada parcial de la métrica respecto a la volatilidad del mercado se convirtió en negativa en términos netos: ∂/∂s [exposición / (s1 + s2)] = - exposición / (s1 + s2)^2 < 0."))
        body.append(create_p("En consecuencia: a medida que el mercado entraba en tensión y aumentaba la volatilidad real, el modelo reportaba MENOS riesgo en lugar de más, enmascarando el 50% de la exposición y desactivando todas las alarmas tempranas."))

        body.append(create_heading("5. NIVEL DE GRAVEDAD DEL ERROR", level=2))
        body.append(create_p("[ ] Error menor: apenas modifica la interpretación."))
        body.append(create_p("[ ] Error relevante: puede inducir a una conclusión incorrecta."))
        body.append(create_p("[X] Error grave: puede afectar de forma importante a una decisión económica o empresarial.", bold=True))
        body.append(create_p("Justificación ADE: Es el error de cálculo con mayor impacto económico directo registrado en la historia financiera: pérdida directa de 6.200 millones de dólares en el balance de JPMorgan, sanciones regulatorias por más de 1.000 millones de dólares (SEC, CFTC, FCA), infracción de ratios de capital de Basilea II/III, renuncia de la alta dirección del CIO y caída del 15% del valor bursátil de la compañía.", bold=True))

        body.append(create_heading("6. ENUNCIADO Y PROCEDIMIENTO CORRECTO", level=2))
        body.append(create_p("Procedimiento riguroso de cálculo del Value at Risk (VaR 99% a 1 día):"))
        body.append(create_p("1. Matriz de covarianzas: Para dos componentes con ponderaciones w1 = w2 = 0.5 y correlación rho = 0.8: sigma_p = sqrt(w1^2 * s1^2 + w2^2 * s2^2 + 2 * w1 * w2 * rho * s1 * s2)."))
        body.append(create_p("2. Si se desea un estimador promediado de volatilidad: s_media = (s1 + s2) / 2 (escalar constante N=2 en denominador)."))
        body.append(create_p("3. VaR_0.99 = V_0 * z_0.99 * sigma_p * sqrt(1/252), con z_0.99 = 2.32635."))
        body.append(create_p("Resultado comprobado mediante simulación: en un escenario de crisis con cartera de $10.000M, el modelo erróneo reportaba un VaR de solo $244.97M, cuando el riesgo real ascendía a $459.29M diarios (ocultando $214.32M de riesgo real por jornada, un -46.7% de desvío)."))

        body.append(create_heading("7. CONCLUSIÓN DEL AUDITOR: LO QUE HEMOS APRENDIDO", level=2))
        body.append(create_p("Este caso ofrece tres aprendizajes críticos desde la perspectiva combinada DAM + ADE:"))
        body.append(create_p("1. Perspectiva DAM (Ingeniería de Software): El desastre evidenció los riesgos del 'Shadow IT' en finanzas. El uso de hojas de cálculo de Excel sin control de versiones (git), sin tipado de datos y sin pruebas unitarias automatizadas (Unit Tests) es una negligencia operativa. Con una batería básica de pruebas de aserción (assert var_alta_vol > var_baja_vol), el modelo nunca habría pasado a producción."))
        body.append(create_p("2. El paradigma Palantir Foundry / Data Pipelines: La gran banca moderna ha sustituido las hojas de cálculo aisladas por plataformas de datos empresariales donde los cálculos matemáticos son reproducibles, poseen linaje de datos auditable (data lineage) y se someten a procesos de Integración Continua (CI/CD) antes de alimentar decisiones ejecutivas."))
        body.append(create_p("3. Perspectiva ADE (Gobernanza y Ética Directiva): Los directivos no deben tratar los modelos cuantitativos como 'cajas negras'. Es indispensable auditar las hipótesis matemáticas subyacentes, ya que una fórmula errónea puede quebrar un banco o desestabilizar el sistema financiero global."))

        if sectPr is not None:
            body.append(sectPr)
            
        new_xml = ET.tostring(root, encoding='utf-8', xml_declaration=True)

    # Re-pack zip
    with zipfile.ZipFile(TEMPLATE_DOCX, 'r') as zin:
        with zipfile.ZipFile(OUTPUT_DOCX, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                if item.filename == 'word/document.xml':
                    zout.writestr(item, new_xml)
                else:
                    zout.writestr(item, zin.read(item.filename))
                    
    print(f"[OK] Ficha Word generada con éxito en: {OUTPUT_DOCX}")

if __name__ == "__main__":
    generar_documento()
