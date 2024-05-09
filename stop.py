import soco

def main():
    devices = soco.discover()
    device = list(devices)[0]
    device.pause()


if __name__ == "__main__":
    main()
