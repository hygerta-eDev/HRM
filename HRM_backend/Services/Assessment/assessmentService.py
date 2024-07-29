from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.assessmentModel import Assessment
from Models.assessmentQuestionsModel import AssessmentQuestion
import json 
from Schema.enums.assessment_options import STANDARD_OPTIONS
import logging
from typing import Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
from Schema.assesmentSchema import AssessmentCreate,AssessmentUpdate


class AssessmentService:
    @staticmethod
    def get_all_assessments(db: Session = Depends(get_db)):
        return db.query(Assessment).all()
    @staticmethod
    def get_all_active_assessments(db: Session = Depends(get_db)):
        return db.query(Assessment).filter(Assessment.deleted_at == None).all()
    @staticmethod
    def get_assessment_by_id(db: Session, assessment_id: int):
        return db.query(Assessment).filter(Assessment.id == assessment_id).first()
    
    
    # def create_assessment(Assessments: AssessmentCreate, db: Session = Depends(get_db)):

    #     db_assessment = Assessment(
    #         employee_id=Assessments.employee_id,
    #         user_id = Assessments.user_id,
    #         job_position_id = Assessments.job_position_id,
    #         evaluation_period = Assessments.evaluation_period,
    #         rate = Assessments.rate,
    #         finished = Assessments.finished,
    #         status = Assessments.status,
    #         performance_objectives = Assessments.performance_objectives,
    #         general_evaluation = Assessments.general_evaluation,
    #         employee_notes = Assessments.employee_notes,
    #         employee_notes_date=Assessments.employee_notes_date,
    #         created_at=Assessments.created_at
    #     )

    #     db.add(db_assessment)
    #     db.commit()
    #     db.refresh(db_assessment)

    #     return db_assessment
    # @staticmethod
    # def update_assessments(assessment_id: int, assessment: AssessmentUpdate, db: Session = Depends(get_db)):
    #     db_assessments = db.query(Assessment).filter(Assessment.deleted_at == None, Assessment.id == assessment_id).first()

    #     if db_assessments:
    #         if assessment.employee_id is not None:
    #             db_assessments.employee_id = assessment.employee_id
    #         if assessment.job_position_id is not None:
    #             db_assessments.job_position_id = assessment.job_position_id
    #         if assessment.user_id is not None:
    #             db_assessments.user_id = assessment.user_id
    #         if assessment.evaluation_period is not None:
    #             db_assessments.evaluation_period = assessment.evaluation_period
    #         if assessment.rate is not None:
    #             db_assessments.rate = assessment.rate
    #         if assessment.finished is not None:
    #             db_assessments.finished = assessment.finished
    #         if assessment.status is not None:
    #             db_assessments.status = assessment.status
    #         if assessment.performance_objectives is not None:
    #             db_assessments.performance_objectives = assessment.performance_objectives
    #         if assessment.employee_notes is not None:
    #             db_assessments.employee_notes = assessment.employee_notes
    #         if assessment.general_evaluation is not None:
    #             db_assessments.general_evaluation = assessment.general_evaluation
    #         if assessment.employee_notes_date is not None:
    #             db_assessments.employee_notes_date = assessment.employee_notes_date
    #         if assessment.updated_at is not None:
    #             db_assessments.updated_at = assessment.updated_at

    #         db.commit()
    #         db.refresh(db_assessments)

    #     return db_assessments

    
    # @staticmethod
    # def delete_assessment(assessment_id: int, db: Session):
    #     db_assessment = db.query(Assessment).filter(Assessment.id == assessment_id).first()

    #     if db_assessment:
    #         db_assessment.soft_delete()  
    #         db.commit()

    #     return db_assessment
    def create_assessment(assessment_data: AssessmentCreate, db: Session = Depends(get_db)):
        db_assessment = Assessment(
            employee_id=assessment_data.employee_id,
            user_id=assessment_data.user_id,
            job_position_id=assessment_data.job_position_id,
            evaluation_period=assessment_data.evaluation_period,
            rate=assessment_data.rate,
            finished=assessment_data.finished,
            status=assessment_data.status,
            performance_objectives=assessment_data.performance_objectives,
            general_evaluation=assessment_data.general_evaluation,
            # employee_notes=assessment_data.employee_notes,
            # employee_notes_date=assessment_data.employee_notes_date,
            created_at=assessment_data.created_at
        )

        db.add(db_assessment)
        db.commit()
        db.refresh(db_assessment)
        logging.info(f"Created Assessment with ID: {db_assessment.id}")
        initial_questions = [
            AssessmentQuestion(
                title="Cilësia e punës",
                description="Puna është përfunduar me saktësi (me pak ose aspak gabime), në mënyrë efikase dhe brenda afateve me mbikëqyrje minimale.",
                assessment_id=db_assessment.id,# weight=1,
                notes="null",
                selected_option=None,
                options=json.dumps(STANDARD_OPTIONS) 
            ),
            AssessmentQuestion(
                title="Besueshmëria",
                description="Në vazhdimësi përformon në nivel të lartë, menaxhon kohën dhe ngarkesën e punës në mënyrë efektive duke i përmbushur përgjegjësitë.",
                assessment_id=db_assessment.id,# weight=1,
                notes="null",
                selected_option=None,
                options=json.dumps(STANDARD_OPTIONS) 
            ),
            AssessmentQuestion(
                title="Gjykimi dhe vendimarrja",
                description="Merr vendime të menduara, të arsyetuara mire, ushtron gjykim të mire, shkathtësi dhe kreativitet në zgjidhjen e problemeve.",
                assessment_id=db_assessment.id,# weight=1,
                notes="null",
                selected_option=None,
                options=json.dumps(STANDARD_OPTIONS) 
            ),
            AssessmentQuestion(
                title="Aftësitë komunikuese",
                description="Komunikimet me shkrim dhe me gojë janë te qarta, të organizuara dhe efektive. I dëgjon mire dhe kupton mire natyrën e problemeve.",
                assessment_id=db_assessment.id,# weight=1,
                notes="null",
                selected_option=None,
                options=json.dumps(STANDARD_OPTIONS) 
            ),
            AssessmentQuestion(
                title="Iniciativa dhe fleksibiliteti",
                description="Demostron iniciativë, shpesh duke kërkuar përgjegjësi shtesë, identifikon probemet dhe zgjidhjet. Përshtatet me sfidat e reja dhe ndryshimet e papritura.",
                assessment_id=db_assessment.id,# weight=1,
                notes="null",
                selected_option=None,
                options=json.dumps(STANDARD_OPTIONS) 
            ),
            AssessmentQuestion(
                title="Bashkëpunimi dhe puna ekipore",
                description="Merr vendime të menduara, të arsyetuara mire, ushtron gjykim të mire, shkathtësi dhe kreativitet në zgjidhjen e problemeve.",
                assessment_id=db_assessment.id,# weight=1,
                notes="null",
                selected_option=None,
                options=json.dumps(STANDARD_OPTIONS) 
            ),
            AssessmentQuestion(
                title="Njohuritë për pozitën e punës:",
                description="Merr vendime të menduara, të arsyetuara mire, ushtron gjykim të mire, shkathtësi dhe kreativitet në zgjidhjen e problemeve.",
                assessment_id=db_assessment.id,# weight=1,
                notes="null",
                selected_option=None,
                options=json.dumps(STANDARD_OPTIONS) 
            ),
            AssessmentQuestion(
                title="Trajnimi dhe zhvillimi",
                description="Vazhdimisht kërkon mënyra për të forcuar performancën dhe monitoron rregullisht zhvillimet e reja në fushën e punës.",
                assessment_id=db_assessment.id,# weight=1,
                notes="null",
                selected_option=None,
                options=json.dumps(STANDARD_OPTIONS) 
            ),
            # Add other questions as needed
        ]

        db.add_all(initial_questions)
        db.commit()

        # Refresh to get IDs for questions
        for question in initial_questions:
            db.refresh(question)
            logging.info(f"Created Question with ID: {question.id}, associated with Assessment ID: {db_assessment.id}")

        return {
            "id": db_assessment.id,  # Return the assessment ID
            "questions": [
                {
                    "id": question.id,
                    "title": question.title,
                    "description": question.description,
                    "selected_option": question.selected_option  # Include selected_option

                    
                }
                for question in initial_questions
            ]
        }
    @staticmethod
    def update_assessments(assessment_id: int, assessment: AssessmentUpdate, db: Session = Depends(get_db)):
        db_assessment = db.query(Assessment).filter(Assessment.deleted_at == None, Assessment.id == assessment_id).first()

        if db_assessment:
            if assessment.employee_id is not None:
                db_assessment.employee_id = assessment.employee_id
            if assessment.job_position_id is not None:
                db_assessment.job_position_id = assessment.job_position_id
            if assessment.user_id is not None:
                db_assessment.user_id = assessment.user_id
            if assessment.evaluation_period is not None:
                db_assessment.evaluation_period = assessment.evaluation_period
            if assessment.rate is not None:
                db_assessment.rate = assessment.rate
            if assessment.finished is not None:
                db_assessment.finished = assessment.finished
            if assessment.status is not None:
                db_assessment.status = assessment.status
            if assessment.performance_objectives is not None:
                db_assessment.performance_objectives = assessment.performance_objectives
            if assessment.employee_notes is not None:
                db_assessment.employee_notes = assessment.employee_notes
            if assessment.general_evaluation is not None:
                db_assessment.general_evaluation = assessment.general_evaluation
            if assessment.employee_notes_date is not None:
                db_assessment.employee_notes_date = assessment.employee_notes_date
            if assessment.updated_at is not None:
                db_assessment.updated_at = assessment.updated_at

            db.commit()
            db.refresh(db_assessment)

        return db_assessment

    @staticmethod
    def delete_assessment(assessment_id: int, db: Session):
        db_assessment = db.query(Assessment).filter(Assessment.id == assessment_id).first()

        if db_assessment:
            db_assessment.soft_delete()
            db.commit()

        return db_assessment

    @staticmethod
    def update_assessment_question_option(assessment_question_id: int, selected_option: str, db: Session):
        db_assessment_question = db.query(AssessmentQuestion).filter(AssessmentQuestion.id == assessment_question_id).first()

        if db_assessment_question:
            options = json.loads(db_assessment_question.options)
            if selected_option in options:
                db_assessment_question.selected_option = selected_option
                db.commit()
                db.refresh(db_assessment_question)

        return db_assessment_question
    
    option_weights = {
        "I tejkalon pritjet": 4,
        "I plotëson pritjet": 3,
        "Ka nevojë për përmirësim": 2,
        "E papranueshme": 1
    }

    def get_weight_from_option(selected_option: str) -> Optional[int]:
        """
        Retrieve the weight for the given selected option.
        """
        return AssessmentService.option_weights.get(selected_option, None)


  

    def update_question_weight(question_id: int, weight: int, db: Session) -> bool:
        """
        Update the question weight in the database.
        """
        question = db.query(AssessmentQuestion).filter(AssessmentQuestion.id == question_id).first()
        if question:
            question.weight = weight
            db.commit()
            return weight
        return None

    def process_question_update(question_id: int, selected_option: str, db: Session) -> Optional[int]:
        """
        Process the question update by mapping the selected option to a weight and updating the question.
        """
        weight = AssessmentService.get_weight_from_option(selected_option)
        
        if weight is None:
            raise HTTPException(status_code=400, detail="Invalid option selected")

        updated_weight = AssessmentService.update_question_weight(question_id, weight, db)
        
        if updated_weight is None:
            raise HTTPException(status_code=500, detail="Failed to update question weight")
        
        return updated_weight