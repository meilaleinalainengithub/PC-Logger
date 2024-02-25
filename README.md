# PC Logger
- Disables Windows Protector
- Sends Screenshots to discord channel
- Sends Microphone audio to discord channel
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
- connect_channel = "CONNECTION MESSAGE CHANNEL ID"

5. Find your victim.