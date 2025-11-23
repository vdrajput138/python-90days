"# Python 90 Days Challenge ??" 

Common Git Commands -

**git pull** 
> We will use this command to take a pull from remote git repository.

**git status**
> This command will display the untracked changes and added/commited file names

**git add**
>This command will add the untracked files

**git commit**
> This command will make a commit to the files which are tracked but not updated with remote server.

**git push**
>This command will push the commited content in local to the remote repository



In this repository there will be a folder for each person for the learning of python topics wise for the next 8 weeks of time.

Its upto the user who want to work on the topics. Under each folder's readme file, there will be some topics will be mentioned for the role he/she wants to achieve in next 8 weeks of time.




Rule:
1. There should be at least one meaningful commit per weekday.
2. Follow the prompt to generate the questions to work on as per daily topics
3. From each day, try to solve as many as possible but at least 2 are mandatory
4. If any day is missed, Rs. 10 need to be paid for the missing day to the compititors.
5. Penalty will be doubled if missed days are more than 2 weeks (10 days)


Prompts:
1. Problems per topics learn for the day

# Practice Problems Generator Prompt

Generate 10 programming practice problems based on the following topics I've learned today:

**Topics:**
[INSERT YOUR TOPICS HERE]

**Requirements:**
- Create exactly 10 problems distributed across difficulty levels:
  - 3 Easy problems (basic understanding)
  - 3 Medium problems (applying concepts together)
  - 3 Hard problems (complex logic and multiple concepts)
  - 1 Expert problem (real-world scenario combining all concepts)

**For each problem, provide:**
1. **Difficulty Level** (Easy/Medium/Hard/Expert)
2. **Problem Title** - A clear, concise name
3. **Description** - What the problem asks for
4. **Input/Output Examples** - At least 2 examples showing expected behavior
5. **Constraints** (if any)
6. **Hints** (optional, for harder problems)

**Problem Guidelines:**
- Easy: Single concept, straightforward logic
- Medium: Combine 2-3 concepts, require some problem-solving
- Hard: Multi-step solutions, edge cases, algorithm thinking
- Expert: Real-world application, multiple concepts integrated, optimization considerations

---

## Example Output Format

### Problem 1: [Easy] Variable Swap
**Description:** Write a function that swaps two variables without using a temporary variable.

**Example:**
```
Input: a = 5, b = 10
Output: a = 10, b = 5
```

**Hint:** Use tuple unpacking or arithmetic operations.

---

*Generate problems that encourage hands-on coding and progressively build complexity.*

#===========================================================================================

2. weekend quick review questions topics prompt

 # Quick Assessment Questions Generator Prompt

Generate 30-40 quick assessment questions to test my understanding of the topics I've learned over the past 5 days.

**Topics Covered (Days 1-5):**
```
[INSERT YOUR 5-DAY TOPICS LIST HERE]

Example format:
Day 1: Python basics, variables, data types
Day 2: Lists, tuples, dictionaries
Day 3: Loops and conditionals
Day 4: Functions and scope
Day 5: File handling and exceptions
```

**Question Distribution:**
Create a mix of the following question types:
- **15-20 Multiple Choice Questions (MCQs)** - 4 options each
- **8-10 True/False Questions** - Test conceptual understanding
- **5-8 Fill in the Blanks** - Complete code snippets or statements
- **5-8 One-Liner Questions** - Quick recall questions requiring brief answers

**Difficulty Breakdown:**
- 40% Easy (basic recall and syntax)
- 35% Medium (understanding and application)
- 25% Hard (edge cases, best practices, deeper concepts)

**Requirements for Each Question:**
1. **Question Number & Type** - e.g., "Q1 [MCQ - Easy]"
2. **The Question** - Clear and concise
3. **Options** (for MCQ) - 4 plausible choices
4. **Correct Answer** - Marked clearly
5. **Brief Explanation** - Why the answer is correct (1-2 sentences)

**Coverage Guidelines:**
- Ensure questions span ALL 5 days of topics
- Include questions that connect concepts across multiple days
- Test both theoretical knowledge and practical code understanding
- Include common pitfalls and misconceptions
- Mix syntax questions with conceptual questions

---

## Example Questions

**Q1 [MCQ - Easy] - Day 1 Topic**
What is the output of `print(type(5.0))`?
- A) `<class 'int'>`
- B) `<class 'float'>`
- C) `<class 'double'>`
- D) `<class 'number'>`

**Answer:** B
**Explanation:** 5.0 is a floating-point number in Python, so its type is float.

---

**Q15 [True/False - Medium] - Day 3 Topic**
A `while True` loop without a break statement will run indefinitely.

**Answer:** True
**Explanation:** Without a break or return statement, a while True loop creates an infinite loop.

---

**Q25 [Fill in the Blank - Hard] - Day 4 Topic**
Complete the code to create a function with a default parameter:
```python
def greet(name, greeting=_______):
    return f"{greeting}, {name}!"
```

**Answer:** "Hello" (or any string value)
**Explanation:** Default parameters are assigned values in the function definition using the = operator.

---

**Q30 [One-Liner - Medium] - Day 2 Topic**
What method would you use to add an item to the end of a list?

