curl -X POST http://localhost:8080/api/generate \
  -H "Content-Type: application/json" \
  -d '{"videoSubject":"AI business ideas","aiModel":"llama3.2:1b","voice":"en_us_001","paragraphNumber":1,"customPrompt":"","subtitlesPosition":"center,top"}'

curl -X POST http://localhost:8080/api/generate \
  -H "Content-Type: application/json" \
  -d '{"videoSubject":"Best tips when travelling to Romania","aiModel":"llama3.2:1b","voice":"en_us_007","paragraphNumber":1,"customPrompt":"","subtitlesPosition":"center,top"}'

curl -X POST http://localhost:8080/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "videoSubject":"Red cars.",
    "aiModel":"llama3.2:1b",
    "voice":"en_us_006",
    "paragraphNumber":2,
    "threads":4,
    "color":"#00FF00",
    "useMusic":true,
    "automateYoutubeUpload":false,
    "customPrompt":"",
    "subtitlesPosition":"center,top"
  }'

curl -X POST http://localhost:8080/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "videoSubject":"Gym motivation.",
    "aiModel":"llama3.1:8b",
    "voice":"en_us_006",
    "paragraphNumber":2,
    "threads":4,
    "color":"#00FF00",
    "useMusic":false,
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

docker cp worker:app/temp/ outConv.m4a

curl -X POST \
  -F "songs=@Songs/song.mp3" \
  http://localhost:8080/api/upload-songs

curl -X POST http://localhost:8080/api/upload-songs \
  $(for f in ./Songs/*.mp3; do echo -n "-F songs=@$f "; done)

curl -X POST http://localhost:8080/api/cancel

docker cp ./Backend/auth_youtube.py worker:/app/backend/
python3 ./backend/auth_youtube.py
docker cp worker:/app/backend/youtube-oauth2.json ./Backend/

curl -X POST http://localhost:11434/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3.1:8b",
    "messages": [
      {
        "role": "user",
        "content": "Generate a catchy and SEO-friendly title for a YouTube shorts video about Gym motivation. Return ONLY one raw title string, single sentence, no numbering, no quotes, no extra commentary. MAX 100 characters."
      }
    ]
  }'

curl -X POST http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3.1:8b",
    "prompt": "Write a brief and engaging description for a YouTube shorts video about Gym Motication. Get straight to the point. Do not start with unnecessary things."
  }'

---------------------------------------------------
Slower - 8b
Llama 3.1 / 2 paragraph / thread doesn't matter? 4 / 4core GitHCodespace = 7:30 minutes
Llama 3.1 / 1 paragraph / thread 4 / 4core GitHCodespace = 6:15 minutes

Faster - 1b
Llama 3.2 / 2 paragraph / thread 4 / 4core GitHCodespace = 3:20 minutes



ffmpeg -y -i ./output.mp4 -i ./4e56288e-6f90-42e6-b61c-b1d0cc8801ed_mixed_audio.m4a -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 192k -shortest ./test_out.mp4