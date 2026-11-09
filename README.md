# QSenti [WIP]
A lightweight sentiment classifier for LLM sessions that batches conversations, scores each message’s sentiment with VADER, and rates overall session health using quantum-inspired interference.

# Example

```python
from qsenti import score_conversation, flush

# Executes qsenti core function, returns None so no variable store.
score_conversation([
    "Can you help me fix this?",
    "Sure, try this...",
    "That didn't work. This is so annoying.",
])
# {'coherence': 0.31, 'label': 'frustrated'}

# This saves the slot-based json to a permanent local file. 
flushed = flush(json_file_path)
# {
# '1': [
#    "Can you help me fix this?",
#    "Sure, try this...",
#    "That didn't work. This is so annoying.",
# ],
# 'senti': {'coherence' 0.31, 'label': 'frustrated'},
# }

```