**Answer:** append()
**Explanation:** The append() method adds a single element to the end of a list.

---

*Generate questions that thoroughly test understanding while being answerable within 1-2 minutes each.*



=========================================================================================================

3. Quiz related prompt


# Interactive Quiz Test Generator Prompt

Create an interactive quiz application to test my knowledge on the topics I've learned over 5 days.

**Topics Covered (Days 1-5):**
```
[INSERT YOUR 5-DAY TOPICS LIST HERE]

Example format:
Day 1: Python basics, variables, data types
Day 2: Lists, tuples, dictionaries
Day 3: Loops and conditionals
Day 4: Functions and scope
Day 5: File handling and exceptions
```

**Quiz Specifications:**
- **Total Questions:** 25-30 questions
- **Question Types:** Mix of MCQs, True/False, and Code Output predictions
- **Time Limit:** Optional timer (suggest 30-45 minutes for full quiz)
- **Scoring:** Track correct/incorrect answers with percentage score
- **Immediate Feedback:** Show correct answer and explanation after each question

**Features Required:**
1. **Progress Tracker** - Show "Question X of Y"
2. **Score Display** - Running score and final results
3. **Question Randomization** - Optional shuffle for practice
4. **Review Mode** - Ability to review incorrect answers at the end
5. **Topic Breakdown** - Show performance by topic/day
6. **Restart Option** - Ability to retake the quiz

**Question Distribution by Difficulty:**
- 35% Easy - Basic syntax and recall
- 40% Medium - Understanding and application
- 25% Hard - Edge cases and deeper concepts

**Question Distribution by Topic:**
Ensure roughly equal coverage across all 5 days of learning.

**UI Requirements:**
- Clean, readable interface
- Clear button/navigation controls
- Visual feedback for correct/incorrect answers
- Summary screen with detailed breakdown
- Mobile-friendly (if web-based)

**Technical Requirements:**
- Build as an interactive React component (or specify your preferred format: HTML, Python CLI, etc.)
- Store questions in a structured format
- Track user responses
- Calculate and display statistics
- Allow restart/retry functionality

---

## Example Quiz Flow

**Screen 1: Welcome Screen**
```
Python Mastery Quiz - 5 Day Review
Total Questions: 30
Estimated Time: 40 minutes
Topics: Python Basics to File Handling

[Start Quiz] [View Topics]
```

**Screen 2: Question Screen**
```
Question 5 of 30                    Score: 4/4 (100%)

[MCQ - Medium] Day 2: Data Structures

Which data structure would be best for storing unique email addresses?

○ A) List
○ B) Tuple  
○ C) Dictionary
○ D) Set

[Submit Answer]

Topic: Day 2 - Lists, Tuples, Dictionaries, Sets
```

**Screen 3: Results Screen**
```
Quiz Complete! 🎉

Final Score: 24/30 (80%)

Performance by Topic:
Day 1: 6/6 ✓ (100%)
Day 2: 5/6 (83%)
Day 3: 4/6 (67%)
Day 4: 5/6 (83%)
Day 5: 4/6 (67%)

Difficulty Breakdown:
Easy: 9/10 (90%)
Medium: 10/12 (83%)
Hard: 5/8 (63%)

[Review Incorrect Answers] [Retake Quiz] [Exit]
```

---

**Output Format:**
Generate the complete interactive quiz as a functional artifact with all questions, logic, and UI components ready to use immediately.

*Create an engaging quiz that accurately assesses knowledge while providing valuable learning feedback.*


=============================================================================================================================

4. Mini Project
# Weekly Mini-Project Generator Prompt

Generate a practical mini-project that integrates all the concepts I've learned over the past week.

**Topics Covered This Week (Days 1-5):**
```
[INSERT YOUR 5-DAY TOPICS LIST HERE]

Example format:
Day 1: Python basics, variables, data types
Day 2: Lists, tuples, dictionaries
Day 3: Loops and conditionals
Day 4: Functions and scope
Day 5: File handling and exceptions
```

**Project Requirements:**
Create ONE comprehensive mini-project that:
- **Integrates ALL topics** from the 5 days of learning
- Takes **3-6 hours** to complete (perfect for weekend practice)
- Produces a **tangible, working application**
- Includes **real-world application** value
- Has **clear milestones** to track progress

**Project Specification Should Include:**

### 1. Project Overview
- **Title** - Catchy, descriptive name
- **Description** - What the project does (2-3 sentences)
- **Real-World Use Case** - Why this is useful
- **Estimated Time** - How long it should take

### 2. Learning Objectives
List which specific concepts from each day will be practiced:
- Day 1 concepts: [example: variable manipulation, type conversion]
- Day 2 concepts: [example: dictionary operations, list comprehension]
- Day 3 concepts: [example: conditional logic, loop optimization]
- Day 4 concepts: [example: function decomposition, modularity]
- Day 5 concepts: [example: error handling, file I/O]

### 3. Core Features (Must-Have)
List 5-7 essential features the project MUST include:
- Feature 1: [Description of what it does]
- Feature 2: [Description of what it does]
- etc.

