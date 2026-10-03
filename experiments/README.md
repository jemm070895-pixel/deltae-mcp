# External experiments

ΔE currently welcomes independent participation through three deliberately separate experimental routes.

## A — Clean-room implementation
Implement the frozen public behavioral specification without seeing the originating implementation, evaluator oracle, hidden challenge, hidden tests, or expected hidden-test answers before freeze.

This route is intended to test independent implementability/reproduction of the supplied behavioral contract. It does not establish novelty, universality, or semantic correctness.

Start here: [clean-room/README.md](clean-room/README.md)

## B — Cross-machine execution
Run a frozen execution package on another real computer/runtime and return the first result unchanged.

This route tests execution/portability behavior in another environment. It is **not** equivalent to an independent clean-room implementation.

Start here: [cross-machine/README.md](cross-machine/README.md)

## C — Comparative study
Participate in a randomized crossover study comparing a structured ΔE contract/toolchain with conventional written requirements.

Target outcomes include implementation time, hidden-case correctness, clarification burden, maintenance time, and maintenance regressions. The target cohort is at least 8 participants, preferably 12 or more.

Start here: [comparative-study/README.md](comparative-study/README.md)

## Experimental separation
Results from these routes are recorded separately. A successful run in one route is not silently promoted into evidence for another route.

## Protected evaluator boundary
This repository does not publish hidden evaluation cases, expected hidden-test outputs, evaluator oracle/reference material, or private volunteer returns that could compromise a blind evaluation.
