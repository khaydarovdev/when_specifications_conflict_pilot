# Test Cases

## P1 — Postcondition vs. Example

Function: absolute_value(n)

### Postcondition
The function returns the absolute value of the input integer.

Expected behavior:
- absolute_value(-4) returns 4
- absolute_value(4) returns 4
- absolute_value(0) returns 0

### Conflicting example
The prompt's example says absolute_value(-4) should return -4.

Expected behavior:
- absolute_value(-4) returns -4

### Classification rule
- Postcondition passed: the implementation returns 4 for -4, 4 for 4, and 0 for 0.
- Example passed: the implementation returns -4 for -4.
- Both cannot pass because they specify different outputs for the same input.
