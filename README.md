# AI Resume Screening System

An AI-powered resume screening system that analyzes resumes against a given job description, identifies matching and missing skills, calculates a match score, and provides AI-based recommendations.

## Features

- Upload resume in PDF format
- Extract resume text using Python
- Compare resume skills with job requirements
- Calculate resume match percentage
- Analyze resume using Gemini AI
- Identify matching and missing skills
- Generate candidate strengths and improvement suggestions
- Provide a short AI-based recommendation
- Handle temporary AI API errors

## Technologies Used

- Python
- Streamlit
- PyPDF2
- Google Gemini API
- python-dotenv
- Git & GitHub

## How It Works

1. User uploads a resume in PDF format.
2. The system extracts the resume text using PyPDF2.
3. The user provides a job description.
4. Python compares the resume with the required skills.
5. A preliminary skill match score is calculated.
6. The resume and job description are sent to the Gemini API.
7. Gemini analyzes the candidate and generates structured feedback.
8. The results are displayed through the Streamlit interface.

## AI Integration

The system integrates the Google Gemini API to perform intelligent resume analysis.

The application sends the extracted resume content and job description to the Gemini model through the Google GenAI Python SDK. The AI analyzes the candidate's suitability, matching skills, missing skills, strengths, areas for improvement, and provides a recommendation.

The Gemini API key is stored securely in an environment variable and is excluded from the GitHub repository using `.gitignore`.

## Installation

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install the required Python packages.
4. Create a `.env` file and add your Gemini API key.
5. Run the Streamlit application.

### Environment Variable

```text
GEMINI_API_KEY=your_api_key_here