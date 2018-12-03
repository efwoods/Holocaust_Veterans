import json
import sys, argparse
import os

def parse(transcript,output):
	return_vector = []

	with open(transcript, 'r') as f:
		loaded_transcript = json.load(f)

	for RESULT in range(len(loaded_transcript['results'])):
		for speaker in range(len(loaded_transcript['speaker_labels'])):		
			if(loaded_transcript['results'][RESULT]['alternatives'][0]['timestamps'][0][1] == loaded_transcript['speaker_labels'][speaker]['from']):
				if(loaded_transcript['speaker_labels'][speaker]['speaker'] != 0):								
					f = open(output,"a+")
					f.write(loaded_transcript['results'][RESULT]['alternatives'][0]['transcript'])
					f.close()

if __name__ == '__main__':
	parse(sys.argv[1], sys.argv[2]) #expected transcript.json and output file
