#  CS13A – Automata Theory and Formal Languages  
### **Lab 2 – Final Term (1st Sem 2024-2025)**

*Topic:* Conversion of Mealy Machine to Moore Machine  
*subject:* CS13A – Automata Theory and Formal Languages  
*Student:* John Albert Yabut  
*course* 3 BSCS A




##  Given Transition Table

| State | 0, Output | 1, Output |
|:------|:-----------|:---------|
|   A   |    A, A    |    B, B  |
|   B   |    C, A    |    D, B  |
|   C   |    D, C    |    B, B  |
|   D   |    B, B    |    C, C  |
|   E   |    D, C    |    E, C  |

---

**Transition Representation:**  
Each arrow is labeled as **Input / Output**

```mermaid
graph LR
    A((A))
    B((B))
    C((C))
    D((D))
    E((E))

    A -->|0 / A| A
    A -->|1 / B| B
    B -->|0 / A| C
    B -->|1 / B| D
    C -->|0 / C| D
    C -->|1 / B| B
    D -->|0 / B| B
    D -->|1 / C| C
    E -->|0 / C| D
    E -->|1 / C| E




##  2. Converted Moore Machine

Each state now has a **single fixed output**.

| Mealy State | Output | New Moore State   |
|-------------|----------|---------------- |
|     A       |     A    |       A_A       |
|     A       |     B    |       A_B       |
|     B       |     A    |       B_A       |
|     B       |     B    |       B_B       |
|     C       |     B    |       C_B       |
|     C       |     C    |       C_C       |
|     D       |     B    |       D_B       |
|     D       |     C    |       D_C       |
|     E       |     C    |       E_C       |

---

### Moore Machine Transitions


    A_init(["A_init (start)"])
    A_A(["A_A / A"])
    A_B(["A_B / B"])
    B_B(["B_B / B"])
    C_A(["C_A / A"])
    C_C(["C_C / C"])
    D_B(["D_B / B"])
    D_C(["D_C / C"])
    E_C(["E_C / C"])

    A_init -->|0| A_A
    A_init -->|1| A_B

    A_A -->|0| A_A
    A_A -->|1| A_B

    A_B -->|0| C_A
    A_B -->|1| C_C

    B_B -->|0| C_A
    B_B -->|1| D_B

    C_A -->|0| D_C
    C_A -->|1| B_B

    C_C -->|0| D_C
    C_C -->|1| B_B

    D_B -->|0| B_B
    D_B -->|1| C_C

    D_C -->|0| B_B
    D_C -->|1| C_C

    E_C -->|0| D_C
    E_C -->|1| E_C



