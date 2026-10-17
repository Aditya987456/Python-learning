## Chapter-0 : installation done.

<br>

## Python Virtual Environment (`venv`)

A virtual environment is an isolated Python environment for a project.

It keeps the project's Python packages separate from the system Python and from other projects.

### Why use it?

Suppose I have two projects:

- Project A needs Flask 2.x
- Project B needs Flask 3.x

Installing everything globally can cause conflicts.

With a virtual environment, each project can have its own packages and versions.

<br>

### Whole Workflow :



#### Create
```bash
python -m venv .venv
```

#### Activate
```bash
source .venv/bin/activate
```

#### Install packages
```bash
python -m pip install <package>
```

#### Work on the project
```bash
python main.py
```

#### Deactivate when finished
```bash
deactivate
```

