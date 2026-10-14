# 🔍 1.ª Tarea General: Auditoría de Errores Matemáticos en Situaciones Reales

- **Asignatura:** [Matemáticas para la Empresa I](../../README.md) (Cód. 2350)
- **Titulación:** Grado en Administración y Dirección de Empresas (Plan 2009) — UMU
- **Profesorado:** Matilde Lafuente Lechuga ([mati@um.es](mailto:mati@um.es))
- **Modalidad:** Trabajo individual / Actividad de Evaluación Continua
- **📅 Fecha Límite de Entrega:** **Martes, 1 de diciembre de 2026** (a través de la tarea habilitada en el Aula Virtual)

---

## 🎯 Finalidad y Objetivos de la Actividad

Esta actividad tiene como finalidad que el alumnado aprenda a **detectar errores matemáticos en los medios de comunicación, publicidad, prensa económica o informes corporativos**, desarrollando una mirada crítica, analítica y ética sobre el uso de los conceptos propios de las matemáticas en el entorno económico y empresarial.

### 📌 Objetivos Específicos:
1. **Aplicar los conocimientos matemáticos** adquiridos en la asignatura a situaciones reales del ámbito económico, empresarial y cotidiano.
2. **Validar y contrastar razonamientos y cálculos** presentes en fuentes y documentos reales.
3. **Identificar errores frecuentes** vinculados a cálculo diferencial (derivadas, pendientes, crecimiento), tasas de variación porcentual, inflación, proporciones, escalas o magnitudes financieras.
4. **Fomentar el rigor y el pensamiento crítico** ante la manipulación o confusión de términos cuantitativos.
5. **Argumentar con precisión técnica**, justificando formalmente la incorrección y proponiendo la formulación matemática exacta.
6. **Relacionar la calidad de la información numérica** con la toma de decisiones empresariales y financieras.

---

## 📂 Materiales y Documentos Disponibles en esta Carpeta

### 🏛️ Propuesta Oficial Realizada: *Caso JPMorgan Chase (London Whale, 2012)*
*Enfoque interdisciplinar de máximo nivel combinando Grado Superior en DAM, ADE, Matemáticas para la Empresa I y el paradigma de plataformas de datos seguras (Palantir Foundry).*

| Documento | Tipo | Descripción |
| :--- | :---: | :--- |
| 📄 **[FICHA_EXPEDIENTE_AUDITORIA_JPMORGAN_CASE.md](./FICHA_EXPEDIENTE_AUDITORIA_JPMORGAN_CASE.md)** | **Markdown Oficial** | **Expediente completo resuelto con aparato crítico, citas oficiales del Senado y JPMorgan, fórmulas LaTeX y reflexión DAM/ADE.** |
| 📘 **[Ficha_Auditoria_Matematica_RESUELTA_JPMorgan.docx](./Ficha_Auditoria_Matematica_RESUELTA_JPMorgan.docx)** | **Word (.docx)** | **Documento Word oficial cumplimentado y maquetado con estilo profesional listo para subir al Aula Virtual.** |
| 💻 **[auditoria_jpmorgan_simulacion.py](./auditoria_jpmorgan_simulacion.py)** | **Python (DAM)** | **Script ejecutable con simulación cuantitativa de carteras de $10.000M y suite de pruebas unitarias (`unittest`) de propiedades axiomáticas de riesgo.** |
| ⚙️ **[generar_ficha_word.py](./generar_ficha_word.py)** | Script Auxiliar | Generador automático que inyecta los datos en la plantilla Word preservando la estructura XML nativa. |

---

### 📚 Documentación Base del Aula Virtual
| Documento | Tipo | Descripción |
| :--- | :---: | :--- |
| 📕 **[TAREA AUDITORIA MATEMÁTICAS.pdf](./TAREA%20AUDITORIA%20MATEM%C3%81TICAS.pdf)** | PDF Oficial | Enunciado completo de la actividad, ficha en blanco y rúbrica oficial de evaluación de la UMU. |
| 📝 **[Ficha Auditoria Matemática.docx](./Ficha%20Auditoria%20Matem%C3%A1tica.docx)** | Word (.docx) | Plantilla editable en blanco original de la profesora Matilde Lafuente. |
| 🔍 **[Ficha Auditoria Matemática con DERIVADAS.pdf](./Ficha%20Auditoria%20Matem%C3%A1tica%20con%20DERIVADAS.pdf)** | Caso Ejemplo | Modelo de referencia previo de la profesora analizando el artículo de *Cinco Días* (*"Las derivadas de la realidad"*). |

