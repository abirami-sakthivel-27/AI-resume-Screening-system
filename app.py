import streamlit as st
from resume_parser import extract_text
from skill_matcher import find_matching_skills, calculate_match_score
from ai_analyzer import analyze_resume

st.title("AI Resume Screening System")

st.write("Upload your resume and paste the job description.")

resume = st.file_uploader(
    "Upload your resume",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste the Job Description"
)

if resume and job_description:

    resume_text = extract_text(resume)
matching_skills, missing_skills = find_matching_skills(
    resume_text,
    job_description
)

match_score = calculate_match_score(
    matching_skills,
    missing_skills
)

st.subheader("Resume Match Score")

st.metric(
    label="Overall Match",
    value=f"{match_score}%"
)
st.subheader("Matching Skills")
st.write(matching_skills)

st.subheader("Missing Skills")
st.write(missing_skills)
st.subheader("AI Resume Analysis")

if st.button("Analyze Resume with AI"):

    with st.spinner("AI is analyzing the resume..."):

        ai_result = analyze_resume(
            resume_text,
            job_description
        )

    st.write(ai_result)