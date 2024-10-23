# 🎸 Music Streaming System

---

In this task, you will build a Music Streaming System that simulates a platform for playing and managing music. The system will incorporate several design patterns, including Factory, Singleton, Observer, Strategy, and Command.

The goal is to create a flexible and scalable system with multiple components, such as music playback, user playlists, subscription models, and user interaction. Each of these components will make use of different design patterns. Below are the requirements and hints on which design patterns to apply.

### Features of the Music Streaming System:

- Music Playback: Users should be able to play different types of music, such as MP3, FLAC, or WAV. The system should allow you to add new music formats in the future without modifying existing code. Use the Factory pattern to achieve this.

- User Playlists: Users can create and manage their own playlists. Playlists should notify the user every time a new song is added or removed. Use the Observer pattern for playlist updates.

- Subscription Models: The platform offers different subscription models (e.g., Free, Premium, Family). Users can select different subscription types, and each will have specific features such as ad-supported or high-quality audio streaming. Use the Strategy pattern to represent different subscription types.

- Global Settings: The system should allow for global settings, such as enabling dark mode or adjusting global volume, which will apply to all users. Use the Singleton pattern to manage global settings.

- User Commands: Users should be able to execute commands such as play, pause, skip, volume up, and volume down. These commands should be easily extendable and reversible (i.e., undo support). Use the Command pattern for managing user commands.
