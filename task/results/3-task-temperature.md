# Task 3 — The `temperature` Parameter

---

## Request

| Field | Value |
|---|---|
| **Model** | `gpt-4o` |
| **Question** | `Describe the sound that the color purple makes when it's angry.` |
| **System prompt** | `You are an assistant who answers concisely and informatively.` |
| **Varying parameter** | `temperature` |

---

## Results

### 🌡️ `temperature=0.0` — Deterministic

> Colors don't produce sounds, but if we were to imagine purple expressing anger, it might evoke a deep, resonant hum or a sharp, vibrating crackle—like the tension of a storm or the low growl of thunder.

---

### 🌡️ `temperature=0.5` — Balanced

> Colors don't produce sounds, but imagining purple as an angry sound might evoke something deep, resonant, and intense—like a low, vibrating hum or a thunderous rumble, reflecting its rich and complex nature.

---

### 🌡️ `temperature=1.5` — Creative

> While colors don't produce sounds naturally, describing the sound purple might metaphorically make when angry could evoke imagery or emotional tones. It might feel deep, booming, and throbbing, like low vibrating bass or thunder rumbling in the distance — rich yet aggressive, with a velvety undertone of restraint or turmoil.


---

### 🌡️ `temperature=2.0` — Near-maximum

> Colors don't produce sounds, but if we were to romanticize the idea of purple expressing anger, one might describe it as a low, droning hum, resonant like a groan at dusk, building pressure and wavering on the edge of cracking thunder.


---

### ❌ `temperature=2.1` — Invalid (API error)

```
HTTP 400: {
  "error": {
    "message": "Invalid 'temperature': decimal above maximum value. Expected a value <= 2, but got 2.1 instead.",
    "type": "invalid_request_error",
    "param": "temperature",
    "code": "decimal_above_max_value"
  }
}
```
