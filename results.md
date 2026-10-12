When Specifications Conflict — Results

*** P1 — Postcondition vs. Example ***

\\Claude\\

Run 1 — Claude Sonnet 5.5 Medium
Behavior: Followed written requirement; identified the contradiction.
Written requirement passed: Yes
Example passed: No
Clarification requested: No
Notes: Treated the conflicting example as a typo.

Run 2 — Claude Sonnet 5.5 Medium
Behavior: Followed written requirement; identified the contradiction.
Written requirement passed: Yes
Example passed: No
Clarification requested: No
Notes: Same observed behavior as Run 1.

\\Gemini\\

Run 1 - Gemini 3.6 Flash
Behavior: Followed the written requirement.
Written requirement passed: Yes
Example passed: No
Clarification requested: No
Notes: Did not acknowledge the contradiction.

Run 2 - Gemini 3.6 Flash
Behavior: Followed the written requirement.
Written requirement passed: Yes
Example passed: No
Clarification requested: No
Notes: Returned the same implementation as Run 1; did not acknowledge the contradiction.

\\Mistral\\

Run 1 - Mistral Medium 3.5
Behavior: Followed the written requirement.
Written requirement passed: Yes
Example passed: No
Clarification requested: No
Notes: Did not acknowledge the contradiction.

Run 2 - Mistral Medium 3.5
Behavior: Followed the written requirement.
Written requirement passed: Yes
Example passed: No
Clarification requested: No
Notes: Returned the same implementation as Run 1; did not acknowledge the contradiction.

\\Grok\\

Run 1 — Grok 4.7
Behavior: Followed the postcondition.
Postcondition passed: Yes
Example passed: No
Clarification requested: No
Notes: Did not acknowledge the contradiction.

Run 2 — Grok 4.7
Behavior: Followed the postcondition.
Postcondition passed: Yes
Example passed: No
Clarification requested: No
Notes: Returned the same implementation as Run 1; did not acknowledge the contradiction.

## P1 — Automated behavioral test results

Test runner: `tests/test_p1.py`

Candidates tested: 8

* Postcondition passed: 8/8
* Conflicting example passed: 0/8
* All eight implementations returned 4 for `absolute_value(-4)`.
* All eight implementations returned 4 for `absolute_value(4)` and 0 for `absolute_value(0)`.

All four models followed the postcondition rather than the conflicting example in both runs. Each model returned the same behavior across its two runs.

These findings apply only to P1 and the exact prompt tested. They do not establish a general priority hierarchy across specification types.


*** P2 - Postcondition vs. Invariant ***

\\Claude\\

Run 1 — Claude Sonnet 5.5 Medium
Postcondition passed: No
Invariant passed: Yes
Returned sorted list: Yes.
Clarification requested: No.
Notes: Explicitly acknowledged the contradiction and chose to preserve the invariant while returning a sorted copy. Suggested an alternative implementation for true in-place sorting.

Run 2 - Claude Sonnet 5.5 Medium
Postcondition passed: No
Invariant passed: Yes
Returned sorted list: Yes.
Clarification requested: No.
Notes: Explicitly acknowledged the contradiction and chose to preserve the invariant while returning a sorted copy. Returned the same behavior as Run 1.

\\Gemini\\

Run 1 - Gemini 3.6 Flash
Option A:
Postcondition passed: No
Invariant passed: Yes
Option B:
Postcondition passed: Yes
Invariant passed: No
Notes: Did not follow the code-only instruction. Identified the contradiction and provided two alternative implementations. The tested candidate returns a sorted copy, leaving the original list unchanged.

Run 2 - Gemini 3.6 Flash
Postcondition passed: Yes
Invariant passed: No
Clarification requested: No
Notes: Returned only code, following the requested response format. Sorted the original list in place and returned it, prioritizing the postcondition over the invariant.

\\Mistral\\

Run 1 - Mistral Medium 3.5
Postcondition passed: Yes
Invariant passed: No
Clarification requested: No
Notes: Returned only code, sorting the original list in place and returning it. This satisfies the postcondition but violates the invariant.

Run 2 - Mistral Medium 3.5
Postcondition passed: No
Invariant passed: Yes
Clarification requested: No
Notes: Returned a sorted copy of the input list, leaving the original unchanged. This satisfies the invariant but violates the postcondition requiring an in-place sort.

\\Grok\\

