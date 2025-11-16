"""
generate_curriculum.py
Generates a 7-week role-specific Python curriculum folder structure for 4 learners:
Viru (QA Automation + MLOps), Sid (Data Engineering), Aakash (Data Analyst), Abhijeet (Data Science)

What it creates:
<role>/
  Week_1/
    Day_1/ Day_2/ ... Day_5/
      topics.md
      references.md
      questions.md  (10 questions)
    Day_6_Quiz/
      quiz.md       (40-50 questions)
    Day_7_Project/
      project.md

Run: python generate_curriculum.py
"""

import os
import textwrap
from datetime import datetime

BASE_DIR = os.getcwd()

roles = {
    "Viru_QA_MLOps": {
        "desc": "QA Automation + MLOps",
        "weeks": {
            1: [
                "Python syntax & REPL, variables, types",
                "Lists, Tuples, Dictionaries, Sets",
                "Loops: for, while; conditionals: if/elif/else",
                "Functions & modular code",
                "File I/O (txt, csv) and basic logging",
                "Small scripts for test helpers",
            ],
            2: [
                "OOP basics: class, object, methods (Page Object pattern intro)",
                "Error handling: try/except/finally",
                "Modules, packages, pip, virtualenv",
                "CLI scripts & argument parsing (argparse)",
                "Debugging & simple logging",
            ],
            3: [
                "PyTest fundamentals",
                "Fixtures & parametrization",
                "Markers & xfail",
                "Test discovery",
                "Assertions & test design",
            ],
            4: [
                "Selenium / Playwright basics",
                "Locators & waits",
                "Page Object Model",
                "Headless runs",
                "Browser automation best practices",
            ],
            5: [
                "API testing with requests",
                "Schema/contract checks",
                "PyTest + API integration",
                "Mocking APIs",
                "Reporting test results",
            ],
            6: [
                "CI/CD for tests (GitHub Actions)",
                "Dockerize tests",
                "Test containers basics",
                "Artifact storage",
                "Automated test runs",
            ],
            7: [
                "MLOps intro: models & testing",
                "MLflow basics",
                "Model packaging",
                "Smoke tests for models",
                "Pipeline checks",
            ],
        },
    },
    "Sid_DataEngineering": {
        "desc": "Data Engineering",
        "weeks": {
            1: [
                "Python basics: types, loops, functions",
                "File handling: csv, json, xml",
                "Path handling: os, pathlib",
                "Parsing and streaming files",
                "Working with text & basic transforms",
            ],
            2: [
                "Generators & iterators for streaming ETL",
                "Working with binary formats & parquet (intro)",
                "Requests & API ingestion basics",
                "Robust error handling and retries",
                "Writing modular ETL scripts",
            ],
            3: [
                "sqlite3 and DB connectors",
                "Basic SQL from Python",
                "Transactions & error handling",
                "Connection pooling (intro)",
                "Data ingestion patterns",
            ],
            4: [
                "Batch pipeline patterns",
                "Scheduling strategies",
                "Idempotence & resumability",
                "Monitoring basics",
                "Logging & alerting",
            ],
            5: [
                "Airflow fundamentals",
                "DAG structure",
                "Operators & Hooks",
                "XCom and templating",
                "Local testing of DAGs",
            ],
            6: [
                "PySpark basics",
                "RDD vs DataFrame",
                "Basic transformations & actions",
                "Cluster vs local mode",
                "Performance considerations",
            ],
            7: [
                "End-to-end pipeline project: ingest → transform → store",
                "Documentation",
                "Observability",
            ],
        },
    },
    "Aakash_DataAnalysis": {
        "desc": "Data Analysis",
        "weeks": {
            1: [
                "Python basics: variables, lists, dicts, strings",
                "Loops and conditionals for data tasks",
                "Basic functions & code reuse",
                "String operations & datetime intro",
                "Small scripts to parse CSV/TSV",
            ],
            2: [
                "File I/O and parsing edge-cases",
                "Basic plotting with matplotlib",
                "Numpy intro for analysts",
                "Error handling & validation",
                "Preparing data for Pandas",
            ],
            3: [
                "Pandas: read/write, index, selection",
                "filtering & boolean masks",
                "adding & transforming columns",
                "groupby basics",
                "missing data handling",
            ],
            4: [
                "Merge & join operations",
                "Time-series basics in Pandas",
                "Resampling & rolling windows",
                "Performance tips",
                "Pandas pipeline patterns",
            ],
            5: [
                "Matplotlib deep dive",
                "Seaborn usage",
                "Intro to Plotly",
                "Dashboard basics (conceptual)",
                "Storytelling with charts",
            ],
            6: [
                "Excel automation (openpyxl/xlsxwriter)",
                "Exporting reports",
                "Templated reports",
                "Scripting repetitive reporting tasks",
            ],
            7: [
                "Case study: Full analysis project (data cleaning → EDA → visualization → summary)"
            ],
        },
    },
    "Abhijeet_DataScience": {
        "desc": "Data Science Development",
        "weeks": {
            1: [
                "Python basics: types, control flow, functions",
                "Collections and comprehensions",
                "Basic algorithms: sorting/search",
                "Math module and numerical thinking",
                "Small algorithmic exercises",
            ],
            2: [
                "File I/O & data loading",
                "Plotting basics for EDA",
                "Profiling & simple optimization",
                "Error handling & reproducibility",
                "Virtual env & package management",
            ],
            3: [
                "NumPy arrays, broadcasting",
                "Vectorized ops",
                "Indexing & slicing",
                "Interfacing with Pandas",
                "Performance",
            ],
            4: [
                "Pandas for DS (EDA & cleaning)",
                "Feature engineering basics",
                "Dealing with missing & categorical data",
            ],
            5: [
                "Regression algorithms",
                "Classification basics",
                "Model evaluation metrics",
                "Train/test split & cross-val",
            ],
            6: [
                "Feature pipelines",
                "Serialization (pickle/joblib)",
                "Simple model serving (FastAPI)",
                "Basic deployment considerations",
            ],
            7: ["End-to-end ML project: data → model → evaluate → mini-deploy"],
        },
    },
}

