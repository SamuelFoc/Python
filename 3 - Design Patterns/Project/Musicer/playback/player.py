from Musicer.commands import Command


class MusicPlayer:
    def __init__(self):
        self.command_history = []

    def set_command(self, command: Command):
        self.command_history.append(command)

    def execute_command(self):
        if self.command_history:
            command = self.command_history.pop()
            command.execute()