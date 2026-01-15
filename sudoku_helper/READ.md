# Sudoku Helper: The Tiny Oracle

## What This Does

You're staring at a Sudoku puzzle. Your pencil hovers over an empty cell. Your brain is screaming. Numbers swim before your eyes.

*What can go here?*

This function whispers the answer.

## The Magic

Feed it three things:
- **The row** where your empty cell lives
- **The column** where your empty cell lives  
- **The 3×3 box** where your empty cell lives

It looks at what's already there (the `5`s and `7`s and `9`s) and tells you: *"Here are the numbers that won't break everything."*

## Example

```python
row =    [5, 3, 0, 0, 7, 0, 0, 0, 0]  # Your horizontal line
column = [6, 0, 0, 1, 9, 5, 0, 0, 0]  # Your vertical line
box =    [5, 3, 0, 6, 0, 0, 0, 9, 8]  # Your 3×3 mini-grid

result = possible_numbers(row, column, box)
print(result)
# Output: [2, 4]
Translation: "Only 2 or 4 can go here without violating the sacred laws of Sudoku."
How It Works
Grabs all digits 1-9 (the full deck)
Looks at what's already used in your row, column, and box
Subtracts the used from the possible
Returns what's left, sorted and neat
The Philosophy
Sudoku is about elimination, not discovery.
You don't find the right number—you remove all the wrong ones until only truth remains.
This function does the removing for you.
Use Cases
You're stuck on a hard puzzle
You want to check if you made a mistake
You're building a Sudoku solver and need the logic
You're procrastinating and this feels productive
Note
This doesn't solve Sudoku. It just tells you what's possible in one cell.
The rest? That's still on you.
"When you have eliminated the impossible, whatever remains, however improbable, must be the truth."
— Sherlock Holmes (who definitely played Sudoku)
