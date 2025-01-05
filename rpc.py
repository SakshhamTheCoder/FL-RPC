import pypresence
import processes
import time

DISCORD_CLIENT_ID = "1325027191049945099"
UPDATE_INTERVAL = 1  # seconds
RETRY_INTERVAL = 5  # seconds


def initialize_rpc(client_id: str) -> pypresence.Presence:
    """
    Initialize the Discord RPC client.
    """
    rpc = pypresence.Presence(client_id)
    rpc.connect()
    return rpc


def update_presence(
    rpc: pypresence.Presence,
    data: str,
    active: bool,
    start_time: float,
):
    """
    Update the Discord Rich Presence based on the window's state, data, and elapsed time.
    """
    state = "Working" if active else "Idling"
    details = data
    presence_details = details if "Rendering" in details else f"{state} on {details}"
    rpc.update(
        details=presence_details,
        large_image="flstudio",
        large_text="FL Studio",
        small_image="working" if active else "idle",
        small_text=state,
        start=start_time,
    )


def clear_presence(rpc: pypresence.Presence):
    """
    Clear the Discord Rich Presence.
    """
    rpc.clear()


def update_rpc():
    """
    Continuously update the Discord Rich Presence based on the FL Studio window state.
    """
    rpc = None
    while True:
        try:
            rpc = initialize_rpc(DISCORD_CLIENT_ID)

            while True:
                if processes.is_fl_window_running():
                    data = processes.get_fl_window_title()
                    active = processes.is_fl_window_active()
                    start_time = processes.get_fl_process_start_time()

                    if start_time:
                        update_presence(rpc, data, active, start_time)
                    else:
                        clear_presence(rpc)
                else:
                    clear_presence(rpc)
                    rpc.close()
                    exit()

                time.sleep(UPDATE_INTERVAL)

        except (
            pypresence.exceptions.DiscordNotFound,
            pypresence.exceptions.DiscordError,
        ):
            time.sleep(RETRY_INTERVAL)

        except Exception:
            if rpc:
                try:
                    rpc.close()
                except Exception:
                    pass


if __name__ == "__main__":
    update_rpc()
