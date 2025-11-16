import os
import json

# ============================================
#  GLOBAL CONFIG
# ============================================

roles = {
    "Viru_QA_MLOps": "QA Automation + MLOps",
    "Sid_DataEngineering": "Data Engineering",
    "Aakash_DataAnalysis": "Data Analysis",
    "Abhijeet_DataScience": "Data Science",
}

# Topics per week per role (very high-level — customizable later)
week_topics = {
    1: ["Functions", "Lists", "Tuples"],
    2: ["Dictionaries", "Sets", "String Handling"],
    3: ["File Handling", "OS Module", "Error Handling"],
    4: ["Modules & Packages", "Virtual Envs", "Logging"],
    5: ["OOP Basics: Class, Object, Methods"],
    6: ["Advanced OOP: Inheritance, Polymorphism"],
    7: ["Project Prep: Data, APIs, Testing"],
}

# References
references = [
    "https://www.programiz.com/python-programming",
    "https://realpython.com/",
    "https://www.youtube.com/@Coreyms",
]


# Generate 10 practice questions based on topic
def generate_questions(topics):
    base_questions = []
    for t in topics:
        base_questions.append(f"Write a Python program related to {t}.")
        base_questions.append(f"Create 3 examples demonstrating {t}.")
        base_questions.append(f"Explain {t} with code.")
    return base_questions[:10]


# Generate quiz questions
def generate_quiz(topics):
    quiz = []
    for t in topics:
        for i in range(6):
            quiz.append(f"MCQ: Concept check on {t} — Question {i+1}")
    return quiz[:50]


# Mini project
def generate_project(week, topics):
    return f"Mini Project Week {week}: Build a program combining {', '.join(topics)}."


# ============================================
#  FUNCTION TO CREATE FILES
# ============================================


def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


# ============================================
#  MAIN CREATION LOGIC
# ============================================

for role, desc in roles.items():
    for week in range(1, 7 + 1):
        week_path = os.path.join(role, f"Week_{week}")
        os.makedirs(week_path, exist_ok=True)

        topics_for_week = week_topics[week]

        # Day 1–5
        for day in range(1, 6):
            day_path = os.path.join(week_path, f"Day_{day}")
            os.makedirs(day_path, exist_ok=True)

            # Topics file
            write_file(
                os.path.join(day_path, "topics.md"),
                f"# Topics for Day {day}\n\n"
                + "\n".join(f"- {t}" for t in topics_for_week),
            )

            # References file
            write_file(
                os.path.join(day_path, "references.md"),
                "# References\n\n" + "\n".join(f"- {ref}" for ref in references),
            )

            # Practice questions
            questions = generate_questions(topics_for_week)
            write_file(
                os.path.join(day_path, "questions.md"),
                "# Practice Questions\n\n"
                + "\n".join(f"{i+1}. {q}" for i, q in enumerate(questions)),
            )

        # Day 6: Quiz
        day6_path = os.path.join(week_path, "Day_6_Quiz")
        os.makedirs(day6_path, exist_ok=True)

        quiz_questions = generate_quiz(topics_for_week)
        write_file(
            os.path.join(day6_path, "quiz.md"),
            "# Weekly Quiz\n\n"
            + "\n".join(f"{i+1}. {q}" for i, q in enumerate(quiz_questions)),
        )

        # Day 7: Project
        day7_path = os.path.join(week_path, "Day_7_Project")
        os.makedirs(day7_path, exist_ok=True)

        write_file(
            os.path.join(day7_path, "project.md"),
            "# Mini Project\n\n" + generate_project(week, topics_for_week),
        )

print("Curriculum folders + files generated successfully!")
