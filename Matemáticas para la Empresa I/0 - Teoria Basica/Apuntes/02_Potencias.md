# 📖 Conceptos Básicos UMU — 02: Potencias

- **Asignatura:** Matemáticas para la Empresa I (Cód. 2350)
- **Titulación:** Grado en ADE — Facultad de Economía y Empresa (Universidad de Murcia)
- **Bloque Aula Virtual:** **PARTE 1 — Tema 2: Potencias**
- **Documento fuente:** *Presentación potencias* (Proyecto de Innovación Educativa, UMU)
- **Archivo original:** [Presentación_potencias.pdf](./Presentación_potencias.pdf)
- **Enfoque de este apunte:** Desde cero, paso a paso, con todas las propiedades de exponentes, ejemplos resueltos de las diapositivas y aplicación a costes en ADE.

---

## 1. Definición y Reglas Básicas

Si $m$ es un número entero positivo, la potencia $m$-ésima de una base $a$, escrita $a^m$, se define como:
$$a^m = \underbrace{a \cdot a \cdot a \cdots a}_{m \text{ veces}}$$

* **Exponente cero:** Si $a \ne 0 \implies \mathbf{a^0 = 1}$  
  *(Ejemplos: $5^0 = 1$, $1000^0 = 1$, $(-4)^0 = 1$)*.
* **Exponente negativo (Dar la vuelta a la base):**
  $$a^{-m} = \frac{1}{a^m} \qquad \left(\frac{a}{b}\right)^{-m} = \left(\frac{b}{a}\right)^m$$
  *(Ejemplos: $5^{-1} = \frac{1}{5}$, $2^{-3} = \frac{1}{8}$, $\left(\frac{2}{3}\right)^{-2} = \left(\frac{3}{2}\right)^2 = \frac{9}{4}$)*.

---

## 2. Propiedades de las Potencias (Tabla Oficial UMU)

| Propiedad | Fórmula | Ejemplo del PDF |
| :--- | :--- | :--- |
| **Producto de igual base** | $a^m \cdot a^n = a^{m+n}$ | $5^{-2} \cdot 5^3 = 5^{-2+3} = 5^1 = 5$ |
| **Cociente de igual base** | $\frac{a^m}{a^n} = a^{m-n}$ | $\frac{3^4}{3^2} = 3^{4-2} = 3^2 = 9$ |
| **Potencia de potencia** | $(a^m)^n = a^{m \cdot n}$ | $(2^2)^3 = 2^6 = 64$ |
| **Distributiva del producto** | $(a \cdot b)^m = a^m \cdot b^m$ | $(x^6 y^3)^{1/3} = x^{6/3} y^{3/3} = x^2 y$ |
| **Distributiva del cociente** | $\left(\frac{a}{b}\right)^m = \frac{a^m}{b^m}$ | $\left(\frac{3}{4}\right)^2 = \frac{9}{16}$ |
| **Exponente fraccionario (Raíz)** | $a^{m/n} = \sqrt[n]{a^m} = (\sqrt[n]{a})^m$ | $8^{2/3} = (\sqrt[3]{8})^2 = 2^2 = 4$ |

---

## 3. Ejercicios Resueltos de las Diapositivas UMU

> [!TIP]
> ### 💡 Ejercicio 1: Fracción con exponente negativo
> **Calcular:** $\left(\frac{8}{27}\right)^{-2/3}$  
> 1. Invertimos la fracción: $\left(\frac{27}{8}\right)^{2/3}$.
> 2. Descomponemos en factores primos: $27 = 3^3$ y $8 = 2^3$.
> 3. Operamos: $\left(\frac{3^3}{2^3}\right)^{2/3} = \frac{3^{3 \cdot \frac{2}{3}}}{2^{3 \cdot \frac{2}{3}}} = \frac{3^2}{2^2} = \mathbf{\frac{9}{4}}$.

> [!TIP]
> ### 💡 Ejercicio 2: Simplificación de potencias
> **Simplificar:** $\frac{5^2 \cdot 5^{-4} \cdot 5^3}{5^0 \cdot 5^{-3} \cdot 5^4}$  
> - Numerador: $5^{2 - 4 + 3} = 5^1$.
> - Denominador: $5^{0 - 3 + 4} = 5^1$.
> - Resultado: $\frac{5^1}{5^1} = 5^{1 - 1} = 5^0 = \mathbf{1}$.

---

## 4. Aplicación a la Empresa (Diapositiva Oficial)

* **Función de coste:** $C(x) = 3x^{4/3} - 3$, donde $x$ es la producción.
* **Precio de venta competitivo:** $p = 6$ u.m.
* **Ingreso:** $I(x) = 6x$.
* **Beneficio:** $B(x) = I(x) - C(x) = 6x - (3x^{4/3} - 3) = \mathbf{6x - 3x^{4/3} + 3}$.
