# Case study: Kubernetes API documentation and generation

**Status:** Evidence-complete for API field conventions and selected documentation checks.  
**Repositories:** https://github.com/kubernetes/kubernetes and https://github.com/kubernetes/community  
**Revisions:** kubernetes/kubernetes f2319f5ce54c9eb4c0438837698fa70e22e34b36; kubernetes/community 309fa9adfc84a8d04b0817a8b11124bf479a8d5e  
**Scope:** API conventions, core/v1 Volume comments, field-name checks, generated-doc scripts, and API changelog verification.

## 1. Question

How does Kubernetes make API field documentation precise enough to support both human readers and machine-readable API tooling?

## 2. Repository context

Kubernetes API types are Go structs with JSON/protobuf tags and structured comments. The API conventions document is maintained in the separate kubernetes/community repository. The main Kubernetes repository contains scripts that validate API documentation and generate several kinds of command/reference documentation.

## 3. Evidence inventory

| Evidence | Type | Source | What it establishes |
|---|---|---|---|
| E1 | P | [API conventions audience and scope](https://github.com/kubernetes/community/blob/309fa9adfc84a8d04b0817a8b11124bf479a8d5e/contributors/devel/sig-architecture/api-conventions.md#L4-L5) | The guide targets users who need deeper API understanding and developers extending the API. |
| E2 | P | [Optional vs. Required](https://github.com/kubernetes/community/blob/309fa9adfc84a8d04b0817a8b11124bf479a8d5e/contributors/devel/sig-architecture/api-conventions.md#L824-L850) | Requiredness is defined semantically and tied to Go comment tags, pointer representation, JSON tags, and API behavior. |
| E3 | P | [Defaulting](https://github.com/kubernetes/community/blob/309fa9adfc84a8d04b0817a8b11124bf479a8d5e/contributors/devel/sig-architecture/api-conventions.md#L968-L1005) | Defaults are treated as API semantics with distinct static, admission, and controller mechanisms. |
| E4 | C/I | [core/v1/types.go](https://github.com/kubernetes/kubernetes/blob/f2319f5ce54c9eb4c0438837698fa70e22e34b36/staging/src/k8s.io/api/core/v1/types.go#L35-L75) | Volume fields have semantic comments, external links, deprecation notes, and machine-readable required/optional markers. |
| E5 | A | [verify-fieldname-docs.sh](https://github.com/kubernetes/kubernetes/blob/f2319f5ce54c9eb4c0438837698fa70e22e34b36/hack/verify-fieldname-docs.sh#L17-L55) | A tool checks API type files for mismatches between field names and their documentation. |
| E6 | A | [verify runner](https://github.com/kubernetes/kubernetes/blob/f2319f5ce54c9eb4c0438837698fa70e22e34b36/hack/make-rules/verify.sh#L80-L90) | The field-name documentation check is included in the quick verification set. |
| E7 | A | [generated-doc verifier](https://github.com/kubernetes/kubernetes/blob/f2319f5ce54c9eb4c0438837698fa70e22e34b36/hack/verify-generated-docs.sh#L17-L29) | Generated documentation can be checked by regenerating it and looking for changes. |
| E8 | A | [generated-doc update script](https://github.com/kubernetes/kubernetes/blob/f2319f5ce54c9eb4c0438837698fa70e22e34b36/hack/update-generated-docs.sh#L17-L20) | Some generated CLI/man/YAML documentation is produced for export rather than checked in by default. |
| E9 | A | [Go API changelog verifier](https://github.com/kubernetes/kubernetes/blob/f2319f5ce54c9eb4c0438837698fa70e22e34b36/hack/verify-go-apidocs.sh#L17-L45) | API changelog tracking exists, but the script explicitly says it is optional and currently does not fail verification. |

## 4. What the project actually does

The API conventions document gives precise semantics for required and optional fields. It connects those semantics to Go pointer types, JSON omitempty tags, and structured comment markers such as +optional and +required. It also explains defaulting as a compatibility-sensitive API behavior, distinguishing static defaults, admission control, and controller changes.

The core/v1 VolumeSource comments demonstrate this style. The HostPath field comment describes the behavior and intended use, links to user-facing documentation, includes a TODO about restricting host mounts, and carries a +optional marker. Other fields include explicit deprecation guidance.

Kubernetes also has a verification script that scans versioned API type files and checks whether field names and documentation are mismatched. The main verify runner includes that check in its quick verification set.

Generated documentation is more nuanced. One script regenerates kubectl, admin, man, and YAML documentation for export. Another invokes a generic generated-file verifier. A separate Go API changelog verifier exists, but its own comment says maintaining the changelog is optional and its current failure path exits successfully.

## 5. Why these practices may exist

**Stated rationale:** The API conventions guide explains that optionality and defaulting affect what clients may send, what readers may assume, and how stored configuration represents desired state. The field-name verifier explicitly exists to catch mismatches between field names and their documentation.

**Inferred rationale:** Structured comments allow a single API declaration to carry human-readable semantics and machine-readable metadata. The conventions document then explains cross-field rules that cannot be understood from one field comment alone.

**Unknown:** This sample does not establish how often every API comment is updated with behavior changes or whether all generated documentation paths are equally important to release quality.

## 6. Comparison with JIT-DW hypotheses

| Hypothesis | Alignment | Evidence and qualification |
|---|---|---|
| Comments can carry both prose and machine-readable metadata | supports | +optional and +required markers sit beside field comments. |
| Cross-field invariants need a broader reference document | supports | API conventions explain defaulting, optionality, and compatibility beyond a single field. |
| Field documentation can be mechanically checked | supports | verify-fieldname-docs is part of the verification set. |
| All generated docs are checked into the repository | contradicts | The generated-doc update script says some outputs are for export and not checked in by default. |
| Every API documentation check blocks CI | contradicts | The Go API changelog verifier is explicitly optional and currently non-blocking. |
| A comment alone is enough to explain API semantics | contradicts | Field comments coexist with a detailed API conventions document. |

## 7. Trade-offs and limitations

- Structured markers increase consistency but require contributors to understand conventions and generators.
- The field-name checker catches a narrow class of mismatches; it does not prove that descriptions are correct.
- Generated documentation has different lifecycle rules from hand-authored API conventions.
- The presence of a verifier does not mean every documentation concern is a hard gate.

## 8. Findings

- **Observed practice:** Kubernetes uses field-level comments and markers, cross-cutting API conventions, and targeted documentation verification.
- **Stated rationale:** API optionality, defaulting, and field naming have compatibility and client-behavior consequences.
- **Inferred rationale:** Machine-readable annotations reduce ambiguity between code declarations and API reference output.
- **Confidence:** High for the inspected API conventions and scripts; medium for generalizing to all API groups.
- **What JIT-DW should adopt:** Structured metadata only where a generator or checker consumes it; separate cross-cutting contract documents for rules that span many fields.
- **What JIT-DW should not copy:** Treating the existence of a verifier as proof that all documentation checks are blocking.
- **What needs pilot validation:** Which metadata and generated-doc checks provide enough value to justify their maintenance cost.
