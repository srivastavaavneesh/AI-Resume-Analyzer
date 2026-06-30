"""
ATS Score Service.
"""

from ai_resume_analyzer.schemas.resume import ResumeData


class ATSService:
    def calculate_score(self, resume: ResumeData) -> dict:
        score = 0
        strengths = []
        improvements = []

        # Contact Information (10)

        contact_score = 0

        if resume.name:
            contact_score += 2

        if resume.email:
            contact_score += 3

        if resume.phone:
            contact_score += 3

        if resume.linkedin:
            contact_score += 1

        if resume.github:
            contact_score += 1

        score += contact_score

        if contact_score == 10:
            strengths.append("Complete contact information.")
        else:
            improvements.append("Complete contact information.")
        # Skills (20)

        skill_count = len(resume.skills)

        if skill_count >= 10:
            score += 20
            strengths.append("Excellent technical skills.")
        elif skill_count >= 6:
            score += 15
            strengths.append("Good technical skills.")
        elif skill_count >= 3:
            score += 10
            improvements.append("Add more technical skills.")
        else:
            score += 5
            improvements.append("Technical skills section is weak.")

        # Experience (20)

        if resume.experience:
            score += 20
            strengths.append("Experience section detected.")
        else:
            improvements.append("Add professional experience.")

        # Education (15)

        if resume.education:
            score += 15
            strengths.append("Education section available.")
        else:
            improvements.append("Education section missing.")

        # Projects (15)

        if resume.projects:
            score += 15
            strengths.append("Projects section available.")
        else:
            improvements.append("Include project experience.")

        # Certifications (10)

        if resume.certifications:
            score += 10
            strengths.append("Certifications detected.")
        else:
            improvements.append("Add certifications.")

        grade = self._grade(score)

        return {
            "score": score,
            "grade": grade,
            "strengths": strengths,
            "improvements": improvements,
        }

    @staticmethod
    def _grade(score: int) -> str:
        if score >= 90:
            return "A+"

        if score >= 80:
            return "A"

        if score >= 70:
            return "B"

        if score >= 60:
            return "C"

        return "D"


ats_service = ATSService()
