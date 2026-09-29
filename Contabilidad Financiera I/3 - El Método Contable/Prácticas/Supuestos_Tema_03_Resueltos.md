# 📑 Supuestos Prácticos Resueltos Paso a Paso — Tema 3: El Método Contable

- **Asignatura:** Contabilidad Financiera I (Cód. 2344)
- **Centro:** Facultad de Economía y Empresa — Universidad de Murcia
- **Tema:** Tema 3 — El Método Contable y la Partida Doble
- **Material de Origen:** Boletín Oficial UMU (`CONTABILIDAD1_SUPUESTOS_TEMA_3.pdf`)

---

## 📌 SUPUESTO 3.1 — "Mister ONK" (Bocadillos de Chato Murciano)

### 1. Análisis de las Operaciones en el Libro Diario y Libro Mayor

#### Asiento 1: Constitución de la Sociedad
María y Teresa constituyen la empresa aportando $20.000$ € que ingresan en la cuenta del Banco Santander.
```
20.000  (572) Bancos c/c (Santander)
            a  (100) Capital Social             20.000
```

#### Asiento 2: Compra de Hornos Especiales y Frigoríficos
Adquisición de maquinaria por $30.000$ €. Se pagan $15.000$ € por banco, se acepta una letra a 2 años por $10.000$ € y el resto ($5.000$ €) a pagar en 6 meses.
```
30.000  (213) Maquinaria
            a  (572) Bancos c/c                  15.000
            a  (175) Efectos a pagar a L/P       10.000
            a  (523) Proveedores de inmov. C/P    5.000
```

#### Asiento 3: Préstamo Bancario a 5 años
El Banco Santander concede préstamo de $120.000$ € a devolver en 5 años, abonado en cuenta corriente.
```
120.000 (572) Bancos c/c
            a  (170) Deudas a L/P ent. crédito  120.000
```

#### Asiento 4: Compra del Local Comercial al Contado
Local por $100.000$ € al contado bancario (Terreno: $70.000$ €, Edificio: $30.000$ €).
```
 70.000 (210) Terrenos y bienes naturales
 30.000 (211) Construcciones
            a  (572) Bancos c/c                 100.000
```

#### Asiento 5: Compra de Motocicleta de Reparto
Motocicleta por $26.000$ €: la mitad ($13.000$ €) al contado por banco y la mitad aceptando letra a 6 meses.
```
 26.000 (218) Elementos de transporte
            a  (572) Bancos c/c                  13.000
            a  (525) Efectos a pagar a C/P       13.000
```

#### Asiento 6: Compra de Chato Murciano (Materia Prima)
Compra de carne/materia prima por $100$ € a pagar en 60 días.
```
    100 (310) Materias primas
            a  (400) Proveedores                    100
```

#### Asiento 7: Devolución Parcial del Préstamo Bancario
Amortización de $10.000$ € del préstamo del Banco Santander con cargo a la cuenta bancaria.
```
 10.000 (170) Deudas a L/P ent. crédito
            a  (572) Bancos c/c                  10.000
```

---

### 2. Libro Mayor (Cuentas en T)

