# Starts the MC Server jar as a separate process to allow this script to continue starting the other programs
Start-Process -FilePath "C:\Program Files\Common Files\Oracle\Java\javapath\javaw.exe" `
              -WorkingDirectory ".\MC Server" `
              -ArgumentList "-Xms512M -Xmx512M -jar server.jar"

# The next command will go here
Write-Output "Next Command here"