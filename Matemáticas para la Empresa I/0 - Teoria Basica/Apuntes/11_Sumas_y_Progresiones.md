# 📖 Conceptos Básicos UMU — 11: Sumas y Progresiones

- **Asignatura:** Matemáticas para la Empresa I (Cód. 2350)
- **Titulación:** Grado en ADE — Facultad de Economía y Empresa (Universidad de Murcia)
- **Bloque Aula Virtual:** **PARTE 3 — Tema 11: Sumas y progresiones**
- **Documento fuente:** *Presentación Sumas y progresiones* (Proyecto de Innovación Educativa, UMU)
- **Archivo original:** [Sumas+y+progresiones.pptx](./Sumas+y+progresiones.pptx)
- **Enfoque de este apunte:** Notación sumatoria ($\sum$), progresiones aritméticas y geométricas (clave para matemáticas financieras y cálculo de rentas).

---

## 1. Notación Sumatoria ($\sum$)

El símbolo $\sum$ (sigma mayúscula) permite compactar sumas de muchos términos:

$$\sum_{i=1}^{n} x_i = x_1 + x_2 + x_3 + \dots + x_n$$

### Ejemplos Resueltos del PPT Oficial:
* $\sum_{i=1}^{3} i^3 = 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = \mathbf{36}$.
* $\sum_{j=1}^{3} (2j - 4) = (2 \cdot 1 - 4) + (2 \cdot 2 - 4) + (2 \cdot 3 - 4) = -2 + 0 + 2 = \mathbf{0}$.
* $\sum_{k=1}^{2} \frac{1}{k + 2} = \frac{1}{1 + 2} + \frac{1}{2 + 2} = \frac{1}{3} + \frac{1}{4} = \mathbf{\frac{7}{12}}$.
* Expresar como sumatorio: $1 + 4 + 9 + 16 = \mathbf{\sum_{i=1}^{4} i^2}$.

---

## 2. Progresiones Aritméticas (P.A.)

Cada término se obtiene sumando una diferencia constante $d$:
$$a_n = a_{n-1} + d$$

* **Término General:** $a_n = a_1 + (n - 1) \cdot d$
* **Suma de los $n$ primeros términos (Fórmula de Gauss):**
  $$S_n = \frac{a_1 + a_n}{2} \cdot n$$

> [!TIP]
> ### 💡 Ejercicio del PPT Oficial:
> Una progresión aritmética tiene $a_1 = 15$ y $d = 4$. ¿Cuántos términos tiene si el último es $a_n = 71$?  
> $$71 = 15 + (n - 1) \cdot 4 \implies 56 = 4(n - 1) \implies n - 1 = 14 \implies \mathbf{n = 15 \text{ términos}}$$

---

## 3. Progresiones Geométricas (P.G.)

Cada término se obtiene multiplicando por una razón constante $r$:
$$a_n = a_{n-1} \cdot r$$

* **Término General:** $a_n = a_1 \cdot r^{n-1}$
* **Suma de $n$ términos:**
  $$S_n = \frac{a_1 \cdot (r^n - 1)}{r - 1}$$
* **Suma Infinita (cuando $|r| < 1$):**
  $$S_\infty = \frac{a_1}{1 - r}$$

> [!IMPORTANT]
> ### 💼 Aplicación Vital en ADE: Valoración de Rentas Perpetuas
> Si un activo genera un dividendo anual constante $C$ con tipo de interés de descuento $i$, su valor actual es la suma infinita de una progresión geométrica con $r = \frac{1}{1+i}$:
> $$\text{Valor} = \frac{C}{i}$$
