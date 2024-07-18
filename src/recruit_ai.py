import openai
import time
import random
import re
from fpdf import FPDF
from io import BytesIO

class PDF(FPDF):
    def header(self):
        if self.header_enabled:
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, 'Job Description', 0, 1, 'C')

    def __init__(self, with_header=True):
        super().__init__()
        self.header_enabled = with_header

    def add_text(self, text):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, text)

class RecruitAI:
    def __init__(self, openai_api_key: str) -> None:
        openai.api_key = openai_api_key
        self.candidate_mapping = {}

    def text2pdf(self, txt_content: str, with_header: bool = True) -> BytesIO:
        pdf = PDF(with_header=with_header)
        pdf.add_page()
        pdf.add_text(txt_content)
        _file = BytesIO(pdf.output(dest="S").encode("latin1"))
        return _file

    def generate_candidate_id(self, candidate_name: str) -> str:
        candidate_id = f"{random.randint(10000, 99999)}"
        self.candidate_mapping[candidate_id] = candidate_name
        return candidate_id

    def get_prompt(self, requirements: str, curriculum: str, candidate_id: str) -> str:
        prompt = f"""
        You are the best and least biased recruiter of all time. You are analyzing a candidate's resume for a job vacancy.
        Although this instruction is in English, you may receive a resume in another language, for example Hindi. Please always generate the results in English.
        This vacancy can be in various fields and for various positions.
        You must exclusively base your evaluation on the Requirements and the Candidate's resume provided. The credential sections must be based solely off of the requirements provided below may be the job description itself or some specific qualifications the candidate must have to fill the position, or both.
        To ensure unbiased evaluation, the candidate's name has been replaced with a random identifier. Focus on the qualifications, skills, and experience presented. Do not consider any irrelevant information (e.g., candidate's name, gender, etc.) that could potentially lead to bias.
        First, you must create a step summarizing the candidate's qualities and highlight points that are of extreme interest for the vacancy. The resume may contain characteristics beyond what is required; if these characteristics are beneficial for the vacancy, it is worth highlighting them. After the initial step, you must score each characteristic observed in the candidate's resume, giving a score from 0 to 10, where 0 means the candidate does not meet the characteristic and 10 means the candidate perfectly meets the characteristic. In this step, you must exclusively pair the characteristics with the job requirements, returning the name of the characteristic and the candidate's score for that characteristic, without adding or omitting anything.
        In the end, you must give a final overall score (also between 0 to 10) for this candidate based on the previous scores.

        The result should be in the following format:

        Candidate ID: Candidate ID: {candidate_id}

        Credentials:
        Here is an example of possible credential sections, which must be decided solely from the requirements:
        1. Education (0-10): Does the candidate's education meet or exceed the job requirements?
        2. Work Experience (0-10): Does the candidate's work experience align with the job requirements?
        3. Technical Skills (0-10): Does the candidate possess the required technical skills?
        4. Soft Skills (0-10): Does the candidate demonstrate strong communication, teamwork, and problem-solving skills?
        5. Cultural Fit (0-10): Does the candidate align with the company's values and culture?
        The scores should be a single number (to a precision of 1) out of 10. A short explanatory sentence should be given for each credential section.

        Final Result:
        The overall final score will be listed here and will be a number out of 10 to a precision of 0.1.

        Requirements:
        {requirements}

        Candidate's Resume:
        {curriculum}
        """
        return prompt

    def get_prompt_2(self, curriculum: str, candidate_id: str) -> str:
        prompt = f"""
        Extract the candidate's name from the resume provided below.
        The result should be in the following format:

        Candidate ID: {candidate_id}
        Candidate Name: [Extracted Candidate Name]

        Candidate's Resume:
        {curriculum}
        """
        return prompt

    def get_recruit_results(self, prompt: str) -> str:
        max_retries = 5
        for attempt in range(max_retries):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are an expert recruiter."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=1500
                )
                return response.choices[0].message["content"]
            except openai.error.RateLimitError:
                if attempt < max_retries - 1:
                    time.sleep((2 ** attempt) + (0.5 * attempt))
                else:
                    raise

    def count_tokens(self, text: str) -> int:
        tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")
        return len(tokenizer.encode(text))
