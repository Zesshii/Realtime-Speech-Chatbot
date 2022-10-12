# these prompts display when the program is initially ran
import chatbot as cb
import get_input_output_devices as iod

iod = iod.Devices()


def is_text_based():
    # ask user if they want to enter the text-based chatbot
    text_based_choice = input("Do you want to use the text-based chatbot? (Y/N): ").lower()
    while text_based_choice != "y" and text_based_choice != "n":
        text_based_choice = input("Incorrect input! Please enter Y or N: ").lower()
    if text_based_choice == "y":
        cb.chatbot_debug()
    return 0


def see_device_list():
    # ask user if they want to see list of available input devices
    look_devices = input("Do you want to see a list of available devices? (Y/N): ").lower()
    while look_devices != "y" and look_devices != "n":
        look_devices = input("Incorrect input! Please enter Y or N: ").lower()
    if look_devices == "y":
        iod.get_devices()
    return 0


def enter_device_index():
    # ask user to enter their device index
    device_index = 1  # default
    while True:
        try:
            device_index = int(input("\nEnter the device index: "))
            break
        except ValueError:
            print("Please enter numbers only!")
            continue
    return device_index


def is_speaker_output():
    # ask user if using speakers as input
    is_loopback = input("\nDo you want to use loopback to record from speakers? (Y/N): ").lower()
    while is_loopback != "y" and is_loopback != "n":
        is_loopback = input("\nDo you want to use loopback to record from speakers? (Y/N): ").lower()
    if is_loopback == "y":
        loopback = True
        return loopback
    loopback = False
    return loopback
