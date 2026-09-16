skills = [
    "python",
    "java",
    "c++",
    "c",
    "sql",
    "mysql",
    "html",
    "css",
    "javascript",
    "react",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data science",
    "pandas",
    "numpy",
    "git",
    "github",
    "docker",
    "aws",
    "azure",
    "linux",
    "mongodb",
    "flask",
    "django",
    "spring",
    "tensorflow",
    "pytorch"
]


def find_matching_skills(resume_text, job_description):

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    matching_skills = []
    missing_skills = []

    for skill in skills:

        if skill in job_description:

            if skill in resume_text:
                matching_skills.append(skill)
            else:
                missing_skills.append(skill)

    return matching_skills, missing_skills
def calculate_match_score(matching_skills, missing_skills):

    total_skills = len(matching_skills) + len(missing_skills)

    if total_skills == 0:
        return 0

    score = (len(matching_skills) / total_skills) * 100

    return round(score, 2)