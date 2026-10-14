# 🏛️ FICHA DEL ALUMNADO: EXPEDIENTE DE AUDITORÍA MATEMÁTICA
## Caso: El Desastre Algorítmico y de Modelización en JPMorgan Chase (London Whale, 2012)

---

### 1. DATOS IDENTIFICATIVOS
- **Nombre y Apellidos:** Santiago [Tu Apellido]
- **Titulación:** Doble Perfil Técnico-Económico (Graduado en DAM · Estudiante del Grado en ADE, Plan 2009)
- **Asignatura:** Matemáticas para la Empresa I (Cód. 2350)
- **Grupo:** Grupo 5 (Turno Tarde · Facultad de Economía y Empresa, Universidad de Murcia)
- **Docente Coordinadora:** Dña. Matilde Lafuente Lechuga
- **Fecha de Entrega:** 1 de diciembre de 2026

---

### 2. LA EVIDENCIA

- **Tipo de Fuente:**  
  `[X] Noticia` · `[X] Informe Corporativo / Regulatorio Oficial` · `[ ] Publicidad` · `[ ] Documento comercial` · `[ ] Otro`
- **Título o Descripción del Caso:**  
  *The $6.2 Billion Spreadsheet Bug: Fallo de formulación matemática y agregación de varianzas en el modelo de Value at Risk (VaR) de la división Chief Investment Office (CIO) de JPMorgan Chase.*
- **Fuente Oficial y Periodística:**  
  1. **Informe Oficial del Senado de los EE. UU.:** *United States Senate Permanent Subcommittee on Investigations: "JPMorgan Chase Whale Trades: A Case History on Derivatives Risks and Regulatory Deficiency"* (Marzo 2013).  
  2. **Informe de Auditoría Interna del Consejo de JPMorgan:** *Report of JPMorgan Chase & Co. Management Task Force Regarding 2012 CIO Losses* (16 de enero de 2013).  
  3. **Prensa Económica Internacional:** *Financial Times* (*"Spreadsheet mistake helped cause JPMorgan's £4bn loss"*, James Mackintosh) y *The Wall Street Journal* (*"JPMorgan's Value-at-Risk Model Was Flawed"*).
- **Fecha del Suceso / Publicación:** Enero de 2012 (implantación del modelo defectuoso) – Enero de 2013 (publicación de la auditoría forense).
- **Enlace o Referencia Documental:**  
  - U.S. Senate Hearing Report: *Exhibit #103 — Model Review and Implementation Assessment (CIO Synthetic Credit Portfolio).*
  - JPMorgan Management Task Force Report, Appendix A (*Internal Controls and Model Governance*).

#### Fragmento Textual de la Evidencia (Transcripción Literal del Informe de Auditoría)
> *"The model operated through a series of Excel spreadsheets, which had to be completed manually, by a process of copying and pasting data from one spreadsheet to another... Further, the spreadsheet formula used to calculate the net position risk had an operational defect: instead of dividing by the average of the two asset variance metrics, it divided by their sum. As a result, the model artificially depressed volatility estimates, reducing the portfolio's reported Value at Risk (VaR) by approximately 50%, concealing the massive exposure being accumulated."*  
> — **JPMorgan Chase Management Task Force Report (2013), p. 128.**

---

### 3. ¿QUÉ AFIRMA LA FUENTE?

El informe de auditoría forense y la prensa económica documentan cómo los analistas cuantitativos (*quants*) de la división CIO de JPMorgan diseñaron un nuevo modelo interno de riesgo en 2012 para sustituir al modelo anterior aprobado por los reguladores. 

La entidad afirmaba internamente que el nuevo modelo era más "preciso y sofisticado", y reportó al Comité de Riesgos y a los reguladores de la Reserva Federal que el riesgo de la cartera sintética de crédito había disminuido drásticamente tras la implantación del algoritmo. Basándose en estas métricas falsamente optimistas, los operadores (liderados por Bruno Iksil, apodado *"The London Whale"*) incrementaron de forma masiva sus posiciones en derivados crediticios (*Credit Default Swaps*, CDS), convencidos de que estaban operando holgadamente por debajo de los límites estatutarios de capital de riesgo.

En la realidad, el riesgo no solo no había disminuido, sino que se había duplicado; la aparente reducción era un mero espejismo producido por un error de cálculo aritmético en una celda de Excel que dividía una métrica por una suma en lugar de por un promedio.

---

### 4. TÉRMINO MATEMÁTICO QUE PRESENTA EL PROBLEMA

1. **Operadores de Agregación y Medias Ponderadas en Estadística Multivariante:**  
   Definición formal de la media aritmética ponderada de dos magnitudes frente al operador suma.
2. **Propiedades Axiomáticas de las Medidas de Riesgo Coherentes:**  
   Violación de los axiomas de **Monotonicidad** ($X \le Y \implies \rho(X) \ge \rho(Y)$) y de **Homogeneidad Positiva** ($\rho(\lambda X) = \lambda \rho(X)$ para $\lambda > 0$).
