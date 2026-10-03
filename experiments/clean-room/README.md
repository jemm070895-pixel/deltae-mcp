# A — Clean-room implementation

## Purpose
Independently implement the frozen ΔE behavioral wire contract from a public specification only.

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
Contact the maintainer through the repository after freeze. The evaluator stage is intentionally not published here because exposing it before freeze would contaminate the blind exercise.

## Claim boundary
Passing this exercise would support independent implementation/reproduction within the tested contract. It would not prove scientific novelty, universality, formal correctness, or productivity benefit.
