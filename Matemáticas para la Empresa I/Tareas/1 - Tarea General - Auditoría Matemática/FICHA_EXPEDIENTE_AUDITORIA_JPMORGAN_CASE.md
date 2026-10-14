# 🏛️ FICHA DEL ALUMNADO: EXPEDIENTE DE AUDITORÍA MATEMÁTICA
## Caso: El Desastre de la Hoja de Cálculo de JPMorgan Chase (London Whale, 2012)

---

### 1. DATOS IDENTIFICATIVOS
- **Nombre y Apellidos:** Santiago [Tu Apellido]
- **Titulación:** Graduado en DAM (Desarrollo de Aplicaciones Multiplataforma) · Estudiante del Grado en ADE (Plan 2009)
- **Asignatura:** Matemáticas para la Empresa I (Cód. 2350)
- **Grupo:** Grupo 5 (Turno Tarde · Facultad de Economía y Empresa, Universidad de Murcia)
- **Docente Coordinadora:** Dña. Matilde Lafuente Lechuga
- **Fecha de Entrega:** 1 de diciembre de 2026

---

### 2. LA EVIDENCIA

- **Tipo de Fuente:**  
  `[X] Noticia` · `[X] Informe Corporativo / Oficial` · `[ ] Publicidad` · `[ ] Documento comercial` · `[ ] Otro`
- **Título o Descripción del Caso:**  
  *El error de cálculo de 6.200 millones de dólares: cómo un fallo en una fórmula de Excel de JPMorgan dividió entre la suma en lugar de hacer una media, reduciendo el riesgo a la mitad.*
- **Fuente Oficial y Medios de Comunicación:**  
  1. **Informe Oficial del Senado de EE. UU.:** *United States Senate Permanent Subcommittee on Investigations: "JPMorgan Chase Whale Trades: A Case History on Derivatives Risks and Regulatory Deficiency"* (2013).  
  2. **Informe de Auditoría Interna de JPMorgan:** *Report of JPMorgan Chase & Co. Management Task Force Regarding 2012 CIO Losses* (16 de enero de 2013).  
  3. **Prensa Económica:** *Financial Times* (*"Spreadsheet mistake helped cause JPMorgan's £4bn loss"*) y *The Wall Street Journal* (*"JPMorgan's Value-at-Risk Model Was Flawed"*).
- **Fecha del Suceso / Publicación:** Enero de 2012 (implementación del modelo) – Enero de 2013 (informe de investigación).
- **Enlace o Referencia Documental:**  
  *U.S. Senate Hearing on CIO Losses (Exhibit 103)* y *JPMorgan Management Task Force Report, p. 128*.

#### Fragmento Textual de la Evidencia (Transcripción Oficial del Informe)
> *"El modelo funcionaba a través de una serie de hojas de cálculo de Excel que se completaban manualmente, copiando y pegando datos de una hoja a otra... La fórmula de la hoja de cálculo utilizada para calcular el riesgo neto de la posición cometió un error operativo crítico: en lugar de dividir por el promedio de dos métricas, dividió por su suma. Como resultado, el modelo redujo artificialmente la volatilidad estimada, disminuyendo el riesgo reportado aproximadamente en un 50% y ocultando la enorme exposición acumulada."*  
> — **JPMorgan Chase Management Task Force Report (2013), p. 128.**

---

### 3. ¿QUÉ AFIRMA LA FUENTE?

A principios de 2012, el departamento de inversiones de JPMorgan (*Chief Investment Office*, CIO) puso en marcha una nueva hoja de cálculo para medir el riesgo diario de sus inversiones financieras. 

El modelo arrojaba un resultado según el cual el riesgo de la cartera había descendido drásticamente respecto al año anterior. Respaldados por esta cifra, los gestores (entre ellos el operador conocido en la prensa como *"The London Whale"*) decidieron aumentar agresivamente sus operaciones, creyendo firmemente que sus posiciones estaban muy por debajo de los límites de riesgo permitidos por la dirección del banco y los reguladores financieros.

