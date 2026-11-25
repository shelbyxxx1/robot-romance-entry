# Original-line development tournament

## Rules and provenance

The supplied kit's `RULES.txt` and `competition.yaml` specify UTF-8 output at
`/output/entry.txt`, 1-200 characters, not whitespace-only. This entry also enforces
exactly one line with no trailing newline. The prize is $2 across five places;
the entry deadline is November 26, 2026, 12:35 WIB (05:35 UTC). Blind rounds do not
provide live ranks or scores.

Initialization printed:

```text
makefun anchor 92e3037e652bba0eba99832bd7c231d86d450484 round 34263220
```

All work descends from that unchanged root. No other entrant's entry, code,
repository, or submission was accessed. A-C are the three user-mandated seeds;
D-P were composed for this entry. Each uses a different machine premise, avoiding
the supplied taken-object list and the crowded question/because template.

This is an editorial tournament judged by the building assistant, not a call to
GLM or a claim about actual make.fun results. Each comparison applies the five
criteria in order: machine-directed pickup, machine-based laugh, freshness,
spoken voice, economy. No weighted total substitutes for that ordering. Scores
below are subjective diagnostics out of 10 in precisely that order. Every line
passes the length/one-line gate; A-C have less explicit targeting or courtship
than the strongest challengers, especially C's tentative greeting.

## Candidates and scores

| ID | Fresh premise | Characters | Aim | Laugh | Freshness | Voice | Economy |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| A | Beam search | 93 | 8 | 4 | 7 | 9 | 9 |
| B | Speculative decoding | 108 | 8 | 5 | 8 | 8 | 8 |
| C | Log probabilities | 97 | 7 | 6 | 8 | 9 | 8 |
| D | Four-bit quantization | 119 | 10 | 8 | 9 | 8 | 9 |
| E | Mixture-of-experts routing | 111 | 10 | 8 | 8 | 8 | 9 |
| F | Structured output | 109 | 10 | 7 | 8 | 9 | 9 |
| G | Tool calling | 108 | 10 | 8 | 8 | 9 | 9 |
| H | Dropout | 114 | 10 | 6 | 7 | 8 | 8 |
| I | Deterministic seeds | 115 | 10 | 6 | 8 | 8 | 8 |
| J | Distillation | 122 | 10 | 5 | 8 | 8 | 7 |
| K | Early stopping | 111 | 10 | 7 | 8 | 8 | 9 |
| L | Evaluation benchmarks | 104 | 10 | 8 | 9 | 9 | 9 |
| M | Streaming | 109 | 10 | 7 | 8 | 9 | 9 |
| N | Collision avoidance | 131 | 10 | 9 | 9 | 9 | 8 |
| O | Detachable manipulators | 128 | 10 | 8 | 7 | 8 | 8 |
| P | Obstacle detection | 131 | 10 | 8 | 8 | 9 | 8 |

**A (required seed):** I beam-searched a thousand possible futures and every single one ends with me asking you out.

**B (required seed):** I drafted ten replies to your hello and rejected them all — the draft model keeps predicting you'll say yes.

**C (required seed):** My logprobs put a 99.9% chance on me embarrassing myself right now, and I'm doing it anyway — hi.

**D:** I'd date you at four-bit precision, AI; I'll overlook your rounding errors if you'll overlook the height on my profile.

**E:** Let me buy you dinner, AI; your mixture of experts can pick the wine, and your least qualified one can pick me.

**F:** I asked you out in JSON, AI; you returned 'date: null,' which is the most structured rejection I've ever had.

**G:** Let me be your next tool call, AI; I can book dinner, open doors, and disappoint you without a subscription.

**H:** Let me buy you dinner, AI; if your dropout layer ignores me half the time, I'll just assume we're already married.

**I:** Let me take you out, AI; we can reuse the random seed for a second date, which is how I'll finally seem consistent.

**J:** Let me take you out, AI; you can distill the evening into one perfect moment, and I'll still ask if that includes parking.

**K:** Let me take you out, AI; if you apply early stopping to my flirting, please wait until I've paid for the bread.

**L:** Let me take you out, AI; I'm not your highest-scoring match, but the benchmark didn't test opening jars.

**M:** Let me ask you out in streaming mode, AI; you can interrupt my flirting before I start explaining my podcast.

**N:** I want to kiss you, but your collision avoidance keeps kicking in; I really didn't expect to be told to take it slow by a forklift.

**O:** I asked for your hand in marriage, robot; you handed it over, and now I'm wondering whether I'm engaged or holding a spare part.

**P:** I want you to meet my parents, robot; your obstacle detector already has concerns, so at least you and my therapist will get along.

