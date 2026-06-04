# 🎮 Gamepad Radial Keyboard – Prototype

## 1. Goal
Create an alternative text input method using a gamepad instead of a physical keyboard.
The system is based on directional (radial) selection and confirmation buttons.

---

## 2. Control Scheme

| Control | Action |
|------|------|
| Left Stick | Direction selection (8-way) |
| RT | Confirm selection |
| B | Backspace |
| LB / RB | Cursor movement (future) |
| LT | Modifier (future – diacritics) |

---

## 3. Input Model

### Two-stage selection:
1. Group selection (8 directions)
2. Letter selection (within group)

---

## 4. English Layout (Frequency-based)

```python
GROUPS = {
    "UP":    ["E", "T", "A"],
    "LEFT":  ["O", "I", "N"],
    "RIGHT": ["R", "S", "H"],
    "DOWN":  ["L", "D", "U"],

    "UP_RIGHT":   ["C", "M", "F", "W"],
    "UP_LEFT":    ["G", "Y", "P"],
    "DOWN_RIGHT": ["B", "V", "K"],
    "DOWN_LEFT":  ["J", "X", "Q", "Z"],
}


---

## 🔚 Závěrem
Teď máš:
- **jasný koncept**
- **uzavřený layout**
- **přenosný prompt**
- **pracovní dokument**

👉 Doporučení:  
V nové instanci GPT-5.5 začni **skeletonem Python projektu** a implementací **input + stavového automatu**.

Až budeš chtít, klidně se sem vrať a porovnáme verze.  
Tenhle projekt má **opravdu dobrý základ**.