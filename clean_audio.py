import os
from pydub import AudioSegment
from pydub.utils import make_chunks

input_folder = "raw_audio"
output_folder = "cleaned_audio"
target_duration_ms = 3000

os.makedirs(output_folder, exist_ok=True)

supported_formats = [".mp3", ".wav", ".m4a", ".ogg"]

for filename in os.listdir(input_folder):
    name, ext = os.path.splitext(filename)
    if ext.lower() in supported_formats:
        file_path = os.path.join(input_folder, filename)
        try:
            print(f"🎧 Processing: {filename}")
            sound = AudioSegment.from_file(file_path)

            if len(sound) > target_duration_ms:
                sound = sound[:target_duration_ms] 
            else:
                silence = AudioSegment.silent(duration=target_duration_ms - len(sound))
                sound += silence   
            
            output_path = os.path.join(output_folder, f"{name}.wav")
            sound.export(output_path, format="wav")
            print(f"✅ Saved: {output_path}")
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")

