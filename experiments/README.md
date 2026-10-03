# External experiments — choose your route before inspecting materials

ΔE welcomes independent participation through three deliberately separate experimental routes.

> **Choose your route before opening its materials.**
>
> If you may want to perform **A — Clean-room implementation**, do **A first**. Route B exposes a ΔE implementation and can therefore prevent a later result from being classified as fully blind clean-room evidence. Prior exposure should be disclosed, not hidden.

## A — Clean-room implementation — public / self-service
Independently implement the frozen public behavioral specification without seeing the originating implementation, evaluator oracle, hidden challenge/tests, or expected hidden answers before freeze.

**Choose A if:** you want to provide independent implementation/reproduction evidence under the strongest available blindness boundary.

Public source-only package and instructions: [A — Clean-room](clean-room/README.md)

**Do not inspect Route B before freezing A.**

## B — Cross-machine execution — public / self-service
Run a frozen sanitized ΔE execution package on another authorized real computer/runtime and preserve the first result unchanged.

**Choose B if:** you want to test portability/execution in another environment and do not need to preserve fully blind Route A status.

Public execution package and instructions: [B — Cross-machine](cross-machine/README.md)

Route B exposes an implementation. It is execution/portability evidence, not independent clean-room implementation evidence.

## C — Comparative empirical study — public enrollment / pre-assignment
Join a randomized crossover comparison of a structured ΔE contract/toolchain and conventional written requirements.

**Choose C if:** you want to participate in the empirical comparison. The public ZIP is enrollment/pre-assignment only; experimental conditions are released after assignment to preserve the study design.

Public enrollment package and instructions: [C — Comparative study](comparative-study/README.md)

Target measures include implementation time, hidden-case correctness, clarification burden, maintenance time, and maintenance regressions. Intended cohort: at least 8 independent implementers, preferably 12 or more.

## Can I participate in more than one route?
Potentially, but **order and disclosure matter**. If fully blind A evidence is desired, complete and freeze A before inspecting B. Route C asks about prior exposure so it can be handled during assignment and analysis.

## Experimental separation
Results from A, B, and C are recorded separately. A result in one route is not silently promoted into evidence for another route. Positive, neutral, negative, and failed results can all be informative when preserved and reported accurately.

## Protected evaluator boundary
This repository does not publish hidden evaluation cases, expected hidden-test outputs, evaluator oracle/reference material, or private volunteer returns that could compromise a blind evaluation.

## Submit external results
Use the dedicated [ΔE external-results upload request](https://www.dropbox.com/request/3gu81cps1oqq7q2mwz8l). Contributors can upload files without access to the project Dropbox or other volunteers' submissions.

When practical, prefix filenames with `A_CLEANROOM_`, `B_CROSSMACHINE_`, or `C_COMPARATIVE_`. Preserve first-run evidence unchanged. Do not submit passwords, credentials, employer secrets, or unrelated personal data. Incoming files are treated as untrusted until inspected. Submission does not by itself count as successful validation.
