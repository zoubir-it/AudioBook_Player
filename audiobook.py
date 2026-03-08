import pyglet
import os
import tkinter as tk
from tkinter import *
root = Tk()
root.title("Audiobook Player")
root.geometry("500x1000+1300+200")
#root.resizable(0,0)



audio_folder = "audio"
audio_files = sorted(os.listdir(audio_folder))

audios_list = []
current_song = 0
player = pyglet.media.Player()


def files_handle():
    
    for file in audio_files:
        name, ext = os.path.splitext(file)
        if ext == ".wav":
            audios_list.append(os.path.join(audio_folder, file))
    return audios_list


files_handle()


status_var = StringVar()
status_var.set("Stopped")
status_label = Label(root, textvariable=status_var, font=("Helvetica", 14))
status_label.pack(pady=10)

def play_song():
    global current_song, audios_list, player
    if not audios_list:
        return
    player.pause()
    player.next_source()

    sound = pyglet.media.load(audios_list[current_song], streaming=False)
    #player = pyglet.media.Player()
    player.queue(sound)
    player.play()

    status_var.set(f"Playing: {os.path.basename(audios_list[current_song])}")

def next_song():
    global current_song, audios_list
    if not audios_list:
        return
    
    current_song = (current_song +1) % len(audios_list)
    play_song()


def previous_song():
    global current_song, audios_list

    if not audios_list:
        return
    
    current_song = (current_song -1) % len(audios_list)
    play_song()
    
    


def stop_song():
    global player
    player.pause()
    status_var.set("stopped")





listbox = tk.Listbox(root, width=50, height=20)
listbox.pack(pady=20)
for audio in audios_list:
    listbox.insert(tk.END, os.path.basename(audio))

def select_song(event):
    global current_song
    selection = listbox.curselection()
    if selection:
        current_song = selection[0]
        play_song()

listbox.bind('<<ListboxSelect>>', select_song)

    
play_btn = Button(root, text="Play",width=10, height=2, bg="red", fg="black", command=play_song)
play_btn.pack(pady=10)

next_btn = Button(root, text="Next", width=10, height=2, bg="blue", fg="white", command=next_song)
next_btn.pack(pady=10)

prev_btn = Button(root, text="Previous", width=10, height=2, bg="blue", fg="white", command=previous_song)
prev_btn.pack(pady=10)

stop_btn = Button(root, text="Stop", width=10, height=2, bg="red", fg="black", command=stop_song)
stop_btn.pack(pady=10)

exit_button = Button(root, text="   Exit  ", background="red", foreground="white", height=2, width=10, command=root.destroy)
exit_button.pack(pady=15)





root.mainloop()

#C:\Users\HP\Documents\audiobook_app