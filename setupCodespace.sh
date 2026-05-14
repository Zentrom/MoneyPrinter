curl -fsSL https://ollama.com/install.sh | sh
OLLAMA_HOST=0.0.0.0:11434 ollama serve
ollama pull llama3.2:1b
docker compose up --build
