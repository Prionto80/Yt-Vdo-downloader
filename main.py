import customtkinter as ctk
from pytube import YouTube


def startdownload():
	ytlink = link.get()
	ytobj = YouTube(ytlink, on_progress_callback=on_progress)
	title.configure(text=ytobj.title, text_color='black')
	ytobj.streams.get_highest_resolution().download()
	finishlbl.configure(text='Downloaded!!', text_color='green')

	#except:
		#finishlbl.configure(text='Error downloading :(', text_color='red')


def on_progress(stream, chunk, bytes_remaining):
	total_size = stream.filesize
	bytes_downloaded = total_size - bytes_remaining
	complete_percent = bytes_downloaded / total_size * 100
	per = str(int(complete_percent))
	percent.configure(text=per + '%')
	percent.update()
	progressbar.set(float(complete_percent)/100)


# System Settings
ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')

# Our App Frame
root = ctk.CTk()
root.geometry('720x480')
root.title('Youtube Video Downloader')

# adding ui element
title = ctk.CTkLabel(root, text='Insert a Youtube link')
title.pack(padx=10, pady=10)

link = ctk.CTkEntry(root, width=350, height=40)
link.pack()

finishlbl = ctk.CTkLabel(root, text='')
finishlbl.pack()

percent = ctk.CTkLabel(root, text='0%')
percent.pack()

progressbar = ctk.CTkProgressBar(root, width=400)
progressbar.set(0)
progressbar.pack()

ctk.CTkButton(root, text='Download', command=startdownload).pack(padx=10, pady=10)

root.mainloop()


