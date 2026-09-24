# 📖 Conceptos Básicos UMU — 06: Ecuaciones

- **Asignatura:** Matemáticas para la Empresa I (Cód. 2350)
- **Titulación:** Grado en ADE — Facultad de Economía y Empresa (Universidad de Murcia)
- **Bloque Aula Virtual:** **PARTE 2 — Tema 6: Ecuaciones**
- **Documento fuente:** *Presentación Ecuaciones* (Proyecto de Innovación Educativa, UMU)
- **Archivo original:** [Presentacion+Ecuaciones.pdf](./Presentacion+Ecuaciones.pdf)
- **Enfoque de este apunte:** Ecuaciones lineales con denominadores, fórmula cuadrática, ecuaciones incompletas, radicales y sistemas aplicados al equilibrio de mercado.

---

## 1. Ecuaciones Lineales de Primer Grado

> [!TIP]
> ### 💡 Ejemplo 7 Oficial UMU: Eliminar denominadores limpiamente
> **Resolver:** $x = \frac{2x + 1}{3} + 1$  
> 1. Multiplica **todos los términos** por $3$ (m.c.m. de denominadores):
>    $$3 \cdot x = 3 \cdot \left(\frac{2x + 1}{3}\right) + 3 \cdot 1$$
> 2. Simplifica:
>    $$3x = 2x + 1 + 3 \implies 3x - 2x = 4 \implies \mathbf{x = 4}$$

---

## 2. Ecuaciones Cuadráticas de Segundo Grado

Forma general: $ax^2 + bx + c = 0$.
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

* **Discriminante $\Delta = b^2 - 4ac$:**
  - $\Delta > 0 \implies$ 2 soluciones reales distintas.
  - $\Delta = 0 \implies$ 1 solución doble ($x = -b / 2a$).
  - $\Delta < 0 \implies$ Sin soluciones reales.

* **Casos incompletos rápidos:**
  - **Falta $c$ ($ax^2 + bx = 0$):** Saca factor común $x$:
    $$2x^2 - 8x = 0 \implies x(2x - 8) = 0 \implies x_1 = 0,\; x_2 = 4$$
  - **Falta $b$ ($ax^2 + c = 0$):** Despeja $x^2$:
    $$3x^2 - 27 = 0 \implies x^2 = 9 \implies x = \pm 3$$

---

## 3. Ecuaciones con Radicales
1. Aislar la raíz en un miembro.
2. Elevar al cuadrado ambos miembros: $(\sqrt{\dots})^2 = (\dots)^2$.
3. Resolver la ecuación y **comprobar siempre** en la ecuación original para descartar soluciones ficticias.

---

## 4. Sistemas de Ecuaciones Lineales (Equilibrio de Mercado en ADE)
$$\begin{cases} Q = 100 - 2P & \text{(Demanda)} \\ Q = 20 + 3P & \text{(Oferta)} \end{cases}$$
Igualando oferta y demanda ($Q_d = Q_s$):
$$100 - 2P = 20 + 3P \implies 80 = 5P \implies \mathbf{P^* = 16 \text{ u.m.}} \implies \mathbf{Q^* = 68 \text{ uds.}}$$
