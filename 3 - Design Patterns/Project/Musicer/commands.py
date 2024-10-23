import logging
from abc import ABC, abstractmethod
from Musicer.playback.music_player_factory import FileInterface
from Musicer.globals import GlobalSettings

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class PlayCommand(Command):
    def __init__(self, music_file: FileInterface):
        self.music_file = music_file

    def execute(self):
        logging.info("Playing MP3 file.")
        self.music_file.play()

class PauseCommand(Command):
    def execute(self):
        logging.info("Pausing music.")

class VolumeUpCommand(Command):
    def __init__(self, settings: GlobalSettings):
        self.settings = settings

    def execute(self):
        new_volume = self.settings.volume + 10
        logging.info(f"Volume increased to {new_volume}.")
        self.settings.adjust_volume(new_volume)
