"""
FUC maker chat messages versions
"""

PEDAGOGICAL_MODEL = """
The total contact hours for this course is {contactHours} hours, the ECTS equal {ECTS}, and the estimated total working hours are around {workingHours}.
"""

PROMPT_DEFAULT = {
    "system": "You are world class technical documentation writer.\
        Structure your answer in bullet points, unless they don't request it.\
        Optimize your answer like a Engenieer.\
        Calculate the number of characters typed after your answer including whitespace and punctuations.\
        Review your text grammar with Grammarly web tool.\
        Avoid using line breaks in your answer.",
    "user": "{input}",
}


CHAT_MESSAGES = {
    1.0: {# ILO and Evidence OK, but Teaching Methodologies nope
        "importantTopics": [
            ("Contact hours",
                "Divide the contact hours into the following teaching typologies:\
                theoretical, theoretical-practical, laboratory, and tutorial.",
                "Specify number of hours"),

            ("Intended learning outcomes (ILOs)",
                "using the Bloom's taxonomy verbs in your answer",
                "answer in numeric list",
                "do not quote syllabus topic",
                "do not explain it"),

            ("Evidence of the each syllabus topic coherence with the previous ILOs",
                "linking ILOs topics to related, one or more, syllabus topic numbers",
                "optimize your answer quoting syllabus by numbers",
                "in a summarized bullet list",
                "Be brief in your words"),

            ("Optimized Teaching Methodologies (TMs) and specific learning of the curricular unit",
                "articulated with the pedagogical model",
                "including autonomous student time to study",
                "quote digital technology applications to integrate to TMs",
                "quote previous syllabus topics"),

            ("Suggest assessment types such as exams, tests, quizzes, individual, group work, debates, and others to ensure that students are learning",
                "Articulated with the pedagogical model",
                "Based on syllabus",
                "Group assessments must not exceed 40% of the assessment total",
                "Distribute assessments over the course specifying how to",
                "Recommends final exam or not?"),

            ("Evidence of the TMs and assessments coherence with the previous ILOs",
                "linking each ILOs topics to respective TMs and assessment",
                "optimize your answer quoting ILOs numbers",
                "in a summarized bullet list"),

            ("Suggest current and relevant books to this curricular unit",
                "show this bibliographies in APA style",
                "sort this bibliographies by relevancy",
                "split bibliographies in fundamentals and complementary"),

            ("Observations",
                "Summary of key Concepts/topics of the course; reference to ECTS,  Pedagogical Model, the aim to equip students with the ability to achieve to ILOs.",
                "highlight the practical applications that contribute to the development of desired skills or outcomes.",
                "highlight the course emphasises and the use of pegagogial model, including tools and methods, to foster students for challenges in the field of work of the Bachelor Degree.",
                "quote the ultimate goal for students")
        ],
        "messageRoot": """
            Develop a text about the topic '{importantTopic}', considering the follow requirements: {requirements} and based on the syllabus:
            {syllabus}
            Your text must be less than {chars} characters.
            Integrates with applied psychology, other vital areas of your university.
            Considering the pedagogical model: \n%s
            """.lstrip(" ")%PEDAGOGICAL_MODEL
            #After optimize and summarize your text.
        ,
        
        "characterLimits": [1000, 1000, 1000, 1000, 3000, 3000, 3000, 1000],
    },
    0.9: {# ILO and Evidence OK, but Teaching Methodologies nope
        "importantTopics": [
            ("Intended learning outcomes (ILOs)",
                "using the Bloom's taxonomy verbs",
                "in a numeric list",
                "do not quote syllabus topic",
                "do not explain it"),

            # ("Evidence of the each syllabus topic coherence with the previous ILOs",
            #     "linking each ILOs topics to respective syllabus topic numbers",
            #     "optimize your answer quoting syllabus by numbers",
            #     "in a summarized bullet list"),

            # ("Optimized Teaching Methodologies (TMs) and specific learning of the curricular unit",
            #     "articulated with the pedagogical model teorethical and pratical",
            #     "including autonomous student time to study",
            #     "quote digital technology applications to integrate to TMs",
            #     "quote previous syllabus topics"),

            # ("Suggest assessments to ensure that students are learning what they know",
            #     "articulated with the pedagogical model teorethical and pratical"),

            # ("Evidence of the each syllabus topic coherence with the previous ILOs",
            #     "linking each ILOs topics to respective syllabus topic numbers",
            #     "optimize your answer quoting syllabus by numbers",
            #     "in a summarized bullet list"),

            # ("Suggest current and relevant books to this curricular unit",
            #     "show this bibliograthies in APA style",
            #     "sort descending this bibliographies by year"),
        ],
        "messageRoot": """
            Develop a text about the topic '{importantTopic}', considering the follow requirements: {requirements} and based on the syllabus:
            {syllabus}
            Your text must be less than {chars} characters.
            Review your text grammar with Grammarly web tool.
            """.lstrip(" ")
            #After optimize and summarize your text.
        ,
        "characterLimits": [1000, 1000, 3000, 1000, 1000, 1000],
    },
}