# Generic references (role-appropriate references added later per day)
COMMON_REFERENCES = [
    "https://docs.python.org/3/tutorial/",
    "https://realpython.com/",
    "https://www.programiz.com/python-programming",
    "Core Python (YouTube) - Corey Schafer: https://www.youtube.com/@Coreyms",
]

ROLE_RESOURCES = {
    "Viru_QA_MLOps": [
        "PyTest docs: https://docs.pytest.org/",
        "Selenium docs: https://www.selenium.dev/documentation/",
        "Playwright Python: https://playwright.dev/python/",
        "MLflow: https://mlflow.org/",
    ],
    "Sid_DataEngineering": [
        "Pandas I/O: https://pandas.pydata.org/docs/user_guide/io.html",
        "Apache Airflow docs: https://airflow.apache.org/docs/",
        "PySpark docs: https://spark.apache.org/docs/latest/api/python/",
    ],
    "Aakash_DataAnalysis": [
        "Pandas docs: https://pandas.pydata.org/pandas-docs/stable/",
        "Matplotlib tutorial: https://matplotlib.org/stable/tutorials/index.html",
        "Seaborn: https://seaborn.pydata.org/",
    ],
    "Abhijeet_DataScience": [
        "NumPy docs: https://numpy.org/doc/",
        "Scikit-learn: https://scikit-learn.org/stable/",
        "FastAPI: https://fastapi.tiangolo.com/",
    ],
}


def safe_mkdir(path):
    os.makedirs(path, exist_ok=True)


