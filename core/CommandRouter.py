import re


class CommandRouter:

    def __init__(self, command=None):
        self.cmd = command
        self.pattern = re.compile(r"{(.+?)}")
        self.datatypes = {
            ':any': r'.+',
            ':str': r'[A-Z-a-z]+',
            ':int': r'\d+'
        }
        self.registeredCmdRegexPatterns = {}
        self.callbackClass = None
        self.oop = True

    def set_callback(self, obj):
        self.callbackClass = obj

    def register(self, cmd_model, callback):
        # Transfer visual model to regex representation. Example: show user {:str} -> show user ([A-Z-a-z]+)
        matches = self.pattern.findall(cmd_model)
        if matches:
            for m in matches:
                cmd_model = str.replace(cmd_model, '{' + m + '}', '(' + self.datatypes[m] + ')')
        cmd_regex = re.compile(cmd_model)

        self.registeredCmdRegexPatterns[cmd_regex] = callback

    def route(self, cmd=None):

        if cmd is not None:
            self.cmd = cmd

        for key in self.registeredCmdRegexPatterns:
            # If a class is set with set_callback, update the key:vp array
            if isinstance(self.registeredCmdRegexPatterns[key], str):
                self.registeredCmdRegexPatterns[key] = [self.callbackClass, self.registeredCmdRegexPatterns[key]]

            # Match input command (self.cmd) with the regex we just created
            matches = key.search(self.cmd)
            if matches and matches.group(0) == self.cmd:
                getattr(self.registeredCmdRegexPatterns[key][0], self.registeredCmdRegexPatterns[key][1])(*matches.groups())
