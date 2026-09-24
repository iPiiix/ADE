# 📖 Matemáticas para la Empresa I — Tema 0.2: Potencias y Logaritmos

- **Asignatura:** Matemáticas para la Empresa I (Cód. 2350)
- **Titulación:** Grado en ADE — Facultad de Economía y Empresa (Universidad de Murcia)
- **Documentos fuente:** *Presentación potencias* y *Presentación logaritmos* (Proyecto de Innovación Educativa, UMU)
- **Archivos originales:** [Presentación_potencias.pdf](./Presentación_potencias.pdf) · [Presentación_logaritmos.pdf](./Presentación_logaritmos.pdf)
- **Enfoque de este apunte:** Explicación desde cero, paso a paso, con todas las propiedades, ejemplos oficiales resueltos y aplicaciones económicas reales.

---

## 🧭 ¿Para qué sirven las Potencias y Logaritmos en ADE?

1. **Cálculo del interés compuesto:** $C_f = C_0 \cdot (1 + r)^t$ (potencia de base $(1+r)$).
2. **Elasticidades y funciones de producción Cobb-Douglas:** $Q = A \cdot K^\alpha L^\beta$ (potencias con exponentes fraccionarios).
3. **Modelos de crecimiento exponencial y amortización:** El tiempo $t$ está en el exponente; para despejarlo, **necesitas logaritmos obligatoriamente**.

---

## 1. Potencias: Definición y Propiedades Esenciales

### 1.1. ¿Qué es una potencia?
Si $m$ es un número entero positivo, la potencia $m$-ésima de una base $a$, escrita $a^m$, es el producto de multiplicar $a$ por sí misma $m$ veces:
$$a^m = \underbrace{a \cdot a \cdot a \cdots a}_{m \text{ veces}}$$

* **Exponente cero:** Si $a \ne 0$, entonces:
  $$a^0 = 1 \qquad (\text{ej: } 5^0 = 1,\; 100^0 = 1,\; (-3)^0 = 1)$$
* **Exponente negativo (Darle la vuelta):**
  $$a^{-m} = \frac{1}{a^m} \qquad \left(\text{ej: } 5^{-1} = \frac{1}{5},\; 2^{-3} = \frac{1}{2^3} = \frac{1}{8}\right)$$
  > En fracciones: $\left(\frac{a}{b}\right)^{-m} = \left(\frac{b}{a}\right)^m$. Ejemplo: $\left(\frac{2}{3}\right)^{-2} = \left(\frac{3}{2}\right)^2 = \frac{9}{4}$.

---

### 1.2. Tabla Maestra de Propiedades de las Potencias

| Propiedad | Fórmula | Ejemplo Fácil | ¿Por qué funciona? |
| :--- | :--- | :--- | :--- |
| **Producto de igual base** | $a^m \cdot a^n = a^{m+n}$ | $2^2 \cdot 2^3 = 2^{2+3} = 2^5 = 32$ | Se suman los factores repetidos. |
| **Cociente de igual base** | $\frac{a^m}{a^n} = a^{m-n}$ | $\frac{3^4}{3^2} = 3^{4-2} = 3^2 = 9$ | Los factores repetidos abajo se cancelan. |
| **Potencia de una potencia** | $(a^m)^n = a^{m \cdot n}$ | $(5^2)^3 = 5^{2 \cdot 3} = 5^6$ | Paquetes repetidos de exponentes. |
| **Distributiva del producto** | $(a \cdot b)^m = a^m \cdot b^m$ | $(2 \cdot 5)^3 = 2^3 \cdot 5^3 = 8 \cdot 125 = 1000$ | El exponente afecta a todos los factores. |
| **Distributiva del cociente** | $\left(\frac{a}{b}\right)^m = \frac{a^m}{b^m}$ | $\left(\frac{3}{4}\right)^2 = \frac{3^2}{4^2} = \frac{9}{16}$ | Afecta a numerador y denominador. |
| **Exponente fraccionario (Raíz)** | $a^{m/n} = \sqrt[n]{a^m} = (\sqrt[n]{a})^m$ | $8^{2/3} = (\sqrt[3]{8})^2 = 2^2 = 4$ | El de arriba es potencia, el de abajo es el índice de la raíz. |