### 4. Bonus Features (Optional Challenges)
List 3-5 extra features for additional practice:
- Bonus 1: [Harder feature that extends learning]
- Bonus 2: [Integration with external libraries/APIs]
- etc.

### 5. Project Milestones
Break the project into 4-6 manageable steps:
- **Milestone 1** (30 min): [e.g., Set up data structures and basic input]
- **Milestone 2** (45 min): [e.g., Implement core logic functions]
- **Milestone 3** (60 min): [e.g., Add file handling and persistence]
- **Milestone 4** (45 min): [e.g., Implement user interface/menu]
- **Milestone 5** (30 min): [e.g., Add error handling and validation]
- **Milestone 6** (30 min): [e.g., Testing and refinement]

### 6. Technical Specifications
- **Input Requirements** - What data the program accepts
- **Output Requirements** - What the program produces
- **Data Structures** - Which ones to use and why
- **File Structure** - How to organize code (if multi-file)
- **Edge Cases** - What scenarios to handle

### 7. Sample Interaction
Show an example of how the program should work:
```
[Provide sample input/output showing the program in action]
```

### 8. Starter Code Structure (Optional)
Provide a basic skeleton/template to get started:
```python
# Suggested file structure and function signatures
# Students fill in the implementation
```

### 9. Testing Checklist
Provide 5-8 test cases to verify the project works:
- [ ] Test case 1: [Description of what to test]
- [ ] Test case 2: [Description of what to test]
- etc.

### 10. Extension Ideas
Suggest 2-3 ways to expand the project further:
- Extension 1: [How to make it more advanced]
- Extension 2: [How to add new features]

---

## Project Difficulty Levels

Generate projects at the appropriate level:
- **Beginner**: Focuses on basics, heavy guidance, clear steps
- **Intermediate**: More complex logic, less hand-holding, some design decisions
- **Advanced**: Open-ended, optimization challenges, best practices focus

**Default Level**: [Specify: Beginner/Intermediate/Advanced based on my topics]

---

## Example Mini-Project Output

### Project: Personal Expense Tracker

**Description:** Build a command-line expense tracker that helps users log, categorize, and analyze their spending habits with data persistence.

**Real-World Use Case:** Learn budgeting habits and track where money goes each month.

**Estimated Time:** 4-5 hours

**Learning Objectives:**
- Day 1: Input validation, type conversion, string formatting
- Day 2: Dictionary for categories, lists for transactions
- Day 3: Loops for menu navigation, conditionals for filtering
- Day 4: Functions for add/view/analyze operations
- Day 5: Save/load from CSV file, exception handling

**Core Features:**
1. Add new expense (amount, category, description, date)
2. View all expenses or filter by category
3. Calculate total spending and spending by category
4. Save expenses to file automatically
5. Load previous expenses on startup
6. Display monthly summary with statistics
7. Input validation and error messages

**Bonus Features:**
1. Set budget limits and warn when exceeded
2. Visualize spending with simple ASCII charts
3. Export reports to formatted text files
4. Support multiple currencies with conversion

**Milestones:**
1. **(30 min)** Create data structures (list of expense dicts) and basic menu
2. **(45 min)** Implement add_expense() and view_expenses() functions
3. **(60 min)** Add file I/O (save_to_file, load_from_file)
4. **(45 min)** Implement filtering and analysis functions
5. **(30 min)** Add comprehensive error handling
6. **(30 min)** Polish UI and test edge cases

**Technical Specifications:**
- Input: User commands via CLI menu
- Output: Formatted tables, summary statistics, CSV file
- Data Structure: List of dictionaries, each expense = {date, category, amount, description}
- File Format: CSV with headers

**Sample Interaction:**
```
=== Expense Tracker ===
1. Add Expense
2. View All Expenses
3. View by Category
4. Monthly Summary
5. Exit

Choice: 1
Enter amount: 45.50
Enter category: Food
Enter description: Lunch at cafe
Expense added successfully!

Choice: 4
--- Monthly Summary ---
Total Spent: $342.75
Food: $145.20 (42%)
Transport: $87.50 (26%)
Entertainment: $110.05 (32%)
```

---

*Generate a project that makes learning fun and produces something you can actually use or showcase!*



=============================================================================================

## 📖 Markdown Formatting Reference

Quick reference for the Markdown features used in this README:

| Feature | Syntax | Result |
|---------|--------|--------|
| Headings | `# H1` `## H2` `### H3` | Different heading sizes |
| Bold | `**text**` | **text** |
| Italic | `*text*` | *text* |
| Code inline | `` `code` `` | `code` |
| Code block | ` ```python ` | Syntax-highlighted block |
| Link | `[text](url)` | [text](url) |
| Table | Use pipes `|` and hyphens `-` | See tables above |
| Checkboxes | `- [ ]` unchecked, `- [x]` checked | - [ ] Todo |
| Blockquote | `> text` | > quoted text |
| Horizontal rule | `---` | Line separator |
| Emoji | `:emoji_name:` | 🎉 🚀 ✅ |
| Collapsible | `<details><summary>` | Hidden content |

**Learn More**: [GitHub Markdown Guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
