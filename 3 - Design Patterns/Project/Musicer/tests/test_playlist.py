import unittest
from Musicer.playlist import User
from Musicer.subscription import FreeSubscription


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.user = User(user_id=1, name="Alice", subscription=FreeSubscription())
        self.playlist = self.user.create_playlist("Chill Beats")

    def test_create_playlist(self):
        self.assertEqual(self.playlist.name, "Chill Beats")
        self.assertIn(self.playlist, self.user.playlists)

    def test_add_song(self):
        self.playlist.add_song("Song A")
        self.assertIn("Song A", self.playlist.songs)

    def test_remove_song(self):
        self.playlist.add_song("Song B")
        self.playlist.remove_song("Song B")
        self.assertNotIn("Song B", self.playlist.songs)

    def test_observer_notification(self):
        self.playlist.add_song("Song C")
        # Here, you would implement a method to capture the notifications.
        # This might require modifying the `update` method to record messages.


if __name__ == "__main__":
    unittest.main()