---

### 1.3. Ejercicios Resueltos Paso a Paso (Del PDF Oficial de la UMU)

> [!TIP]
> ### 💡 Ejercicio 1: Producto con bases iguales y exponentes fraccionarios
> **Calcular:** $7^3 \cdot 7^{2/3}$  
> **Solución:** Misma base ($7$), sumamos los exponentes:
> $$3 + \frac{2}{3} = \frac{9}{3} + \frac{2}{3} = \frac{11}{3} \implies \mathbf{7^{11/3}} = \sqrt[3]{7^{11}}$$

> [!TIP]
> ### 💡 Ejercicio 2: Fracción con exponente negativo
> **Calcular:** $\left(\frac{8}{27}\right)^{-2/3}$  
> **Solución:**
> 1. Eliminamos el signo menos invirtiendo la fracción:
>    $$\left(\frac{8}{27}\right)^{-2/3} = \left(\frac{27}{8}\right)^{2/3}$$
> 2. Descomponemos en factores primos: $27 = 3^3$ y $8 = 2^3$:
>    $$\left(\frac{3^3}{2^3}\right)^{2/3} = \frac{(3^3)^{2/3}}{(2^3)^{2/3}} = \frac{3^{3 \cdot \frac{2}{3}}}{2^{3 \cdot \frac{2}{3}}} = \frac{3^2}{2^2} = \mathbf{\frac{9}{4}}$$

> [!TIP]
> ### 💡 Ejercicio 3: Simplificación de torres de potencias
> **Simplificar:** $\frac{5^2 \cdot 5^{-4} \cdot 5^3}{5^0 \cdot 5^{-3} \cdot 5^4}$  
> **Solución:**
> 1. Agrupamos el numerador: $5^{2 + (-4) + 3} = 5^1$.
> 2. Agrupamos el denominador: $5^{0 + (-3) + 4} = 5^1$.
> 3. Dividimos: $\frac{5^1}{5^1} = 5^{1-1} = 5^0 = \mathbf{1}$.

> [!IMPORTANT]
> ### 📈 Aplicación Económica del PDF Oficial (Función de Costes y Beneficios)
> **Enunciado:** La función de coste total de una empresa es $C(x) = 3x^{4/3} - 3$, donde $x$ es el nivel de producción. Si el producto se vende en un mercado competitivo a un precio unitario de $p = 6$ u.m.:
> 1. **Función de Ingreso:** $I(x) = p \cdot x = 6x$.
> 2. **Función de Beneficio:**
>    $$B(x) = I(x) - C(x) = 6x - (3x^{4/3} - 3) = \mathbf{6x - 3x^{4/3} + 3}$$
> *(Observa cómo en ADE las potencias con exponentes fraccionarios como $x^{4/3}$ representan costes marginales crecientes)*.

---

## 2. Logaritmos: El Reverso de la Potenciación

### 2.1. Definición Formal
El logaritmo de un número $x$ en una base $b$ es el exponente al que hay que elevar la base $b$ para obtener el número $x$:
$$\log_b(x) = y \iff b^y = x$$

* **Condiciones obligatorias:** La base debe ser positiva y distinta de 1 ($b > 0, b \ne 1$).
* **Regla de oro:** El argumento $x$ **siempre debe ser estrictamente positivo** ($x > 0$).
  > ❌ **NO EXISTE** el logaritmo de un número negativo: $\nexists \log_2(-4)$.  
  > ❌ **NO EXISTE** el logaritmo de cero: $\nexists \log(0)$.

### 2.2. Bases Frecuentes
1. **Logaritmo Decimal (Base 10):** Se escribe simplemente $\log(x)$:
   $$\log(100) = 2 \iff 10^2 = 100 \qquad \log(0{,}001) = -3 \iff 10^{-3} = 0{,}001$$
2. **Logaritmo Neperiano o Natural (Base $e \approx 2{,}71828$):** Se escribe $\ln(x)$:
   $$\ln(e) = 1 \iff e^1 = e \qquad \ln(1) = 0 \iff e^0 = 1$$

