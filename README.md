# Holocaust_Veterans
[Spark Summary](https://spark.adobe.com/page/QU7C7RN82eRj3/)

This project is based off of the [USC Shoa Foundation Visual History Archive](https://sfi.usc.edu/vha) & the [Clemson Veteran History project](https://tigerprints.clemson.edu/cgi/viewcontent.cgi?article=1084&context=foci)
 
## Anticipated Workflow
The pipeline for the Holocaust/Veterans project is as follows:
1. Gather data:
	- automatically with a script
	- Manually record audio from the videos with [Audacity](https://www.audacityteam.org/download/)
2. Generate transcripts from the audio using speech-to-text
	- `transcribe.sh` is used for this purpose
	- The syntax for using transcribe.sh is as follows:
		- `~/Holocaust_Veterans/transcribe.sh "@NAME_OF_AUDIO_FILE.wav" > NAME_OF_JSON_LOG.json`
3. Clean the transcript data
	- use `parser.py` to take a transcription, differentiate between the interviewer and interviewee, and output only the interviewee's responses into a text file 
	- The output is formatted in such a way that it can be inserted into the text field of parameters.json during Natural Language Understanding Analysis
	- This parsed text output of the interviewee's responses will be used as input to Personality Insights during Analysis
	- The syntax for using `parser.py` is as follows:
		- `python parser.py transcript.json output.txt`
4. Analyze the data
There are two ways in which you can analyze the data:
	1. [Natural language Understanding](https://natural-language-understanding-demo.ng.bluemix.net/)
		- `NLU.sh` is a curl call to a lite Natural language understanding service; It utilizes the parameters set in `parameters.json` 
		- `NLU.sh` will output the analysis of the text field in `parameters.json`
		- The output from `NLU.sh` will print to stdout on the console by default
		- The output from `NLU.sh` may be piped to an output file of choice to save the output by using the appropriate command (i.e. `~/Holocaust_Veterans/.../NLU.sh > NLU_OUTPUT.txt`)
		- NOTE: The text field of `parameters.json` must be updated with the text you wish the analyze through the Natural Language Understanding Service before using `NLU.sh` for analysis
		- The syntax for using `NLU.sh` is `~/Holocaust_Veterans/.../NLU.sh`

	2. [Personality Insights](https://personality-insights-demo.ng.bluemix.net/)
		- `PI.sh` is a curl call to a lite personality insights service
		- `PI.sh` accepts a text file on input and will output a json of the personality insights from the text file
		- NOTE: it is recommended that a [JSON tree viewer](https://codebeautify.org/jsonviewer) is implemented for ease of readability before visualization
		- The proper syntax for using `PI.sh` is as follows: `~/Holocaust_Veterans/.../PI.sh "@INTERVIEWEE_RESPONSES.txt" > INTERVIEWEE_PERSONALITY_INSIGHTS.json`
 		
5. Visualize the data
You can visualize the personality insights by using a JSON tree viewer in conjunction with `plot.py` to generate the plot found under the "Results" Section of the Spark Summary linked above. `plot.py` will get you started on creating your own graph, but you will need to either automate the plotting of values on the y-axis, or hardcode these values to plot a desired graph.
