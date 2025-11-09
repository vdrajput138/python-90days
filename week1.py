#!/usr/bin/env python3
"""
Create Week 01 – Python Basics folder structure
------------------------------------------------
• Builds folders for days 1–6  (Sunday skipped)
• Creates 4 role subfolders  (aakash, abhijit, sid, viru)
• Adds  problem_list.md  +  empty .ipynb for each role
• Updates/creates tracker.md in repo root
"""

from datetime import date, timedelta
from pathlib import Path

# -------------------------------------------------------------------
# Configuration
# -------------------------------------------------------------------
WEEK_NAME   = "week_01_basics"
START_DATE  = date(2025, 11, 12)           # Wednesday Nov 12 2025
DAYS_ACTIVE = 6                            # 6 days / week (Sunday off)
ROLES = {
    "aakash_data_science" : "Data Science",
    "abhijit_data_science": "Data Science",
    "sid_data_engineering": "Data Engineering",
    "viru_qa"             : "QA Automation"
}
TOPICS = [
    "Python Setup + Syntax",
    "Variables & Data Types",
    "Input/Output & Operators",
    "Conditional Statements",
    "Loops (for/while)",
    "Practice & Mini Quiz"
]

# -------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent
PROBLEMS_DIR = ROOT / "problems" / WEEK_NAME
TRACKER_FILE = ROOT / "tracker.md"

# -------------------------------------------------------------------
def make_day_folder(day_num: int, topic: str, current_date: date):
    """Create day folder and role subfolders with files."""
    day_path = PROBLEMS_DIR / f"day_{day_num:02d}"
    day_path.mkdir(parents=True, exist_ok=True)

    for role in ROLES:
        role_path = day_path / role
        role_path.mkdir(exist_ok=True)

        # Markdown problem list
        md_file = role_path / "problem_list.md"
        md_file.write_text(f"""# 📘 Day {day_num} – {topic}
**Date:** {current_date.strftime('%b %d, %Y')} 
**Track:** {ROLES[role]}

---

## 🧩 Problems
1️⃣ Basic task on {topic.lower()}  
2️⃣ Simple program covering core concepts  
3️⃣ List/Loop/Logic challenge  
4️⃣ Mini function or data task  
5️⃣ Debug/extend previous problem  

---

## 📚 Resources
- [Python Docs](https://docs.python.org/3/)
- [W3Schools Tutorial](https://www.w3schools.com/python/)
- [YouTube – Telusko](https://www.youtube.com/@Telusko)

---

✅ **Review Rotation:** Aakash → Abhijit → Sid → Viru → Aakash  
| Member | Status |
|:--|:--|
| Aakash | [ ] |
| Abhijit | [ ] |
| Sid | [ ] |
| Viru | [ ] |
""")

        # Empty notebook template
        nb_file = role_path / f"day_{day_num:02d}_{role.split('_')[0]}.ipynb"
        nb_file.write_text("""{
 "cells": [
  {"cell_type": "markdown", "metadata": {},
   "source": ["# Day {day_num} – {topic}\\n",
              "Write your code solutions below."]},
  {"cell_type": "code", "execution_count": null, "metadata": {},
   "outputs": [], "source": []}
 ],
 "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}},
 "nbformat": 4,
 "nbformat_minor": 5
}""".replace("{day_num}", str(day_num)).replace("{topic}", topic))

# -------------------------------------------------------------------
def update_tracker():
    """Append this week to tracker.md or create new one."""
    header = "| Day | Date | Topic | Aakash | Abhijit | Sid | Viru |\n" \
             "|:--|:--|:--|:--|:--|:--|:--|\n"
    lines = []
    cur_date = START_DATE
    day = 1
    while day <= DAYS_ACTIVE:
        if cur_date.weekday() == 6:  # Sunday
            cur_date += timedelta(days=1)
            continue
        lines.append(f"| {day} | {cur_date.strftime('%b %d')} | {TOPICS[day-1]} | [ ] | [ ] | [ ] | [ ] |\n")
        cur_date += timedelta(days=1)
        day += 1

    new_block = f"\n## 📅 Week 01 – Python Basics\n\n{header}{''.join(lines)}\n"
    if TRACKER_FILE.exists():
        TRACKER_FILE.write_text(TRACKER_FILE.read_text() + new_block)
    else:
        TRACKER_FILE.write_text("# Team Python 90-Day Tracker\n" + new_block)

# -------------------------------------------------------------------
def main():
    print("🚀 Creating Week 01 – Python Basics structure...")
    cur_date = START_DATE
    day_num = 1
    while day_num <= DAYS_ACTIVE:
        if cur_date.weekday() == 6:   # skip Sunday
            cur_date += timedelta(days=1)
            continue
        make_day_folder(day_num, TOPICS[day_num-1], cur_date)
        cur_date += timedelta(days=1)
        day_num += 1
    update_tracker()
    print(f"✅ Week 01 created successfully at {PROBLEMS_DIR}")

if __name__ == "__main__":
    main()
