from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

if __name__ != "__main__":
    #from .openaiKey import OPENAI_API_KEY as OPEN_API_KEY
    from .openaiKey import OPENAI_API_KEY_GONCALO as OPEN_API_KEY
    from .chatMessagesVersions import UserInterface

else:
    #from openaiKey import OPENAI_API_KEY as OPEN_API_KEY
    from openaiKey import OPENAI_API_KEY_GONCALO as OPEN_API_KEY
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

    interface = UserInterface(0.9, syllabus)

    interface.showAnswers()
    interface.exportAnswers("answers", "txt")

    # interface._UserInterface__translateAnswersToPT()
    # interface.showTranslations()
    # interface.exportTranslations("translations", "txt")

    # interface.exportAnswersTranslations("fullText", "txt")