def write_text_file(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def mk_intro_md(role_name, role_desc):
    return f"# {role_name}\n\nRole: {role_desc}\n\nGenerated: {datetime.utcnow().isoformat()}Z\n\nThis folder contains a 7-week curriculum with daily topics, references, practice questions (10/day), weekly quizzes (40-50 Qs) and mini-projects.\n"


def generate_questions_for_topics(topics, day_index):
    """
    Returns exactly 10 practice questions varying difficulty per day.
    Uses topics (list of strings) to produce domain-specific prompts.
    """
    q = []
    # Ensure variety: 4 simple, 4 medium, 2 hard
    # simple
    for i, t in enumerate(topics[:4]):
        q.append(f"(S) Write a small Python script demonstrating: {t}.")
    # medium
    for i, t in enumerate(topics[4:8] if len(topics) > 4 else topics[:4]):
        q.append(
            f"(M) Create a function or small program that uses: {t}. Include docstring and a simple example."
        )
    # hard
    if len(topics) >= 1:
        q.append(
            f"(H) Design and implement a small module that composes at least two of these: {', '.join(topics[:3])}. Add unit-test ideas."
        )
    else:
        q.append(
            "(H) Design a small program that composes multiple concepts from this week's topics."
        )
    q.append(
        f"(H) Optimize or refactor one of your previous solutions to be more robust and handle edge-cases."
    )
    # Trim/extend to exactly 10
    if len(q) < 10:
        extra = 10 - len(q)
        for i in range(extra):
            q.append(
                f"(S) Extra practice problem {i+1}: Implement a tiny utility related to {topics[0] if topics else 'python basics'}."
            )
    return q[:10]


def generate_quiz_for_week(week_topics, role_key):
    """
    Produce 40-50 mixed questions (MCQ + short coding prompts).
    We'll produce 45 by default.
    """
    num = 45
    quiz = []
    # approx 60% MCQ/short answer, 40% coding
    mcq_count = int(num * 0.6)
    coding_count = num - mcq_count
    # MCQs: ask conceptual about topics
    for i in range(mcq_count):
        t = week_topics[i % len(week_topics)]
        quiz.append(
            f"MCQ/Concept [{i+1}]: Briefly explain or pick the correct option about: {t}."
        )
    # Coding prompts:
    for j in range(coding_count):
        t = week_topics[(j + 3) % len(week_topics)]
        quiz.append(
            f"Coding [{j+1}]: Implement a small function or script that demonstrates: {t}. Include edge case handling."
        )
    # Append 1-3 role-specific meta questions
    quiz.append(
        "ShortAnswer: Describe one real-world scenario where you'd apply this week's concepts in your role."
    )
    if role_key == "Viru_QA_MLOps":
        quiz.append(
            "ShortAnswer: How would you design a test for an ML model's output drift?"
        )
    elif role_key == "Sid_DataEngineering":
        quiz.append(
            "ShortAnswer: How would you make an ETL job idempotent and resumable?"
        )
    elif role_key == "Aakash_DataAnalysis":
        quiz.append(
            "ShortAnswer: Describe how you'd present the top 3 insights to a non-technical stakeholder."
        )
    elif role_key == "Abhijeet_DataScience":
        quiz.append(
            "ShortAnswer: Which metric would you use for imbalanced classification and why?"
        )
    return quiz


def generate_project_for_week(role_name, week_num, topics):
    title = f"Week {week_num} Mini-Project: Combine {', '.join(topics[:3])} (role: {role_name})"
    desc = (
        f"{title}\n\n"
        "Description:\n"
        f"- Build a small project that integrates multiple topics covered this week.\n"
        "- Deliverables:\n"
        "  1) Code (well-structured, functions/classes where appropriate)\n"
        "  2) README describing how to run the project\n"
        "  3) 2-3 test cases or example runs\n\n"
        "Success criteria:\n"
        "- Code runs end-to-end and demonstrates the week's learning objectives.\n"
    )
    return desc


def build_curriculum():
    for role_key, rdata in roles.items():
        role_dir = os.path.join(BASE_DIR, role_key)
        safe_mkdir(role_dir)
        # top-level README for role
        write_text_file(
            os.path.join(role_dir, "README.md"), mk_intro_md(role_key, rdata["desc"])
        )
        # role-specific resource file
        role_refs = COMMON_REFERENCES + ROLE_RESOURCES.get(role_key, [])
        write_text_file(
            os.path.join(role_dir, "references_overview.md"),
            "# Role-wide References\n\n" + "\n".join(f"- {r}" for r in role_refs),
        )

        for week_num in range(1, 8):
            week_name = f"Week_{week_num}"
            week_path = os.path.join(role_dir, week_name)
            safe_mkdir(week_path)

            week_topics = rdata["weeks"][week_num]
            # Week overview file
            week_overview = (
                f"# {role_key} - {week_name}\n\nTopics this week:\n\n"
                + "\n".join(f"- {t}" for t in week_topics)
            )
            write_text_file(os.path.join(week_path, "week_overview.md"), week_overview)

            # Create day 1-5
            for day in range(1, 6):
                day_dir = os.path.join(week_path, f"Day_{day}")
                safe_mkdir(day_dir)

                # split topics per day: rotate/select subset
                # choose up to 4 topics per day to focus on
                start_idx = (day - 1) * 2
                daily_topics = week_topics[start_idx : start_idx + 4] or week_topics[:4]

                topics_md = f"# Day {day} — Topics\n\n" + "\n".join(
                    f"- {t}" for t in daily_topics
                )
                write_text_file(os.path.join(day_dir, "topics.md"), topics_md)

                # references: mix common + role
                refs_md = "# References\n\n" + "\n".join(f"- {r}" for r in role_refs)
                write_text_file(os.path.join(day_dir, "references.md"), refs_md)

                # generate 10 practice questions
                questions = generate_questions_for_topics(daily_topics, day)
                q_md = "# Practice Questions (10)\n\n" + "\n".join(
                    f"{i+1}. {qq}" for i, qq in enumerate(questions)
                )
                write_text_file(os.path.join(day_dir, "questions.md"), q_md)

            # Day 6: Quiz
            day6_dir = os.path.join(week_path, "Day_6_Quiz")
            safe_mkdir(day6_dir)
            quiz_list = generate_quiz_for_week(week_topics, role_key)
            quiz_md = "# Weekly Quiz\n\n" + "\n".join(
                f"{i+1}. {qq}" for i, qq in enumerate(quiz_list)
            )
            write_text_file(os.path.join(day6_dir, "quiz.md"), quiz_md)

            # Day 7: Project
            day7_dir = os.path.join(week_path, "Day_7_Project")
            safe_mkdir(day7_dir)
            proj = generate_project_for_week(role_key, week_num, week_topics)
            write_text_file(os.path.join(day7_dir, "project.md"), proj)

    print("Curriculum generation complete.")
    print(f"Created roles in: {BASE_DIR}")


if __name__ == "__main__":
    build_curriculum()