---

### 2.3. Las 3 Propiedades Operativas de los Logaritmos

$$\begin{aligned}
\text{1. Logaritmo de un producto:} &\quad \log_b(x \cdot y) = \log_b(x) + \log_b(y) \\
\text{2. Logaritmo de un cociente:} &\quad \log_b\left(\frac{x}{y}\right) = \log_b(x) - \log_b(y) \\
\text{3. Logaritmo de una potencia:} &\quad \log_b(x^k) = k \cdot \log_b(x)
\end{aligned}$$

---

### 2.4. Ejercicios Resueltos de Logaritmos (Del PDF Oficial UMU)

> [!TIP]
> ### 💡 Ejercicio 4: Descomposición en función de $\log 2$
> **Calcular en función de $\log 2$:**
> - $\log 4 = \log(2^2) = 2 \cdot \log 2$
> - $\log(0{,}0625)$:
>   $$\log(0{,}0625) = \log\left(\frac{625}{10000}\right) = \log\left(\frac{1}{16}\right) = \log(2^{-4}) = \mathbf{-4 \cdot \log 2}$$

> [!TIP]
> ### 💡 Ejercicio 5: Cálculo mental aplicando definición
> **Calcular:** $\log_2(64) + \log_2\left(\frac{1}{4}\right) - \log_3(9) - \log_2(2)$  
> **Solución:**
> - $\log_2(64) = 6$ (porque $2^6 = 64$)
> - $\log_2\left(\frac{1}{4}\right) = \log_2(2^{-2}) = -2$
> - $\log_3(9) = 2$ (porque $3^2 = 9$)
> - $\log_2(2) = 1$
> **Resultado:** $6 + (-2) - 2 - 1 = 6 - 5 = \mathbf{1}$.

---

### 2.5. Resolución de Ecuaciones Logarítmicas (Método Oficial UMU)

**Método en 3 pasos:**
1. Agrupar con las propiedades para tener **un solo logaritmo a cada lado** de la igualdad: $\log(A) = \log(B)$.
2. Igualar los argumentos: $A = B$ y resolver la ecuación resultante.
3. **Paso crítico:** Comprobar que las soluciones no hagan negativo o cero ningún argumento original.

> [!TIP]
> ### 💡 Ejemplo 6: Ecuación logarítmica con descarte de soluciones
> **Resolver:** $\log(x^2 - 4x + 3) = \log(3 - 2x)$  
> 1. Como ya tenemos un solo logaritmo a cada lado, igualamos:
>    $$x^2 - 4x + 3 = 3 - 2x$$
> 2. Pasamos todo a la izquierda:
>    $$x^2 - 2x = 0 \implies x(x - 2) = 0 \implies x_1 = 0,\; x_2 = 2$$
> 3. **Comprobación:**
>    - Para $x = 0$: $\log(3) = \log(3)$ $\implies$ **Válida**.
>    - Para $x = 2$: $3 - 2(2) = -1 < 0$ $\implies$ ¡Logaritmo de número negativo! $\implies$ **Descartada**.  
>    **Solución única:** $\mathbf{x = 0}$.

> [!TIP]
> ### 💡 Ejemplo 7: Ecuación con coeficientes multiplicando
> **Resolver:** $2\log(x) - \log(x + 6) = 3\log(2)$  
> 1. Subimos los coeficientes como exponentes:
>    $$\log(x^2) - \log(x + 6) = \log(2^3)$$
> 2. Aplicamos la resta como cociente:
>    $$\log\left(\frac{x^2}{x + 6}\right) = \log(8)$$
> 3. Igualamos y resolvemos:
>    $$\frac{x^2}{x + 6} = 8 \implies x^2 = 8x + 48 \implies x^2 - 8x - 48 = 0$$
>    Factorizamos: $(x - 12)(x + 4) = 0 \implies x = 12$ ó $x = -4$.  
> 4. Como $x > 0$ por el $\log(x)$ original, descartamos $x = -4$.  
>    **Solución única:** $\mathbf{x = 12}$.
