curl -X POST http://localhost:8080/api/generate \
  -H "Content-Type: application/json" \
  -d '{"videoSubject":"AI business ideas","aiModel":"llama3.2:1b","voice":"en_us_001","paragraphNumber":1,"customPrompt":"","subtitlesPosition":"center,top"}'

curl -X POST http://localhost:8080/api/generate \
  -H "Content-Type: application/json" \
  -d '{"videoSubject":"Best tips when travelling to Romania","aiModel":"llama3.2:1b","voice":"en_us_007","paragraphNumber":1,"customPrompt":"","subtitlesPosition":"center,top"}'

curl -X POST http://localhost:8080/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "videoSubject":"George Bush",
    "aiModel":"llama3.2:1b",
    "voice":"en_us_010",
    "paragraphNumber":2,
    "threads":4,
    "color":"#FFFF00",
    "useMusic":true,
    "automateYoutubeUpload":false,
    "customPrompt":"",
    "subtitlesPosition":"center,top"
  }'

curl http://localhost:8080/api/jobs/<jobId>
curl "http://localhost:8080/api/jobs/<jobId>/events?after=0"

docker cp worker:/app/temp/output.mp4 ./output.mp4

SSH into container:
docker exec -it CONTAINERNAME sh
docker cp ./Songs/song.mp3 worker:/app/Songs

curl -X POST \
  -F "songs=@Songs/song.mp3" \
  http://localhost:8080/api/upload-songs

curl -X POST http://localhost:8080/api/upload-songs \
  $(for f in ./Songs/*.mp3; do echo -n "-F songs=@$f "; done)

---------------------------------------------------
Slower - 8b
Llama 3.1 / 2 paragraph / thread doesn't matter? 4 / 4core GitHCodespace = 7:30 minutes
Llama 3.1 / 1 paragraph / thread 4 / 4core GitHCodespace = 6:15 minutes

Faster - 1b
Llama 3.2 / 2 paragraph / thread 4 / 4core GitHCodespace = 3:20 minutes