curl -X POST http://localhost:8080/api/generate \
  -H "Content-Type: application/json" \
  -d '{"videoSubject":"AI business ideas","aiModel":"llama3.2:1b","voice":"en_us_001","paragraphNumber":1,"customPrompt":"","subtitlesPosition":"center,top"}'

curl http://localhost:8080/api/jobs/<jobId>
curl "http://localhost:8080/api/jobs/<jobId>/events?after=0"

docker cp worker:/app/temp/output.mp4 ./output.mp4
python3 -m http.server 8000