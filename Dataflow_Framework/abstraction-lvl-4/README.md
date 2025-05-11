# 🔁 Level 4 – Stream Processing and State

Welcome to **Level 4**, where we leave behind simple line-by-line functions and move into **stream-based, stateful processing**! 
---

## 🎯 Objectives

✅ Transform all processors to use the interface:

```python Iterator[str] -> Iterator[str]
```

✅ Reuse existing str -> str processors via a wrapper/decorator

✅ Support stateful processors (e.g., counters, buffers)

✅ Enable fan-in/fan-out behavior (emit fewer or more lines than received)

✅ Introduce processors that take configuration on init

---

## 🧠 Why Stream Processing?
- The old model (str -> str) had serious limitations:

❌ Could not drop or duplicate lines

❌ Could not keep state across lines

❌ Could not process multi-line logic (grouping, joining)

Now, each processor can process a stream and return a stream, giving you full control and expressiveness.

---

## 📦 Folder Structure
abstraction-level-4/
├── cli.py
├── core.py
├── main.py
├── pipeline.py
├── types.py
├── pipeline.yaml
└── processors/
    ├── __init__.py
    ├── upper.py       # stateless (wrapped)
    ├── splitter.py    # fan-out
    ├── counter.py     # stateful

---

## 🚀 Run the Pipeline
```bash
python cli.py process-command --input input.txt --config pipeline.yaml
```

## 🧪 Testing Tips
✅ Stateless functions can be unit tested with mocked iterators.

✅ Fan-out processors should be tested with multi-yield expectations.

✅ Stateful processors need sequence tests to validate line history or counters.

## 💡 Design Insights
- [str] -> Iterator[str]	✅
- Reuse of old str -> str funcs	✅ via wrapper
- Stateful processors	✅
- Fan-in / fan-out behaviors	✅
- Configurable processors	✅ (basic)
- Testable in isolation	✅

