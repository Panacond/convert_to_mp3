import os

if __name__ == "__main__":
    input_file = "cartoon.mp4"
    list_song = [
        ["farm","00:00:10","00:02:31"],
        ["train","00:02:51","00:06:20"],
        ["frend farm","00:06:39","00:08:51"],
        ["leo friend","00:09:06","00:11:36"],
        ["3 wave","00:14:25","00:17:20"],
        ["fruits","00:19:52","00:21:51"]
    ]

    for i in list_song:
        output_file = f"'leo the truck - {i[0]}.mp3'"
        time_start = i[1]
        time_finish = i[2]
        command = f"ffmpeg -i {input_file} -ss {time_start} -to {time_finish} -metadata artist='leo' {output_file}"
        print(command)
        os.system(command)