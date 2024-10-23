import unittest
from Musicer.globals import GlobalSettings


class TestGlobalSettings(unittest.TestCase):

    def setUp(self):
        self.settings = GlobalSettings()

    def test_initial_settings(self):
        self.assertEqual(self.settings.volume, 50)
        self.assertEqual(self.settings.theme, "light")

    def test_adjust_volume(self):
        self.settings.adjust_volume(70)
        self.assertEqual(self.settings.volume, 70)

    def test_set_theme(self):
        self.settings.set_theme("dark")
        self.assertEqual(self.settings.theme, "dark")


if __name__ == "__main__":
    unittest.main()