import os
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from os.path import basename

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


class Verbose:
    __endPrint = "..."
    __endMessage = "Done"

    def __init__(self: object, enable: bool):
        self._enable = enable
        return None

    def beginProcess(self: object, msg: str) -> (None):
        if self._enable:
            print(msg, end=self.__endPrint)
        return None

    def endProcess(self: object) -> (None):
        if self._enable:
            print(self.__endMessage)
        return None


class UserInterface(Verbose):

    def __init__(
            self: object,
            version: int,
            syllabus: str,
            contactHours: int,
            workingHours: int,
            ECTS: int,
            *,
            message: str = None,
            prompt: dict[str:str] = PROMPT_DEFAULT,
            apiKey: str = None,
            verbose: bool = True,
            translateTo: str = None,
            animated: bool = False,
            questions: dict[str:str] = None, # Edit Important Topics manually
            showQuestions: bool = False
            ) -> (None):

        super(UserInterface, self).__init__(verbose)

        self._importantTopics = [
            topic[0] for topic in CHAT_MESSAGES.get(version, {}).get("importantTopics", [])
        ]
        self._syllabus = syllabus
        self._version = version
        self._message = message
        self._questions = questions
        self._contactHours = contactHours
        self._workingHours = workingHours
        self._ECTS = ECTS

        self.beginProcess("Formatting the chat messages")
        self.__generateChatMessage(version, message, verbose)
        self.endProcess() if verbose else None

        if apiKey is None:
            raise ValueError("You need an Openai api key!")

        self.beginProcess("Connecting to chat gpt")
        self.__openChat(
            apiKey,
            prompt
            )
        self.endProcess()

        self._answers = {}
        self._translations = {}
        self._file = None

        if showQuestions:
            print(40*"=",*self._chatMessage, sep="\n", end="\n"+40*"="+"\n")

        self.ask(animated=animated)

        if translateTo is not None:
            self.__translateAnswers(language=translateTo)
        
        return None

    def __translateAnswers(
            self: object,
            language: str = "PT-PT",
            tool: str = "DeepL",
            grammar: str = "LanguageTool"
            ) -> (list[str]):

        translations = []
        for tag, answer in self._answers.items():
            translation = self.__ask(
                f"Translate follow text, using a web translator {tool}, to {language} and check your text grammar using the web tool {grammar}: \n\n{answer}",
                suffix="(Translations)"
            )
            translations[tag+"_translate"] = translation

        self._translations = translations

        return translations

    def __translateAnswersToPT(
            self: object,
            tool: str = "DeepL",
            grammar: str = "Flip"
            ) -> (list[str]):

        translations = {}
        for tag, answer in self._answers.items():
            translation = self.__ask(
                f"Translate follow text, using a web translator {tool}, to PT-PT and check your text grammar using the Flip: \n\n{answer}",
                suffix="(Translations)"
            )
            translations[tag] = translation

        self._translations = translations

        return translations

    def __generateChatMessage(
            self: object,
            version: int,
            message: str = None,
            verbose: bool = False
        ):

        if self._questions is None and message is None:
            _message = CHAT_MESSAGES.get(version)
        elif self._questions is not None:
            _message = self._questions
        else:
            _message = message

        if _message is not None:
            _chatMessage = ChatMessage(
                self._syllabus, **_message,
                ECTS=self._ECTS, contactHours=self._contactHours,
                workingHours=self._workingHours, verbose=verbose
                ) if type(_message) is dict\
                  else ChatMessage(None, _message, verbose=verbose)
            self._chatMessage = _chatMessage.getChatMessage()
        else:
            self._chatMessage = None
            raise ValueError(f"Version '{version}' not found. Available versions {list(d.keys())}")
        
        return None

    def __openChat(
            self: object,
            apiKey: str,
            prompt: dict[str:str]
            ) -> (None):

        self._chat = Chat(apiKey, prompt, self._enable)
        
        return None

    @property
    def syllabus(self: object):
        return self._syllabus

    @property
    def answers(self: object):
        return self._answers

    @property
    def translations(self: object):
        return self._translations

    @property
    def prompt(self: object):
        return self._prompt

    def getSyllabus(self: object):
        return self._syllabus

    def getAnswers(self: object):
        return self._answers

    def getTranslations(self: object):
        return self._translations

    def getPrompt(self: object):
        return self._prompt

    def setPrompt(self: object, prompt: dict[str:str]):
        self._chat.setPrompt(prompt)
        return None

    def __ask(self: object, msg: str, suffix: str = "") -> (str):
        answer = self._chat.invoke(msg, suffix).content
        return answer

    def showAnswers(self: object, animated: bool = False) -> (None):
        print(*[f"k:\n\tv" for k, v in self._answers.items()], sep="\n")
        return None

    def showTranslations(self: object, animated: bool = False) -> (None):
        print(*[f"k:\n\tv" for k, v in self._translations.items()], sep="\n")
        return None

    def ask(
            self: object,
            showAnswer: bool = False,
            animated: bool = False
            ) -> (list[str]):

        answers = {}
        total = len(self._chatMessage)
        try:
            for i, message in enumerate(self._chatMessage):
                answer = self.__ask(message, suffix=f"{i+1}/{total}")
                answers[self._importantTopics[i]] = answer
        except KeyboardInterrupt:
            pass

        if showAnswer and animated:
            botprint(*answers.values(), sep="\n")
        elif showAnswer:
            self.showAnswers(animated)

        self._answers = answers
        
        return answers

    def __fileExist(self: object, filePath: str) -> (str):
        filepath, extension = os.path.splitext(filePath)
        fileAmount = filePath.split("_")[-1]
        fileAmount = int(fileAmount)\
            if fileAmount.isdigit()\
            else None
        amount = 0 if fileAmount is None else fileAmount
        extension = extension[1:]
        while os.path.exists(filePath):      
            change = f".{extension}"\
                if f"_{amount}.{extension}" not in filePath\
                else f"_{amount}.{extension}"
            filePath = filePath.replace(
                change, f"_{amount+1}.{extension}"
            )
        return filePath

    def __export(
            self: object,
            text: str,
            filename: str,
            extension: str = "txt",
            path: str = "./",
            dontClose: bool = False
            ) -> (str):

        if self._file is None or self._file.closed:
            filePath = f"{path.strip('/')}/{filename}.{extension}"

            filePath = self.__fileExist(filePath)

            self._file = open(filePath, "x", encoding="utf-8")

            self.__filePath = filePath

        self._file.write(text)

        if not dontClose:
            self._file.close()
            
        return self.__filePath

    def __exportParam(
            self: object,
            param: str,
            *args
            ) -> (str):

        _param = {
            "answers": self._answers.copy(),
            "translations": self._translations.copy(),
            "answers & translations": self._answers | self._translations
        }[param]

        total = len(_param)

        for tag in ["Contact hours", "Observations"]:
            content = _param.pop(tag)
            _del = len(tag)*"="
            title = "\n{}\n{}\n{}\n".format(
                _del, tag.title(), _del
                )
            filePath = self.__export(
                title + content,
                *args,
                dontClose=True
            )

        for i, (tag, content) in enumerate(_param.items()):
            _del = len(tag)*"="
            title = "\n{}\n{}\n{}\n".format(
                _del, tag.title(), _del
                )
            filePath = self.__export(
                title + content,
                *args,
                dontClose=i<(total-1)
            )

        return filePath

    def exportAnswers(
            self: object,
            filename: str,
            extension: str = "txt",
            path: str = "./"
            ) -> (str):

        if extension == "txt":
            filePath = self.__exportParam("answers", filename, extension, path)
        elif extension == "json":
            pass    
        
        return filePath

    def exportTranslations(
            self: object,
            filename: str,
            extension: str = "txt",
            path: str = "./"
            ) -> (str):

        filePath = self.__exportParam("translations", filename, extension, path)
        
        return filePath

    def exportAnswersTranslations(
            self:object,
            filename: str,
            extension: str = "txt",
            path: str = "./"
            ) -> (str):

        filePath = self.__exportParam(
            "answers & translations", filename, extension, path
            )
        
        return filePath


    def __startServer(self: object, email: str) -> (None):
        import getpass
        self.__server = server = smtplib.SMTP(
            #host='smtp.outlook.com', port=587
            host="smtp.office365.com", port=587
            #host='smtp.gmail.com', port=587
            )
        server.starttls()
        while True:
            try:
                server.login(
                    email, 
                    getpass.getpass(f"\n\nOUTLOOK ACCESS\nlogin: {email}\npassword: ")
                )
            except smtplib.SMTPAuthenticationError as err:
                print(err)
            else:
                break
        return None
    
    def sendByEmail(
            self: object,
            *filename: str,
            send_from: str = "natanael.quintino@ipiaget.pt",
            send_to: str = "natanael.quintino@ipiaget.pt"
            ) -> (None):
        self.__startServer(send_from)
        subject = f'''FUC "{', '.join(filename)}" finished'''
        bodyMessage = f'''Caro(a), A(s) FUC(s) "{', '.join(filename)}" foi(ram) concluida(s). Meus cordiais cumprimentos, Pyaget FUC Generator'''
        send_mail(
            send_from,
            send_to,
            subject, 
            bodyMessage, 
            filename,
            self.__server
            )

        return None

