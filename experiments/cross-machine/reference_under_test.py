import json

ALLOWED_STATUSES = {"PASS", "FAIL", "UNKNOWN", "UNMAPPABLE"}
FIELDS = (
    "replay", "digest_mismatch", "missing_cap", "unknown_critical",
    "malformed", "required_absent", "required_null", "diagnostic_only", "lossy"
)

def _active(v):
    return v is True or (type(v) in (int, float) and not isinstance(v, bool) and v == 1)

def evaluate(x):
    if not isinstance(x, dict):
        return "MALFORMED"
    for key in FIELDS:
        if key in x and x[key] not in (None, False, 0, True, 1):
            return "MALFORMED"
    errs = []
    if _active(x.get("replay")):
        errs.append("REPLAY")
    if _active(x.get("digest_mismatch")):
        errs.append("BINDING_MISMATCH")
    if _active(x.get("missing_cap")) or _active(x.get("unknown_critical")):
        errs.append("NEGOTIATION_FAIL")
    if _active(x.get("malformed")) or _active(x.get("required_absent")) or _active(x.get("required_null")):
        errs.append("MALFORMED")
    if errs:
        return errs if len(errs) > 1 else errs[0]
    if _active(x.get("diagnostic_only")) or _active(x.get("lossy")):
        return "UNKNOWN"
    status = x.get("status")
    if status in ALLOWED_STATUSES:
        return status
    return "PASS"