```
        (572) Bancos c/c                       (100) Capital Social
    DEBE      │     HABER                  DEBE      │     HABER
──────────────┼──────────────          ──────────────┼──────────────
(1)  20.000   │  15.000  (2)                         │   20.000  (1)
(3) 120.000   │ 100.000  (4)                         │
              │  13.000  (5)                         │
              │  10.000  (7)                         │
──────────────┼──────────────                        │
    140.000   │ 138.000                              │
Saldo Deudor = 2.000 €                 Saldo Acreedor = 20.000 €

        (213) Maquinaria                   (170) Deudas L/P ent. crédito
    DEBE      │     HABER                  DEBE      │     HABER
──────────────┼──────────────          ──────────────┼──────────────
(2)  30.000   │                        (7)  10.000   │  120.000  (3)
──────────────┼──────────────          ──────────────┼──────────────
Saldo Deudor = 30.000 €                Saldo Acreedor = 110.000 €

 (210) Terrenos y bienes nat.                 (211) Construcciones
    DEBE      │     HABER                  DEBE      │     HABER
──────────────┼──────────────          ──────────────┼──────────────
(4)  70.000   │                        (4)  30.000   │
──────────────┼──────────────          ──────────────┼──────────────
Saldo Deudor = 70.000 €                Saldo Deudor = 30.000 €

   (218) Elementos de transporte             (175) Efectos a pagar L/P
    DEBE      │     HABER                  DEBE      │     HABER
──────────────┼──────────────          ──────────────┼──────────────
(5)  26.000   │                                      │   10.000  (2)
──────────────┼──────────────                        │
Saldo Deudor = 26.000 €                Saldo Acreedor = 10.000 €

 (523) Prov. inmovilizado C/P                (525) Efectos a pagar C/P
    DEBE      │     HABER                  DEBE      │     HABER
──────────────┼──────────────          ──────────────┼──────────────
              │   5.000  (2)                         │   13.000  (5)
Saldo Acreedor = 5.000 €               Saldo Acreedor = 13.000 €

      (310) Materias primas                       (400) Proveedores
    DEBE      │     HABER                  DEBE      │     HABER
──────────────┼──────────────          ──────────────┼──────────────
(6)     100   │                                      │      100  (6)
Saldo Deudor = 100 €                   Saldo Acreedor = 100 €
```

---

### 3. Balance de Situación Final de "Mister ONK"

```
          ACTIVO (Estructura Económica)         |        PASIVO Y PN (Estructura Financiera)
================================================+===================================================
A) ACTIVO NO CORRIENTE                156.000 € | A) PATRIMONIO NETO                        20.000 €
   • Terrenos y bienes naturales:      70.000 € |    • Capital Social:                      20.000 €
   • Construcciones:                   30.000 € | 
   • Maquinaria:                       30.000 € | B) PASIVO NO CORRIENTE                   120.000 €
   • Elementos de transporte:          26.000 € |    • Deudas a L/P con ent. crédito:      110.000 €
                                                |    • Efectos a pagar a largo plazo:       10.000 €
B) ACTIVO CORRIENTE                     2.100 € | 
   • Existencias (Materias primas):       100 € | C) PASIVO CORRIENTE                       18.100 €
   • Tesorería (Bancos c/c):            2.000 € |    • Efectos a pagar a corto plazo:       13.000 €
                                                |    • Proveedores de inmovilizado C/P:      5.000 €
                                                |    • Proveedores:                            100 €
------------------------------------------------+---------------------------------------------------
TOTAL ACTIVO:                         158.100 € | TOTAL PATRIMONIO NETO Y PASIVO:          158.100 €
```
$$\mathbf{\text{Verificación: } 158.100\text{ € (Activo)} = 138.100\text{ € (Pasivo Total)} + 20.000\text{ € (Neto)} \quad \checkmark}$$

---

## 📌 SUPUESTO 3.2 — "Computerizando S.L." (Deducción de Hechos Contables)

A partir de la evolución diaria del cuadro de elementos patrimoniales:

1. **Día 1:** Clientes disminuye en $500$ € ($1.000 \to 500$) y Efectivo aumenta en $500$ € ($8.000 \to 8.500$).  
   * **Enunciado propuesto:** *"Los clientes pagan en efectivo $500$ € de las facturas que tenían pendientes de cobro."* (Hecho permutativo de activo).
2. **Día 2:** Inmovilizado Material aumenta en $1.500$ € ($7.000 \to 8.500$), Efectivo disminuye en $500$ € ($8.500 \to 8.000$) y Deudas con proveedores aumenta en $1.000$ € ($3.000 \to 4.000$).  
   * **Enunciado propuesto:** *"Se adquiere mobiliario/maquinaria para la oficina por $1.500$ €, pagando $500$ € en efectivo y acordando pagar los $1.000$ € restantes a plazo."*
3. **Día 3:** Efectivo disminuye en $3.000$ € ($8.000 \to 5.000$) y Capital Social disminuye en $3.000$ € ($15.000 \to 12.000$).  
   * **Enunciado propuesto:** *"La sociedad acuerda una reducción de capital social con devolución de aportaciones en efectivo a los socios por importe de $3.000$ €."*
