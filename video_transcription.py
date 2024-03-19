import http.client
import os

# Replace 'path/to/your/video.mp4' with the actual path to your video file
file = 'your video path'
#eg video_file = 'ENGLISH SPEECH _ MARK ZUCKERBERG_ Free Speech (English Subtitles) - YouTube - Google Chrome 2024-03-19 10-12-13.mp4'
video_file = file

with open(video_file, 'rb') as f:
    video_data = f.read()

conn = http.client.HTTPSConnection("whisper-speech-to-text1.p.rapidapi.com")

#change payload if required
payload = f"-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{os.path.basename(video_file)}\"\r\n\r\n{video_data.decode('latin-1')}\r\n-----011000010111000001101001--\r\n\r\n"

headers = {
    'content-type': "multipart/form-data; boundary=---011000010111000001101001",
    'X-RapidAPI-Key': "{Your Key Goes here}",
    'X-RapidAPI-Host': "whisper-speech-to-text1.p.rapidapi.com"
}

conn.request("POST", "/speech-to-text", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