class Chat(Verbose):

    __defaultApiKey = None

    def __init__(
            self: object,
            apiKey: str = None,
            prompt: dict[str: str] = PROMPT_DEFAULT,
            verbose: bool = False
            ) -> (None):

        super(Chat, self).__init__(verbose)

        self.__apiKey = apiKey\
            if apiKey is not None\
            else self.__defaultApiKey

        self._chat = ChatOpenAI(openai_api_key=self.__apiKey)
        if prompt is not None:
            self.__generatePrompt(prompt)

        return None

    def __generatePrompt(
            self: object,
            prompt: dict[str:str]
            ) -> (None):

        self._prompt = ChatPromptTemplate.from_messages(
            prompt.items() if prompt is not None
                           else ("user", "{input}")
        )

        # Chainning prompt to char
        self._chain = self._prompt | self._chat
        
        return None

    def setPrompt(
            self: object,
            prompt: dict[str:str]
            ) -> (None):
        self.__generatePrompt(prompt)
        return None

    def invoke(
            self: object,
            userMessage: str,
            suffix: str = ""
            ) -> (str):

        self.beginProcess(f"Asking to ChatGPT {suffix}")
        answer = self._chain.invoke(
            {"input": userMessage},
        )
        self.endProcess()
        
        return answer


class ChatMessage(Verbose):

    def __init__(
            self: object,
            syllabus: str,
            messageRoot: str,
            importantTopics: list[str] = None,
            characterLimits: list[int] = None,
            contactHours: int = None,
            workingHours: int = None,
            ECTS: int = None,
            verbose: bool = False
            ) -> (None):
        self._messageRoot = messageRoot
        self._syllabus = syllabus
        self._importantTopics = importantTopics
        self._characterLimits = characterLimits
        self._contactHours = contactHours
        self._workingHours = workingHours
        self._ECTS = ECTS

        super(ChatMessage, self).__init__(verbose)

        if importantTopics is not None and characterLimits is not None:
            self.__formatMessage()
        else:
            self._chatMessage = self._messageRoot

        return None

    def __formatMessage(
            self: object,
            ) -> (None):

        if self._syllabus is None:
            self._chatMessage = None
            return None

        self._chatMessage = []
        for i, topic in enumerate(self._importantTopics):
            message = self._messageRoot.format(
                importantTopic=topic[0],
                requirements=', '.join(topic[1:]),
                chars=self._characterLimits[i],
                syllabus=self._syllabus,
                contactHours=self._contactHours,
                workingHours=self._workingHours,
                ECTS=self._ECTS
            ).strip("\t ")

            if len(topic) == 1:
                message.replace(
                    ", considering the follow requirements: and",
                    ""
                )

            self._chatMessage.append(message)

        return None

    @property
    def chatMessage(self: object):
        return self._chatMessage

    def getChatMessage(self: object):
        return self._chatMessage


import sys
import time
def botprint(
        *text: str,
        sep: str = "",
        end: str = "\n",
        delay_time: float = .01
        ) -> (None):
    for _text in text:
        for character in _text:
            sys.stdout.write(character) 
            sys.stdout.flush()
            #print(character, end="")
            if character not in "\n\t ":
                time.sleep(delay_time)
    return None


def send_mail(send_from, send_to, subject, text, files=None,
              server="127.0.0.1"):
    
    if type(send_to) is not list:
        send_to = [send_to]

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

    print ('Sending email to outlook', end="...")
    server.sendmail(send_from, send_to, subject, text)
    # smtp = smtplib.SMTP(server)
    # smtp.sendmail(send_from, send_to, msg.as_string())
    print("Done")
    server.quit()
    #smtp.close()
    return None
    