4. **Día 4:** Efectivo disminuye en $600$ € ($5.000 \to 4.400$) y Deudas con proveedores disminuye en $600$ € ($4.000 \to 3.400$).  
   * **Enunciado propuesto:** *"Se realiza un pago en efectivo de $600$ € para amortizar deudas pendientes con los proveedores."*
5. **Día 5:** Ordenadores (existencias) aumenta en $1.000$ € ($2.000 \to 3.000$), Efectivo disminuye en $400$ € ($4.400 \to 4.000$) y Proveedores aumenta en $600$ € ($3.400 \to 4.000$).  
   * **Enunciado propuesto:** *"Se compran ordenadores destinados a la venta por importe de $1.000$ €, pagando $400$ € en efectivo y dejando a deber los $600$ € restantes a los proveedores."*
6. **Día 6:** Ordenadores disminuye en $2.000$ € ($3.000 \to 1.000$), Clientes aumenta en $1.500$ € ($500 \to 2.000$) y Efectivo aumenta en $500$ € ($4.000 \to 4.500$).  
   * **Enunciado propuesto:** *"Se venden ordenadores a precio de coste por valor de $2.000$ €, cobrando $500$ € en efectivo y concediendo a los clientes aplazamiento de pago por los $1.500$ € restantes."*

---

## 📌 SUPUESTO 3.3 — Sociedad de Cursos de Golf

### Asientos en el Libro Diario

#### 0. Constitución de la Sociedad
Capital de $100.000$ € (60% en Banco Santander y 40% en Caja).
```
60.000  (572.1) Banco Santander
40.000  (570)   Caja, euros
            a  (100) Capital Social            100.000
```

#### 1. Firma de Préstamos
BBVA a 6 años ($120.000$ €), Caixabank a 4 años ($7.000$ €) y particular a 1 año ($3.000$ € en caja).
```
120.000 (572.2) BBVA c/c
  7.000 (572.3) Caixabank c/c
  3.000 (570)   Caja, euros
            a  (170.1) Deudas L/P con ent. crédito BBVA  120.000
            a  (170.2) Deudas L/P ent. crédito Caixabank   7.000
            a  (521)   Deudas a corto plazo (particular)   3.000
```

#### 2. Adquisición de Dólares al Contado
Compra de $600$ $ al tipo de cambio $1$ € = $1$ $ con efectivo de caja.
```
   600  (571) Caja, moneda extranjera
            a  (570) Caja, euros                    600
```

#### 3. Compra del Campo de Golf
Precio total $200.000$ €: Terreno ($100.000$ €), Edificio ($60.000$ €) y Carritos eléctricos ($40.000$ €).  
Se pagan $167.000$ € por bancos (Santander y BBVA) y el resto ($33.000$ €) al contado por caja.
```
100.000 (210) Terrenos y bienes naturales
 60.000 (211) Construcciones
 40.000 (218) Elementos de transporte (carritos)
            a  (572.1) Banco Santander          60.000
            a  (572.2) BBVA c/c                107.000
            a  (570)   Caja, euros              33.000
```

#### 4. Mobiliario con Letra a 7 meses
```
 50.000 (216) Mobiliario
            a  (525) Efectos a pagar a C/P      50.000
```

#### 5. Adquisición de Marca Registrada "Augusta Challenge"
Adquisición de propiedad industrial por $600$ $ al contado con los dólares de caja.
```
   600  (203) Propiedad industrial
            a  (571) Caja, moneda extranjera        600
```

#### 6. Compra de Ordenadores e Impresora
Equipos por $6.000$ €: $1.000$ € en efectivo, letra a 6 meses por $500$ €, letra a 16 meses por $2.500$ € y crédito simple a 18 meses por $2.000$ €.
```
  6.000 (217) Equipos para procesos de inf.
            a  (570) Caja, euros                 1.000
            a  (525) Efectos a pagar a C/P         500
            a  (175) Efectos a pagar a L/P       2.500
            a  (173) Proveedores inmov. L/P      2.000
```

#### 7. Solicitud de Presupuesto por Colegio
> ⚠️ **NO SE REGISTRA:** La solicitud o emisión de un presupuesto es un acto informativo que no altera el patrimonio de la empresa en ese momento.