---

### 💡 Síntesis del Caso JPMorgan Resuelto (Matemáticas Accesibles de 1.º de ADE)
- **El Fallo Aritmético (Tema 0):** Para dos volatilidades del $10\%$ ($x_1 = 0{,}10, x_2 = 0{,}10$), la media aritmética correcta es $\frac{x_1 + x_2}{2} = 10\%$. En Excel dividieron por la suma $(x_1 + x_2)$, obteniendo $\frac{0{,}10 \times 0{,}10}{0{,}20} = 5\%$. ¡El modelo ocultó la mitad del riesgo ($50\%$)!
- **La Derivada (Tema 1):** La función de riesgo correcta $f(x) = K \cdot x$ tiene derivada positiva $f'(x) = K > 0$ (creciente). La función errónea $g(x) = \frac{K}{x}$ tiene derivada negativa $g'(x) = -\frac{K}{x^2} < 0$ (decreciente: al aumentar el pánico del mercado, el modelo decía que había menos riesgo).
- **El Impacto Empresarial (ADE):** Pérdida de $6.200M USD y multas de más de $1.000M.
- **La Solución Informática (DAM / Palantir):** Sustituir hojas de cálculo manuales no testeadas por pipelines de datos empresariales con pruebas unitarias (`assert`).

---

## 📋 Estructura Obligatoria de la Ficha del Alumnado

La entrega debe realizarse rellenando la **Ficha del Alumnado** ([Ficha Auditoria Matemática.docx](./Ficha%20Auditoria%20Matem%C3%A1tica.docx)), la cual contiene las siguientes secciones:

### 1. Datos Identificativos
- **Nombre y apellidos:**
- **Grupo:** Grupo 5 (Subgrupo A / B)
- **Fecha:**

### 2. La Evidencia
- **Tipo de fuente:** `[ ] Noticia` · `[ ] Publicidad` · `[ ] Informe` · `[ ] Página web` · `[ ] Documento comercial` · `[ ] Otro`
- **Título o descripción del caso:** Titular exacto del artículo o campaña analizada.
- **Fuente:** Medio de comunicación o entidad emisora (ej. *El País*, *Cinco Días*, *Expansión*, informe del Banco de España, etc.).
- **Fecha de publicación:**
- **Enlace o referencia bibliográfica / digital:**
- **Fragmento adjunto:** Captura de pantalla, recorte de prensa o imagen que demuestre la afirmación.

### 3. ¿Qué afirma la fuente?
- Transcripción textual y entrecomillada del párrafo o gráfico donde reside el fallo o la ambigüedad matemática.

### 4. Término Matemático que Presenta el Problema
- Concepto(s) teóricos afectados (p. ej., *Derivada*, *Tasa de variación*, *Inflación*, *Pendiente de la recta tangente*, *Extremo relativo*, *Elasticidad*, etc.).

### 5. Diagnóstico Matemático
- Desglose y numeración detallada de los errores detectados:
  - Distinguir entre imprecisiones terminológicas, errores de cálculo aritmético, confusión entre magnitudes absolutas y relativas, o falacias lógicas en la interpretación matemática.

### 6. Nivel de Gravedad del Error
Marcar una casilla y redactar una justificación económica/empresarial:
- `[ ] Error menor:` Apenas modifica la interpretación del dato.
- `[ ] Error relevante:` Puede inducir a una conclusión errónea en el lector o inversor.
- `[ ] Error grave:` Puede afectar de forma severa a una decisión económica, de inversión o política empresarial.

### 7. Enunciados Correctos
- Reescribir las frases de forma rigurosa y matemáticamente impecable (utilizando las hipótesis correctas: existencia de límite, derivabilidad, definición de tasa porcentual, etc.).

