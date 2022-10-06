import speech_recognition as sr

class Devices:
    def __init__(self):
        self.device_list = sr.Microphone.list_microphone_names()

    def get_devices(self):
        for i, j in enumerate(self.device_list):
            print(f"Device: {j} || Index: {i}")
