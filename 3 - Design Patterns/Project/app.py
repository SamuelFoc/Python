from Musicer.subscription import FreeSubscription, PremiumSubscription
from Musicer.playback.music_player_factory import MusicPlayerFactory
from Musicer.playback.player import MusicPlayer
from Musicer.commands import VolumeUpCommand, PlayCommand, PauseCommand
from Musicer.playlist import User



# Creating users with unique IDs and specific settings
user1 = User(user_id=1, name="Alice", subscription=FreeSubscription())
user2 = User(user_id=2, name="Bob", subscription=PremiumSubscription())

# Each user creates their own playlists
playlist1 = user1.create_playlist("Alice's Chill Beats")
playlist2 = user2.create_playlist("Bob's Workout Mix")

# User 1 adds and removes songs from their playlist
playlist1.add_song("Song A")
playlist1.add_song("Song B")
playlist1.remove_song("Song A")

# User 2 manages their own playlist
playlist2.add_song("Song C")
playlist2.remove_song("Song C")

# Stream music based on subscription
user1.stream_music()  # Alice's free subscription
user2.stream_music()  # Bob's premium subscription

# Adjust user settings
user1.adjust_volume(70)
user2.adjust_volume(30)
user1.set_theme("dark")

# Factory for creating music files
mp3_file = MusicPlayerFactory.create_music_file("mp3")

# Using Command pattern for user actions
music_player = MusicPlayer()
play_command = PlayCommand(mp3_file)
pause_command = PauseCommand()
volume_up_command = VolumeUpCommand(user1.global_settings)

music_player.set_command(play_command)
music_player.execute_command()

music_player.set_command(volume_up_command)
music_player.execute_command()

music_player.set_command(pause_command)
music_player.execute_command()