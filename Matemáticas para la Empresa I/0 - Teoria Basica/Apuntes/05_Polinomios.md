# 📖 Conceptos Básicos UMU — 05: Polinomios

- **Asignatura:** Matemáticas para la Empresa I (Cód. 2350)
- **Titulación:** Grado en ADE — Facultad de Economía y Empresa (Universidad de Murcia)
- **Bloque Aula Virtual:** **PARTE 2 — Tema 5: Polinomios**
- **Documento fuente:** *Presentación Polinomios* (Proyecto de Innovación Educativa, UMU)
- **Archivo original:** [Presentación_Polinomios.pdf](./Presentación_Polinomios.pdf)
- **Enfoque de este apunte:** Operaciones con polinomios, valor numérico, división clásica, regla de Ruffini y raíces.

---

## 1. Operaciones con Polinomios y Valor Numérico

* **Valor Numérico:** Resultado de sustituir $x$ por un número.  
  *Ejemplo del PDF:* Para $P(x) = \frac{1}{2}x + 5$:
  - $P(1) = \frac{1}{2}(1) + 5 = \frac{11}{2}$.
  - $P(-10) = \frac{1}{2}(-10) + 5 = 0 \implies x = -10$ es una **raíz** de $P(x)$.
* **Suma y Resta:** Se agrupan únicamente los términos del mismo grado (monomios semejantes).
* **Multiplicación:** Se multiplica cada término del primer polinomio por todos los términos del segundo.

---

## 2. División de Polinomios y Regla de Ruffini

### 2.1. Regla de Ruffini (Para dividir entre $x - a$)
Permite dividir un polinomio por un binomio de primer grado de forma rápida y encontrar raíces.

> **Ejemplo de la diapositiva UMU:** Dividir $P(x) = 2x^3 + 3x - 5$ entre $(x + 2)$.  
> *(Nota: Colocamos un $0$ en el término ausente $x^2$)*.
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

## 3. Teorema del Resto y Factorización

* **Teorema del Resto:** El resto de dividir $P(x)$ entre $(x - a)$ coincide con el valor numérico $P(a)$.
* **Raíz de un polinomio:** Si $P(a) = 0$, entonces $x = a$ es una raíz y el polinomio es divisible por $(x - a)$.
* **Factorización completa:**
  $$P(x) = a_n \cdot (x - r_1)(x - r_2)\cdots(x - r_n)$$
