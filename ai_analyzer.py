from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_resume(resume_text, job_description):

    prompt = f"""
You are an AI resume screening assistant.

Analyze the candidate's resume against the given job description.

Resume:
{resume_text}

Job Description:
{job_description}

Give the analysis using exactly these sections:

### Candidate Suitability
Briefly explain how suitable the candidate is for this job.

### Matching Skills
List the important skills found in both the resume and job description.

### Missing Skills
List the important skills required by the job description but not clearly found in the resume.

### Candidate Strengths
Mention the candidate's relevant strengths.

### Areas for Improvement
Mention what the candidate could improve to better match the job.

### Recommendation
Give a short, neutral recommendation about the candidate's fit.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"AI analysis is temporarily unavailable. Please try again later.\n\nError: {e}"