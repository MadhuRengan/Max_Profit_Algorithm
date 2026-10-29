# Max Profit Algorithm

A Python project that uses **Dynamic Programming** to maximize profit by finding the best combination of buildings within a given time limit.

## Problem

Three types of buildings can be constructed, each with different construction times and earnings.

| Building | Build Time | Income/Unit |
|---|---|---|
| Theatre (T) | 5 | $1,500 |
| Pub (P) | 4 | $1,000 |
| Commercial Park (C) | 10 | $2,000 |

Only one building can be constructed at a time. Completed buildings generate income for the remaining time.

## Approach

Dynamic Programming is used to calculate the maximum profit at each time unit while tracking the optimal building combination.

**Time Complexity:** O(n)

## Example

**Input:**
```text
Time Unit: 13
```

**Output:**
```text
Earnings: $16500
T: 2 P: 0 C: 0
```

## Tech Stack

Python | Dynamic Programming

## Run

Once the Python solution is added to the repository:

```bash
python max_profit.py
```

