# Day 21 — Weekly Review (Stack & Queue, Week 3)

**Date:** June 17, 2026
**Problems covered:** LC 496 (Next Greater Element I), LC 20 (Valid Parentheses)
**Goal for the day:** Re-solve Day 15 and Day 20 problems from scratch to fix recurring confusion points from Days 15–20.

---

## 1. Problems Identified Before Today's Session

| Day | Problem | Issue |
|-----|---------|-------|
| Day 15 | Valid Parentheses | Confused comparison direction (`pairs[i] != top`) |
| Day 16 | Min Stack | Confused about managing two stacks simultaneously |
| Day 17/18 | Queue using Stacks / Stack using Queues | Confused which structure empties vs fills |
| Day 20 | Next Greater Element I (Monotonic Stack) | Confused `if` vs `while` usage |

**Root cause identified:** Difficulty deciding whether to process *one* element from the stack (`if`) or process *all qualifying* elements before moving on (`while`).

---

## 2. Concepts Fixed Today

### 2.1 `if` vs `while`
- `if`: checks a condition **once**.
- `while`: keeps checking and repeating **as long as** the condition stays true.
- Monotonic stack problems often need to pop **multiple** smaller elements in a row, so `while` is required, not `if`.

### 2.2 Dictionary syntax `{key: value}`
- Correct syntax: `dic = {")": "(", "}": "{", "]": "["}`
- Mistakes made and corrected:
  - Used `{}` instead of `[]` when accessing a dictionary value (`prices["item"] = 1000`, not `prices{"item"}`)
  - Mixed quotes/colons/commas incorrectly when defining multiple key-value pairs in one line
  - Confused which side (open vs. close bracket) should be the key — corrected to: **the symbol you search WITH is the key**

### 2.3 `stack.pop()` is a method, not an index
- Mistake: `stack.pop[]`
- Correct: `stack.pop()` — parentheses for actions/methods, square brackets for accessing a position (list index or dict key).

### 2.4 Variable role confusion: `i` vs `dic[i]`
- `i` = the lookup key itself (e.g., the number 4)
- `dic[i]` = the value stored under that key (e.g., -1, the actual answer)
- Mistake made repeatedly: `total.append(i)` instead of `total.append(dic[i])`
- Fixed by re-explaining with a locker analogy: `i` is the locker's name tag, `dic[i]` is what's inside the locker.

### 2.5 Loop placement / indentation
- Mistake: `return True` placed inside the `for` loop → caused early exit after the first character.
- Fixed: `return True` must be at the same indentation level as `for`, executed only after the loop fully completes.
- Mistake: `stack.append(i)` placed inside the `while` loop → caused incorrect re-comparison.
- Fixed: moved outside `while`, but still inside `for`.

### 2.6 Empty stack edge case (LC 20)
- If a closing bracket appears with an empty stack, calling `.pop()` directly causes an `IndexError`.
- Fix: check `if not stack: return False` **before** calling `.pop()`.

---

## 3. Final Solutions (Self-Written After Hints)

### LC 20 — Valid Parentheses
```python
def isValid(s):
    stack = []
    dic = {")":"(", "}":"{", "]":"["}

    for i in s:
        if i in "({[":
            stack.append(i)
        else:
            if not stack:
                return False
            top = stack.pop()
            if dic[i] != top:
                return False
    return True
```

### LC 496 — Next Greater Element I
```python
def nextGreaterElement(nums1, nums2):
    stack = []
    dic = {}

    for i in nums2:
        while stack and i > stack[-1]:
            dic[stack.pop()] = i
        stack.append(i)
    for i in stack:
        dic[i] = -1

    total = []
    for i in nums1:
        total.append(dic[i])
    return total
```

Both solutions were re-written from a blank file after the initial walkthrough, with 0 lines copy-pasted.

---

## 4. Quiz Results (5 Questions)

| # | Topic | Result |
|---|-------|--------|
| 1 | `if` vs `while` difference | Correct |
| 2 | Stack top index (`stack[-1]`) | Correct |
| 3 | Dictionary value assignment syntax | Incorrect on 1st attempt (used `{}` instead of `[]`), correct on 2nd attempt |
| 4 | Manual trace of monotonic stack with `nums = [2, 1, 5]` | Incorrect on 1st attempt, correct on 2nd attempt (`stack = [5]`, `dic = {1: 5, 2: 5}`) |
| 5 | Why `dic[i]` instead of `i` when appending to result list | Required 3 clarifying explanations before fully correct |

**Score: 2/5 correct on first attempt, 5/5 correct after re-explanation.**

---

## 5. What Changed By End of Session

- Solved LC 20 unaided (blank file, no copy-paste) after 1 round of guided correction (dictionary syntax).
- Solved LC 496 unaided (blank file, no copy-paste) after 2 rounds of guided correction (`pop()` syntax, loop placement).
- Total number of distinct bugs self-corrected without being given the answer directly: 6 (across both problems).

---

## 6. Next Steps

1. **Daily retention practice:** Before starting tomorrow's new lesson, re-write today's two solutions from a blank file in under 5 minutes. Mark any point where stuck — do not look up the answer, just note the location of the gap.
2. **Day 22 (June 18, 2026):** LC 704 (Binary Search) — start of Week 4.
3. **Weak point log to track going forward:**
   - Dictionary `{key: value}` syntax (commas, colons, quote placement)
   - Deciding dictionary key direction based on "what value do I search with"
   - `for`/`while` loop body indentation (what executes once vs. what executes per element)

---

## 7. Timeline Reference

- **Day 21 of 330** (June 17, 2026)
- **Days remaining to Meta target offer (Day 331):** 308 days
