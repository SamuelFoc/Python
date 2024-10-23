# 🎶 Musicer - A Design Patterns Project 🎶

Welcome to **Musicer**! This project is a showcase of **design patterns** in action, applied in a music streaming service simulation. The implementation covers several design patterns such as **Command**, **Factory**, **Observer**, **Strategy**, and more. Each user can create playlists, manage global settings, control playback, and select different subscription tiers.

## 🚀 Features

- **User Playlists**: Each user can create their own playlists and add/remove songs.
- **Subscription Management**: Choose between Free or Premium subscriptions, each with its own streaming quality.
- **Global Settings**: Manage global settings like volume and theme across the application.
- **Playback Controls**: Play, pause, and control volume of the music player.
- **Observer Notifications**: Playlist owners get notified of any changes to their playlists (e.g., adding/removing songs).

---

## 🎨 Design Patterns Used

This project implements several design patterns to demonstrate their use in software architecture.

### 🏭 Factory Pattern

Used in the **MusicPlayerFactory** to create different types of music files (MP3, WAV, FLAC) without exposing the object creation logic.

#### When to use:

- When you need to create objects without specifying the exact class type.
- Ideal when there are many subclasses and you want to abstract their creation process.

#### Pros:

- Encapsulates object creation.
- Promotes loose coupling between client and the concrete classes.

#### Cons:

- May increase complexity with numerous subclasses.

### 🕹️ Command Pattern

Implemented for playback control commands like **PlayCommand**, **PauseCommand**, and **VolumeUpCommand**. These encapsulate user actions as objects.

#### When to use:

- When you need to encapsulate user actions or operations (e.g., for undo/redo operations).
- If you want to queue or log user actions.

#### Pros:

- Decouples sender and receiver of actions.
- Easily extendable with new commands.

#### Cons:

- Can lead to too many command classes.

### 👁️ Observer Pattern

Used in the **Playlist** class to notify users of any changes to their playlists.

#### When to use:

- When one object needs to notify others of changes (e.g., model-view relationships).

#### Pros:

- Enables loose coupling between objects.

#### Cons:

- Can lead to memory leaks if observers are not correctly removed.

### 🎯 Strategy Pattern

Applied in the **Subscription** system, where the `FreeSubscription` and `PremiumSubscription` provide different streaming strategies.

#### When to use:

- When you want to define a family of interchangeable algorithms.

#### Pros:

- Easily interchangeable behavior without modifying the client.

#### Cons:

- Increases the number of classes.

### 🧑‍🤝‍🧑 Singleton Pattern

Used for the **GlobalSettings** to ensure that only one instance of settings exists across the entire application.

#### When to use:

- When you need exactly one instance of a class across the system.

#### Pros:

- Ensures a single, global point of access.

#### Cons:

- Can be hard to unit test and manage in multi-threaded environments.

---

## 📂 Project Structure

```bash
Musicer/
│__init__.py
│commands.py
│global.py
│Playback/
│   ├── __init__.py
│   ├── file_types.py
│   ├── music_player_factory.py
│   └── player.py
│playlist.py
│subscription.py
│tests/
│   ├── __init__.py
│   ├── test_commands.py
│   ├── test_global.py
│   ├── test_playback.py
│   ├── test_playlist.py
│   └── test_subscription.py
└── app.py
```

---

## 🧪 Running Tests

To run the tests for the different components, navigate to the project directory and execute the following command:

```bash
python test.py
```

Alternatively, you can run specific test suites (e.g., for playback or subscription):

```bash
python -m unittest Musicer.tests.test_playback
python -m unittest Musicer.tests.test_subscription
```

---

## ⚙️ Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/musicer.git
   ```

2. Navigate to the project directory:

   ```bash
   cd musicer
   ```

3. Install the required dependencies (if any):

   ```bash
   pip install -r requirements.txt
   ```

---

## 💡 Usage

1. **Create Users**: Users can create their own accounts, with unique global settings and playlists.
2. **Playlists**: Users can create, update, and get notified about changes to their playlists.
3. **Subscription Management**: Choose between free and premium subscription options, each affecting the streaming quality.
4. **Playback**: Play, pause, and control music using the command pattern.
5. **Global Settings**: Adjust volume, themes, and other global settings.

---

## 🏗️ Future Improvements

- Add more music file formats (e.g., AAC, OGG).
- Implement undo/redo functionality for commands.
- Enhance user notifications with more granular details (e.g., time stamps).
- Expand test coverage to ensure robustness.

---

## 🧑‍💻 Contributing

Feel free to submit issues or pull requests! Contributions are welcome. Before contributing, make sure to run tests and adhere to the coding standards.

---

## 📜 License

This project is licensed under the MIT License.

---

🎉 **Thank you for exploring Musicer!** 🎶
