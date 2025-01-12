# FL RPC

## Overview

FL RPC is a lightweight Python script designed to display your current FL Studio project name as your Discord status. It uses the `pypresence` library to interact with the Discord API, and uses `pygetwindow` and `psutil` to detect the FL Studio window. The script runs seamlessly in the background and shows the state in the notification tray.

---

## Usage

### Compiling an Executable

To use FL RPC as an executable, follow these steps:

1. **Install `pyinstaller`:**

    ```bash
    pip install pyinstaller
    ```

2. **Install Required Libraries:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Clone the Repository:**

    ```bash
    git clone https://github.com/SakshhamTheCoder/FL-RPC.git
    ```

4. **Compile the Script:**
   Run the following command inside the cloned folder to generate an executable:

    ```bash
    pyinstaller --onefile --noconsole --add-data "icon.png;." main.py
    ```

5. **Run the Executable:**
   Start the executable file inside the `/dist/` folder and open FL Studio.

### Running the Script Normally

1. **Install Required Libraries:**

    ```bash
    pip install -r requirements.txt
    ```

2. **Start the Script:**
   Run the following command:

    ```bash
    python main.py
    ```

3. **Open FL Studio:**
   Ensure FL Studio is running alongside the script.

---

## Contributing

We’re excited to welcome contributions to FL RPC. To contribute:

1. **Fork the Repository:**
   Create your own copy of the repository on GitHub.

2. **Create a Branch:**
   Use a descriptive name for your branch, such as `feature/new-functionality` or `bugfix/issue-name`.

3. **Commit Changes:**
   Make your changes and commit them with clear, concise messages.

4. **Push Your Branch:**
   Push your branch to your forked repository.

5. **Submit a Pull Request:**
   Open a pull request on the main repository with a detailed description of your changes.

---

## License

FL RPC is licensed under the MIT License. You’re free to use, modify, and distribute this software under the terms of the license.

---

## Additional Information

-   **Repository URL:** [FL RPC GitHub](https://github.com/SakshhamTheCoder/FL-RPC)
-   **Support:** For any issues, feel free to open a GitHub issue or contribute directly to the project.
