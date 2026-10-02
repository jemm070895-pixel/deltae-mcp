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

## Current independent-validation stage

The project is now seeking genuinely independent reproduction.

A volunteer receives a frozen public behavioral specification and independently creates a Python implementation without access to the original implementation, evaluator oracle, hidden tests, or expected hidden-test answers. AI assistance is permitted if disclosed.

Evaluator material remains separate so that an independent result can later be tested without leaking expected answers in advance.

## Comparative empirical study

A separate randomized crossover study has also been prepared to test an open empirical question:

> Does using a structured ΔE contract/toolchain, compared with conventional written requirements, measurably affect implementation time, hidden-case correctness, clarification burden, maintenance time, or maintenance regressions?

This is a hypothesis to be tested, **not a claim that ΔE is better**.

The study requires a cohort of independent implementers: **at least 8 participants, preferably 12 or more**. Positive, neutral, and negative results are all informative.

This comparative study is separate from the individual clean-room reproduction exercise.

## Participation

Independent developers, research software engineers, researchers, and students interested in software reproducibility or independent implementation are welcome to ask about either validation exercise.

Participation is voluntary and unpaid. Participation does not imply endorsement of ΔE or its claims.

## Public/private boundary

This public repository intentionally excludes:

- hidden evaluation cases;
- expected hidden-test outputs;
- evaluator oracle/reference material;
- private volunteer returns before evaluation;
- secret material that could compromise an independent reproduction.

## Project status

**Experimental validation in progress.**

This repository is currently a public-facing project overview. Additional public materials will be added only after checking that they do not compromise ongoing independent evaluation.

## Maintainer

**Jorge Martínez** — independent, self-taught developer/researcher based in Phoenix, Arizona.
