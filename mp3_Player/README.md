# MP3 Player

A simple audio player developed in Python using the **Pygame** library, allowing users to select and control MP3 file playback interactively.

## FIRST VERSION

## Features

- **Music Listing**: Displays all MP3 files present in the `music/` folder
- **Selection by Index**: Allows you to choose which song to play through a number
- **Playback Control**: Offers commands to control the audio:
  - `[P]` - Pause the song
  - `[R]` - Resume the paused song
  - `[S]` - Stop the song
- **Input Validation**: Validates user input to prevent errors
- **Error Handling**: Checks if files and folders exist before processing

## Requirements

- Python 3.14
- Pygame (`pip install pygame`)

## Installation

1. Clone or download this repository
2. Navigate to the project folder:
   ```bash
   cd mp3_Player/v1
   ```
3. Install the dependencies:
   ```bash
   pip install pygame
   ```

## How to Use

1. Place your MP3 files in the `music/` folder within the `v1/` directory
2. Run the program:
   ```bash
   python main.py
   ```
3. The program will display a numbered list of available songs
4. Type the number corresponding to the song you want to play
5. Use the `P`, `R`, and `S` commands to control playback
6. Type `Q` to exit the program

## Project Structure

```
mp3_Player/
├── README.md
└── v1/
    ├── main.py          # Main player script
    └── music/           # Folder containing MP3 files
```

## Main Functions

### `main()`
- Initializes Pygame
- Validates the existence of the `music/` folder
- Manages the main loop of the application
- Displays the song selection menu

### `play_music(folder, song_name)`
- Loads and plays an MP3 file
- Displays playback controls
- Manages user commands (Pause, Resume, Stop)

## Usage Example

```
==================== MP3 PLAYER ====================
1. song1.mp3
2. song2.mp3
3. song3.mp3

 Enter the song # to play (or 'Q' to quit): 1

Now playing: song1.mp3

    Commands:
      [P] PAUSE
      [R] RESUME
      [S] STOP

> P
PAUSED
> R
RESUMED
> S
STOPPED
```

## Notes

- The file suppresses the Pygame support message through the `PYGAME_HIDE_SUPPORT_PROMPT` environment variable
- Code comments are now in English
- The program continues running in the main loop until the user chooses to exit with `Q`

## Author

Antonio Zago, 2006;
First version created on 27/11/2025
=======
# PythonProjects
Diversos projetos em desenvolvimento para fins de prática da linguagem de programação python
>>>>>>> 7344da85d3aec29336c67b5c781575ccb8413cf2
