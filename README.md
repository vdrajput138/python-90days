# 🐍 Python 90 Days Challenge

Welcome to the Python 90 Days Challenge! This repository is designed to help you master Python through consistent daily practice and weekend projects over the next 8 weeks.

---

## 📁 Repository Structure

Each participant will have their own folder with a personalized learning path based on their target role (Data Analyst, Backend Developer, ML Engineer, etc.). The topics are organized week by week in the folder's README file.

---

## 🛠️ Initial Setup - Virtual Environment

Before starting the challenge, set up your Python virtual environment to keep dependencies isolated and organized.

### **Step 1: Create Virtual Environment**

**Windows:**
```bash
# Navigate to your project folder
cd python-90-days-challenge

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

**macOS/Linux:**
```bash
# Navigate to your project folder
cd python-90-days-challenge

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### **Step 2: Install Dependencies**

Once your virtual environment is activated (you'll see `(venv)` in your terminal), install required packages:

```bash
# Upgrade pip first
pip install --upgrade pip

# Install all requirements
pip install -r requirements.txt
```

### **Step 3: Verify Installation**

Check that everything is installed correctly:

```bash
# List all installed packages
pip list

# Check Python version
python --version
```

### **Step 4: Deactivate (when done coding)**

To deactivate the virtual environment:

```bash
deactivate
```

---

### 📦 Common Requirements

Your `requirements.txt` might include packages like:

```txt
# Testing and Code Quality
pytest==7.4.3
black==23.12.0
flake8==6.1.0

# Data Analysis (if needed)
pandas==2.1.4
numpy==1.26.2
matplotlib==3.8.2

# Web Development (if needed)
flask==3.0.0
requests==2.31.0

# Utilities
python-dotenv==1.0.0
```

> **💡 Tip**: Always activate your virtual environment before coding and deactivate when done!

---

### ⚠️ Important Notes

- **Never commit** the `venv/` folder to Git (add it to `.gitignore`)
- **Always activate** your virtual environment before running Python code
- **Update requirements.txt** when you install new packages:
  ```bash
  pip freeze > requirements.txt
  ```
- Each team member should create their own virtual environment

---

### 🔍 Troubleshooting

**Issue**: `python` command not found
- **Solution**: Try `python3` instead, or check Python installation

**Issue**: `venv\Scripts\activate` not working on Windows
- **Solution**: Use PowerShell and run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

**Issue**: Package installation fails
- **Solution**: Make sure virtual environment is activated and pip is updated

---

## 🔧 Common Git Commands

Here are the essential Git commands you'll use daily:

| Command | Description |
|---------|-------------|
| `git pull` | Pull latest changes from remote repository |
| `git status` | Display untracked changes and file status |
| `git add .` | Add all untracked files to staging |
| `git commit -m "message"` | Commit tracked files with a message |
| `git push` | Push committed changes to remote repository |

**Daily Git Workflow:**
```bash
git pull                           # Start your day
# ... work on your code ...
git add .                          # Stage your changes
git commit -m "Day X: Topic name"  # Commit with meaningful message
git push                           # Push to remote
```

---

## 📜 Challenge Rules

### ✅ Mandatory Requirements

1. **Daily Commits**: Make at least **1 meaningful commit per weekday** (Mon-Fri)
2. **Daily Problems**: Solve at least **2 problems minimum** from the daily 10-problem set
3. **Use Prompts**: Follow the provided prompts to generate practice questions
4. **Weekend Projects**: Complete mini-projects on weekends to integrate weekly learnings

### ❌ Penalties

| Violation | Penalty |
|-----------|---------|
| Miss 1 day | ₹10 per day |
| Miss 2+ weeks (10+ days) | **Double penalty** (₹20 per day) |

> **Note**: Penalties are paid to fellow competitors as accountability motivation!

---

## 🎯 Learning Workflow

### **Monday - Friday** (Weekdays)
1. Learn new topics for the day
2. Generate 10 practice problems using **Prompt #1**
3. Solve at least 2 problems (aim for more!)
4. Commit your solutions with meaningful messages

### **Saturday** (Assessment Day)
1. Review the entire week's topics
2. Generate 30-40 quick questions using **Prompt #2**
3. Take the interactive quiz using **Prompt #3**
4. Identify weak areas for focused review

### **Sunday** (Project Day)
1. Use **Prompt #4** to generate a mini-project
2. Spend 3-6 hours building the project
3. Integrate all concepts learned during the week
4. Commit and push your completed project

---

## 📝 Practice Prompts

### 1️⃣ Daily Problems Generator

**When to use**: Every day after learning new topics

**What it generates**: 10 coding problems (3 Easy, 3 Medium, 3 Hard, 1 Expert)

<details>
<summary>Click to view prompt</summary>

```markdown
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

*Generate problems that encourage hands-on coding and progressively build complexity.*
```

</details>

---

### 2️⃣ Weekend Quick Assessment Questions

**When to use**: Saturday - for rapid knowledge review

**What it generates**: 30-40 mixed-format questions (MCQs, True/False, Fill-in-blanks, One-liners)

<details>
<summary>Click to view prompt</summary>

```markdown
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

*Generate questions that thoroughly test understanding while being answerable within 1-2 minutes each.*
```

</details>

---

### 3️⃣ Interactive Quiz Generator

**When to use**: Saturday - for comprehensive testing with scoring

**What it generates**: Full interactive quiz with 25-30 questions, progress tracking, and performance analysis

<details>
<summary>Click to view prompt</summary>

```markdown
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

**Technical Requirements:**
- Build as an interactive React component (or specify your preferred format: HTML, Python CLI, etc.)
- Store questions in a structured format
- Track user responses
- Calculate and display statistics
- Allow restart/retry functionality

---

*Create an engaging quiz that accurately assesses knowledge while providing valuable learning feedback.*
```

</details>

---

### 4️⃣ Weekly Mini-Project Generator

**When to use**: Sunday - for hands-on application of weekly concepts

**What it generates**: Complete project specification with milestones, features, and testing checklist (3-6 hours to complete)

<details>
<summary>Click to view prompt</summary>

```markdown
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

1. **Project Overview** - Title, description, real-world use case
2. **Learning Objectives** - Which concepts from each day will be practiced
3. **Core Features** (Must-Have) - 5-7 essential features
4. **Bonus Features** (Optional) - 3-5 extra challenges
5. **Project Milestones** - 4-6 manageable steps with time estimates
6. **Technical Specifications** - Input/output requirements, data structures
7. **Sample Interaction** - Example of program in action
8. **Starter Code Structure** - Basic skeleton/template
9. **Testing Checklist** - 5-8 test cases
10. **Extension Ideas** - 2-3 ways to expand further

---

*Generate a project that makes learning fun and produces something you can actually use or showcase!*
```

</details>

---

## 📊 Progress Tracking

### Commit Message Format
Use clear, descriptive commit messages:

```bash
✅ Good Examples:
"Day 5: Solved 3 dictionary manipulation problems"
"Week 1 Project: Expense Tracker - Core features complete"
"Day 12: Completed OOP basics - 4 problems solved"

❌ Bad Examples:
"update"
"fixes"
"code changes"
```

### Weekly Checklist Template

Copy this to your weekly folder:

```markdown
## Week [X] Progress

**Topics Covered:**
- [ ] Day 1: [Topic]
- [ ] Day 2: [Topic]
- [ ] Day 3: [Topic]
- [ ] Day 4: [Topic]
- [ ] Day 5: [Topic]

**Problems Solved:** [X/50] (minimum 10 required)

**Weekend Activities:**
- [ ] Saturday: Completed quick assessment (Score: ___%)
- [ ] Saturday: Took interactive quiz (Score: ___%)
- [ ] Sunday: Mini-project completed ✓

**Missed Days:** [X] (Penalty: ₹___)
```

---

## 💡 Tips for Success

### 🎯 Consistency Tips
- Set a fixed time each day for coding (even 30 minutes counts!)
- Don't break the chain - commit something every weekday
- Quality over quantity - understand solutions deeply
- Review previous week's topics regularly

### 🚀 Problem-Solving Strategy
1. **Read carefully** - Understand what's being asked
2. **Plan first** - Write pseudocode before coding
3. **Start simple** - Get basic version working first
4. **Test thoroughly** - Check edge cases
5. **Refactor** - Improve code after it works

### 📚 Learning Resources
- **Official Docs**: [Python.org](https://docs.python.org/3/)
- **Practice Platform**: [LeetCode](https://leetcode.com/), [HackerRank](https://hackerrank.com/)
- **Community**: Stack Overflow, Reddit r/learnpython
- **Visualize Code**: [Python Tutor](https://pythontutor.com/)

---

## 🏆 Challenge Goals

By the end of 90 days, you will:
- ✅ Have solved **100+ coding problems**
- ✅ Built **12+ mini-projects**
- ✅ Developed **consistent coding habits**
- ✅ Created a **portfolio** of Python projects
- ✅ Gained **real-world programming skills**

---

## 🤝 Accountability Partners

Stay motivated by:
- Sharing daily progress with fellow challengers
- Code review each other's solutions
- Discuss alternative approaches
- Celebrate weekly wins together!

---

## 📞 Need Help?

- **Stuck on a problem?** Ask in the discussion forum
- **Missed multiple days?** Don't give up! Jump back in
- **Found a bug?** Create an issue in the repo
- **Have suggestions?** Pull requests welcome!

---

## 🎉 Let's Get Started!

1. Fork this repository
2. Create your personal folder
3. Copy your learning roadmap
4. Make your first commit today!

**Remember**: The best time to start was yesterday. The next best time is NOW!

---

*Happy Coding! 🚀*

---