#### 8. Venta de Carritos Eléctricos al Precio de Coste
Venta por $40.000$ €: cobrando la mitad ($20.000$ €) al contado por caja y el resto ($20.000$ €) a cobrar en 6 meses.
```
 20.000 (570) Caja, euros
 20.000 (543) Créditos a C/P por enajenación inmovilizado
            a  (218) Elementos de transporte    40.000
```

#### 9. Pago Anticipado de Deuda de Ordenadores (a 18 meses)
Pago de la deuda comercial de $2.000$ € mediante caja.
```
  2.000 (173) Proveedores de inmovilizado L/P
            a  (570) Caja, euros                 2.000
```

#### 10. Imposición a Plazo Fijo a 6 meses
Apertura de depósito a plazo de $1.000$ € en efectivo.
```
  1.000 (548) Imposiciones a corto plazo
            a  (570) Caja, euros                 1.000
```

#### 11. Compra de Acciones de Inditex y Obligaciones a Corto Plazo por BBVA
Acciones de Inditex por $500$ € y deuda pública por $1.000$ € a través del BBVA.
```
    500 (540) Inversiones financieras C/P instrumentos patrimonio
  1.000 (541) Valores representativos de deuda a C/P
            a  (572.2) BBVA c/c                  1.500
```

---

### Saldos Finales de Tesorería:
- **Caja (570):** Entradas: $40.000 + 3.000 + 20.000 = 63.000$ €. Salidas: $600 + 33.000 + 1.000 + 2.000 + 1.000 = 37.600$ €. Saldo Deudor: $\mathbf{25.400\text{ €}}$.
- **Banco Santander (572.1):** Entradas $60.000$ €; Salidas $60.000$ €. Saldo: $\mathbf{0\text{ €}}$.
- **BBVA (572.2):** Entradas $120.000$ €; Salidas $107.000 + 1.500 = 108.500$ €. Saldo Deudor: $\mathbf{11.500\text{ €}}$.
- **Caixabank (572.3):** Saldo Deudor: $\mathbf{7.000\text{ €}}$.
- **Total Tesorería:** $25.400 + 11.500 + 7.000 = \mathbf{43.900\text{ €}}$.

---

## 📌 SUPUESTO 3.4 — Cálculo de Magnitudes Desconocidas en Balances

Aplicando la Ecuación Fundamental: $\mathbf{\text{Activo Total} = \text{Pasivo Total} + \text{Patrimonio Neto}}$

| Magnitud | Sociedad W | Sociedad X | Sociedad Y | Sociedad Z |
| :--- | :---: | :---: | :---: | :---: |
| Capital Social | 78.000 € | 50.000 € | 45.000 € | 20.000 € |
| Reservas | 12.000 € | 19.100 € | 14.300 € | **3.000 € (?)** |
| Resultado del Ejercicio | 6.970 € | 1.100 € | **-5.000 € (?)** | -2.600 € |
| **PATRIMONIO NETO** | **96.970 €** | **70.200 €** | **54.300 €** | **20.400 €** |
| Cuentas a pagar (Pasivo) | **8.530 € (?)** | 17.800 € | 22.700 € | 6.600 € |
| **TOTAL PASIVO + NETO** | **105.500 €** | **88.000 €** | **77.000 €** | **27.000 €** |
| Maquinaria | 71.800 € | **56.850 € (?)** | 40.000 € | 15.000 € |
| Cuentas a cobrar | 31.000 € | 27.520 € | 18.600 € | 9.870 € |
| Bancos y caja | 2.700 € | 3.630 € | 18.400 € | 2.130 € |
| **TOTAL ACTIVO** | **105.500 €** | **88.000 €** | **77.000 €** | **27.000 €** |

---

## 📌 SUPUESTO 3.5 — Clasificación en el Cuadro de Cuentas del PGC: "Bastet S.L."

