from abc import ABC, abstractmethod

# ABSTRACT INTERFACE FOR MUSIC FILE
# ---
# The play method must be implemented based
# on the file type (MP3, FLAC, WAV, etc.)
class FileInterface(ABC):
    @abstractmethod
    def play(self) -> None:
        pass

# ---

# INDIVIDUAL FILE TYPES IMPLEMENTATIONS
# ---
# Play method is implemented for each
# type of the music file
class MP3(FileInterface):
    def play(self):
        # Don't forget to create unit test for this method
        # when implementing it!
        print("Playing MP3")
    
class WAV(FileInterface):
    def play(self):
        # Don't forget to create unit test for this method
        # when implementing it!
        print("Playing WAV")

class FLAC(FileInterface):
    def play(self):
        # Don't forget to create unit test for this method
        # when implementing it!
        print("Playing FLAC")