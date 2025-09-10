# Author - louboi
# Description - Program to execute various commands using rcon
# Credits:
#  - Example aio-mc-rcon from Iapetus-11 [https://github.com/Iapetus-11]

# Import the rcon module and asyncio for better I/O performance
from aiomcrcon import Client
import asyncio
import sys

# Define the variables needed for connections
IP = "127.0.0.1" # IP of the minecraft server (should be able to be a fully qualified domain)
PORT = 25575 # Port of the Rcon console as defined in the server.properties file on the MC server
PASSWORD = "Strong_Password_123" # Password for the Rcon console also defined in the server.properties file
OPTION = int(sys.argv[1]) # int(input("Option Number: ")) # The command selection (will come from a website, but that will come soon[tm])
TAGS = sys.argv[2] # input("Additional options: ") # Any additional options for the command that is to be run (will also come from website)

async def main(IP: str, PORT: int, PASSWORD: str, COMMAND: str) -> str:
    """Core function to make the connection and send the command. All inputs are strings apart from PORT, which is an integer"""
    # Start the client connection
    client = Client(IP, PORT, PASSWORD)
    await client.connect()

    # Send the command and print the response
    response = await client.send_cmd(COMMAND)
    print(response)
    # Close the connection
    await client.close()

match OPTION:
    case 1:
        COMMAND = "ban " + TAGS
        if __name__ == "__main__":
            asyncio.run(main(IP, PORT, PASSWORD, COMMAND))
    case 2:
        COMMAND = "ban-ip " + TAGS
        if __name__ == "__main__":
            asyncio.run(main(IP, PORT, PASSWORD, COMMAND))
    case 3:
        COMMAND = "op " + TAGS
        if __name__ == "__main__":
            asyncio.run(main(IP, PORT, PASSWORD, COMMAND))
    case 4:
        COMMAND = "deop " + TAGS
        if __name__ == "__main__":
            asyncio.run(main(IP, PORT, PASSWORD, COMMAND))
    case 5:
        COMMAND = "gamerule" + TAGS
        if __name__ == "__main__":
            asyncio.run(main(IP, PORT, PASSWORD, COMMAND))
    case 6:
        COMMAND = "difficulty" + TAGS
        if __name__ == "__main__":
            asyncio.run(main(IP, PORT, PASSWORD, COMMAND))
    case 7:
        COMMAND = "give" + TAGS
        if __name__ == "__main__":
            asyncio.run(main(IP, PORT, PASSWORD, COMMAND))
    case 8:
        COMMAND = "kick " + TAGS
        if __name__ == "__main__":
            asyncio.run(main(IP, PORT, PASSWORD, COMMAND))
    case 9:
        COMMAND = "kill " + TAGS
        if __name__ == "__main__":
            asyncio.run(main(IP, PORT, PASSWORD, COMMAND))
    case 10:
        COMMAND = "pardon " + TAGS
        if __name__ == "__main__":
            asyncio.run(main(IP, PORT, PASSWORD, COMMAND))
    case 11:
        COMMAND = "pardon-ip " + TAGS
        if __name__ == "__main__":
            asyncio.run(main(IP, PORT, PASSWORD, COMMAND))
    case 12:
        COMMAND = "weather" + TAGS
        if __name__ == "__main__":
            asyncio.run(main(IP, PORT, PASSWORD, COMMAND))