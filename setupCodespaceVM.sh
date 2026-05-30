curl -fsSL https://ollama.com/install.sh | sh
sudo mkdir -p /etc/systemd/system/ollama.service.d
sudo tee /etc/systemd/system/ollama.service.d/override.conf >/dev/null <<'EOF'
[Service]
Environment=OLLAMA_HOST=0.0.0.0:11434
EOF
sudo systemctl daemon-reload
sudo systemctl restart ollama.service
sudo systemctl enable ollama.service
