from abc import ABC, abstractmethod
from Musicer.subscription import Subscription
from Musicer.globals import GlobalSettings


class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

class User(Observer):
    def __init__(self, user_id: int, name: str, subscription: Subscription):
        self.id = user_id  # Added user ID
        self.name = name
        self.subscription = subscription
        self.playlists = []  # A user can have multiple playlists
        self.global_settings = GlobalSettings()

    def update(self, message: str):
        print(f"Notification for {self.name}: {message}")

    def create_playlist(self, playlist_name: str):
        new_playlist = Playlist(playlist_name, self)
        new_playlist.register_observer(self)
        self.playlists.append(new_playlist)
        print(f"{self.name} created playlist: {playlist_name}")
        return new_playlist

    def stream_music(self):
        print(f"{self.name} is streaming music:")
        self.subscription.stream()

    def adjust_volume(self, volume):
        self.global_settings.adjust_volume(volume)

    def set_theme(self, theme):
        self.global_settings.set_theme(theme)

        
class Playlist:
    def __init__(self, name: str, owner: User):
        self.name = name
        self.songs = []
        self.observers = []
        self.owner = owner

    def add_song(self, song: str):
        self.songs.append(song)
        self.notify_observers(f'Song "{song}" added to playlist "{self.name}".')

    def remove_song(self, song: str):
        if song in self.songs:
            self.songs.remove(song)
            self.notify_observers(f'Song "{song}" removed from playlist "{self.name}".')

    def register_observer(self, observer: Observer):
        self.observers.append(observer)

    def notify_observers(self, message: str):
        for observer in self.observers:
            observer.update(message)