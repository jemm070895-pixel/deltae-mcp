# ΔE MCP v2.1

**Experimental software conformance/audit contract — independent reproducibility and empirical evaluation.**

## What is ΔE?

ΔE MCP v2.1 is an experimental, frozen software conformance/audit contract for transformations of information. It records and checks whether changed coordinates are explicitly accounted for by admissible, target-bound witnesses, while preserving uncertainty when available evidence is insufficient.

Possible outcomes include:

- `PASS`
- `FAIL`
- `UNKNOWN`
- `UNMAPPABLE`
- `INVALID_INPUT`

ΔE is **not a truth oracle** and does not claim to establish semantic correctness.

## Current evidence

The v2.1 line has undergone internal adversarial testing, clean-room reconstruction, and differential interoperability testing.

In a tested clean-room domain, an independently written implementation matched the frozen reference on **100,000 seeded requests with zero divergences**.

These results establish reproducibility **within the tested domain**. They do **not** establish novelty, superiority, general semantic correctness, or productivity benefit.

## External participation

There are now three deliberately separate ways to participate:

- **A — Clean-room implementation:** independently implement the public behavioral specification before seeing evaluator secrets.
- **B — Cross-machine execution:** run a frozen sanitized package on another real computer/runtime and preserve the first result.
- **C — Comparative study:** join a randomized crossover comparison of ΔE versus conventional written requirements.

See **[External experiments](experiments/README.md)** for the exact purpose, safeguards, and claim boundary of each route.

## Current independent-validation stage

The project is seeking genuinely independent reproduction.

A clean-room volunteer receives a frozen public behavioral specification and independently creates a Python implementation without access to the original implementation, evaluator oracle, hidden tests, or expected hidden-test answers. AI assistance is permitted if disclosed.

Evaluator material remains separate so that an independent result can later be tested without leaking expected answers in advance.

## Comparative empirical study

A separate randomized crossover study has also been prepared to test an open empirical question:

> Does using a structured ΔE contract/toolchain, compared with conventional written requirements, measurably affect implementation time, hidden-case correctness, clarification burden, maintenance time, or maintenance regressions?

This is a hypothesis to be tested, **not a claim that ΔE is better**.

The study requires a cohort of independent implementers: **at least 8 participants, preferably 12 or more**. Positive, neutral, and negative results are all informative.

## Public/private boundary

This public repository intentionally excludes:

- hidden evaluation cases;
- expected hidden-test outputs;
- evaluator oracle/reference material;
- private volunteer returns before evaluation;
- secret material that could compromise an independent reproduction.

Historical packages that contain reference/oracle/expected material are also kept out of the public participation paths when their publication could contaminate a later blind exercise.

## Project status

**Experimental validation in progress.**

## Maintainer

**Jorge Martínez** — independent, self-taught developer/researcher based in Phoenix, Arizona.
