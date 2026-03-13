# Task 7 — The `presence_penalty` Parameter


---

## Request

| Field | Value |
|---|---|
| **Model** | `gpt-4o` |
| **Question** | `What is entropy in LLM responses?` |
| **System prompt** | `You are an assistant who answers concisely and informatively.` |
| **Varying param** | `presence_penalty` |

---

## Results

###  `presence_penalty=-2.0` — Hyper-focused, deep, no branching

> In the context of large language models (LLMs), entropy measures the uncertainty or unpredictability of the model's response. It quantifies the diversity or randomness of the model's predicted probability distribution over the next token or word. A higher entropy indicates the model is less confident in predicting the next token (more uncertainty), while lower entropy suggests greater confidence or more deterministic responses. It is often used in applications like temperature scaling or sampling to control the creativity or diversity of the model's outputs.

**Topics covered:** entropy, probability distribution, uncertainty, token prediction — nothing else.

---

###  `presence_penalty=0.0` — Default baseline

> Entropy in LLM (Large Language Model) responses refers to the measure of uncertainty or randomness in the probabilities assigned to various possible next tokens when generating a response. It quantifies how "surprising" or unpredictable the distribution of token choices is.
>
> - **Low entropy**: Indicates the model is confident about what the next token should be, often leading to repetitive or generic responses.
> - **High entropy**: Suggests more randomness or diversity in token selection, which can result in more varied and creative responses but risks being incoherent.
>
> Controlling entropy helps balance predictability and creativity in the output of LLMs.

**Topics covered:** entropy definition, low vs high entropy contrast, creativity/predictability tradeoff.


---

### `presence_penalty=1.0` — Starts branching into adjacent concepts

> Entropy in the context of large language models (LLMs) refers to a measure of uncertainty or randomness in their generated responses. It quantifies the diversity or unpredictability in the probability distribution over possible tokens (words or characters) during text generation. Lower entropy indicates more predictable, concentrated outputs, while higher entropy reflects greater variability.
>
> For example:
> - **Low Entropy:** The model generates highly deterministic and predictable answers (e.g., repeating common phrases or safe responses).
> - **High Entropy:** The output becomes more diverse but may risk incoherence or less relevance if the randomness is excessive.
>
> Adjusting entropy-related parameters like **temperature** allows fine-tuning the balance between creativity and precision in LLM outputs.

**Topics covered:** entropy, low/high contrast, *token granularity ("words or characters")*, **temperature** (new topic introduced).

**Observation:** Compared to `0.0`, a new topic appeared — **temperature** — as the closing point. The model is being nudged away from entropy-specific vocabulary toward adjacent concepts. The structure is also slightly richer (*"For example:"*).

---

###  `presence_penalty=2.0` — Maximum topic diversity

> In the context of large language models (LLMs) like GPT, **entropy** refers to the level of randomness or unpredictability in the model's generated responses. It's a measure derived from **information theory** that quantifies how uncertain or diverse the model's choices are when picking words during text generation.
>
> - **Low entropy** means more predictable and repetitive responses, often resembling human-like determinism.
> - **High entropy** indicates greater diversity or creativity but risks incoherence if it's too high.
>
> Entropy can be influenced by settings such as **temperature**, which adjusts the probability distribution over possible next tokens. Lower temperatures result in deterministic outputs (lower entropy), while higher temperatures encourage more varied outcomes (higher entropy).

**Topics covered:** entropy, **information theory** (new), low/high contrast, **temperature** (explained in depth), probability distribution, determinism vs creativity.