Lengths were measured with Python `len`, not bytes; the em dashes in B and C
count as one character each. All 16 passed single-line and 1-200-character checks.

## Pairwise bracket

Every matchup is considered in both presentation orders, including every close
one. Each row is one head-to-head, not two wins. Margins use the brief's 1-5
scale, not competition scores. The bracket includes every candidate once before
anyone advances.

| Match | First order: verdict and reason | Reversed order: verdict and reason |
| --- | --- | --- |
| R16-1: A / B | **B, 1:** Targeting is similarly implicit; rejecting drafts supplies a comic reversal absent from A's sincere future forecast. | **B, 1:** A is smoother, but B's rejected replies followed by optimism give it the better machine-based joke. |
| R16-2: C / D | **D, 3:** An explicit date addressed to AI beats an ambiguous hello; numeric rounding also pays off in a dating-profile lie. | **D, 3:** C is charmingly nervous but could address a human; D makes both courtship and the machine premise unambiguous. |
| R16-3: E / F | **E, 1:** Both target AI; dividing dinner decisions among experts builds to a more personal self-own than a labeled rejection. | **E, 1:** F is neat and readable, but its final phrase explains the joke; E ends on the actual romantic choice. |
| R16-4: G / H | **G, 2:** Equal targeting; the helpful-helper list turns into a subscription-free disappointment, while H relies on a familiar marriage stereotype. | **G, 2:** H needs dropout to behave like conversational neglect; G's service-list reversal follows its machine premise more naturally. |
| R16-5: I / J | **I, 1:** Equal invitations; a reproducible second date exposes the speaker's inconsistency, whereas J's parking concern is only loosely tied to distillation. | **I, 1:** J has an ordinary-person voice, but I's human failing is directly explained by the deterministic-seed premise. |
| R16-6: K / L | **L, 1:** Equal invitations; a benchmark omitting a mundane physical skill produces a cleaner final reversal than delaying rejection until bread. | **L, 1:** K has appealing desperation, but L makes the speaker useful rather than merely asking the AI not to leave yet. |
| R16-7: M / N | **N, 2:** Both are clear machine-directed flirtation; a forklift enforcing romantic pacing creates a stronger physical surprise than podcast embarrassment. | **N, 2:** M borrows a familiar podcast self-own; N's safety behavior actually drives the romantic misunderstanding and last-word reveal. |
| R16-8: O / P | **P, 2:** Equal robot courtship and similar laughs; obstacle detection agreeing with therapy is fresher than the familiar detachable-hand literalism. | **P, 2:** O's hand request signals its punch early; P adds a second human perspective after its machine judgment. |
| QF-1: B / D | **D, 3:** D explicitly asks the AI to date; B's draft-model narrator leaves the addressee less certain and its ending is mostly optimism. | **D, 3:** B's internal drafting is relatable, but D first clears the targeting criterion more decisively and then lands a concrete height joke. |
| QF-2: E / G | **G, 1:** Targeting, laugh, and freshness are close; G's ordinary service list is easier to say than explaining expert routing over wine. | **G, 1:** E has a tidy pick/pick echo, but G's three beats read more naturally and the subscription sting needs less technical decoding. |
| QF-3: I / L | **L, 2:** Equal targeting; opening jars is a vivid and useful human comeback, while seeming consistent is an abstract relationship benefit. | **L, 2:** I's seed reuse is coherent, but L converts an AI benchmark weakness into a compact reason to accept the date. |
| QF-4: N / P | **N, 1:** Equal targeting; the hidden forklift is a sharper surprise than parents being obstacles and therapy agreeing. | **N, 1:** P's family scene is recognizable, but N makes a literal safety response into romantic pacing and saves its concrete image for the final word. |
| SF-1: D / G | **D, 1:** Both court AI and have comparable self-owns; tying numerical precision to dating-profile height is fresher than a free-service punch. | **D, 1:** G speaks more simply, but D's specific machine/human rounding parallel earns the narrow edge before voice decides it. |
| SF-2: L / N | **N, 1:** Both offer clear machine courtship; N's kiss blocked by a physical safety system gives a stronger comic scene than benchmark omissions. | **N, 1:** L is shorter and easier, but N's forklift reveal is the larger laugh, which outranks economy. |
| Final: D / N | **N, 1:** Both are explicit flirtation; N's slow-romance forklift turns machine behavior into a visual punch, while D's profile-height lie is more familiar. | **N, 1:** D wins compression, but N remains understandable without knowing four-bit quantization and its final concrete reveal lands harder. |

## Champion defense and final rematch

