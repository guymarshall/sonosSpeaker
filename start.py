import soco
import socket

def main():
    devices = soco.discover()
    device = list(devices)[0]

    computer_name = socket.gethostname()

    raw_file_name = "song (Fairytail - Alexander Rybak).wav"
    file_name = raw_file_name.replace(" ", "%20").replace("(", "%28").replace(")", "%29")
    music_url = f"http://{computer_name}/{file_name}"

    device.play_uri(music_url)


if __name__ == "__main__":
    main()
