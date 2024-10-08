# IdleAssistant

**IdleAssistant** is a lightweight application designed to automate simple user interactions on your computer, including random mouse movements, keystrokes, and automatic window switching. It's particularly useful for preventing inactivity timeouts during long periods of non-use.

## Features

- **Random Mouse Movement**: Moves the mouse cursor randomly across the screen to simulate user activity.
- **Auto Alt-Tab**: Automatically switches between open windows at random intervals.
- **Random Keystrokes**: Sends random keystrokes to keep applications active.
- **System Tray Icon**: Runs silently in the system tray with an easy way to exit the application.

## Installation

### Prerequisites

- Python 3.x installed on your machine.
- `pip` (Python package installer) for managing Python packages.

### Steps to Install

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/IdleAssistant.git
   cd IdleAssistant
   
3. **Install Required Packages**:
   ```bash
   pip install pyautogui keyboard pystray pillow

## Running the Application

1. **Run the script**:
   ```bash
   python idleassistant.py

2. **Exit the Application**:
   ```bash
   Click the ESC key or right-click on the system tray icon and select Exit.

## Usage
Once the application is running, it will start performing random mouse movements, Alt-Tabbing between open windows, and sending random keystrokes according to the predefined intervals.

## Contributing
Contributions are welcome! If you'd like to contribute to IdleAssistant, please fork the repository and create a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements
- [pyautogui](https://pyautogui.readthedocs.io/en/latest/) - For automating mouse and keyboard actions.
- [keyboard](https://keyboard.readthedocs.io/en/latest/) - For capturing keyboard events.
- [pystray](https://pystray.readthedocs.io/en/latest/) - For creating a system tray icon.
- [Pillow](https://python-pillow.org/) - For image processing.
   
