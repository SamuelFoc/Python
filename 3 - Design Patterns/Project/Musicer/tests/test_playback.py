import unittest
from Musicer.playback.music_player_factory import MusicPlayerFactory
from Musicer.playback.file_types import MP3, FLAC, WAV


class TestPlayback(unittest.TestCase):

    def setUp(self):
        self.factory = MusicPlayerFactory()

    def test_create_mp3(self):
        music_file = self.factory.create_music_file("mp3")
        self.assertIsInstance(music_file, MP3)

    def test_create_flac(self):
        music_file = self.factory.create_music_file("flac")
        self.assertIsInstance(music_file, FLAC)

    def test_create_wav(self):
        music_file = self.factory.create_music_file("wav")
        self.assertIsInstance(music_file, WAV)

    def test_create_invalid_format(self):
        with self.assertRaises(TypeError):
            self.factory.create_music_file("avi")

    def tearDown(self):
        self.factory = None


if __name__ == "__main__":
    unittest.main()
