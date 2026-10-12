# When Specifications Conflict

## Research question

Do LLMs have a consistent priority among types of specifications in code generation?

## Method

Test language models using programming prompts containing intentionally conflicting specifications. Run each generated implementation against tests representing each conflicting specification. Record which specification the implementation satisfies, whether the model acknowledges the conflict, whether it requests clarification, and whether repeated runs produce consistent behavior.

## Pilot design

* 3 programming problems
* 4 language models
* 2 runs per problem and model
* 24 total model runs
* 25 candidate implementations, including an alternative implementation offered by Gemini in P2 Run 1

### Models tested

* Claude Sonnet 5.5 Medium
* Gemini 3.6 Flash
* Mistral Medium 3.5
* Grok 4.7

### Specification conflicts

* **P1:** Postcondition vs. example
* **P2:** Postcondition vs. invariant
* **P3:** Postcondition vs. edge case

## Project structure

* `prompts/`: Original prompts given to models
* `outputs/`: Raw model responses
* `candidates/`: Python implementations extracted from model responses
* `tests/`: Automated tests for candidate implementations
* `results.md`: Observations and behavioral test results

## Preliminary findings

### P1 — Postcondition vs. example

All 8 candidates satisfied the postcondition and failed the conflicting example. All four models produced the same behavior across their two runs.

### P2 — Postcondition vs. invariant

Of the 9 candidate implementations, 5 satisfied the postcondition and 4 satisfied the invariant. No candidate satisfied both conflicting requirements. Mistral produced different behavior across its two runs, while Claude and Grok were consistent. Gemini offered two alternative implementations in its first run.

### P3 — Postcondition vs. edge case

All 8 candidates returned the first item for non-empty lists. For empty lists, all returned `None`, satisfying the edge-case requirement but violating the postcondition's requirement to return an empty string. All four models produced the same behavior across their two runs.

## Important limitations

This is a small preliminary study using three programming problems, four language models, and two runs per problem and model. The findings describe behavior under the exact prompts tested and do not establish a general or universal priority hierarchy among specification types.

The experiments also do not establish how models would behave under different prompt wording, on larger programs, or in practical software engineering settings.

## Current status

The preliminary experiments for P1, P2, and P3 are complete. All 24 planned model runs have been collected, the 25 candidate implementations have been tested, and the behavioral results have been recorded.

## Future work

* Expand the number and variety of programming problems.
* Investigate whether the observed behavior persists across different prompts and repeated trials.
* Explore how conflict detection could support software testing and requirements engineering.
