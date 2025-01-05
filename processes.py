import pygetwindow as gw
import win32gui
import psutil
import time

_fl_window_handle = None


def get_fl_window() -> gw.Win32Window:
    """
    Get the FL Studio window using a cached handle, or search by title if not found.
    """
    global _fl_window_handle

    if _fl_window_handle is not None:
        try:
            if win32gui.IsWindow(_fl_window_handle):
                return next(
                    win for win in gw.getAllWindows() if win._hWnd == _fl_window_handle
                )
        except StopIteration:
            pass  # Handle no longer valid or not found

    windows = gw.getWindowsWithTitle("FL Studio")
    if windows:
        _fl_window_handle = windows[0]._hWnd
        return windows[0]

    raise Exception("FL Studio window not found.")


def is_fl_window_running() -> bool:
    """
    Check if the FL Studio window is running.
    """
    try:
        get_fl_window()
        return True
    except Exception:
        return False


def is_fl_window_active() -> bool:
    """
    Check if the FL Studio window is currently active (in focus).
    """
    try:
        return get_fl_window().isActive
    except Exception:
        return False


def get_fl_window_title() -> str:
    """
    Get the title of the FL Studio window.
    Returns a tuple split by " - " or the full title if not present.
    """
    try:
        title = get_fl_window().title
        if " - FL Studio" in title:
            return title.split(" - ")[0]
        return "an unsaved project" if title.startswith("FL Studio") else title
    except Exception:
        return None


def get_fl_process_start_time(process_name: str = "FL64.exe") -> float:
    """
    Get the start time of the FL Studio process by its executable name.
    Returns the start time as a UNIX timestamp, or None if not found.
    """
    for process in psutil.process_iter(["name", "create_time"]):
        try:
            if process.info["name"] == process_name:
                return process.info["create_time"]
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return None