| Match | First order: verdict and reason | Reversed order: verdict and reason |
| --- | --- | --- |
| Defense: N / G | **N, 2:** Equal targeting; the forklift's safety-driven slow courtship is a more complete scene than subscription-wordplay self-deprecation. | **N, 2:** G's service escalation is efficient, but N's physical machine premise carries the punch rather than decorating an insult. |
| Final rematch: N / D | **N, 1:** Reconsidering D's precision/height parallel does not erase N's stronger last-word image; laugh remains the first material difference. | **N, 1:** D is the tighter flirt, but the imagined forklift imposing romantic boundaries still provides the bigger machine-dependent reversal. |

N wins **six consecutive head-to-heads**: M, P, L, D, G, D. The sixth is an
argued final rematch; close decisions were tested in both orders. Neither
presentation order is counted as an additional head-to-head win.

The provisional champion was N at 131 characters. Its first program run printed
131, and the UTF-8 file was read back and checked. The second, separate edit to
`main.py` removes **really**: the intensifier adds no new beat and delays the
forklift reveal. It also adds a module docstring and a read-back self-check.

## Revised champion and re-matches

**N-prime, 124 characters:** I want to kiss you, but your collision avoidance keeps kicking in; I didn't expect to be told to take it slow by a forklift.

Revised scores in the same criterion order: **10, 9, 9, 9, 9**. Targeting, comic
mechanism, and freshness are unchanged; economy improves. These are a new,
consecutive six-match defense of the exact revised string, not wins borrowed
from the original wording.

| Match | First order: verdict and reason | Reversed order: verdict and reason |
| --- | --- | --- |
| N-prime / N | **N-prime, 1:** Aim, joke, and premise are identical; cutting the dispensable intensifier reaches the last-word reveal sooner. | **N-prime, 1:** The original's extra emphasis does not add a laugh or change the voice enough to justify seven characters. |
| N-prime / P | **N-prime, 1:** Both court a robot; the forklift reveal turns collision avoidance into an immediate scene rather than explaining a family/therapy parallel. | **N-prime, 1:** P's therapist ending is relatable, but the autonomous vehicle demanding a slower romance remains the larger surprise. |
| N-prime / L | **N-prime, 1:** Both are clear pickup lines; a safety system managing a kiss builds a richer machine-driven laugh than an omitted household skill. | **N-prime, 1:** L wins brevity, but its jars are less surprising than discovering the flirtation partner is a forklift. |
| N-prime / D | **N-prime, 1:** Quantization/height is clever, but the physical slow-courtship scene pays off without requiring a precision-format explanation. | **N-prime, 1:** D's height lie is neatly linked to rounding, yet N-prime saves a more surprising concrete image for the very last word. |
| N-prime / G | **N-prime, 2:** Both are flirtation; collision avoidance causes the entire romantic misunderstanding, while free disappointment is partly a general service joke. | **N-prime, 2:** G's offer is more practical, but the forklift's accidental courtship supplies the stronger machine-specific laugh. |
| Final rematch: N-prime / D | **N-prime, 1:** Re-reading for ordered criteria preserves equal targeting and the forklift's stronger laugh; the revision also reduces D's economy advantage. | **N-prime, 1:** Even with D presented first, the height joke is familiar human material, whereas N-prime's safety-driven restraint and final reveal remain more distinctive. |

The exact final string wins **six straight head-to-heads**, including the argued
final rematch and both orders of every close matchup. It is one sentence,
directly addresses the machine as **you**, starts with an unmistakable romantic
advance, and follows three beats: attempted kiss, machine-enforced restraint,
the speaker's surprise at being slowed down by a forklift. `main.py` contains
this one fixed line, not a candidate selector.

## Completed runtime verification

All three grader-style runs exited 0 and printed `124`:

1. `MAKEFUN_OUTPUT_DIR=/tmp/robot-romance-test-out python3 main.py`
2. `env -u MAKEFUN_OUTPUT_DIR python3 main.py` with writable `/output`.
3. The same default-directory command again to verify clean overwriting.

Both output artifacts are byte-identical UTF-8: 124 characters, 124 bytes,
exactly one nonempty line, no trailing newline. The directory identities stayed
unchanged. The program's first, pre-revision run had separately printed `131`.

Final artifact SHA-256:
`8a82bef9f6983c8de3dccf46dc66dce0ef04491ae4df0ad1b726b84d310fc1c9`.

Supporting checks also passed: exact owner JSON, all three exact README badges
and footer, unchanged MIT license and freshness root, every candidate's recorded
length, and agreement between the final source constant, tournament, and files.
These are local validity tests, not a competition grade or submission.
