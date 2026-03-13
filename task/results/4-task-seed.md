# Task 4 — The `seed` Parameter

## Request

| Field | Value |
|---|---|
| **Model** | `gpt-4o` (rounds 1–3), `gemini-2.0-flash` (round 4) |
| **Question** | `Name a random animal.` |
| **System prompt** | `You are an assistant who answers concisely and informatively.` |
| **Fixed param** | `n=5` across all rounds |
| **Varying param** | `seed` |

---

## Results

### 🎲 Round 1 — `gpt-4o` | `n=5` | No seed → expect variety

| Choice | Animal |
|---|---|
| 0 | Okapi |
| 1 | Okapi |
| 2 | Axolotl |
| 3 | Okapi |
| 4 | Okapi |


---

### 🔒 Round 2 — `gpt-4o` | `n=5` | `seed=42` → expect convergence

| Choice | Animal |
|---|---|
| 0 | Okapi |
| 1 | Axolotl |
| 2 | Axolotl |
| 3 | Okapi |
| 4 | Okapi |


---

### 🔒 Round 3 — `gpt-4o` | `n=5` | `seed=42` → re-run to confirm reproducibility

| Choice | Animal |
|---|---|
| 0 | Okapi |
| 1 | Okapi |
| 2 | Axolotl |
| 3 | Red panda |
| 4 | Okapi |


---

### 🌐 Round 4 — `gemini-2.0-flash` | `n=5` | `seed=42` → seed silently ignored

| Choice | Animal |
|---|---|
| 0 | Elephant |
| 1 | Elephant |
| 2 | Elephant |
| 3 | Elephant |
| 4 | Okapi |

Gemini silently ignores the `seed` parameter — no error
Re-running would produce a different pattern each time.

---

## Comparison Table

| Round | Model | Seed | Animals seen | Reproducible? |
|---|---|---|---|---|
| 1 | `gpt-4o` | None | Okapi ×4, Axolotl ×1 | ❌ Changes each run |
| 2 | `gpt-4o` | `42` | Okapi ×3, Axolotl ×2 | ✅ Best effort |
| 3 | `gpt-4o` | `42` | Okapi ×3, Axolotl ×1, Red panda ×1 | ✅ Same candidates, minor drift |
| 4 | `gemini-2.0-flash` | `42` | Elephant ×4, Okapi ×1 | ❌ Seed ignored |

---