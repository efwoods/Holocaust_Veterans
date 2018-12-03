curl -X POST -u "api_username:api_password" --header "Content-Type: audio/wav" --data-binary $1 "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?timestamps=true&speaker_labels=true"

# See Speech-to-Text Api Reference for detail on functionality
# Replace api_username & api_password with service credentials of a speech-to-text service
