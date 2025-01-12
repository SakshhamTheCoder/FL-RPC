import threading
import rpc
import pystray
from pystray import MenuItem as item, Menu as menu
from PIL import Image
import os
import sys


def resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and for PyInstaller
    """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def start_rpc():
    """
    Start the RPC client.
    """
    rpc.update_rpc()


def exit_program(icon, _):
    """
    Exit the program.
    """
    icon.stop()


icon_menu = menu(item("Exit", exit_program))
icon_image = Image.open(resource_path("icon.png"))

icon = pystray.Icon(
    "FL RPC",
    icon=icon_image,
    title="FL RPC (running)",
    menu=icon_menu,
)


rpc_thread = threading.Thread(target=start_rpc, daemon=True)
rpc_thread.start()


icon.run()
