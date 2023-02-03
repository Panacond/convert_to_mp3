import os

if __name__ == "__main__":
    input_file = "input.mp4"
    list_song = [
        ["title","00:59:11","01:01:32"]
    ]

    for i in list_song:
        artist = "artist"
        output_file = f"'{artist} - {i[0]}.mp3'"
        time_start = i[1]
        time_finish = i[2]
        command = f"ffmpeg -i {input_file} -ss {time_start} -to {time_finish} -metadata artist='{artist}' -metadata title='{i[0]}' {output_file}"
        print(command)
        os.system(command)