### 8. ¿Qué hemos aprendido con este ejemplo?
- Reflexión crítica final y conclusión pedagógica sobre el caso auditado.

---

## 📊 Rúbrica Oficial de Evaluación

Cada criterio se califica de **1 a 4 puntos** según el siguiente baremo:

| Criterio | 🌟 Excelente (4) | 👍 Bien (3) | ⚠️ Suficiente (2) | ❌ Insuficiente (1) |
| :--- | :--- | :--- | :--- | :--- |
| **1. Selección de la evidencia** | Caso real muy adecuado, actual y 100% verificable. | Caso adecuado con fuentes accesibles. | Caso con información o contexto limitado. | Caso poco adecuado, inventado o no verificable. |
| **2. Reconstrucción matemática** | Completa, formal, rigurosa y con simbología clara. | Correcta con pequeñas omisiones de notación. | Parcial o poco clara. | Incorrecta o ausente. |
| **3. Diagnóstico del error** | Identifica con absoluta precisión la raíz teórica y justifica el fallo. | Identifica correctamente el error general. | Detecta parcialmente el problema sin profundizar. | No identifica o diagnostica erróneamente el fallo. |
| **4. Corrección propuesta** | Procedimiento y resultado totalmente exactos y fundamentados. | Corrección esencialmente correcta. | Presenta imprecisiones o errores menores. | Corrección incorrecta o sin justificación matemática. |
| **5. Argumentación** | Muy clara, rigurosa, convincente y con léxico económico-matemático. | Clara, ordenada y adecuada. | Limitada o superficial. | Confusa, incoherente o ausente. |
| **6. Consecuencias y aplicación** | Vincula con gran madurez el error con decisiones directivas/financieras reales. | Relación clara con el ámbito empresarial. | Relación superficial con el impacto económico. | Sin relación alguna con la realidad de la empresa. |
| **7. Presentación** | Muy ordenada, impecable, maquetación profesional y sin erratas. | Clara, legible y estructurada. | Mejorable o descuidada en formato. | Desordenada, ilegible o difícil de seguir. |

---

## 💡 Ejemplo Resuelto de Referencia (Derivadas)

En el documento [Ficha Auditoria Matemática con DERIVADAS.pdf](./Ficha%20Auditoria%20Matem%C3%A1tica%20con%20DERIVADAS.pdf) se analiza un caso real publicado por el diario *Cinco Días*:

- **Titular analizado:** *"La caja de Inditex y las derivadas de la realidad"* (8 de junio de 2023).
- **Afirmación errónea de la prensa:**
  1. *"En matemáticas, la derivada es la pendiente de una curva..."*
  2. *"...aunque los datos en sí sean muy negativos, si están subiendo, su derivada es positiva."*
  3. *"La inflación, por ejemplo, es una derivada: es la velocidad a la que suben o bajan los precios..."*
- **Diagnóstico del error:**
  - **Error 1:** La derivada en un punto es la pendiente de la *recta tangente* a la gráfica de la función en dicho punto, no la pendiente de "una curva" arbitraria.
  - **Error 2:** Exige la condición previa de que la función que modeliza los datos económicos sea **derivable** en dicho intervalo o punto.
  - **Error 3:** Confusión conceptual: la inflación es una **tasa de variación porcentual** discreta de un índice de precios (IPC) entre dos periodos temporales, no un límite infinitesimal (derivada continua).
- **Gravedad asignada:** **Error Relevante**, puesto que altera la comprensión pública de indicadores macroeconómicos esenciales.

---

## ⏰ Instrucciones de Entrega

1. Descargar la plantilla: [Ficha Auditoria Matemática.docx](./Ficha%20Auditoria%20Matem%C3%A1tica.docx).
2. Cumplimentar todas las secciones asegurando la máxima puntuación según la rúbrica.
3. Exportar a formato **PDF** antes de subir la entrega definitiva para garantizar que las capturas y ecuaciones mantengan su formato.
4. Subir al buzón de entrega en el **Aula Virtual de la Universidad de Murcia** antes del **1 de diciembre de 2026 a las 23:59 h**.