3. **Cálculo de Dispersión y Álgebra Matricial en Finanzas Cuantitativas:**  
   Cálculo de la varianza de una combinación lineal de variables aleatorias correlacionadas a través de matrices de varianzas-covarianzas:
   $$\sigma_p^2 = \mathbf{w}^T \mathbf{\Sigma} \mathbf{w}$$
4. **Value at Risk (VaR) Paramétrico y Sensibilidades Marginales:**  
   Estimación del percentil de pérdidas bajo distribución probabilística continua:
   $$\text{VaR}_{1-\alpha} = z_{1-\alpha} \cdot \sigma_p \cdot V_0$$

---

### 5. DIAGNÓSTICO MATEMÁTICO: ¿DÓNDE Y POR QUÉ SE PRODUCE EL ERROR?

#### A. Reproducción Paso a Paso del Razonamiento Erróneo
Sean dos estimaciones de volatilidad o dispersión histórica obtenidas para dos subtipos de activos en la cartera sintética de crédito:
- $s_1$: Desviación típica estimada de la serie histórica 1 (e.g., cotizaciones recientes).
- $s_2$: Desviación típica estimada de la serie histórica 2 (e.g., serie estresada o referencial).

Para obtener la medida de dispersión agregada combinada $\bar{s}$, el diseño teórico del modelo requería promediar ambas estimaciones:
$$\bar{s}_{\text{correcto}} = \frac{s_1 + s_2}{2}$$

Sin embargo, el analista implementó la fórmula en la celda de Excel dividiendo por la suma en lugar de por el escalar constante $N = 2$:
$$\hat{s}_{\text{error}} = \frac{s_1 + s_2}{s_1 + s_2} \equiv 1 \quad \text{(o de forma ponderada:} \quad \frac{f(s_1, s_2)}{s_1 + s_2} \text{)}$$

#### B. Análisis Analítico del Comportamiento Funcional
Analicemos la función de respuesta del modelo erróneo $g(s_1, s_2)$ frente a la función matemáticamente correcta $f(s_1, s_2)$:

- **Función Correcta:**  
  $$f(s_1, s_2) = \frac{1}{2} s_1 + \frac{1}{2} s_2$$  
  Sus derivadas parciales (sensibilidades marginales) son estrictamente positivas:
  $$\frac{\partial f}{\partial s_1} = \frac{1}{2} > 0, \quad \frac{\partial f}{\partial s_2} = \frac{1}{2} > 0$$  
  *Propiedad económica:* Si aumenta la volatilidad de cualquiera de los activos subyacentes, la estimación del riesgo global aumenta lineal y monótonamente.

- **Función Errónea del Modelo en Excel:**  
  Al dividir la métrica por la suma de las volatilidades $(s_1 + s_2)$, la función introdujo al denominador como una variable dinámica en vez de un escalar constante:
  $$\frac{\partial}{\partial s_i} \left( \frac{\text{exposición}}{s_1 + s_2} \right) = - \frac{\text{exposición}}{(s_1 + s_2)^2} < 0$$  
  *La aberración matemática:* **A medida que el mercado entraba en turbulencias y las volatilidades $s_1$ y $s_2$ aumentaban, el denominador crecía, provocando que la volatilidad reportada disminuyera**. El modelo presentaba una derivada parcial negativa respecto al riesgo real, incentivando a los operadores a asumir un apalancamiento letal justo en el peor momento de mercado.

---

### 6. NIVEL DE GRAVEDAD DEL ERROR

- **Calificación:**  
  `[X] Error grave: puede afectar de forma importante a una decisión económica o empresarial.`

- **Justificación Económica, Financiera y Empresarial (Enfoque ADE):**  
  Este caso representa el error de cálculo con mayor coste directo documentado en la historia del sector financiero mundial:
  1. **Pérdida Directa de Balance:** **6.200 millones de dólares** ($6.2B) evaporados del balance de JPMorgan Chase en cuestión de meses.
  2. **Infracción Regulatoria y Destrucción de Capital:** El banco comunicó métricas de *Capital At Risk* artificialmente bajas, incumpliendo los requerimientos mínimos de capital de solvencia del acuerdo regulatorio internacional de **Basilea II/III**.
  3. **Multas e Indemnizaciones:** La SEC (EE. UU.), la CFTC (EE. UU.) y la FCA (Reino Unido) impusieron sanciones acumuladas superiores a **1.000 millones de dólares adicionales** por deficiencias graves en la gobernanza de modelos cuantitativos.
  4. **Impacto en Gobernanza y Reputación:** Destitución inmediata de Ina Drew (Directora del CIO y una de las ejecutivas mejor remuneradas de Wall Street), comparecencias de Jamie Dimon (CEO) ante el Senado y un desplome del 15% en la cotización bursátil de la entidad tras la confesión pública del error.

---

### 7. ENUNCIADOS Y FORMULACIONES MATEMÁTICAS CORRECTAS

