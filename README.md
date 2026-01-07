# Minecraft-Dashboard-Admin-Tools
Minecraft Dashboard &amp; Admin Tools (M.D.A.T) is a web-based management site for managing your Minecraft server(s), including users, mods and other files.

# Usage:
***All instructions are written assuming you are using windows. Linux instructions will come later, MacOS instruction will not be written as I can't verify the instructions work.***
```bash
curl -s https://raw.githubusercontent.com/username/repo/branch/script.sh | bash   
```

## Pre-Requisites:
If you encounter an errors with any of these steps, please refer yourself to te correct documentation that will be linked at the end of the instructions.

### Code
1. Go to the [releases page](https://github.com/louboi/Minecraft-Dashboard-Admin-Tools/releases)
2. Click on the Source Code zip button to download the code
3. Click on the file and then click on *Extract All* to extract code folder
4. Move the extracted folder to a location of your choice (just remember where you put it)

### Java
1. Please go to [The Oracle Website](https://www.oracle.com/java/technologies/downloads/) and download the most recent version of java available (Version 24 at the point of writing this).
2. Run the downloaded .exe (should be named something similar to *jdk-24_windows-x64_bin.exe*) to install Java
3. If you want to verify the install, open a terminal and type *java --version* to see the version number, if the command doesn't work then please read the documentation [(found here)](https://docs.oracle.com/en/java/javase/24/install/overview-jdk-installation.html)
4. If the command returns the correct version number (should be either 24.0.5 or above) then you can move on

### Minecraft server files
1. Please download the most recent version of the server files from [Minecraft.net](https://www.minecraft.net/en-us/download/server)
2. Move the downloaded java (server.jar) into the *MC Server* folder within the *Minecraft-Dashboard-Admin-Tools* folder
3. Right-Click on the *MC Server* folder and click on *Open in terminal*
4. Type in command *java -Xmx1024M -Xms1024M -jar server.jar nogui* to run the server, it will stop before continuing at first as you need to edit the EULA file.
5. Navigate back to the *MC Server* folder in your file explorer, **Do not close the terminal yet, as it will still be needed**
6. Open the eula.txt file and change *eula=false* to *eula=true*
7. Go back to the terminal and re-run the command (you can just press the up arrow to navigate through past commands and then press enter to run them)
8. After the server has fully started, you can type *stop* to stop the server, ready for you to continue.
9. If the server did not start, or ended with an error please go to the [Minecraft Wiki](https://minecraft.wiki/w/Tutorial:Setting_up_a_Java_Edition_server) to get extra help

### Python & Modules
These instruction will also show you how to activate a virtual environment. **IMPORTANT NOTICE: TO GET VIRTUAL ENVIRONMENTS TO WORK YOU MAY HAVE TO EDIT YOUR SYSTEM EXECUTION POLICIES, PLEASE DO SO AT YOUR OWN RISK AND READ THE DOCUMENTATION IF YOU ARE UNSURE**

#### Python
1. Got to the [Python website](https://www.python.org/downloads/windows/) and download the most recent version of python **Must be at least 3.13+**
2. Run the downloaded executable to install python
3. Open your terminal and type *python --version* to ensure the correct version is installed
4. If it shows and older version or has not installed please read the [documentation](https://docs.python.org/3.13/) or just search your issue

#### Additional Modules
1. Ensure pip is installed and fully updated by opening your terminal and typing *python -m pip install --upgrade pip* **the version should be 25.2+**
2. Staying in yor terminal you can install your other packages by running each of the commands below
   1. Aio-Mc-Rcon
   2. flask

## Project Roadmap
None of these are an absolute definite (except the commands), however, they are being considered. Do not expect any of these features to be added quickly. If you are desperate for a feature, or have an idea for one that could be added, then create and issue and I will try and address it asap.

### User management page
These are potential features relating to the User management page (Called Userpage.html).

#### Commands:
1. ban
2. op
3. deop
4. give
5. kick
6. kill
7. pardon

#### Stats:

1. Last played
2. Total playtime
3. Past bans/kicks
4. in game stats
   1. Health
   2. XP-Level

