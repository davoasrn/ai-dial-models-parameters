# Task 5 — The `max_tokens` Parameter

---

## Request

| Field | Value |
|---|---|
| **Model** | `gpt-4o` |
| **Question** | `What is a token when working with LLMs?` |
| **System prompt** | `You are an assistant who answers concisely and informatively.` |
| **Varying param** | `max_tokens` |

---

## Results

### `max_tokens=10` — Brutally truncated

**`finish_reason`: `"length"` **

**`completion_tokens` used:** `10` / `10`

---

### `max_tokens=50` — Mid-explanation cut

**`finish_reason`: `"length"` **

**`completion_tokens` used:** `50` / `50`

---

### `max_tokens=500` — Natural completion

**`finish_reason`: `"stop"` **

**`completion_tokens` used:** `167` / `500`

---