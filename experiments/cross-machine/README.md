# B — Cross-machine execution

## Purpose
Test a frozen ΔE execution artifact on a real external computer/runtime and preserve the first result unchanged.

This is the route analogous to the early external laptop test. It is intentionally distinguished from the clean-room implementation experiment.

## What a participant does
1. Receive the current sanitized cross-machine package.
2. Extract it into a new empty folder on a computer they are authorized to use.
3. Do not edit package files before the first run.
4. Follow the included OS/runtime instructions.
5. Preserve the first generated result unchanged.
6. If execution fails before a result is generated, preserve the first terminal output/screenshot unchanged.
7. Return the result plus basic OS/Python environment information.

Do not bypass employer, school, endpoint-security, or administrator restrictions on a managed computer.

## Why the executable package is not committed here yet
Historical execution packages include material that is safe for their original purpose but could contaminate someone who later chooses the blind clean-room route. A sanitized public package is being prepared and must not contain evaluator secrets or expected hidden answers.

Until that sanitized package is published, volunteers should contact the maintainer before running this route.

## Claim boundary
A successful cross-machine run is evidence about execution/portability in that environment. By itself it is not third-party clean-room reproduction and does not validate scientific novelty or universality.

## Direct result submission
Return the unchanged first-run result through the [ΔE external-results upload request](https://www.dropbox.com/request/3gu81cps1oqq7q2mwz8l). Prefix filenames with `B_CROSSMACHINE_` when practical.
