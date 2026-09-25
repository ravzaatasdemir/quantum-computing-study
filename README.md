# Quantum Computing Study

A shared workspace for learning quantum computing: curated resources, study notes, and code — from linear algebra basics to quantum algorithms, noisy hardware, and error correction.

Everyone in the group adds their own notes and notebooks here. The goal is to learn by deriving things on paper and then implementing them from scratch.

## Repository structure

```
quantum-computing-study/
├── RESOURCES.md        # All courses, books, docs and tools (with links)
├── CONTRIBUTING.md     # How to add your work
├── requirements.txt    # Shared Python environment
├── notes/              # Short Markdown notes and summaries, by topic
├── notebooks/          # Jupyter notebooks, one folder per topic
│   ├── 00-setup/
│   ├── 01-linear-algebra/
│   ├── 02-qubits-and-gates/
│   ├── 03-entanglement/
│   ├── 04-algorithms/
│   ├── 05-noise-and-hardware/
│   ├── 06-variational/
│   └── 07-error-correction/
├── src/qsim/           # Shared, reusable code (e.g. our own NumPy state-vector simulator)
└── members/            # Personal scratch space: members/<github-username>/
```

## Getting started

```bash
git clone https://github.com/ravzaatasdemir/quantum-computing-study.git
cd quantum-computing-study
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python notebooks/00-setup/check_setup.py
```

If the last command prints a Bell-state histogram with roughly equal `00` and `11` counts, your environment works.

## Topics

| # | Topic | Covers |
|---|-------|--------|
| 01 | Linear algebra | Complex numbers, Dirac notation, unitary/Hermitian matrices, eigenvalues, tensor products |
| 02 | Qubits and gates | Single-qubit gates, Bloch sphere, measurement, quantum circuits |
| 03 | Entanglement | Bell states, teleportation, superdense coding, CHSH game |
| 04 | Algorithms | Deutsch–Jozsa, Bernstein–Vazirani, Simon, QFT, phase estimation, Shor, Grover |
| 05 | Noise and hardware | Density matrices, channels, transpilation, noise models, error mitigation |
| 06 | Variational | VQE, QAOA, quantum machine learning |
| 07 | Error correction | Shor code, stabilizer formalism, surface codes |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). In short: work on a branch, name files with your GitHub username, open a pull request.

## License

Code is released under the [MIT License](LICENSE). Linked resources belong to their respective authors.
