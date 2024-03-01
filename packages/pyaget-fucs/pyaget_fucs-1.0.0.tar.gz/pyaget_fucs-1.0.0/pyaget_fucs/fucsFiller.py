import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

if __name__ != "__main__":
    from .chatMessagesVersions import UserInterface

else:
    from chatMessagesVersions import UserInterface

    # Clip here your syllabus content
    syllabus = """
    1. Introduction and overview: internal organization of a computer 
    2. Digital representation of information 
    3. Logical functions 
    4. Study of a didactic architecture 
    5. Architecture of a processor 
    6. Arithmetic circuits 
    7. Sequential circuits 
    8. Memory system 
    9. Input / Output Peripherals 
    """

    # ===============================
    # Not implemented
    # ===============================
    expertiseChoice = 2
    expertise = {
        1: "Cibersecurity",
        2: "Artificial Intelligence"
    }[expertiseChoice]
    # ===============================

    contactHours = 45
    workingHours = 150
    ECTS = workingHours/25

    openai_key = {
        1: os.environ["OPENAI_API_KEY"], # GPT 3.5
        2: os.environ["OPENAI_API_KEY_GONCALO"], # GPT 4
    }[1]

    interface = UserInterface(
        1.0, syllabus, contactHours, workingHours, ECTS,
        apiKey=openai_key, showQuestions=False
        )

    interface.showAnswers()
    interface.exportAnswers("answers", "txt", ".")
    # interface.sendByEmail(
    #     "answers.txt",
    #     send_from="natanael.quintino@ipiaget.pt",
    #     send_to="natanael.quintino@ipiaget.pt"
    #     )

    # interface._UserInterface__translateAnswersToPT()
    # interface.showTranslations()
    # interface.exportTranslations("translations", "txt")

    # interface.exportAnswersTranslations("fullText", "txt")
