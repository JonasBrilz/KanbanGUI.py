![MIT](https://img.shields.io/badge/license-MIT-blue.svg)
![ci-tests](https://github.com/JonasBrilz/KanbanGUI.py/actions/workflows/tests.yml/badge.svg)

# KanbanGUI.py

**Description:**

Prototype CRUD interface for Kanban project management in Python using BSON documents.

**CRUD Functionality:**

**C**reate Items, such as Epics, Tasks and Subtasks 

**R**ead Items' Contents

**U**pdate Items during their entire lifespan

**D**elete Items when unnecessary

## Installation

1. [Clone Project](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
2. Install UV: Follow instructions at https://docs.astral.sh/uv/getting-started/installation/
3. Enter your MongoDB credentials in file `resources/credentials.txt`
4. Install dependencies using `uv sync`
5. Run Project using `uv run --active python -m module`
6. Start creating Items with the 'Add Item'-Button

## Tests

When Creating the project, measures were taken to create a robust testing suite to ensure functionality and reliability.

**Build Status:**

GitHub Actions CI-Testing workflow status:

![ci-tests](https://github.com/JonasBrilz/KanbanGUI.py/actions/workflows/tests.yml/badge.svg)

**Local Testing:**

Run the tests locally by following these steps:
1. [Clone Project](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
2. Install UV: Follow instructions at https://docs.astral.sh/uv/getting-started/installation/
3. Install dependencies using `uv sync`
4. Run Tests using `uv run --active pytest`

## License

MIT License

Copyright (c) 2024 Jonas Brilz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
