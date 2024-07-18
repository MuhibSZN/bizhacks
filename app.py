import streamlit as st
from src.recruit_ai import RecruitAI
from src.pdf_processing import get_text_from_pdf

def main():
    st.title("Recruitment Analysis Tool")

    openai_api_key = st.text_input("Enter your OpenAI API key:", type="password")

    if openai_api_key:
        recruit_ai = RecruitAI(openai_api_key=openai_api_key)

        st.header("Upload Job Description PDF")
        job_desc_file = st.file_uploader("Choose the job description PDF file", type="pdf")

        st.header("Upload Candidate Resume PDF")
        resume_file = st.file_uploader("Choose the candidate resume PDF file", type="pdf")

        if job_desc_file and resume_file:
            job_description_str = get_text_from_pdf(job_desc_file)
            resume_str = get_text_from_pdf(resume_file)

            candidate_id = recruit_ai.generate_candidate_id("Unknown Candidate")

            name_prompt = recruit_ai.get_prompt_2(curriculum=resume_str, candidate_id=candidate_id)
            name_response = recruit_ai.get_recruit_results(name_prompt)

            candidate_name_extracted = re.search(r"Candidate Name: ([A-Za-z\s]+)", name_response)
            candidate_actual_name = candidate_name_extracted.group(1).strip() if candidate_name_extracted else "Unknown Candidate"

            recruit_ai.candidate_mapping[candidate_id] = candidate_actual_name

            prompt = recruit_ai.get_prompt(requirements=job_description_str, curriculum=resume_str, candidate_id=candidate_id)

            token_count = recruit_ai.count_tokens(prompt)
            st.write(f"The prompt contains {token_count} tokens.")

            response = recruit_ai.get_recruit_results(prompt)

            response_with_actual_name = response.replace(f"Candidate {candidate_id}", f"Candidate {candidate_actual_name}")

            st.header("Recruitment Analysis Results")
            st.write(response_with_actual_name)

            st.header("Candidate Mapping")
            st.write(recruit_ai.candidate_mapping)

if __name__ == "__main__":
    main()
