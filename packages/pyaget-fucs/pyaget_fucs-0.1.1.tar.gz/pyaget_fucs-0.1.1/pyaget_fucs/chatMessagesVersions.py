"""
FUC maker chat messages versions
"""

CHAT_MESSAGES = {
    1.0: {
        "importantTopics":None,
        "messageRoot":None,
        "characterLimits": [1000, 1000, 3000],
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

PROMPT_DEFAULT = {
    "system": "You are world class technical documentation writer."
                + "When asked a question, structure your answer in bullet points, unless they don't request it."
                + "Optimize your answers like a Engenieer"
                + "Calculate the number of characters typed after your answer",
    "user": "{input}",
}

import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

try:  
    from .openaiKey import OPENAI_API_KEY
except ImportError:
    from openaiKey import OPENAI_API_KEY

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
            *,
            message: str = None,
            prompt: dict[str:str] = PROMPT_DEFAULT,
            apiKey: str = OPENAI_API_KEY,
            verbose: bool = True,
            translateTo: str = None,
            animated: bool = False
            ) -> (None):

        super(UserInterface, self).__init__(verbose)

        self._syllabus = syllabus
        self._version = version
        self._message = message

        self.beginProcess("Formatting the chat messages")
        self.__generateChatMessage(version, message, verbose)
        self.endProcess() if verbose else None

        self.beginProcess("Connecting to chat gpt")
        self.__openChat(
            apiKey if apiKey is not None else OPENAI_API_KEY,
            prompt
            )
        self.endProcess()

        self._answers = []
        self._translations = []
        self._file = None

        print(*self._chatMessage)

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
        for answer in self._answers:
            translation = self.__ask(
                f"Translate follow text, using a web translator {tool}, to {language} and check your text grammar using the web tool {grammar}: \n\n{answer}",
                suffix="(Translations)"
            )
            translations.append(translation)

        self._translations.extend(translations)

        return translations

    def __translateAnswersToPT(
            self: object,
            tool: str = "DeepL",
            grammar: str = "Flip"
            ) -> (list[str]):

        translations = []
        for answer in self._answers:
            translation = self.__ask(
                f"Translate follow text, using a web translator {tool}, to PT-PT and check your text grammar using the Flip: \n\n{answer}",
                suffix="(Translations)"
            )
            translations.append(translation)

        self._translations.extend(translations)

        return translations

    def __generateChatMessage(
            self: object,
            version: int,
            message: str = None,
            verbose: bool = False
        ):
        _message = CHAT_MESSAGES.get(version)\
            if message is None\
            else message

        if _message is not None:
            _chatMessage = ChatMessage(self._syllabus, **_message,
                                       verbose=verbose)\
                if type(_message) is dict\
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
        print(*self._answers, sep="\n")
        return None

    def showTranslations(self: object, animated: bool = False) -> (None):
        print(*self._translations, sep="\n")
        return None

    def ask(
            self: object,
            showAnswer: bool = False,
            animated: bool = False
            ) -> (list[str]):

        answers = []
        total = len(self._chatMessage)
        for i, message in enumerate(self._chatMessage):
            answer = self.__ask(message, suffix=f"{i+1}/{total}")
            answers.append(answer)

        if showAnswer and animated:
            botprint(*answers, sep="\n")
        elif showAnswer:
            self.showAnswers(animated)

        self._answers.extend(answers)
        
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
            "answers": self._answers,
            "translations": self._translations,
            "answers & translations": self._answers + self._translations
        }[param]

        _del = 15*"="
        total = len(_param)
        title = "\n{}\n {} #%2d/{:>2} \n{}\n\n".format(
            _del, param.title(), total, _del
            )

        for i, content in enumerate(_param):
            filePath = self.__export(
                (title % (i+1)) + content,
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
        
        return None

class Chat(Verbose):

    __defaultApiKey = OPENAI_API_KEY

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
            verbose: bool = False
            ) -> (None):
        self._messageRoot = messageRoot
        self._syllabus = syllabus
        self._importantTopics = importantTopics
        self._characterLimits = characterLimits

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

        messageRoot = self._messageRoot
        importantTopics = self._importantTopics
        characterLimits = self._characterLimits

        self._chatMessage = []
        for i, topic in enumerate(importantTopics):
            message = messageRoot.format(
                importantTopic=topic[0],
                requirements=', '.join(topic[1:]),
                chars=characterLimits[i],
                syllabus=self._syllabus,
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


import sys,time
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