| Descripción del Elemento | Grupo | N.º Cuenta | Denominación Oficial PGC | Masa Patrimonial |
| :--- | :---: | :---: | :--- | :---: |
| Facturas a pagar a suministradores de porcelana | **4** | **400** | Proveedores | **PC** |
| Letras de cambio a pagar a suministradores | **4** | **401** | Proveedores, efectos comerciales a pagar | **PC** |
| Acciones del Banco Santander a largo plazo | **2** | **250** | Inversiones financieras a L/P inst. patrimonio | **ANC** |
| Factura pendiente de pago al asesor (plan de viabilidad) | **4** | **410** | Acreedores por prestaciones de servicios | **PC** |
| Acciones de Telefónica para vender antes de un año | **5** | **540** | Inversiones financieras a C/P inst. patrimonio | **AC** |
| Préstamo recibido del Banco Santander a 10 años | **1** | **170** | Deudas a largo plazo con entidades de crédito | **PNC** |
| Pagaré pendiente al arrendador nave mes de marzo | **4** | **411** | Acreedores, efectos comerciales a pagar | **PC** |
| Facturas a cobrar por venta de gatos de la suerte | **4** | **430** | Clientes | **AC** |
| Letras de cambio y pagarés a cobrar por ventas | **4** | **431** | Clientes, efectos comerciales a cobrar | **AC** |
| Letras del Tesoro a cobrar en 6 meses | **5** | **541** | Valores representativos de deuda a C/P | **AC** |
| Factura a 90 días por compra de herramientas duraderas | **5** | **523** | Proveedores de inmovilizado a corto plazo | **PC** |
| Cantidades entregadas por clientes a cuenta de pedidos | **4** | **438** | Anticipos de clientes | **PC** |
| Facturas y letras a cobrar en 22 meses por venta furgoneta| **2** | **253** | Créditos a L/P por enajenación inmovilizado | **ANC** |
| Pago a Ayuntamiento por derecho expositores (15 meses) | **2** | **202** | Concesiones administrativas | **ANC** |
| Facturas y letras a cobrar en 6 meses por venta de mesa | **5** | **543** | Créditos a C/P por enajenación inmovilizado | **AC** |
| Pagarés y letras a pagar en 2 años por compra de horno | **1** | **175** | Efectos a pagar a largo plazo | **PNC** |
| Vehículos de reparto propiedad de la empresa | **2** | **218** | Elementos de transporte | **ANC** |
| Cuenta a plazo fijo de 6 meses en banco | **5** | **548** | Imposiciones a corto plazo | **AC** |
| Obligaciones del Estado a 5 meses hasta vencimiento | **5** | **541** | Valores representativos de deuda a C/P | **AC** |
| Factura a cobrar por servicio de transporte eventual | **4** | **440** | Deudores | **AC** |
| Factura a pagar en 1 mes por compra de impresora | **5** | **523** | Proveedores de inmovilizado a corto plazo | **PC** |
| Programas informáticos de nóminas y contabilidad | **2** | **206** | Aplicaciones informáticas | **ANC** |
| Terreno adquirido con el propósito de especular/venderlo | **2** | **220** | Inversiones en terrenos y bienes naturales | **ANC** |
| La Hacienda Pública le debe a Bastet 1.000 € | **4** | **470** | Hacienda Pública, deudora por diversos conceptos| **AC** |
| Pagaré a 120 días por compra de programas informáticos | **5** | **525** | Efectos a pagar a corto plazo | **PC** |
| Deuda con Hacienda Pública a corto plazo por impuestos | **4** | **475** | Hacienda Pública, acreedora conceptos fiscales | **PC** |
| Depósito a plazo fijo a 2 años | **2** | **258** | Imposiciones a largo plazo | **ANC** |
| Deuda a corto plazo con la Seguridad Social | **4** | **476** | Organismos de la Seguridad Social, acreedores | **PC** |
| Préstamo concedido a otra empresa a devolver en 20 meses | **2** | **252** | Créditos a largo plazo | **ANC** |
| Patente adquirida para fabricar los gatos (23.000 €) | **2** | **203** | Propiedad industrial | **ANC** |
| Porcelana en almacén para elaborar los gatos | **3** | **310** | Materias primas | **AC** |
| Gatos de la suerte elaborados y terminados | **3** | **350** | Productos terminados | **AC** |

---

## 📌 SUPUESTO 3.6 — Efecto de Asientos y Balance Final

### 1. Análisis del Impacto de Cada Asiento en el Balance Inicial

1. **Asiento 1:** $6.000$ (253) Créditos a L/P por enajenación inmovilizado a (213) Maquinaria $6.000$.  
   * *Efecto:* Permutativo de Activo No Corriente. Disminuye el Inmovilizado Material en $6.000$ € y aumenta en $6.000$ € las Inversiones Financieras a L/P. El Activo No Corriente sigue sumando **126.000 €**.
