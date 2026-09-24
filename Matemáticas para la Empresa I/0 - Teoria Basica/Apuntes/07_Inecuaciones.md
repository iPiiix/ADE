# 📖 Conceptos Básicos UMU — 07: Inecuaciones y Desigualdades

- **Asignatura:** Matemáticas para la Empresa I (Cód. 2350)
- **Titulación:** Grado en ADE — Facultad de Economía y Empresa (Universidad de Murcia)
- **Bloque Aula Virtual:** **PARTE 2 — Tema 7: Inecuaciones**
- **Documento fuente:** *Presentación Desigualdades* (Proyecto de Innovación Educativa, UMU)
- **Archivo original:** [desigualdades_presentacion.pdf](./desigualdades_presentacion.pdf)
- **Enfoque de este apunte:** Intervalos, inecuaciones lineales con cambio de sentido de signo, inecuaciones cuadráticas por tramos y valor absoluto.

---

## 1. Intervalos en la Recta Real

| Tipo | Notación | Definición | Inclusión |
| :--- | :---: | :--- | :---: |
| **Abierto** | $(a, b)$ | $\{x \in \mathbb{R} : a < x < b\}$ | No incluye extremos |
| **Cerrado** | $[a, b]$ | $\{x \in \mathbb{R} : a \le x \le b\}$ | Incluye extremos |
| **Semiabierto** | $[a, b)$ | $\{x \in \mathbb{R} : a \le x < b\}$ | Incluye $a$, pero no $b$ |
| **Infinito** | $[a, +\infty)$ | $\{x \in \mathbb{R} : x \ge a\}$ | Desde $a$ hasta infinito |

---

## 2. Inecuaciones Lineales: Regla Crítica del Signo Negativo

> [!CAUTION]
> Al multiplicar o dividir por un número **negativo**, el sentido de la desigualdad **se invierte obligatoriamente**:
> $$-3x \le 12 \implies x \ge \frac{12}{-3} \implies \mathbf{x \ge -4} \implies x \in [-4, +\infty)$$

---

## 3. Inecuaciones de Segundo Grado (Método de Intervalos)

**Resolver:** $x^2 - 4x + 3 < 0$
1. **Raíces:** $x^2 - 4x + 3 = 0 \implies (x - 1)(x - 3) = 0 \implies x_1 = 1,\; x_2 = 3$.
2. **Dividir la recta real:** $(-\infty, 1)$, $(1, 3)$, $(3, +\infty)$.
3. **Comprobar un punto en cada tramo:**
   - En $(-\infty, 1)$ ($x = 0$): $0^2 - 4(0) + 3 = +3 > 0$ (+).
   - En $(1, 3)$ ($x = 2$): $2^2 - 4(2) + 3 = -1 < 0$ (-).
   - En $(3, +\infty)$ ($x = 4$): $4^2 - 4(4) + 3 = +3 > 0$ (+).
4. Como buscamos $< 0$, la solución es:
   $$\mathbf{x \in (1, 3)}$$

---

## 4. Valor Absoluto $|x|$
* $|x| \le k \iff -k \le x \le k$ (intervalo acotado).
* $|x| \ge k \iff x \ge k \text{ ó } x \le -k$ (dos semirrectas exteriores).
