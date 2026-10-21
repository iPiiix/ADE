# 📐 Matemáticas para la Empresa I — Tema 3: Derivación y Optimización de Funciones de una Variable

- **Asignatura:** Matemáticas para la Empresa I (Cód. 2350)
- **Titulación:** Grado en ADE — Facultad de Economía y Empresa (Universidad de Murcia)
- **Profesora Coordinadora:** Matilde Lafuente Lechuga ([mati@um.es](mailto:mati@um.es))
- **Grupos:** 1 y 5 (Curso 2026-2027)
- **Material Oficial:** [📄 Tema 3. Derivación de funciones de una variable (PDF)](./Tema_03_Derivacion_Funciones_Una_Variable.pdf) · [📝 Relación de Ejercicios 3 (PDF)](../Prácticas/Relacion3-26-27.pdf)

---

## 📑 Índice de Contenidos

1. [Tasa de Cambio y Concepto de Derivada en un Punto](#1-tasa-de-cambio-y-concepto-de-derivada-en-un-punto)
   - 1.1. Tasa de Cambio Media e Instantánea
   - 1.2. Definición Formal de Derivada
   - 1.3. Interpretación Geométrica: Recta Tangente
   - 1.4. Interpretación Económica: El Principio de Marginalidad
2. [Función Derivada y Reglas de Derivación](#2-función-derivada-y-reglas-de-derivación)
   - 2.1. Álgebra de Derivadas (Suma, Producto, Cociente)
   - 2.2. Regla de la Cadena (Funciones Compuestas)
   - 2.3. Tabla de Derivadas de Funciones Elementales
3. [Monotonía y Puntos Críticos](#3-monotonía-y-puntos-críticos)
   - 3.1. Criterio de Crecimiento y Decrecimiento (Signo de la 1ª Derivada)
   - 3.2. Puntos Críticos ($f'(x) = 0$)
4. [Optimización Libre: Extremos Relativos (Locales)](#4-optimización-libre-extremos-relativos-locales)
   - 4.1. Criterio del Test de la Primera Derivada
   - 4.2. Criterio del Test de la Segunda Derivada
5. [Curvatura y Puntos de Inflexión](#5-curvatura-y-puntos-de-inflexión)
   - 5.1. Concavidad y Convexidad (Signo de la 2ª Derivada)
   - 5.2. Puntos de Inflexión
6. [Extremos Absolutos (Globales) en Intervalos Cerrados](#6-extremos-absolutos-globales-en-intervalos-cerrados)
   - 6.1. Teorema de Weierstrass
   - 6.2. Algoritmo de Búsqueda de Extremos Globales
7. [Aplicaciones Empresariales y Económicas](#7-aplicaciones-empresariales-y-económicas)
   - 7.1. Coste Marginal, Ingreso Marginal y Beneficio Óptimo ($IMg = CMg$)
   - 7.2. Elasticidad-Precio de la Demanda

---

## 1. Tasa de Cambio y Concepto de Derivada en un Punto

### 1.1. Tasa de Cambio Media e Instantánea
Dada una función real de una variable $y = f(x)$, si la variable independiente experimenta una variación desde $x_0$ hasta $x_0 + \Delta x$:
* **Incremento de la variable:** $\Delta x$
* **Incremento de la función:** $\Delta y = f(x_0 + \Delta x) - f(x_0)$
* **Tasa de Cambio Media (TCM):**
  $$\text{TCM} = \frac{\Delta y}{\Delta x} = \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}$$
  *Significado:* Mide la variación media que experimenta $y$ por cada unidad de incremento en $x$.

### 1.2. Definición Formal de Derivada
La **derivada** de la función $f$ en el punto $x_0$, denotada por $f'(x_0)$ o $\frac{df}{dx}(x_0)$, es el límite de la tasa de cambio cuando el incremento tiende a cero:
$$f'(x_0) = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x} = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}$$

Si el límite existe y es finito, decimos que $f$ es **derivable en $x_0$**.
> ⚠️ **Propiedad fundamental:** *Toda función derivable en un punto es continua en dicho punto*. (El recíproco no siempre es cierto: ej. $f(x)=|x|$ es continua en $0$ pero no derivable).

### 1.3. Interpretación Geométrica: Recta Tangente
Geométricamente, $f'(x_0)$ representa la **pendiente** ($m$) de la recta tangente a la curva $y = f(x)$ en el punto $(x_0, f(x_0))$:
$$y - f(x_0) = f'(x_0) \cdot (x - x_0)$$

### 1.4. Interpretación Económica: El Principio de Marginalidad
En Economía y Administración de Empresas, la derivada mide el **comportamiento marginal**: la variación aproximada de la variable dependiente ante un incremento de **una unidad adicional** en la variable independiente:
$$f'(x_0) \approx f(x_0 + 1) - f(x_0)$$

---

## 2. Función Derivada y Reglas de Derivación

### 2.1. Álgebra de Derivadas
Sean $f$ y $g$ funciones derivables y $k \in \mathbb{R}$:
1. **Constante por función:** $(k \cdot f)' = k \cdot f'$
2. **Suma / Resta:** $(f \pm g)' = f' \pm g'$
3. **Producto:** $(f \cdot g)' = f' \cdot g + f \cdot g'$
4. **Cociente:** $\left(\frac{f}{g}\right)' = \frac{f' \cdot g - f \cdot g'}{g^2} \quad (g \neq 0)$

### 2.2. Regla de la Cadena (Composición de Funciones)
Si $z = g(y)$ e $y = f(x)$, entonces la función compuesta $z = (g \circ f)(x) = g(f(x))$ es derivable respecto a $x$:
$$\frac{dz}{dx} = \frac{dz}{dy} \cdot \frac{dy}{dx} \iff [g(f(x))]' = g'(f(x)) \cdot f'(x)$$

### 2.3. Tabla Resumen de Derivadas Inmediatas
| Función $f(x)$ | Derivada Simple $f'(x)$ | Derivada Compuesta $[u(x)]'$ |
| :--- | :--- | :--- |
| **Constante** $k$ | $0$ | — |
| **Potencia** $x^n$ | $n x^{n-1}$ | $n [u(x)]^{n-1} \cdot u'(x)$ |
| **Exponencial** $e^x$ | $e^x$ | $e^{u(x)} \cdot u'(x)$ |
| **Exponencial** $a^x$ | $a^x \ln a$ | $a^{u(x)} \ln a \cdot u'(x)$ |
| **Logaritmo** $\ln x$ | $\frac{1}{x}$ | $\frac{u'(x)}{u(x)}$ |
| **Logaritmo** $\log_a x$ | $\frac{1}{x \ln a}$ | $\frac{u'(x)}{u(x) \ln a}$ |

---

## 3. Monotonía y Puntos Críticos

### 3.1. Criterio de Crecimiento y Decrecimiento
Sea $f$ derivable en un intervalo abierto $I$:
* Si $f'(x) > 0, \ \forall x \in I \implies f$ es **estrictamente creciente** en $I$.
* Si $f'(x) < 0, \ \forall x \in I \implies f$ es **estrictamente decreciente** en $I$.
* Si $f'(x) = 0, \ \forall x \in I \implies f$ es **constante** en $I$.

### 3.2. Puntos Críticos (Estacionarios)
Los puntos del dominio donde la derivada se anula son los **puntos críticos**:
$$f'(x) = 0$$
Son los candidatos a extremos locales (máximos o mínimos).

---

## 4. Optimización Libre: Extremos Relativos (Locales)

### 4.1. Test de la Primera Derivada
Sea $x_0$ un punto crítico ($f'(x_0) = 0$):
* Si $f'(x)$ pasa de **positiva ($+$) a negativa ($-$)** al cruzar $x_0 \implies x_0$ es un **MÁXIMO RELATIVO**.
* Si $f'(x)$ pasa de **negativa ($-$) a positiva ($+$)** al cruzar $x_0 \implies x_0$ es un **MÍNIMO RELATIVO**.
* Si $f'(x)$ conserva el mismo signo a ambos lados de $x_0 \implies$ no hay extremo (punto de inflexión con tangente horizontal).

### 4.2. Test de la Segunda Derivada
Sea $f$ dos veces derivable en $x_0$ con $f'(x_0) = 0$:
* Si $f''(x_0) < 0 \implies x_0$ es un **MÁXIMO RELATIVO** (curvatura hacia abajo $\cap$).
* Si $f''(x_0) > 0 \implies x_0$ es un **MÍNIMO RELATIVO** (curvatura hacia arriba $\cup$).
* Si $f''(x_0) = 0 \implies$ el test no decide (recurrir al test de la 1ª derivada o derivadas de orden superior).

---

## 5. Curvatura y Puntos de Inflexión

### 5.1. Concavidad y Convexidad
* Si $f''(x) > 0, \ \forall x \in I \implies f$ es **convexa** en $I$ ($\cup$, forma de cuenco, la gráfica queda por encima de sus rectas tangentes).
* Si $f''(x) < 0, \ \forall x \in I \implies f$ es **cóncava** en $I$ ($\cap$, forma de campana, la gráfica queda por debajo de sus rectas tangentes).

### 5.2. Puntos de Inflexión
Un punto $x_0$ es de **inflexión** si la función cambia de curvatura (de cóncava a convexa o viceversa).
* **Condición necesaria:** $f''(x_0) = 0$ o no existe $f''(x_0)$.
* **Condición suficiente:** $f'''(x_0) \neq 0$ (o cambio de signo efectivo en $f''(x)$ al cruzar $x_0$).

---

## 6. Extremos Absolutos (Globales) en Intervalos Cerrados

### 6.1. Teorema de Weierstrass
> Si una función $f(x)$ es **continua** en un intervalo cerrado y acotado $[a, b]$, entonces $f$ alcanza en dicho intervalo un **máximo absoluto** y un **mínimo absoluto**.

### 6.2. Algoritmo de Búsqueda de Extremos Globales en $[a, b]$:
1. Calcular los puntos críticos interiores en $(a, b)$ resolviendo $f'(x) = 0$.
2. Descartar los puntos críticos que queden fuera del intervalo $[a, b]$.
3. Evaluar $f(x)$ en:
   - Los puntos críticos interiores seleccionados: $f(x_1), f(x_2), \dots$
   - Los extremos del intervalo: $f(a)$ y $f(b)$.
4. El **mayor valor** obtenido es el Máximo Absoluto; el **menor valor** es el Mínimo Absoluto.

---

## 7. Aplicaciones Empresariales y Económicas

### 7.1. Análisis Marginal de la Empresa
* **Función de Coste Total:** $C(x)$
  * **Coste Marginal:** $CMg(x) = C'(x) = \frac{dC}{dx}$ (coste de fabricar una unidad adicional).
  * **Coste Medio:** $CMe(x) = \frac{C(x)}{x}$.
* **Función de Ingresos:** $I(x) = p(x) \cdot x$
  * **Ingreso Marginal:** $IMg(x) = I'(x) = \frac{dI}{dx}$.
* **Función de Beneficio:** $B(x) = I(x) - C(x)$
  * **Condición de Primer Orden (CPO) para Beneficio Máximo:**
    $$B'(x) = 0 \iff I'(x) - C'(x) = 0 \iff IMg(x) = CMg(x)$$
  * **Condición de Segundo Orden (CSO):**
    $$B''(x) < 0 \iff I''(x) < C''(x)$$

### 7.2. Elasticidad-Precio de la Demanda
Mide la sensibilidad porcentual de la cantidad demandada $q$ ante una variación porcentual del precio $p$:
$$\varepsilon_p = \frac{\frac{dq}{q}}{\frac{dp}{p}} = \frac{p}{q} \cdot \frac{dq}{dp}$$
* $|\varepsilon_p| > 1$: Demanda **elástica** (subir el precio reduce los ingresos totales).
* $|\varepsilon_p| = 1$: Demanda de **elasticidad unitaria** (ingresos máximos).
* $|\varepsilon_p| < 1$: Demanda **inelástica** o rígida (subir el precio incrementa los ingresos totales).
