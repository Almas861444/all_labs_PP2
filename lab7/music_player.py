import pygame
import os

pygame.init()

music_file = r"C:\Users\Алмас\Desktop\Documents\labs_PP2\labs\lab7\musics"

musiclist = []
for song in os.listdir(music_file):
    if song.endswith(".mp3"):
        music = os.path.join(music_file, song)
        musiclist.append(music)

current_index = 0 
pygame.mixer.init()

def play_song():
    pygame.mixer.music.load(musiclist[current_index])
    pygame.mixer.music.play()
    print(f"Playing: {musiclist[current_index]}")

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Raim_Songs")

play_song()

running = True
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    print("Playing")
                else:
                    pygame.mixer.music.pause()
                    print("Stopped")
                paused = not paused

            elif event.key == pygame.K_RIGHT:
                current_index = (current_index + 1) % len(musiclist)
                play_song()

            elif event.key == pygame.K_LEFT:
                current_index = (current_index - 1) % len(musiclist)
                play_song()

pygame.quit()