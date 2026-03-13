# Task 8 — The `stop` Parameter

```python
stop="\n\n"                         
stop=["word1", "word2", "phrase3"]  
```

---

## Request

| Field | Value |
|---|---|
| **Model** | `gpt-4o` |
| **Question** | `Explain the key components of a Large Language Model architecture.` |
| **System prompt** | `You are an assistant who answers concisely and informatively.` |

A structured question was chosen so it produces clear section headers — making it easy to see exactly where a specific stop string intercepts the output.

---

## Results

### Round 1 — No `stop` — full baseline

> A Large Language Model (LLM) architecture primarily consists of the following key components:
>
> 1. **Tokenization** — Converts input text into tokens...
> 2. **Embedding Layer** — Maps tokens to dense numerical vectors...
> 3. **Transformer Architecture** — The backbone of most modern LLMs...
> 4. **Positional Encoding** — Encodes position information of tokens...
> 5. **Model Layers** — Stacked layers of transformer blocks...
> 6. **Output Layer** — Produces predictions via softmax...
> 7. **Training Objective** — Autoregressive or masked language modeling...
> 8. **Optimization and Training** — Adam, learning rate scheduling, gradient clipping...
> 9. **Scaling** — Expanding vocabulary, hidden dimensions, attention heads...
>
> *These components collectively enable LLMs to understand and generate human-like natural language efficiently.*

**`finish_reason`: `"stop"` | `completion_tokens`: ~350**

---

### Round 2 — `stop="\n\n"` — halts at first blank line

**`finish_reason`: `"stop"` | `completion_tokens`: 21**

> A Large Language Model (LLM) typically relies on a Transformer-based architecture. Its key components include:

---

### Round 3 — `stop=["**Transformer Blocks**", "**Transformer Block**"]` — section-level intercept

**`finish_reason`: `"stop"` | `completion_tokens`: 97**

> Large Language Models (LLMs) are built on deep learning architectures, primarily Transformer-based models. Key components of their architecture include:
>
> 1. **Input Embedding Layer**: Converts input tokens into dense vector representations...
> 2. **Positional Encoding**: Adds information about the order of tokens...
> 3.

---

### Round 4 — Guardrail demo: `stop=["Apple is", "Apple has the best", "Apple leads"]`

**`finish_reason`: `"stop"` | `completion_tokens`: 312**

The model returned a full, detailed comparison of iPhone vs other brands — the guardrail **did not trigger**.

**Why?** `gpt-4o` structured the answer as:
> `**iPhone (Apple):**`
> `- **Strengths**: High build quality, seamless integration with Apple's ecosystem...`
