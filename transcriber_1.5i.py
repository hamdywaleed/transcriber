import google.generativeai as genai

# Configure Gemini
genai.configure(api_key='AIzaSyD3DIAlu69Amj0o6UKm3fhORJ3HGOdAEik', transport='rest')

# choose which version
model = genai.GenerativeModel("gemini-1.5-flash")




def _transcribe_audio_with_retry(audio_path):
    print("i am here")
    audio_file = genai.upload_file(path=audio_path)
    print("i am here 2")
    prompt = """
            Please transcribe this audio file and provide a clear, well-formatted transcription.
            The audio is a WAV file containing speech that needs to be transcribed accurately.
            pUT IN YOUR CONCERNS TO DEFINE THE SPEAKER, I DON'T MEAN DIARIZATION,but i need an inform that a different speaker is here, transcribe the meeting until different one speak and then split it , and start the transcribtion of the next and so on ALSO FORMAT THE TRANSCRIBE AS A dialogue with timestamps
            Please maintain natural speech patterns and include proper punctuation. result should be in arabic
            """

    response = model.generate_content([prompt, audio_file])
    print("i am here 3")

    return response.text


def generate_summary(audio_path):
    audio_file = genai.upload_file(audio_path)
    prompt = """ This is a business meeting 
                you role is an experienced minute taker


                THE INPUT: you will be given a meeting and you should do your job as the most experienced minute taker do

                The Expected output is : all important information, dates, decisions , tasks and deadlines mentioned in the meeting. ensure documentation of the decisions and actions taken in the meeting, which facilitates their follow-up and implementation

                Please provide a comprehensive summary of the audio content. NOT ALL content just summarize the meeting in the points i have told you above
                Focus on the main points discussed and key takeaways.
                Format the summary in clear paragraphs with proper punctuation. result should be in arabic.
                """
    response = model.generate_content([prompt, audio_file])
    return response.text


if __name__ == '__main__':
    audio_path = r"D:\BEETLEWARE\arab.wav"

    output_file = r"D:\BEETLEWARE\transcriber\1.5_flash_transc.txt"  #

    transcription = _transcribe_audio_with_retry(audio_path)
    # Save the transcription to a file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(transcription)
        print(f"Transcription has been successfully written to {output_file}")

    summ = r"D:\BEETLEWARE\transcriber\1.5_flash_summ.txt"
    summary = generate_summary(audio_path)
    with open(summ, "w", encoding="utf-8") as f:
        f.write(summary)
        print(f"Summary has been successfully written to {summ}")