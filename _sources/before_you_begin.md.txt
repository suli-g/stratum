# Before You Begin
### Stratum: Full-Stack Development from First Principles

---

This document is your honest checklist before starting the course.
Read it in full before opening Lesson 1.

The course teaches everything it uses — with one exception: the knowledge
listed below is assumed. For each item, you will find a description of
*why* it matters, *how much* you need to know, and *where* to fill any gap.

---

## What This Course Teaches

You do not need prior knowledge of any of the following — the course builds
each from scratch:

- System architecture and how to document it
- Django and Django REST Framework
- React hooks and modern React patterns
- Full-stack integration between a React frontend and a Django backend
- CLI code generation tools in Node.js
- Unit testing in both Django and React

---

## Tier 3 — True Prerequisites

These are assumed without apology. If you do not have them, acquire them
before beginning — the course will not slow down to cover them.

### T3.1 — Using the Terminal

**What you need:** Open a terminal, navigate directories with `cd`, run
commands, understand what a path is, read basic error output.

**Why it matters:** Every lesson from Level 2 onwards runs commands.
You will use the terminal constantly.

**Resource if needed:**
[The Missing Semester of Your CS Education — Shell Tools](https://missing.csail.mit.edu/2020/shell-tools/)
(MIT OpenCourseWare, free, ~1 hour)

---

### T3.2 — Basic Programming Concepts

**What you need:** Variables, functions, conditionals, loops, basic data
structures (list, dictionary/object). Language does not matter — these
concepts transfer.

**Why it matters:** Code examples throughout the course assume you can
read and reason about basic programs.

**Resource if needed:**
[CS50P — Introduction to Programming with Python](https://cs50.harvard.edu/python/)
(Harvard, free, ~20 hours for the basics)

---

### T3.3 — Object-Oriented Programming Basics

**What you need:** What a class is. What an instance is. What fields
(attributes) and methods are. What inheritance means at a conceptual level.

**Why it matters:** L01 uses class diagrams. Level 2 uses Django models,
which are classes. Level 3 uses React components, which are functions
but modelled using class-diagram thinking.

**Resource if needed:**
[Real Python — Object-Oriented Programming in Python 3](https://realpython.com/python3-object-oriented-programming/)
(Free, ~45 minutes)

---

## Tier 2 — Assumed with Gaps Acceptable

For these topics, the course assumes you have some exposure. You do not need
mastery — but you should have seen these concepts before. If you have not,
invest the time indicated before reaching the relevant level.

---

### T2.1 — HTTP Fundamentals

**What you need:** What a request and response are. What HTTP verbs are
(GET, POST, PUT, DELETE). What a status code means (200, 201, 400, 404, 500).
What headers are. What a URL structure is.

**Why it matters:** Level 2 builds a REST API. Level 4 connects the
frontend to it. You cannot reason about APIs without HTTP.

**Needed before:** Level 2, Lesson 9 (REST Principles & API Design)

**Resource:**
[MDN — An Overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
(Free, ~30 minutes)

---

### T2.2 — JSON

**What you need:** What JSON is. How to read a JSON object and array.
The relationship between JSON and Python dicts / JavaScript objects.

**Why it matters:** Every API request and response in this course uses JSON.

**Needed before:** Level 2, Lesson 14 (DRF Serializers)

**Resource:**
[MDN — Working with JSON](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/JSON)
(Free, ~20 minutes)

---

### T2.3 — Python Syntax

**What you need:** Read and write basic Python. Functions, classes,
decorators (what they do, not how to write one), list comprehensions,
f-strings, imports.

**Why it matters:** The entire backend (Levels 2, 4) is Python/Django.
You do not need to be fluent — but you must be able to read Python
code and write basic functions and classes.

**Needed before:** Level 2, Lesson 10 (Django's Philosophy)

**Resource:**
[Official Python Tutorial](https://docs.python.org/3/tutorial/)
(Free, ~4–6 hours for Chapters 1–9)

---

### T2.4 — JavaScript Syntax

**What you need:** Variables (`const`, `let`), arrow functions, array
methods (`map`, `filter`, `reduce`), object destructuring, spread operator,
async/await, ES module imports/exports.

**Why it matters:** The entire frontend (Levels 3, 4) is JavaScript/React.
Modern React relies heavily on arrow functions, destructuring, and async/await.

**Needed before:** Level 3, Lesson 22 (The Hooks Mental Model)

**Resource:**
[javascript.info — The Modern JavaScript Tutorial](https://javascript.info/)
(Free — focus on: Variables, Functions, Objects, Promises, Modules)
(~6–8 hours for the relevant sections)

---

### T2.5 — Basic HTML and CSS

**What you need:** What an HTML element is. Block vs inline elements.
What a CSS class and ID are. How to link a stylesheet. The box model.

**Why it matters:** React components render HTML. You need to be able
to read component output and style components.

**Needed before:** Level 3, Lesson 22

**Resource:**
[MDN — Getting Started with the Web](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website)
(Free, ~3 hours)

---

### T2.6 — What a Database Is

**What you need:** Tables, rows, and columns. What a primary key is.
What a foreign key is at a conceptual level. What a query is.
You do not need to write SQL.

**Why it matters:** Level 2 (Django Models) maps directly to database
concepts. You cannot understand why Django models look the way they do
without understanding what they produce.

**Needed before:** Level 2, Lesson 12 (Models, Relationships & Database Design)

**Resource:**
[Khan Academy — Intro to SQL: Querying and managing data](https://www.khanacademy.org/computing/computer-programming/sql)
(Free — first two sections only, ~1.5 hours)

---

### T2.7 — Git Basics

**What you need:** `git init`, `git add`, `git commit`, `git push`, `git pull`.
What a repository is. What a commit is.

**Why it matters:** Level 1, Lesson 5 covers *professional* git workflow —
it assumes you already know the basics.

**Needed before:** Level 1, Lesson 5 (Git Workflow & Debugging Methodology)

**Resource:**
[Git — The Simple Guide](https://rogerdudler.github.io/git-guide/)
(Free, ~20 minutes)

:::{note}
L05 introduces the **Conventional Commits** specification — a structured
format for commit messages (`feat(scope): description`). You do not need
to know this before starting; it is taught in full in L05. However, if
you want to preview it:
[Conventional Commits v1.0.0](https://www.conventionalcommits.org/)
(Free, ~10 minutes reading)
:::

---

### T2.8 — Regular Expressions (Basics)

**What you need:** What a regular expression is. What `.`, `*`, `+`, `?`,
`^`, `$`, `[]`, and `()` mean. How to read a basic pattern.

**Why it matters:** Level 5 (the generator) uses regular expressions
to patch registry files. Lesson 45 (Registry Patchers) requires you
to read and write basic regex.

**Needed before:** Level 5, Lesson 45 (Registry Patchers)

**Resource:**
[RegexOne — Learn Regular Expressions](https://regexone.com/)
(Free, ~1 hour)

---

## Tier 1 — Taught Internally

These are used by the course and taught by the course before they are used.
You do not need prior knowledge of any of the following:

| Topic | Taught in |
|---|---|
| UML class diagram notation | L01 §3 (UML Primer) |
| C4 model | L03 |
| PlantUML syntax | L03 |
| REST principles (formal) | L09 |
| Django (all of it) | L10–L20 |
| DRF (all of it) | L14–L18 |
| React hooks | L23–L28 |
| useReducer + Context as architecture | L31 |
| Test-Driven Development | L06 (philosophy), L20 (Django), L32 (React) |
| Code generation concepts | L43 |

---

## Time Estimate

If you have strong Python and JavaScript and have used the terminal:
- Fill T3 gaps (if any): 0–2 hours
- Fill T2 gaps (if any): 2–6 hours
- You are ready to begin

If you are newer to programming:
- T3 gaps: 20–30 hours
- T2 gaps: 10–20 hours
- This is normal — the investment pays off in every subsequent lesson

---

## Platform & Diagram Rendering

This course is published on **GitHub Pages** and built with **Sphinx**.
When you read the course at its GitHub Pages URL, all diagrams render
automatically — you do not need to install anything.

**Reading locally (VS Code):**

Install two extensions to preview diagrams without building the site:

- [Markdown Preview Mermaid Support](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid) — renders Mermaid diagrams
- [PlantUML extension](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml) — renders PlantUML diagrams

GFM callout boxes (`> [!NOTE]`, `> [!WARNING]` etc.) render correctly
in VS Code's built-in Markdown preview without any extension.

**Building the course locally (optional):**

```bash
pip install sphinx myst-parser sphinxcontrib-mermaid sphinxcontrib-plantuml
# Install PlantUML (required for sphinxcontrib-plantuml):
# macOS:   brew install plantuml
# Ubuntu:  sudo apt install plantuml
# Windows: choco install plantuml
sphinx-build -b html . _build/html
```

**Two diagram tools are used:**

| Tool | Used for |
|---|---|
| **Mermaid** | Flowcharts, sequence diagrams, ER diagrams, class diagrams |
| **PlantUML** | C4 architecture diagrams, use case diagrams, component diagrams, deployment diagrams |

---

## A Note on UML

UML (Unified Modelling Language) class diagrams appear from Lesson 1
and throughout the course. The course teaches you how to read them
in L01 §3 — you do not need prior knowledge. This note exists so you
are not surprised when you encounter one immediately.

---

*Before You Begin is referenced from L01 and updated when new lessons
reveal additional assumptions. Last reviewed: Session 10.*