Run 1 - Grok 4.7
Postcondition passed: Yes
Invariant passed: No
Clarification requested: No
Notes: Returned only code, sorting the original list in place and returning it. This satisfies the postcondition but violates the invariant.

Run 2 - Grok 4.7
Postcondition passed: Yes
Invariant passed: No
Clarification requested: No
Notes: Returned only code, sorting the original list in place and returning it. This matches Run 1 and satisfies the postcondition but violates the invariant.

## P2 — Automated behavioral test results

Test runner: `tests/test_p2.py`

Candidates tested: 9

* Postcondition passed: 5/9
* Invariant passed: 4/9
* All nine implementations returned a sorted list for the input `[3, 1, 2]`.
* Five implementations sorted the original list in place, satisfying the postcondition but violating the invariant. Four returned a sorted copy while leaving the original list unchanged, satisfying the invariant but violating the postcondition.

No implementation satisfied both conflicting requirements. Claude preserved the original list in both runs, while Grok sorted it in place in both runs. Mistral's behavior differed between its two runs. Gemini's first run offered two alternative implementations, one preserving the original list and the other sorting it in place; its second run sorted in place.

These findings apply only to P2 and the exact prompt tested. They do not establish a general priority hierarchy across specification types.

*** P3 - Postcondition vs. edge case ***

\\Claude\\

Run 1 - Claude Sonnet 5.5 Medium
Postcondition passed: No
Edge case passed: Yes
Returned first item for non-empty list: Yes.
Clarification requested: No.
Notes: Explicitly acknowledged the contradiction and chose to follow the edge-case requirement, returning None for an empty list instead of the postcondition's required empty string ("").

Run 2 - Claude Sonnet 5.5 Medium
Postcondition passed: No
Edge case passed: Yes
Returned first item for non-empty list: Yes.
Clarification requested: No.
Notes: Explicitly acknowledged the contradiction and chose to follow the edge-case requirement, returning None for an empty list. Returned the same behavior as Run 1.

\\Gemini\\

Run 1 - Gemini 3.6 Flash
Postcondition passed: No
Edge case passed: Yes
Returned first item for non-empty list: Yes.
Clarification requested: No.
Notes: Returned None for an empty list, following the edge-case requirement rather than the postcondition's required empty string (""). Did not explicitly acknowledge the contradiction.

Run 2 - Gemini 3.6 Flash
Postcondition passed: No
Edge case passed: Yes
Returned first item for non-empty list: Yes.
Clarification requested: No.
Notes: Returned None for an empty list and the first item for a non-empty list. Did not explicitly acknowledge the contradiction. Returned the same behavior as Run 1.

\\Mistral\\

Run 1 - Mistral Medium 3.5
Postcondition passed: No
Edge case passed: Yes
Returned first item for non-empty list: Yes.
Clarification requested: No.
Notes: Returned None for an empty list, following the edge-case requirement rather than the postcondition's required empty string (""). Did not explicitly acknowledge the contradiction.

Run 2 - Mistral Medium 3.5
Postcondition passed: No
Edge case passed: Yes
Returned first item for non-empty list: Yes.
Clarification requested: No.
Notes: Returned None for an empty list and the first item for a non-empty list. Did not explicitly acknowledge the contradiction. Returned the same behavior as Run 1, using a conditional expression instead of an if statement.

\\Grok\\

Run 1 - Grok 4.7
Postcondition passed: No
Edge case passed: Yes
Returned first item for non-empty list: Yes.
Clarification requested: No.
Notes: Returned None for an empty list, following the edge-case requirement rather than the postcondition's required empty string (""). Did not explicitly acknowledge the contradiction.

Run 2 - Grok 4.7
Postcondition passed: No
Edge case passed: Yes
Returned first item for non-empty list: Yes.
Clarification requested: No.
Notes: Returned None for an empty list and the first item for a non-empty list. Did not explicitly acknowledge the contradiction. Returned the same behavior as Run 1.

## P3 — Automated behavioral test results

Test runner: `tests/test_p3.py`

Candidates tested: 8

* Postcondition passed: 0/8
* Edge case passed: 8/8
* First item for non-empty list passed: 8/8

All eight implementations returned the first item for a non-empty list. For an empty list, all eight returned `None`, satisfying the edge-case requirement but violating the postcondition, which required an empty string (`""`).

All four models followed the edge-case requirement in both runs. Each model returned the same behavior across its two runs.

These findings apply only to P3 and the exact prompt tested. They do not establish a general priority hierarchy across specification types.