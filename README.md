# AI Quality Operations Copilot

## Problem statement
QA teams and program leaders need a repeatable way to review solved contact tickets against the approved knowledge base / SOP. The target solution will classify a ticket, explain the reason, and point to the exact supporting KB/SOP step.

## Primary users
- QA
- Program leaders
- Stakeholders who need auditable quality signals

## Input / output contract
**Input:** a solved contact ticket shared by the user.

**Output:**
1. Classification
2. Reason for the classification
3. Evidence: the supporting KB/SOP step number

## Success metrics (initial)
The project will be evaluated on four measurable dimensions:

- **Answer quality:** target >=90% correct classification on the controlled evaluation set.
- **Evidence hit rate:** target >=95% of accepted answers cite the expected KB/SOP step.
- **Refusal behavior:** 100% of out-of-scope / unsupported cases should avoid fabricated evidence.
- **Latency:** establish a baseline first; optimize only after accuracy and evidence quality are stable.

These are project targets, not current measured results.

## Current scope (T003)
This checkpoint establishes the Python project structure, local environment, runnable package, tests, and project README. LLM, RAG, evaluation, UI, and deployment work will be added in later tasks.

## Local setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m pytest -q
```

## Run the skeleton

```bash
python -m ai_quality_operations_copilot "Customer reports an unauthorized refund request"
```

The current implementation is deliberately deterministic. It exists to prove the input/output contract before AI components are introduced.

## Evidence for T003
- Repository structure exists under `src/` and `tests/`.
- Local virtual environment created as `.venv/` (excluded from source control).
- Test suite passes.
- README contains users, problem statement, input/output contract, and measurable success metrics.
- Next step: T018 Git/GitHub workflow on this real project.