En la realidad, el riesgo real no había bajado en absoluto: **se había duplicado**. La supuesta tranquilidad era un error puramente aritmético cometido por el analista al programar la celda en Excel.

---

### 4. TÉRMINO MATEMÁTICO QUE PRESENTA EL PROBLEMA

1. **Media aritmética simple vs. División por la suma (Aritmética básica - Tema 0):**  
   Confusión en el divisor entre el número de elementos ($N = 2$) y el valor de la suma de los propios datos.
2. **Funciones de una variable: Funciones crecientes vs. decrecientes y signo de la derivada (Tema 1):**  
   - Una función de riesgo debe ser **estrictamente creciente** respecto a la volatilidad del mercado (su primera derivada debe ser positiva: $f'(x) > 0$).
   - Al introducir la variable en el denominador, el error convirtió la función en **decreciente** (derivada negativa: $g'(x) < 0$), haciendo que a más riesgo real en el mercado, el modelo calculara menor riesgo en pantalla.
3. **Porcentajes y magnitudes proporcionales (Tema 0).**

---

### 5. DIAGNÓSTICO MATEMÁTICO: EXPLICACIÓN PASO A PASO CON NÚMEROS REALES

#### A. El Cálculo Teórico Correcto (Hacer la Media)
Imaginemos que tenemos dos estimaciones de volatilidad del mercado obtenidas de dos periodos distintos:
- Primera estimación: $x_1 = 10\% = 0{,}10$
- Segunda estimación: $x_2 = 10\% = 0{,}10$

El método correcto exige calcular el **promedio simple** (la media aritmética entre ambas cifras):
$$\text{Promedio correcto} = \frac{x_1 + x_2}{2} = \frac{0{,}10 + 0{,}10}{2} = \frac{0{,}20}{2} = \mathbf{0{,}10 \quad (10\%)}$$

Si el banco tiene una inversión de $1.000$ millones de dólares, el riesgo estimado al $10\%$ es:
$$\text{Riesgo Real} = 1.000 \times 10\% = \mathbf{100 \text{ millones de dólares}}$$

#### B. El Error Cometido en la Celda de Excel (Dividir por la Suma)
En lugar de escribir un $2$ fijo en el denominador, el analista programó la fórmula en Excel dividiendo entre la suma $(x_1 + x_2)$:
$$\text{Fórmula errónea de Excel} = \frac{x_1 \cdot x_2}{x_1 + x_2} = \frac{0{,}10 \cdot 0{,}10}{0{,}10 + 0{,}10} = \frac{0{,}01}{0{,}20} = \mathbf{0{,}05 \quad (5\%)}$$

Con este fallo, el riesgo estimado que apareció en la pantalla del banco fue:
$$\text{Riesgo Reportado por Excel} = 1.000 \times 5\% = \mathbf{50 \text{ millones de dólares}}$$

**¡El error matemático hizo desaparecer el 50% del riesgo real!**  
Los directivos pensaban que su riesgo máximo era de 50 millones, cuando en realidad se estaban jugando 100 millones.

#### C. Demostración con la Primera Derivada (Tema 1: Crecimiento y Decrecimiento)
Para comprender la gravedad del fallo desde el punto de vista del cálculo de funciones:

* **Función que debería tener el modelo:**  
  Si llamamos $x$ a la volatilidad del mercado y $K$ al volumen de inversión ($K > 0$):
  $$f(x) = K \cdot x$$
  Calculamos su derivada respecto a la volatilidad:
  $$f'(x) = K > 0$$
  Como la derivada es positiva en todo su dominio, la función es **estrictamente creciente**. Es decir: *si la inestabilidad del mercado ($x$) sube, el riesgo medido ($f(x)$) también sube*.

* **Función resultante del error en Excel:**  
  Al colocar la variable de volatilidad en el denominador dividiendo a la exposición:
  $$g(x) = \frac{K}{x} = K \cdot x^{-1}$$
  Calculamos su derivada:
  $$g'(x) = -K \cdot x^{-2} = -\frac{K}{x^2} < 0$$
  Como el cuadrado $x^2 > 0$ y $K > 0$, la derivada es **estrictamente negativa**.  
  **La aberración matemática:** La función se convirtió en **decreciente**. Cuando el mercado entraba en crisis y la volatilidad crecía, la fórmula de Excel arrojaba un número cada vez menor, diciendo que "había menos riesgo" en el peor momento posible.

---

### 6. NIVEL DE GRAVEDAD DEL ERROR

- **Calificación:**  
  `[X] Error grave: puede afectar de forma importante a una decisión económica o empresarial.`

- **Justificación Económica y Empresarial (Enfoque ADE):**  
  Este fallo aritmético provocó el mayor quebranto operativo por error de software de la historia bancaria:
  1. **Pérdida Directa:** JPMorgan perdió **6.200 millones de dólares** ($6.2B) en su balance.
  2. **Multas Regulatorias:** Sanciones por más de **1.000 millones de dólares** impuestas por la SEC y los reguladores británicos (FCA).
  3. **Dimisiones y Reputación:** Destitución de los máximos responsables de inversión y una caída inmediata del 15% en el valor de las acciones del banco.

---

### 7. ENUNCIADO Y PROCEDIMIENTO CORRECTO

- **Enunciado Correcto:**  
  Para promediar dos estimaciones de volatilidad ($x_1$ y $x_2$), el divisor debe ser una constante entera correspondiente al número de observaciones ($N = 2$), nunca la suma de las variables:
  $$\bar{x} = \frac{x_1 + x_2}{2}$$

- **Procedimiento Numérico Corregido:**
  $$\text{Volatilidad Corregida} = \frac{0{,}10 + 0{,}10}{2} = 0{,}10 \quad (10\%)$$
  $$\text{Riesgo Diario Real} = \text{Posición} \times \bar{x} = 1.000\,\text{M\$} \times 0{,}10 = \mathbf{100\,\text{M\$}}$$
  El procedimiento correcto restablece la condición de que la derivada sea positiva ($f'(x) > 0$), garantizando que el modelo alerte del peligro cuando el mercado se vuelve inestable.

---

### 8. CONCLUSIÓN DEL AUDITOR: LO QUE HEMOS APRENDIDO

Este caso ilustra tres lecciones clave que unen mi formación previa en **DAM (programación)** con mis estudios actuales en **ADE (gestión de empresas)**:

1. **La lección de DAM (Programación y Calidad de Código):**  
   El banco confió decisiones de miles de millones de dólares a una simple hoja de cálculo de Excel mantenida sin controles. En el desarrollo de software profesional esto es inaceptable:
   - No había control de versiones (`git`).
   - No había separación de datos y lógica.
   - **No había pruebas unitarias (`Unit Tests`):** Con una sola línea de código de comprobación (`assert riesgo_calculado >= 100`), el sistema informático habría detectado el error y habría impedido su uso de inmediato.

2. **La alternativa moderna: Palantir Foundry y Pipelines de Datos:**  
   Hoy en día, las grandes corporaciones y bancos sustituyen las hojas de cálculo manuales por plataformas como **Palantir Foundry**, donde las operaciones matemáticas son automáticas, están testeadas por ingenieros y no dependen de que una persona escriba una fórmula a mano en una celda de Excel.

3. **La lección de ADE (Dirección de Empresas y Control Interno):**  
   Los directivos nunca deben aceptar una cifra como válida solo porque "lo dice el ordenador" o "viene de un modelo matemático". La dirección debe entender las hipótesis básicas y auditar los cálculos, porque un error aritmético elemental puede poner en quiebra a la empresa.
