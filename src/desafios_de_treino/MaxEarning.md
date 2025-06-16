# Teste de Mesa - Maximização de Ganhos com Dias de Folga

**Dados de Entrada:**
- `earnings = [60, 70, 80, 40, 80, 90, 100, 20]`
- `k = 3` (máximo de dias consecutivos trabalhados)

---

## Dia 0 (i=0)
- **Inicialização:**
  - `dp_work[0] = earnings[0] = 60` (trabalhar no dia 0)
  - `dp_skip[0] = 0` (folgar no dia 0)

---

## Dia 1 (i=1)
### Cálculo de `dp_work[1]` (trabalhar no dia 1)
- `min(k, i+1) = min(3, 2) = 2` → testar `j=1` e `j=2`

| j | Cálculo                                 | Valor |
|---|----------------------------------------|-------|
| 1 | `dp_skip[0] + earnings[1] = 0 + 70`    | 70    |
| 2 | `sum(earnings[:2]) = 60 + 70`          | 130   |

- **Resultado:** `dp_work[1] = max(70, 130) = 130`

### Cálculo de `dp_skip[1]` (folgar no dia 1)
- `max(dp_work[0], dp_skip[0]) = max(60, 0) = 60`

---

## Dia 2 (i=2)
### Cálculo de `dp_work[2]` (trabalhar no dia 2)
- `min(3, 3) = 3` → testar `j=1`, `j=2`, `j=3`

| j | Cálculo                                      | Valor |
|---|---------------------------------------------|-------|
| 1 | `dp_skip[1] + earnings[2] = 60 + 80`        | 140   |
| 2 | `dp_skip[0] + sum(earnings[1:3]) = 0 + 150` | 150   |
| 3 | `sum(earnings[:3]) = 60 + 70 + 80`          | 210   |

- **Resultado:** `dp_work[2] = max(140, 150, 210) = 210`

### Cálculo de `dp_skip[2]` (folgar no dia 2)
- `max(dp_work[1], dp_skip[1]) = max(130, 60) = 130`

---

## Dia 3 (i=3)
### Cálculo de `dp_work[3]` (trabalhar no dia 3)
- `min(3, 4) = 3` → testar `j=1`, `j=2`, `j=3`

| j | Cálculo                                      | Valor |
|---|---------------------------------------------|-------|
| 1 | `dp_skip[2] + earnings[3] = 130 + 40`       | 170   |
| 2 | `dp_skip[1] + sum(earnings[2:4]) = 60 + 120`| 180   |
| 3 | `dp_skip[0] + sum(earnings[1:4]) = 0 + 190` | 190   |

- **Resultado:** `dp_work[3] = max(170, 180, 190) = 190`

### Cálculo de `dp_skip[3]` (folgar no dia 3)
- `max(dp_work[2], dp_skip[2]) = max(210, 130) = 210`

---

## Dia 4 (i=4)
### Cálculo de `dp_work[4]` (trabalhar no dia 4)
- `min(3, 5) = 3` → testar `j=1`, `j=2`, `j=3`

| j | Cálculo                                      | Valor |
|---|---------------------------------------------|-------|
| 1 | `dp_skip[3] + earnings[4] = 210 + 80`       | 290   |
| 2 | `dp_skip[2] + sum(earnings[3:5]) = 130 + 120`| 250   |
| 3 | `dp_skip[1] + sum(earnings[2:5]) = 60 + 200`| 260   |

- **Resultado:** `dp_work[4] = max(290, 250, 260) = 290`

### Cálculo de `dp_skip[4]` (folgar no dia 4)
- `max(dp_work[3], dp_skip[3]) = max(190, 210) = 210`

---

## Dia 5 (i=5)
### Cálculo de `dp_work[5]` (trabalhar no dia 5)
- `min(3, 6) = 3` → testar `j=1`, `j=2`, `j=3`

| j | Cálculo                                      | Valor |
|---|---------------------------------------------|-------|
| 1 | `dp_skip[4] + earnings[5] = 210 + 90`       | 300   |
| 2 | `dp_skip[3] + sum(earnings[4:6]) = 210 + 170`| 380   |
| 3 | `dp_skip[2] + sum(earnings[3:6]) = 130 + 210`| 340   |

- **Resultado:** `dp_work[5] = max(300, 380, 340) = 380`

### Cálculo de `dp_skip[5]` (folgar no dia 5)
- `max(dp_work[4], dp_skip[4]) = max(290, 210) = 290`

---

## Dia 6 (i=6)
### Cálculo de `dp_work[6]` (trabalhar no dia 6)
- `min(3, 7) = 3` → testar `j=1`, `j=2`, `j=3`

| j | Cálculo                                      | Valor |
|---|---------------------------------------------|-------|
| 1 | `dp_skip[5] + earnings[6] = 290 + 100`      | 390   |
| 2 | `dp_skip[4] + sum(earnings[5:7]) = 210 + 190`| 400   |
| 3 | `dp_skip[3] + sum(earnings[4:7]) = 210 + 270`| 480   |

- **Resultado:** `dp_work[6] = max(390, 400, 480) = 480`

### Cálculo de `dp_skip[6]` (folgar no dia 6)
- `max(dp_work[5], dp_skip[5]) = max(380, 290) = 380`

---

## Dia 7 (i=7)
### Cálculo de `dp_work[7]` (trabalhar no dia 7)
- `min(3, 8) = 3` → testar `j=1`, `j=2`, `j=3`

| j | Cálculo                                      | Valor |
|---|---------------------------------------------|-------|
| 1 | `dp_skip[6] + earnings[7] = 380 + 20`       | 400   |
| 2 | `dp_skip[5] + sum(earnings[6:8]) = 290 + 120`| 410   |
| 3 | `dp_skip[4] + sum(earnings[5:8]) = 210 + 210`| 420   |

- **Resultado:** `dp_work[7] = max(400, 410, 420) = 420`

### Cálculo de `dp_skip[7]` (folgar no dia 7)
- `max(dp_work[6], dp_skip[6]) = max(480, 380) = 480`

---

## Resultado Final
`max(dp_work[-1], dp_skip[-1]) = max(420, 480) = 480`

**Sequência Ótima:**
1. Trabalhar dias 0-2 (60+70+80 = 210)
2. Folgar dia 3 (0)
3. Trabalhar dias 4-6 (80+90+100 = 270)
4. Folgar dia 7 (0)
**Total:** 210 + 0 + 270 + 0 = 480