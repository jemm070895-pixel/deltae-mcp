# A — Clean-room implementation

## Purpose
Independently implement the frozen ΔE behavioral wire contract from a public specification only.

## Before you continue
To preserve a fully blind clean-room result, do **not** inspect Route B implementation/execution artifacts, historical ΔE implementations, evaluator material, hidden tests, or expected answers before your implementation is frozen. If you have already seen any ΔE implementation, disclose that exposure; the result can still be useful, but it must not be classified as fully blind clean-room evidence.

## Public source-only participation package
Download: [DeltaE_PUBLIC_CLEANROOM_SOURCE_ONLY_v1.0.zip](https://www.dropbox.com/scl/fi/dgv7zfnh2b47b86d22hji/DeltaE_PUBLIC_CLEANROOM_SOURCE_ONLY_v1.0.zip?rlkey=hujhjwrmywu6k8208poti2nnl&dl=0)

SHA-256:
`8a9a5c09664413067ae4126ce1f47b24944fcd13b08bb8ec89ebbda7811787d7`

This package contains the public specification, step-by-step instructions, AI-use guidance, an empty implementation location, and the source-only freeze/return procedure. It intentionally excludes the originating implementation, evaluator oracle, hidden challenge/tests, expected hidden answers, and internal corpus.

**Do not run or inspect Route B before freezing Route A if you want to preserve fully blind clean-room status.**

## Public behavioral specification
For each non-empty input line, read exactly one JSON object.

Condition fields:
`replay`, `digest_mismatch`, `missing_cap`, `unknown_critical`, `malformed`, `required_absent`, `required_null`, `diagnostic_only`, `lossy`.

For those condition fields:
- active only for JSON boolean `true` or JSON number `1`;
- inactive when absent, `false`, `0`, or `null`;
- any other value makes the input malformed.

Hard conditions, in precedence order:
1. `replay` → `REPLAY`
2. `digest_mismatch` → `BINDING_MISMATCH`
3. `missing_cap` OR `unknown_critical` → `NEGOTIATION_FAIL`
4. `malformed` OR `required_absent` OR `required_null` → `MALFORMED`

If exactly one hard error applies, output that error as one JSON string. If two or more apply, output one JSON array containing all applicable hard errors in precedence order.

With no hard error: if `diagnostic_only` or `lossy` is active, output `"UNKNOWN"`. Otherwise, if `status` is exactly one of `PASS`, `FAIL`, `UNKNOWN`, `UNMAPPABLE`, output that status. Otherwise output `"PASS"`.

Write exactly one JSON result per processed input line.

## Blindness rule
Before freezing your implementation, do not inspect or request:
- originating/reference ΔE implementation;
- Route B implementation/execution artifacts;
- evaluator oracle;
- hidden challenge/tests;
- expected hidden-test answers.

AI/coding assistance is permitted if disclosed, but give it only this public specification before freeze.

## Freeze
When implementation is complete, preserve the exact source and record:
- SHA-256;
- byte size;
- runtime and OS;
- UTC freeze timestamp;
- participant identifier (nickname/initials are sufficient);
- AI/tool assistance and any prior ΔE exposure.

Do not change the implementation after freeze.

## Return / next stage
Submit the frozen source and attestation through the result-submission link below. The evaluator stage is intentionally not published here because exposing it before freeze would contaminate the blind exercise.

## Claim boundary
Passing this exercise would support independent implementation/reproduction within the tested contract. It would not prove scientific novelty, universality, formal correctness, or productivity benefit.

## Direct result submission
After freezing the exact implementation, submit the frozen source plus freeze/attestation information through the [ΔE external-results upload request](https://www.dropbox.com/request/3gu81cps1oqq7q2mwz8l). Prefix filenames with `A_CLEANROOM_` when practical. The evaluator stage remains private until the freeze is recorded.