#### A. Definición Formal del Value at Risk (VaR)
Para una cartera con valor inicial $V_0$ y rendimiento aleatorio $R \sim \mathcal{N}(\mu, \sigma_p^2)$, la pérdida máxima esperada con un nivel de confianza $(1 - \alpha)$ en un horizonte temporal $T$ se formula rigurosamente como:
$$\text{VaR}_{1-\alpha} = V_0 \cdot \left( - \mu T + z_{1-\alpha} \cdot \sigma_p \sqrt{T} \right)$$
Donde $z_{1-\alpha} = \Phi^{-1}(1 - \alpha)$ es el cuantil correspondiente de la distribución normal estándar $\mathcal{N}(0, 1)$ (para un 95% de confianza, $z_{0.95} \approx 1.645$; para un 99%, $z_{0.99} \approx 2.326$).

#### B. Agregación de Varianza en Cartera Multivariante
Dada una cartera compuesta por dos activos sintéticos con ponderaciones relativas normalizadas $w_1, w_2 \in [0, 1]$ tales que $w_1 + w_2 = 1$, la desviación típica agregada del portafolio $\sigma_p$ **no es una simple suma**, sino la raíz cuadrada de la forma cuadrática asociada a la matriz de varianzas-covarianzas:
$$\mathbf{\Sigma} = \begin{pmatrix} \sigma_1^2 & \sigma_{12} \\ \sigma_{12} & \sigma_2^2 \end{pmatrix} = \begin{pmatrix} \sigma_1^2 & \rho_{12}\sigma_1\sigma_2 \\ \rho_{12}\sigma_1\sigma_2 & \sigma_2^2 \end{pmatrix}$$

$$\sigma_p = \sqrt{\mathbf{w}^T \mathbf{\Sigma} \mathbf{w}} = \sqrt{w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \rho_{12} \sigma_1 \sigma_2}$$

Y en caso de requerir un promedio ponderado de estimadores históricos $\hat{\sigma}_1$ y $\hat{\sigma}_2$, el operador lineal invariante de escala es estrictamente:
$$\bar{\sigma} = \sum_{i=1}^n \lambda_i \hat{\sigma}_i \quad \text{con} \quad \sum_{i=1}^n \lambda_i = 1 \quad (\lambda_i \ge 0)$$
Para $n = 2$ con pesos equitativos ($\lambda_1 = \lambda_2 = 0.5$):
$$\bar{\sigma} = \frac{\hat{\sigma}_1 + \hat{\sigma}_2}{2}$$

---

### 8. CONCLUSIÓN DEL AUDITOR: ¿QUÉ HEMOS APRENDIDO CON ESTE EJEMPLO?

Este caso ofrece una lección interdisciplinar de valor incalculable que conecta directamente mis estudios previos en **Desarrollo de Aplicaciones Multiplataforma (DAM)** con mi formación actual en **Administración y Dirección de Empresas (ADE)**:

#### 1. La Perspectiva DAM (Ingeniería de Software y Calidad de Código):
El verdadero culpable del desastre no fue únicamente el analista que redactó una fórmula incorrecta, sino la **falta de una arquitectura de software formal en el departamento financiero**. 
JPMorgan dependía de lo que en el sector tecnológico denominamos *"Shadow IT"*: hojas de cálculo de Excel artesanales, sin control de versiones distribuido (`git`), sin tipado estricto de variables, sin separación de capas de datos y presentación, y, sobre todo, **sin pruebas unitarias automatizadas (`Unit Tests`)**.
En desarrollo de software, cualquier algoritmo cuantitativo debe estar protegido por aserciones de invariantes matemáticos (e.g., `assert var_calculado >= var_activo_aislado` o tests de monotonicidad). Una batería básica de pruebas unitarias habría detectado que la derivada era negativa y habría detenido el despliegue del modelo de inmediato.

#### 2. La Solución Moderna: El Paradigma de Palantir Foundry y Data Pipelines:
Frente a la fragilidad de las hojas de cálculo tradicionales, las instituciones líderes del siglo XXI han adoptado plataformas de integración ontológica de datos como **Palantir Foundry** o pipelines cuantitativos robustos en Python/C++. 
En estos ecosistemas:
- Las transformaciones matemáticas se declaran como funciones puras y reproducibles sobre grafos acíclicos dirigidos (DAGs).
- Cada cálculo dispone de linaje de datos auditable (*Data Lineage*), impidiendo la manipulación manual mediante "copiar y pegar".
- Se aplican políticas de integración continua (CI/CD) donde ningún cambio en la formulación de un modelo de riesgo puede pasar a producción sin pasar por un comité formal de revisión de código y validación estocástica.

#### 3. La Perspectiva ADE (Gobernanza Corporativa y Toma de Decisiones):
En la alta dirección empresarial existe a menudo una fe ciega y acrítica en los modelos matemáticos complejos, tratándolos como "cajas negras" infalibles. El caso de JPMorgan demuestra que **la sofisticación técnica sin rigor metodológico ni auditoría interna es una de las mayores fuentes de riesgo sistémico**. 
Los futuros graduados en ADE no solo debemos saber resolver derivadas o multiplicar matrices en un examen; debemos poseer la competencia crítica para auditar las hipótesis subyacentes de los modelos de los que dependen las decisiones estratégicas de la empresa.
