import requests

# DeepSeek API details
api_key = "sk-ad83af18849147e0946bded7b0308d53"  # Replace with your actual API key
url = "https://api.deepseek.com"  # Replace with the actual API endpoint

# Prepare the request
headers = {
    "Authorization": f"Bearer {api_key}"
}

# Prepare the audio file
audio_path = r"D:\BEETLEWARE\test_videos\Time & Energy are Your Most Valuable Resources! ｜ Mel Robbins.wav"

# Open the file and keep it open during the request
with open(audio_path, "rb") as audio_file:
    audio_file_data = {"file": audio_file}
    # Send the request
    response = requests.post(url, headers=headers, files=audio_file_data)

# Check the response after the file block ends
if response.status_code == 200:
    transcription = response.json().get("transcription")
    print("Transcription successful!")
    print(f"Transcription: {transcription}")
else:
    print(f"Error: {response.status_code}")
