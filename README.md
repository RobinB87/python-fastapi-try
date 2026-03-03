Small BE project to try out FastAPI a bit

# Install

1. Create virtual environment

```bash
python -m venv venv
```

2. Activate it

```bash
source venv/bin/activate
```

3. Install base FastAPI dependencies

```bash
pip install fastapi "uvicorn[standard]"
```

4. Run

```bash
uvicorn main:app --reload
```

# Testing

1. Install pytest and httpx

```bash
pip install pytest
pip install httpx
```

2. Run tests

```bash
python -m pytest
```

# Project structure
The file __init__.py marks a directory as a Python package, which allows you to import from it.