2. **Asiento 2:** $50$ (400) Proveedores a (570) Caja, euros $50$.  
   * *Efecto:* Pago de deudas comerciales. Disminuye la Tesorería en $50$ € y disminuye el Pasivo Corriente (Acreedores comerciales) en $50$ €.
3. **Asiento 3:** $100$ (430) Clientes a (300) Mercaderías $100$.  
   * *Efecto:* Permutativo de Activo Corriente. Se dan de baja existencias por $100$ € (quedando a $0$ €) y surge derecho de cobro en Deudores comerciales por $+100$ €.
4. **Asiento 4:** $18.000$ (520) Deudas a C/P con ent. crédito a (572) Bancos c/c $18.000$.  
   * *Efecto:* Se amortiza la totalidad de las deudas financieras a corto plazo iniciales ($-18.000$ €) pagando con tesorería bancaria ($-18.000$ €).
5. **Asiento 5:** $1.000$ (572) Bancos c/c a (540) Inversiones financieras C/P $1.000$.  
   * *Efecto:* Permutativo de Activo Corriente. Se venden las acciones temporales recuperando $1.000$ € de liquidez bancaria (las IF C/P quedan a $0$ €).
6. **Asiento 6:** $60.000$ (170) Deudas a L/P ent. crédito a (520) Deudas a C/P ent. crédito $60.000$.  
   * *Efecto:* **Reclasificación temporal de pasivo.** Se trasladan $60.000$ € de deuda que antes vencía a largo plazo al corto plazo porque vencerá en el ejercicio siguiente. Disminuye el Pasivo No Corriente en $60.000$ € y aumenta el Pasivo Corriente en $+60.000$ €.
7. **Asiento 7:** $60.000$ (170) Deudas a L/P ent. crédito a (100) Capital Social $60.000$.  
   * *Efecto:* **Capitalización de deuda bancaria.** La entidad bancaria canjea el resto de su deuda a largo plazo por acciones de la compañía, convirtiéndose en socia. Se extingue el Pasivo No Corriente ($-60.000 \to 0$ €) y aumenta el Patrimonio Neto (Capital Social $+60.000 \to 80.000$ €).

---

### 2. Balance de Situación Final

* **Activo No Corriente:** $126.000$ € ($120.000$ Inmovilizado material $+ 6.000$ Créditos L/P).
* **Activo Corriente:**
  * Existencias: $100 - 100 = 0$ €
  * Deudores comerciales (Clientes): $+100$ €
  * Inversiones financieras C/P: $1.000 - 1.000 = 0$ €
  * Tesorería (Efectivo y bancos): $31.000 - 50\text{ (caja)} - 18.000\text{ (banco)} + 1.000\text{ (banco)} = 13.950$ €
  * Total Activo Corriente: $100 + 13.950 = \mathbf{14.050\text{ €}}$
* **TOTAL ACTIVO:** $126.000 + 14.050 = \mathbf{140.050\text{ €}}$

* **Patrimonio Neto:** Capital Social $= 20.000 + 60.000 = \mathbf{80.000\text{ €}}$
* **Pasivo No Corriente:** Deudas a largo plazo $= 120.000 - 60.000\text{ (as. 6)} - 60.000\text{ (as. 7)} = \mathbf{0\text{ €}}$
* **Pasivo Corriente:**
  * Deudas a corto plazo con entidades de crédito: $18.000 - 18.000\text{ (as. 4)} + 60.000\text{ (as. 6)} = 60.000$ €
  * Acreedores comerciales (Proveedores): $100 - 50\text{ (as. 2)} = 50$ €
  * Total Pasivo Corriente: $60.000 + 50 = \mathbf{60.050\text{ €}}$
* **TOTAL PATRIMONIO NETO Y PASIVO:** $80.000 + 0 + 60.050 = \mathbf{140.050\text{ €}}$

$$\mathbf{\text{Verificación: } 140.050\text{ € (Activo)} = 60.050\text{ € (Pasivo)} + 80.000\text{ € (Neto)} \quad \checkmark}$$
