# 📖 Matemáticas para la Empresa I — Tema 0.3: Álgebra, Polinomios y Ecuaciones

- **Asignatura:** Matemáticas para la Empresa I (Cód. 2350)
- **Titulación:** Grado en ADE — Facultad de Economía y Empresa (Universidad de Murcia)
- **Documentos fuente:** *Presentación Expresiones algebraicas*, *Presentación Polinomios* y *Presentación Ecuaciones* (Proyecto de Innovación Educativa, UMU)
- **Archivos originales:** [Presentación_Expresiones+algebraicas.pdf](./Presentación_Expresiones+algebraicas.pdf) · [Presentación_Polinomios.pdf](./Presentación_Polinomios.pdf) · [Presentacion+Ecuaciones.pdf](./Presentacion+Ecuaciones.pdf)
- **Enfoque de este apunte:** Desde nivel cero, con el método de despeje infalible, identidades notables, Ruffini y resolución de ecuaciones lineales y cuadráticas.

---

## 1. Expresiones Algebraicas e Identidades Notables

### 1.1. Las 3 Identidades Notables Sagradas (Fórmulas que ahorran horas)

En las diapositivas de la UMU se recalca que debes saberlas de memoria en ambas direcciones:

$$\begin{aligned}
\text{1. Cuadrado de una suma:} &\quad (a + b)^2 = a^2 + 2ab + b^2 \\
\text{2. Cuadrado de una resta:} &\quad (a - b)^2 = a^2 - 2ab + b^2 \\
\text{3. Suma por diferencia:} &\quad (a + b)(a - b) = a^2 - b^2
\end{aligned}$$

> ⚠️ **El error universitario más grave:** Decir que $(a + b)^2 = a^2 + b^2$. **¡FALTA EL DOBLE PRODUCTO $2ab$!**  
> *Ejemplo:* $(x + 3)^2 = x^2 + 2 \cdot x \cdot 3 + 3^2 = x^2 + 6x + 9$.

---

### 1.2. Fracciones Algebraicas: Simplificación
Para simplificar una fracción con variables, **debes factorizar primero numerador y denominador**. Nunca taches sumandos.

* **Ejemplo correcto del PDF:**
  $$\frac{x^2 - 9}{x^2 + 6x + 9} = \frac{(x + 3)(x - 3)}{(x + 3)^2} = \mathbf{\frac{x - 3}{x + 3}}$$

---

## 2. Polinomios y Regla de Ruffini

### 2.1. Valor numérico de un polinomio
Sustituir la variable $x$ por un número concreto.  
*Ejemplo del PDF:* Si $P(x) = \frac{1}{2}x + 5$:
- Para $x = 1$: $P(1) = \frac{1}{2}(1) + 5 = \frac{11}{2}$.
- Para $x = -10$: $P(-10) = \frac{1}{2}(-10) + 5 = -5 + 5 = 0 \implies x = -10$ es una **raíz** de $P(x)$.

---

### 2.2. División por Ruffini (Para dividir entre $x - a$)
Sirve para descomponer polinomios en factores cuando el grado es mayor que 2.

> **Ejemplo resuelto de la diapositiva UMU:** Dividir $P(x) = 2x^3 + 3x - 5$ entre $(x + 2)$.  
> *(Atención: como no hay término en $x^2$, ponemos un $0$)*.
> 
> Raíz candidata: $x = -2$.
> 
> ```
>       |   2    0    3   -5
>   -2  |       -4    8  -22
>  -----+--------------------
>       |   2   -4   11  -27  <-- Resto
> ```
> - **Cociente:** $C(x) = 2x^2 - 4x + 11$
> - **Resto:** $R = -27$

---

## 3. Ecuaciones: El Arte de Despejar sin Errores

### 3.1. Ecuaciones Lineales de Primer Grado (Regla del Denominador)

> [!TIP]
> ### 💡 Ejemplo 7 de la Presentación UMU: Quitar denominadores correctamente
> **Resolver:**
> $$x = \frac{2x + 1}{3} + 1$$
> **Razona así (el método infalible):**  
> Para eliminar el $3$, multiplica **toda la ecuación (cada término)** por $3$:
> $$3 \cdot x = 3 \cdot \left(\frac{2x + 1}{3}\right) + 3 \cdot 1$$
> $$3x = 2x + 1 + 3 \implies 3x - 2x = 4 \implies \mathbf{x = 4}$$

---

### 3.2. Ecuaciones Cuadráticas de Segundo Grado
La forma general es $ax^2 + bx + c = 0$. Su fórmula general es:
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

* **Discriminante $\Delta = b^2 - 4ac$:**
  - $\Delta > 0$: Dos soluciones reales distintas.
  - $\Delta = 0$: Una solución real doble ($x = -b / 2a$).
  - $\Delta < 0$: No existen soluciones reales (la parábola no corta al eje $X$).

* **Casos incompletos (Mucho más rápidos, ¡no uses la fórmula larga!):**
  1. **Si falta $c$ ($ax^2 + bx = 0$):** Saca factor común la $x$:
     $$2x^2 - 8x = 0 \implies x(2x - 8) = 0 \implies x_1 = 0,\; x_2 = 4$$
  2. **Si falta $b$ ($ax^2 + c = 0$):** Despeja la $x^2$ y haz la raíz:
     $$3x^2 - 27 = 0 \implies x^2 = 9 \implies x = \pm\sqrt{9} = \pm 3$$

---

### 3.3. Ecuaciones con Radicales (Paso a Paso)
1. **Aislar la raíz** en un lado de la igualdad.
2. **Elevar al cuadrado** ambos miembros: $(\sqrt{\dots})^2 = (\dots)^2$.
3. **Resolver** la ecuación resultante.
4. **Comprobación obligatoria:** Al elevar al cuadrado pueden aparecer soluciones falsas.

---

### 3.4. Sistemas de 2 Ecuaciones Lineales (Equilibrio de Mercado)
En ADE se usan constantemente para calcular el precio y cantidad de equilibrio ($Q_d = Q_s$):
$$\begin{cases} 2x + y = 7 \\ x - y = 2 \end{cases}$$
Sumando ambas ecuaciones (reducción):
$$3x = 9 \implies x = 3 \implies y = 7 - 2(3) = 1 \implies \mathbf{(x, y) = (3, 1)}$$
