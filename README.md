# Windows-Prevent-Sleep


**How this works:**

prevent_sleep: This function uses SetThreadExecutionState with flags to prevent the system from sleeping and turning off the display.

allow_sleep: This function resets the execution state to allow normal sleep behavior.

The application has a simple GUI with "ON", "OFF", and "Exit" buttons.




**Steps to create a .exe file:**

Install PyInstaller: First, you need to install PyInstaller. Open your command prompt and run the following command:

`pip install pyinstaller`

Generate the Executable: Once PyInstaller is installed, navigate to the folder where your Python script (prevent_sleep.py) is located. Run the following command:

`pyinstaller --onefile --windowed prevent_sleep.py`

--onefile: This option creates a single .exe file containing all the required dependencies.

--windowed: This prevents a command-line window from appearing when you run the executable (useful for GUI applications).

Locate the .exe File: After PyInstaller completes the process, it will create a dist folder in the same directory as your script. Inside the dist folder, you'll find prevent_sleep.exe.

Distribute the .exe: You can now share the prevent_sleep.exe file with your user. They can simply double-click the .exe to launch the application, and the GUI will be shown.




**Steps to Add PyInstaller to PATH:**

Open Environment Variables:

Right-click on "This PC" or "Computer" on your desktop or in File Explorer.
Select Properties.
Click on Advanced system settings.
In the System Properties window, click on Environment Variables.

Edit User Variables:

In the User variables section, find and select the Path variable, then click Edit.
Click New and add the following path:

`C:\Users\Username\AppData\Roaming\Python\Python311\Scripts`

Apply and Close:

Click OK to close all the windows.

Restart Command Prompt:

Close the current command prompt window and open a new one to apply the changes.


Verify Installation:

Run the following command to check if PyInstaller is now recognized:

`pyinstaller --version`


Run PyInstaller:

Navigate to your project directory and run:

`pyinstaller --onefile --windowed prevent_sleep.py`

Adding the directory to PATH ensures that Windows can find the pyinstaller.exe executable from any command prompt window. Let me know if this resolves the issue
