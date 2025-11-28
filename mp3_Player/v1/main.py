import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame


def play_music(folder, song_name):

    # MERGES AND STORES IN A VARIABLE THE FOLDER AND .mp3 FILE LOCATION
    file_path = os.path.join(folder, song_name)

    # CHECKS IF THE FILE REALLY EXISTS (REINFORCING SECURITY PREVENTS UNEXPECTED ISSUES)
    if not os.path.exists(file_path):
        print("File not found")
        return
    
    pygame.mixer.music.load(file_path) # LOADS THE AUDIO
    pygame.mixer.music.play() # PLAYS THE AUDIO

    # DISPLAYS THE NAME OF THE CURRENT SONG
    print(f"\nNow playing: {song_name}")
    
    # PRINTS A MENU/LEGEND SO THE USER KNOWS HOW TO MANIPULATE THE SONG (PAUSE, RESUME, STOP)
    print("""
        Commands:
          [P] PAUSE
          [R] RESUME
          [S] STOP
    """)

    # RUNS A LOOP WAITING FOR THE USER TO CHOOSE BETWEEN THE PREVIOUS OPTIONS.
    # THE LOOP WILL STOP WHEN THE USER TYPES "S" TO STOP.
    while True:

        command = input("> ").upper()

        if command == "P":
            pygame.mixer.music.pause()
            print("PAUSED")

        elif command == "R":
            pygame.mixer.music.unpause()
            print("RESUMED")

        elif command == "S":
            pygame.mixer.music.stop()
            print("STOPPED")
            return

        else: 
            print("Invalid command")


def main():

    # INITIALIZES THE PYGAME LIBRARY
    try:
        pygame.mixer.init()

    except pygame.error as e:
        print("Audio initialization failed! ", e)
        return
    

    # FOLDER WITH .mp3 FILES
    folder = "v1/music"

    # CHECKS IF THE 'folder' IS A VALID DIRECTORY
    if not os.path.isdir(folder):
        print(f"Folder '{folder}' not found!")
        return
    
    # LIST OF .mp3 FILES INSIDE THE 'folder'
    mp3_files = [file for file in os.listdir(folder) if file.endswith(".mp3")]

    # CHECKS IF .mp3 FILE EXISTS
    if not mp3_files: print("No .mp3 file found!"); return

    # MAIN LOOP OF THE APP
    while True:

        print("==================== MP3 PLAYER ====================")

        # PRINTS EACH FILE FROM THE 'mp3_file' LIST WITH A NUMBER (SUMMARY INDEX) => EX.: 1. Music1
        for index, song in enumerate(mp3_files, start=1):
            print(f"{index}. {song}")

        
        # INPUT SELECTION (LIST INDEX BASED ON THE "SUMMARY INDEX" FROM THE LOOP ABOVE)
        choice_input = input("\n Enter the song # to play (or 'Q' to quit): ")

        # IF THE USER TYPES THE LETTER "q" or "Q", THE PROGRAM WILL CLOSE
        if choice_input.upper() == "Q":
            print("Bye!")
            break

        # CHECKS IF THE USER INPUT IS A DIGIT
        if not choice_input.isdigit():
            print("Enter a valid number!!")
            continue

        # CONVERTS THE USER'S TEXT INPUT TO AN INTEGER AND DECREMENTS 1 (REDUCES A NUMBER BECAUSE LISTS START AT INDEX 0, SO ID 1 = 0, ID 2 = 1, ...)
        choice = int(choice_input) - 1

        # CHECKS IF THE "SUMMARY/INDEX ID" IS VALID WITHIN THE AMOUNT OF SONGS/FILES AND CALLS THE FUNCTION THAT WILL PLAY THE SONG
        if 0 <= choice < len(mp3_files):
            play_music(folder, mp3_files[choice])
        else:
            print("Invalid choice!! Try again.")


if __name__ == "__main__":
    main()