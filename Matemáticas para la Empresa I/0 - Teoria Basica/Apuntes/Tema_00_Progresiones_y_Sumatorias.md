# 📖 Matemáticas para la Empresa I — Tema 0.5: Sumatorias, Progresiones y Áreas Elementales

- **Asignatura:** Matemáticas para la Empresa I (Cód. 2350)
- **Titulación:** Grado en ADE — Facultad de Economía y Empresa (Universidad de Murcia)
- **Documentos fuente:** *Presentación Sumas y progresiones* y *Presentación Áreas de triángulos y rectángulos* (Proyecto de Innovación Educativa, UMU)
- **Archivos originales:** [Sumas+y+progresiones.pptx](./Sumas+y+progresiones.pptx) · [Area_triangulo_rectangulo.pptx](./Area_triangulo_rectangulo.pptx)
- **Enfoque de este apunte:** Comprensión clara del símbolo sumatorio ($\sum$), progresiones aritméticas y geométricas (clave para matemáticas financieras y cálculo de rentas) y deducción geométrica de áreas.

---

## 1. Notación Sumatoria ($\sum$): Compactar Sumas Largas

El símbolo $\sum$ (sigma mayúscula) indica que debemos sumar una serie de términos siguiendo una fórmula desde un índice inicial hasta un índice final:

$$\sum_{i=1}^{n} x_i = x_1 + x_2 + x_3 + \dots + x_n$$

### 1.1. Ejemplos Resueltos del PPT Oficial de la UMU

* **Ejemplo 1:**
  $$\sum_{i=1}^{3} i^3 = 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = \mathbf{36}$$
* **Ejemplo 2:**
  $$\sum_{j=1}^{3} (2j - 4) = (2 \cdot 1 - 4) + (2 \cdot 2 - 4) + (2 \cdot 3 - 4) = -2 + 0 + 2 = \mathbf{0}$$
* **Ejemplo 3 (Suma con fracciones):**
  $$\sum_{k=1}^{2} \frac{1}{k + 2} = \frac{1}{1 + 2} + \frac{1}{2 + 2} = \frac{1}{3} + \frac{1}{4} = \frac{4 + 3}{12} = \mathbf{\frac{7}{12}}$$
* **Escribir en notación de sumatorio:**
  $$1 + 4 + 9 + 16 = 1^2 + 2^2 + 3^2 + 4^2 = \mathbf{\sum_{i=1}^{4} i^2}$$

---

## 2. Progresiones Aritméticas (P.A.): Suma Constante

Una progresión aritmética es una sucesión donde cada término se obtiene **sumando una cantidad fija $d$** (llamada diferencia) al término anterior:
$$a_n = a_{n-1} + d$$

### 2.1. Fórmulas Fundamentales
* **Término General:**
  $$a_n = a_1 + (n - 1) \cdot d$$
* **Suma de los $n$ primeros términos (Fórmula de Gauss):**
  $$S_n = \frac{a_1 + a_n}{2} \cdot n$$

> [!TIP]
> ### 💡 Ejercicio del PPT Oficial
> **Enunciado:** Una progresión aritmética tiene primer término $a_1 = 15$ y diferencia $d = 4$. ¿Cuántos términos tiene si el último término es $a_n = 71$?  
> **Solución:**
> $$71 = 15 + (n - 1) \cdot 4 \implies 56 = 4(n - 1) \implies n - 1 = 14 \implies \mathbf{n = 15 \text{ términos}}$$

---

## 3. Progresiones Geométricas (P.G.): Multiplicación Constante

En una progresión geométrica, cada término se obtiene **multiplicando por una razón fija $r$**:
$$a_n = a_{n-1} \cdot r$$

### 3.1. Fórmulas Fundamentales
* **Término General:**
  $$a_n = a_1 \cdot r^{n-1}$$
* **Suma de los $n$ primeros términos:**
  $$S_n = \frac{a_1 \cdot (r^n - 1)}{r - 1} = \frac{a_n \cdot r - a_1}{r - 1}$$
* **Suma Infinita (cuando $|r| < 1$):**
  $$S_\infty = \frac{a_1}{1 - r}$$

> [!IMPORTANT]
> ### 💼 ¿Por qué esto es vital en ADE?: Matemáticas Financieras
> Cuando una empresa valora una **renta perpetua** (un flujo constante de dinero $C$ cada año con un tipo de interés $i$), el valor actual es exactamente la suma infinita de una progresión geométrica de razón $r = \frac{1}{1 + i}$:
> $$\text{Valor Actual} = \sum_{t=1}^{\infty} \frac{C}{(1+i)^t} = \frac{C}{i}$$

---

## 4. Geometría Elemental: Áreas de Rectángulos y Triángulos

Del archivo de la UMU `Area_triangulo_rectangulo.pptx`:

1. **Paralelogramo / Rectángulo:**
   $$\text{Área} = \text{base} \cdot \text{altura} = b \cdot h$$
   *(Ej: Rectángulo de base $4\text{ cm}$ y altura $2\text{ cm} \implies A = 4 \cdot 2 = 8\text{ cm}^2$)*.

2. **Triángulo:**
   $$\text{Área} = \frac{\text{base} \cdot \text{altura}}{2} = \frac{b \cdot h}{2}$$
   * **¿Por qué se divide entre 2?:** Porque cualquier triángulo (rectángulo o isósceles) es exactamente la mitad de un paralelogramo al colocar otro triángulo gemelo girado a su lado.
   * *Ejemplo del PPT:* Triángulo de base $9\text{ cm}$ y altura $3\text{ cm}$:
     $$\text{Área} = \frac{9 \cdot 3}{2} = \frac{27}{2} = \mathbf{13{,}5\text{ cm}^2}$$
