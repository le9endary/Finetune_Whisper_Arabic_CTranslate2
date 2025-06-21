import os
import pandas as pd

# Define the base paths
base_audio_folders = [
    'D:/python/final_whisper_datacreation/set1/output',
    'D:/python/final_whisper_datacreation/set2/output',
    'D:/python/final_whisper_datacreation/set3/output',

]

base_transcript_folders = [
    'D:/python/final_whisper_datacreation/set1/corrected_transcripts',
    'D:/python/final_whisper_datacreation/set2/corrected_transcripts',
    'D:/python/final_whisper_datacreation/set3/corrected_transcripts',

]

# Initialize list to hold data
data = []

# Iterate over each set
for audio_folder, transcript_folder in zip(base_audio_folders, base_transcript_folders):
    # Get the list of audio files and corresponding transcript files
    audio_files = sorted([f for f in os.listdir(audio_folder) if f.endswith('.wav')])
    transcript_files = sorted([f for f in os.listdir(transcript_folder) if f.endswith('.txt')])

    # Ensure that the number of audio files matches the number of transcript files
    if len(audio_files) != len(transcript_files):
        raise ValueError(f"Mismatch between number of audio and transcript files in {audio_folder} and {transcript_folder}")

    # Collect data from each set
    for audio_file, transcript_file in zip(audio_files, transcript_files):
        audio_path = os.path.join(audio_folder, audio_file)
        transcript_path = os.path.join(transcript_folder, transcript_file)

        # Ensure the files match by name if necessary
        if os.path.splitext(audio_file)[0] != os.path.splitext(transcript_file)[0]:
            raise ValueError(f"Mismatched file names: {audio_file} and {transcript_file}")

        with open(transcript_path, 'r', encoding='utf-8') as f:
            transcript_text = f.read().strip()

        data.append((audio_path, transcript_text))

# Create a DataFrame and save it as a CSV file
df = pd.DataFrame(data, columns=['audio_file', 'transcript'])
csv_file_path = 'whisper_training_data_all_sets.csv'
df.to_csv(csv_file_path, index=False, encoding='utf-8-sig')

# Verify the content by reading it back
df_loaded = pd.read_csv(csv_file_path, encoding='utf-8-sig')

# Print out the first few rows to verify the content
print("Sample data from the DataFrame loaded from CSV:")
print(df_loaded.head())

# Save a sample row to a text file to verify correct writing
sample_transcript_path = 'sample_transcript.txt'
with open(sample_transcript_path, 'w', encoding='utf-8') as f:
    f.write(df_loaded['transcript'][0])

# Read back the sample text file to ensure it's written correctly
with open(sample_transcript_path, 'r', encoding='utf-8') as f:
    sample_transcript = f.read()

print("\nSample transcript read back from text file:")
print(sample_transcript)
