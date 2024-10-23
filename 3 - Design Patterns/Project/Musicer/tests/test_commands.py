import unittest
import logging
from Musicer.playback.music_player_factory import MusicPlayerFactory
from Musicer.commands import PlayCommand, PauseCommand, VolumeUpCommand
from Musicer.globals import GlobalSettings


class TestCommands(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Configure logging for the test cases
        logging.basicConfig(level=logging.INFO)

    def setUp(self):
        self.factory = MusicPlayerFactory()
        self.mp3_file = self.factory.create_music_file("mp3")
        self.settings = GlobalSettings()

    def test_play_command(self):
        play_command = PlayCommand(self.mp3_file)
        with self.assertLogs(level='INFO') as log:
            play_command.execute()
        self.assertIn("Playing MP3 file.", log.output[0])

    def test_pause_command(self):
        pause_command = PauseCommand()
        with self.assertLogs(level='INFO') as log:
            pause_command.execute()
        self.assertIn("Pausing music.", log.output[0])

    def test_volume_up_command(self):
        volume_up_command = VolumeUpCommand(self.settings)
        initial_volume = self.settings.volume
        volume_up_command.execute()
        self.assertEqual(self.settings.volume, initial_volume + 10)


if __name__ == "__main__":
    unittest.main()
