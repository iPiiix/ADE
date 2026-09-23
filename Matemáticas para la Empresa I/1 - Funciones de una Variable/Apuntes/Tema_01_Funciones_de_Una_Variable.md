# 📈 Matemáticas para la Empresa I — Tema 1: Funciones Reales de una Variable

- **Asignatura:** Matemáticas para la Empresa I (Cód. 2350)
- **Titulación:** Grado en ADE — Facultad de Economía y Empresa (Universidad de Murcia)
- **Grupo:** Grupo 5 (Turno Tarde) · **Profesora:** Matilde Lafuente Lechuga
- **Documento fuente:** *Tema I. Funciones Reales de una Variable (Curso 2026-2027)*
- **Archivo original diapositivas:** [Tema_01_Presentacion_Oficial.pdf](./Tema_01_Presentacion_Oficial.pdf)
- **Enfoque de este apunte:** Explicación limpia, visual y sin saltos raros. Si sacabas un 1 o llevas años sin tocar una gráfica, aquí tienes el puente directo para entender de verdad qué es una función económica, cómo se calcula su dominio, cómo hacer límites y cuándo es continua.

---

## 🧭 Diccionario Rápido: De Jerga Universitaria a Palabras Normales

| Término oficial | Cómo se lee | Qué significa en la empresa (Ejemplo real) |
| :---: | :--- | :--- |
| $x$ (Variable exógena) | "Variable independiente" | Lo que tú decides o lo que viene de fuera (ej: el precio que le pones a una camiseta, o las horas de curro). |
| $y$ ó $f(x)$ (Variable endógena) | "Variable dependiente" | El resultado final que depende de $x$ (ej: el beneficio que consigues o la cantidad de clientes que entran). |
| $\operatorname{Dom}(f)$ | Dominio | Los valores de $x$ con los que la fórmula no explota (matemáticamente) y que tienen sentido real (económicamente: no fabricar tornillos negativos). |
| Pendiente $a$ de una recta | Inclinación de $y = ax + b$ | Cuánto sube o baja el resultado $y$ por cada unidad extra que aumentas la $x$. En economía es el **coste marginal** o **ingreso marginal**. |
| $(g \circ f)(x) = g(f(x))$ | Composición de funciones | Una cadena de montaje: primero calculas $f(x)$ y al resultado que te da le aplicas la fórmula $g$. |
| $\lim_{x \to x_0} f(x)$ | Límite cuando $x$ tiende a $x_0$ | A qué número se acerca el resultado $f(x)$ cuando nos ponemos pegaditos al valor $x_0$ (sin necesidad de pisarlo). |
| Función continua | Continuidad | La gráfica se puede dibujar de un solo trazo sin levantar el lápiz del papel (no hay saltos de precio bruscos ni roturas). |

---

## 1. ¿Qué es una Función y qué es el Dominio?

Una función es una **máquina de procesar números**: metes un valor $x$ por la entrada, la fórmula hace una operación y te devuelve un único resultado $y = f(x)$.

```
   [ Entrada: x ] ---> [ Máquina: f(x) ] ---> [ Salida: y = f(x) ]
   (ej. Unidades)        (Multiplicar x 15€)     (Ingreso Total)
```

$$\operatorname{Dom}(f) = \{x \in \mathbb{R} \ / \ \exists f(x)\}$$

### 🔍 Las 3 Reglas de Oro para calcular Dominios:
1. **Fracciones:** El denominador jamás puede valer cero.
   - Ejemplo: $f(x) = \frac{5}{x - 3} \implies x - 3 = 0 \iff x = 3$.  
     $$\operatorname{Dom}(f) = \mathbb{R} \setminus \{3\} \quad \text{(todos los números reales excepto el 3)}$$
2. **Raíces cuadradas:** Lo de dentro debe ser mayor o igual que 0.
   - Ejemplo: $f(x) = \sqrt{x - 4} \implies x - 4 \ge 0 \iff x \ge 4$.  
     $$\operatorname{Dom}(f) = [4, +\infty)$$
3. **Logaritmos:** Lo de dentro debe ser estrictamente positivo ($> 0$).
   - Ejemplo: $f(x) = \ln(x + 2) \implies x + 2 > 0 \iff x > -2$.  
     $$\operatorname{Dom}(f) = (-2, +\infty)$$

> 💼 **Sentido Económico vs Matemático:**  
> Matemáticamente, $f(x) = 100 - 2x$ existe para $x = -50$. Pero si $x$ son kilos de naranjas, **no existen los kilos negativos**. En economía casi siempre se añade la restricción implícita $x \ge 0$.

---

## 2. Catálogo de Funciones Elementales (Las Formas Visuales)

### 2.1. Funciones Lineales: Rectas ($f(x) = ax + b$)
* **$a$ es la pendiente (inclinación):**
  - Si $a > 0$: La recta es **creciente** (hacia arriba).
  - Si $a < 0$: La recta es **decreciente** (hacia abajo).
  - Si $a = 0$: La recta es **horizontal** constante ($f(x) = b$).
* **$b$ es la ordenada en el origen:** El punto exacto donde la recta corta el eje vertical $Y$ (cuando $x = 0$).

