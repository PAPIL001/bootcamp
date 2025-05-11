# ⚙️ Level 3 – Dynamic Loading of Processors

In this level, we upgrade our architecture to support **dynamic pipelines**, defined externally in a YAML config file. 

---

## 📦 Folder Structure

abstraction-level-3/
├── cli.py
├── core.py
├── main.py
├── pipeline.py
├── types.py
├── pipeline.yaml
└── processors/
├── init.py
├── snake.py
└── upper.py

---

## 🔧 Setup Instructions

### 1. Install required packages

```bash
pip install typer[all] PyYAML
```

### 2. Input example
```input.txt:
Hello World
This is Dynamic
```
pipeline.yaml:
pipeline:
  - type: processors.snake.to_snakecase
  - type: processors.upper.to_uppercase

  ---

## 🚀 How to Run
```bash
python cli.py process-command --input input.txt --config pipeline.yaml
```
To write output to a file:
```
bash
python cli.py process-command --input input.txt --config pipeline.yaml --output result.txt
```
Then view it:
```bash
cat result.txt
```

---

## 🧠 How It Works
- ✅ Dynamic Processor Loading
Each step in the YAML file defines a dotted path to a processor function. The pipeline.py file uses importlib to load these at runtime, forming a flexible and customizable pipeline.

yaml
- type: processors.snake.to_snakecase
This is dynamically resolved to:
python from processors.snake import to_snakecase

---

## 📌 Highlights
- Feature	Status✅
- YAML-driven pipeline	✅
- Plugin-like processor loading	✅
- Clean modular architecture	✅
T- yper CLI integration	✅
- Easy extension with new processors	✅
- Clear error handling for invalid configs	✅

---

## 🧱 Add New Processors
Just drop a new .py file in the processors/ folder with a str -> str function and refer to it in pipeline.yaml. No other changes required!

---

## 🛠️ Developer Notes
- Dynamic imports use importlib.import_module() and getattr() to load callables.

- All processors must follow the signature: Callable[[str], str].

- A strong separation of concerns is maintained:

- core.py → applies processing logic

- pipeline.py → builds processor list

- main.py → handles orchestration

- cli.py → user interface

