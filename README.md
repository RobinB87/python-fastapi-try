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