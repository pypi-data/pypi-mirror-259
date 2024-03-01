from enum import Enum

class ScriptingLanguage(str, Enum):
    python = 'python'
    r = 'r'

class Script:
    def __init__(self, name: str, content: str, language: ScriptingLanguage) -> None:
        self.name = name
        self.content = content
        self.language = language

    def get_name(self) -> str:
        return self.name

    def get_content(self) -> str:
        return self.content

    def get_scripting_language(self) -> str:
        return self.language.value