### 2.2. Funciones Cuadráticas: Parábolas ($f(x) = ax^2 + bx + c$)
* Si $a > 0$: Las ramas van hacia arriba (forma de $\cup$, "parábola contenta"). Tiene un **mínimo** en el vértice (típico para **minimizar costes**).
* Si $a < 0$: Las ramas van hacia abajo (forma de $\cap$, "parábola triste"). Tiene un **máximo** en el vértice (típico para **maximizar beneficios**).
* **Vértice (Punto clave):**
  $$x_{\text{vértice}} = -\frac{b}{2a}$$

### 2.3. Otras Gráficas Clave
* **Proporcionalidad Inversa:** $f(x) = \frac{1}{x}$. Es una hipérbola con asíntotas en los ejes (si produces más unidades, el coste fijo unitario baja hacia cero).
* **Valor Absoluto:** $f(x) = |x|$. Convierte todo a positivo (forma de $V$).
* **Exponenciales:** $f(x) = a^x$ (con $a > 0$).
  - Si $a > 1$: Crecimiento explosivo (ej: interés compuesto $C_n = C_0(1+i)^n$).
  - Si $0 < a < 1$: Decrecimiento exponencial (ej: depreciación de maquinaria).
* **Logaritmos:** $f(x) = \ln(x)$. Es la función inversa de la exponencial ($e^{\ln x} = x$). Solo existe para $x > 0$, pasa por el punto $(1, 0)$ y crece muy despacio.

---

## 3. Las Funciones de la Economía y la Empresa

En la carrera todas las letras raras cobran sentido con estas 7 fórmulas básicas:

| Función | Fórmula | Explicación en palabras sencillas |
| :--- | :---: | :--- |
| **Coste Total** | $C(x) = C_v(x) + C_F$ | Coste variable (materias primas por unidad) + Coste fijo (alquiler del local). |
| **Ingreso Total** | $I(x) = p \cdot x$ | Precio de venta $p$ multiplicado por la cantidad de unidades vendidas $x$. |
| **Beneficio** | $B(x) = I(x) - C(x)$ | Lo que entra en caja menos lo que cuesta producir. Si $B > 0$, ganas dinero. |
| **Demanda** | $Q_D = f(p)$ | Cantidad que los clientes quieren comprar según el precio $p$ (suele ser decreciente: si sube el precio, compran menos). |
| **Oferta** | $Q_S = g(p)$ | Cantidad que las empresas quieren vender según el precio $p$ (suele ser creciente: si sube el precio, les interesa producir más). |
| **Producción** | $Q = f(K) \text{ ó } f(L)$ | Cantidad de producto final obtenido según las máquinas $K$ o trabajadores $L$ empleados. |
| **Utilidad** | $U(q)$ | Placer o satisfacción personal que siente el consumidor al consumir $q$ unidades de un bien. |

---

## 4. Límites de una Función de una Variable

El límite responde a la pregunta: ***"Si la $x$ se va acercando cada vez más al número $x_0$, ¿hacia qué número se va disparando el resultado $f(x)$?"***

$$\lim_{x \to x_0} f(x) = L$$

### 4.1. Límites Laterales: La Regla del Encuentro
* $\lim_{x \to x_0^+} f(x)$: Acercarse a $x_0$ por la **derecha** (valores más grandes, ej: $2.01, 2.001$).
* $\lim_{x \to x_0^-} f(x)$: Acercarse a $x_0$ por la **izquierda** (valores más pequeños, ej: $1.99, 1.999$).

> ⚠️ **TEOREMA FUNDAMENTAL:**  
> El límite en un punto existe **SI Y SOLO SI los dos límites laterales existen y son idénticos**:
> $$\lim_{x \to x_0^+} f(x) = \lim_{x \to x_0^-} f(x) = L \iff \lim_{x \to x_0} f(x) = L$$
> Si por la izquierda da 4 y por la derecha da 7, el límite global **NO EXISTE**.

### 4.2. Las 7 Indeterminaciones Matemáticas
Cuando al sustituir un límite te sale algo que no se puede calcular directamente:

$$\frac{0}{0}, \quad \frac{\infty}{\infty}, \quad +\infty - \infty, \quad 0 \cdot \infty, \quad 0^0, \quad \infty^0, \quad 1^\infty$$

*(Indeterminación significa que no sabemos el resultado a simple vista y hay que operar, simplificar o factorizar).*

---

## 5. Continuidad de una Variable: "La Prueba del Lápiz"

Una función es continua en un punto $x_0$ si su gráfica no tiene saltos, agujeros ni asíntotas.

Matemáticamente requiere cumplir **3 condiciones**:
1. **Existe $f(x_0)$:** El punto pertenece al dominio.
2. **Existe $\lim_{x \to x_0} f(x)$:** Los límites por la izquierda y derecha coinciden en un número finito.
3. **Coinciden ambos:** 
   $$\lim_{x \to x_0} f(x) = f(x_0)$$

### 💡 Propiedades Rápidas para Exámenes:
* **Polinomios:** Siempre continuos en todo $\mathbb{R}$.
* **Exponenciales y racionales:** Continuas en todo su dominio (solo dan problemas donde el denominador se anula).
