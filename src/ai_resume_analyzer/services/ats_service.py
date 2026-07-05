"""
ATS Score Service.

Provides functionality to calculate an ATS (Applicant Tracking System)
compatibility score for resumes. The scoring logic evaluates sections such as:
- Contact information
- Skills
- Experience
- Education
- Projects
- Certifications

Each section contributes points toward a total score, which is then mapped
to a letter grade (A+ through D). The service also returns strengths and
areas for improvement to guide candidates in enhancing their resumes.
"""

from ai_resume_analyzer.schemas.resume import ResumeData


class ATSService:
    def calculate_score(self, resume: ResumeData) -> dict:
        """
        Calculate ATS Score

        Args:
            resume (ResumeData): Parsed resume data containing fields like
                                 name, email, phone, linkedin, github,
                                 skills, experience, education, projects,
                                 and certifications.

        Returns:
            dict: {
                "score": int,             # Total ATS score
                "grade": str,             # Letter grade (A+, A, B, C, D)
                "strengths": list[str],   # Positive aspects of the resume
                "improvements": list[str] # Suggestions for improvement
            }
        """
        score = 0
        strengths = []
        improvements = []

        # -------------------------------
        # Contact Information (10 points)
        # -------------------------------
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

        # -------------------------------
        # Skills (20 points)
        # -------------------------------
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

        # -------------------------------
        # Experience (20 points)
        # -------------------------------
        if resume.experience:
            score += 20
            strengths.append("Experience section detected.")
        else:
            improvements.append("Add professional experience.")

        # -------------------------------
        # Education (15 points)
        # -------------------------------
        if resume.education:
            score += 15
            strengths.append("Education section available.")
        else:
            improvements.append("Education section missing.")

        # -------------------------------
        # Projects (15 points)
        # -------------------------------
        if resume.projects:
            score += 15
            strengths.append("Projects section available.")
        else:
            improvements.append("Include project experience.")

        # -------------------------------
        # Certifications (10 points)
        # -------------------------------
        if resume.certifications:
            score += 10
            strengths.append("Certifications detected.")
        else:
            improvements.append("Add certifications.")

        # -------------------------------
        # Final Grade
        # -------------------------------
        grade = self._grade(score)

        return {
            "score": score,
            "grade": grade,
            "strengths": strengths,
            "improvements": improvements,
        }

    @staticmethod
    def _grade(score: int) -> str:
        """
        Convert numeric score into letter grade.

        Args:
            score (int): ATS score

        Returns:
            str: Grade (A+, A, B, C, D)
        """
        if score >= 90:
            return "A+"
        if score >= 80:
            return "A"
        if score >= 70:
            return "B"
        if score >= 60:
            return "C"
        return "D"


# Singleton instance of ATSService for reuse
ats_service = ATSService()
