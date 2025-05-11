# 🧭 Level 6 – State-Based Routing System
In this level, we implement a state-driven processor routing system where each processor decides the next state (tag) based on logic, allowing for fine-grained control, reusability, and data-directed flows.

---

## 🚀 Overview
In this system:

- Input lines are assigned an initial state (start).

- Each processor handles lines tagged with a specific state.

- Processors emit new (tag, line) pairs, guiding them to the next processor.

- Routing is no longer a static DAG but driven by tags and a processor map.

- The system reads its configuration from a config.yaml, dynamically importing the processors.


This level emphasizes:

- State transitions over static routing

- Configurable and extensible pipelines

- A centralized Router class managing execution

---

## 📁 Folder Structure
abstraction-level-6/
├── cli.py                  # Typer CLI entrypoint
├── main.py                 # Main runner
├── router.py               # Core state-routing engine
├── config.yaml             # Configurable routing map
├── input.txt               # Sample input lines
└── processors/             # Modular processing units
    ├── start.py
    ├── filters.py
    ├── formatters.py
    └── output.py

---

## ▶️ How to Run
Make sure you're in the abstraction-level-6/ directory and run:
```
bash
python cli.py process input.txt config.yaml
```

This will:

- Load lines from input.txt

- Route them through processors based on config.yaml

- Print final output to the terminal

---

## 🛠️ Key Concepts
- Router	Controls the flow of data by tag/state transitions
- config.yaml	Declares how tags map to specific processor functions
- processors/	Each file defines processing logic for a specific tag/state
- start.py	Initial tag assignment (e.g. error, warn, general)
- filters.py	Filters or modifies error and warning flows
- formatters.py	Applies transformations (e.g. snakecase)
- output.py	Terminal output for finished lines

---

## 📌 Additional Notes
- ✅ Each processor returns (next_tag, new_line), making routing dynamic.

- ⚙️ New processors can be plugged in by updating config.yaml.

- 🚫 Invalid or missing tags raise errors to prevent undefined flows.

- 🔄 Infinite loops are possible if processors re-tag lines without resolution—consider adding guards in future levels.
