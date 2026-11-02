# Python Fundamentals

Part of a self-directed career transition from field operations into AI automation.

## Overview
Small Python programs that solve everyday problems:
chore checklist with allowance, patient check in tool, inventory re-order tool and a drink tally tool

## Featured Programs
- **`chore_allowance.py`** - tracks a kid's chores across the week and pays $10 if none were missed
- **`clinic_checkin.py`** - determines if a patient is checked in or needs to reschedule
- **`coffee_tally.py`** - tallies drinks sold for day at close
- **`reorder.py`** - alerts when product needs to be reordered

## Practice Exercises
The other files are short exercises covering variables, loops,
functions, and reading/writing files.

## How to Run
Requires Python 3.13.

Run it from the project folder.
```
python chore_allowance.py
```

## Skills Demonstrated
- Python: functions, loops, input validation, file handling, debugging
- Git/GitHub: regular commits, `.gitignore` for data files

## What I Learned
- In `clinic_checkin.py`, the program accepted a bad copay, the bad value was silently lost and the user would see nothing. The cause was 3 questions sharing one validation flag. Fixed by building a function with its own flag, loop and error check inside it. Each question calls it, so each question gets its own flag. 
- In `chore_allowance.py`, the program saved duplicate records. The save step added to the file each time instead of replacing it, so old records piled up alongside new ones. Fixed it by switching the save from append to replace. 