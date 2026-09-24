# 📖 Conceptos Básicos UMU — 03: Logaritmos

- **Asignatura:** Matemáticas para la Empresa I (Cód. 2350)
- **Titulación:** Grado en ADE — Facultad de Economía y Empresa (Universidad de Murcia)
- **Bloque Aula Virtual:** **PARTE 1 — Tema 3: Logaritmos**
- **Documento fuente:** *Presentación logaritmos* (Proyecto de Innovación Educativa, UMU)
- **Archivo original:** [Presentación_logaritmos.pdf](./Presentación_logaritmos.pdf)
- **Enfoque de este apunte:** La inversa de la potenciación, bases 10 y $e$, propiedades fundamentales y resolución de ecuaciones logarítmicas oficiales.

---

## 1. Definición Formal y Reglas

El logaritmo de un número $x$ en una base $b$ es el exponente al que hay que elevar $b$ para obtener $x$:
$$\log_b(x) = y \iff b^y = x$$

* **Condiciones obligatorias:** La base debe ser positiva y distinta de 1 ($b > 0, b \ne 1$).
* **Regla de oro:** El argumento siempre debe ser estrictamente positivo ($x > 0$).
  > ❌ **NO EXISTE** el logaritmo de un número negativo ($\nexists \log_b(-x)$) ni el de cero ($\nexists \log_b(0)$).

### Bases habituales:
* **Logaritmo Decimal (Base 10):** Se escribe $\log(x)$. Ejemplo: $\log(100) = 2 \iff 10^2 = 100$.
* **Logaritmo Neperiano (Base $e \approx 2{,}718$):** Se escribe $\ln(x)$. Ejemplo: $\ln(e) = 1 \iff e^1 = e$.

---

## 2. Propiedades Operativas

1. **Producto:** $\log_b(x \cdot y) = \log_b(x) + \log_b(y)$
2. **Cociente:** $\log_b\left(\frac{x}{y}\right) = \log_b(x) - \log_b(y)$
3. **Potencia:** $\log_b(x^k) = k \cdot \log_b(x)$
4. **Casos clave:** $\log_b(b) = 1$ y $\log_b(1) = 0$.

---

## 3. Ejercicios Resueltos de las Diapositivas UMU

> [!TIP]
> ### 💡 Ejercicio 1: Cálculo mental con la definición
> **Calcular:** $\log_2(64) + \log_2\left(\frac{1}{4}\right) - \log_3(9) - \log_2(2)$  
> - $\log_2(64) = 6$ (porque $2^6 = 64$)
> - $\log_2(1/4) = -2$ (porque $2^{-2} = 1/4$)
> - $\log_3(9) = 2$ (porque $3^2 = 9$)
> - $\log_2(2) = 1$
> **Resultado:** $6 + (-2) - 2 - 1 = \mathbf{1}$.

> [!TIP]
> ### 💡 Ejercicio 2: En función de $\log 2$
> $\log(0{,}0625) = \log\left(\frac{625}{10000}\right) = \log\left(\frac{1}{16}\right) = \log(2^{-4}) = \mathbf{-4 \cdot \log 2}$.

---

## 4. Ecuaciones Logarítmicas (Paso a Paso)

> [!TIP]
> ### 💡 Ejemplo Oficial 1:
> **Resolver:** $\log(x^2 - 4x + 3) = \log(3 - 2x)$  
> 1. Igualamos argumentos: $x^2 - 4x + 3 = 3 - 2x$.
> 2. Pasamos todo a un lado: $x^2 - 2x = 0 \implies x(x - 2) = 0 \implies x_1 = 0,\; x_2 = 2$.
> 3. **Comprobación:**
>    - Para $x = 0$: $\log(3) = \log(3)$ $\implies$ **Válida**.
>    - Para $x = 2$: $3 - 2(2) = -1 < 0$ $\implies$ No existe logaritmo negativo $\implies$ **Descartada**.  
>    **Solución única:** $\mathbf{x = 0}$.

> [!TIP]
> ### 💡 Ejemplo Oficial 2:
> **Resolver:** $2\log(x) - \log(x + 6) = 3\log(2)$  
> 1. Subimos exponentes y agrupamos: $\log\left(\frac{x^2}{x + 6}\right) = \log(8)$.
> 2. Igualamos: $\frac{x^2}{x + 6} = 8 \implies x^2 - 8x - 48 = 0 \implies (x - 12)(x + 4) = 0$.
> 3. Como $x > 0$ por el $\log(x)$ original, descartamos $x = -4$.  
>    **Solución única:** $\mathbf{x = 12}$.
