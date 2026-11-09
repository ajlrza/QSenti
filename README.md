# QuantumSentimentor [WIP]
A lightweight logger for LLM apps that batches conversations, scores each message’s sentiment with VADER, and rates overall session health using quantum-inspired interference.

# Example

```python
from qsenti import score_conversation

result = score_conversation([
    {"role": "user", "content": "Can you help me fix this?"},
    {"role": "assistant", "content": "Sure, try this..."},
    {"role": "user", "content": "That didn't work. This is so annoying."},
])
# {'coherence': 0.31, 'label': 'frustrated'}
```
