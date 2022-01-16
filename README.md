### **Script Details**

- This script will translate a phrase to Chinese simplified characters and pinyin and then translate it back to English using Google Translate API

- Google Translate API Documentation: https://py-googletrans.readthedocs.io/en/latest/



- **Note, in order to view Chinese characters I used Git Bash as PowerShell was not displaying characters properly (also need to enable Unicode UTF-8 on Windows machines):
https://stackoverflow.com/questions/57131654/using-utf-8-encoding-chcp-65001-in-command-prompt-windows-powershell-window/57134096#57134096


### **Project Notes**

- File management: first I created the directory, created the pipenv virtual environment, and installed googletrans to the virtual environment. I used Powershell to complete these tasks (later switched to Git Bash).

- Atom: I learned to activate the virtual environment using the `pipenv shell` rather than `pipenv run "command"` as both activate the virtual environment, however only `pipenv shell` let Atom utilize the virtual environment when running the python script.

- Git: Utilized Git commands from Powershell and Git Bash for version control. I only had two versions, one to initialize the repository on Github and another once the script was complete. For future reference, I could have increased the version control frequency for better practice. Since this specific script is small, it did not cause issues with this project.
