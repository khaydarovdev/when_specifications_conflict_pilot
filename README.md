# When Specifications Conflict

## Research question
Do LLMs have a consistent priority among types of specifications in code generation?

## Method
Test language models using programming prompts containing intentionally conflicting specifications. Run each generated implementation against tests representing each conflicting specification. Record which specification the implementation satisfies, whether the model acknowledges the conflict, and whether repeated runs produce consistent behavior.

## Pilot design
- 3 programming problems
- 4 language models
- 2 runs per problem and model
- 24 planned outputs

## Project structure
- prompts/: Original prompts given to models
- outputs/: Raw model responses
- candidates/: Python implementations extracted from model responses
- tests/: Test cases representing conflicting specifications
- results.md: Observations and test results

## Current progress
P1 has been tested with three models, with two runs per model: six outputs total. All six follow the postcondition and fail the conflicting example. One additional model is still needed to complete P1 across four models.

## Important limitation
The current P1 runs use the same prompt wording. They measure repeatability under that wording, not sensitivity to prompt phrasing.
