from enum import Enum

class documentsTitle(str, Enum):
    identity_card = 'Letërnjoftimi'
    passport = 'Pasaporta'
    driver_license  = 'Patenta e Shoferit'
    employment_contracts = 'Kontratat e Punësimit'
    job_descriptions = 'Përshkrimet e Punës'
    assessments = 'Vlerësimet'
    investigation_by_the_court='Dokumenti i hetimeve nga gjykata',
    criminal_past='E kaluara kriminale'
    training_certificate = 'Certifikatat e Trajnimit'
    Others = 'Planet e Zhvillimit'



CATEGORY_TITLE_MAPPING = {
    1: [documentsTitle.identity_card, documentsTitle.passport, documentsTitle.driver_license],
    2: [documentsTitle.employment_contracts, documentsTitle.job_descriptions],
    3: [documentsTitle.assessments],
    4: [documentsTitle.training_certificate],
    5: [documentsTitle.investigation_by_the_court,documentsTitle.criminal_past],
    6: [documentsTitle.Others]
}
