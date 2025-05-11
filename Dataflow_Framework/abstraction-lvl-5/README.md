# 📦 Level 5 – DAG Routing and Conditional Flows

This level introduces directed acyclic graph (DAG)-based pipeline orchestration with tag-aware conditional routing of lines between processors.

---

## 🧠 Overview
- In this level, the processing model evolves from a linear pipeline to a flexible DAG, allowing:

- Conditional flow of data between processors using tags.

- Multiple downstream paths depending on the semantic tag of each line (e.g., errors, warnings, general).

- Modular, stateful processors that can be reused across paths.

- Seamless support for fan-out and fan-in structures in pipelines.

- Each processor takes a single input line, returns tagged output, and the routing logic uses the tag to determine the next node(s) in the DAG.

---

## 📁 Folder Structure
abstraction-level-5/
├── cli.py
├── main.py
├── pipeline.py
├── routing.py
├── types.py
├── processors/
│   ├── __init__.py
│   ├── core.py
│   ├── tagging.py
│   └── counting.py
├── input.txt
└── pipeline.yaml
🚀 Run Instructions


Make sure you're inside the abstraction-level-5/ directory.
Then run the CLI command as follows:
```
bash
python cli.py process --input input.txt --config pipeline.yaml
```
This will execute the DAG pipeline defined in pipeline.yaml using the data from input.txt.

---

## 🛠 Features Introduced
- ✅ Tag-based routing between processors

- ✅ Conditional branches in the processing graph

- ✅ Support for stateful processors (e.g., line counter)

- ✅ Multiple output paths based on content classification
-
- ✅ Easy extensibility by adding new nodes or edge rules in the config

---

## 📌 Highlights
- 🧩 Composable architecture: Each processor is independently testable and pluggable.

- 🧠 Routing engine: Clean separation between processor logic and flow control.

- 🏷️ Tagged line semantics: Enables context-aware routing, error/warning handling, and filtering.

- 🔁 Reusability: Existing str -> Iterator[TaggedLine] processors remain compatible.

