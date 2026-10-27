#!/bin/bash
# IAESTE Exchange Suite - Multi-Device Network Launcher

PORT=3456
DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

# 1. Detect Local IP
LOCAL_IP=$(ipconfig getifaddr en0 || ipconfig getifaddr en1 || ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | head -n 1)
if [ -z "$LOCAL_IP" ]; then
  LOCAL_IP="127.0.0.1"
fi
LOCAL_URL="http://${LOCAL_IP}:${PORT}"

echo "=================================================="
echo " IAESTE EXCHANGE SUITE - MULTI-DEVICE LAUNCHER   "
echo "=================================================="
echo "Local IP: ${LOCAL_IP}"
echo "Local Offline URL: ${LOCAL_URL}"

# 2. Check/Start Python HTTP Server with Health Check
SERVER_HEALTHY=0
if lsof -i :${PORT} > /dev/null 2>&1; then
  if curl -s -f --max-time 2 "http://127.0.0.1:${PORT}" > /dev/null 2>&1; then
    SERVER_HEALTHY=1
    echo "Local HTTP server is healthy and responding on port ${PORT}."
  else
    echo "Port ${PORT} is occupied by an unresponsive process. Restarting..."
    lsof -ti :${PORT} | xargs kill -9 2>/dev/null
    sleep 1
  fi
fi

if [ $SERVER_HEALTHY -eq 0 ]; then
  echo "Starting local HTTP server on port ${PORT}..."
  python3 -m http.server ${PORT} > /dev/null 2>&1 &
  sleep 1
fi

# 3. Check/Start Cloudflare Tunnel
CLOUDFLARED_BIN="/opt/homebrew/bin/cloudflared"
if [ ! -f "$CLOUDFLARED_BIN" ]; then
  CLOUDFLARED_BIN="$(which cloudflared)"
fi

if [ -f "$CLOUDFLARED_BIN" ]; then
  # Check if cloudflared is running and healthy
  RESTART_TUNNEL=1
  if pgrep -f "cloudflared tunnel" > /dev/null 2>&1; then
    # Check if log has Unauthorized or disconnected errors
    if tail -n 20 cloudflared.log 2>/dev/null | grep -E "Unauthorized|Tunnel not found" > /dev/null; then
      echo "Existing Cloudflare tunnel session expired. Restarting tunnel..."
      pkill -9 -f "cloudflared tunnel" 2>/dev/null
      sleep 1
    else
      PUBLIC_URL=$(grep -oE "https://[a-zA-Z0-9-]+\.trycloudflare\.com" cloudflared.log 2>/dev/null | tail -n 1)
      if [ -n "$PUBLIC_URL" ]; then
        RESTART_TUNNEL=0
        echo "Cloudflare tunnel is active."
      fi
    fi
  fi

  if [ $RESTART_TUNNEL -eq 1 ]; then
    echo "Starting Cloudflare Public Tunnel..."
    rm -f cloudflared.log
    $CLOUDFLARED_BIN tunnel --url http://127.0.0.1:${PORT} > cloudflared.log 2>&1 &
    
    # Wait up to 12 seconds for the URL to generate
    for i in {1..12}; do
      sleep 1
      PUBLIC_URL=$(grep -oE "https://[a-zA-Z0-9-]+\.trycloudflare\.com" cloudflared.log 2>/dev/null | tail -n 1)
      if [ -n "$PUBLIC_URL" ]; then
        break
      fi
    done
  fi
fi

if [ -z "$PUBLIC_URL" ]; then
  PUBLIC_URL="${LOCAL_URL}"
fi

echo "Public HTTPS URL: ${PUBLIC_URL}"

# 4. Generate network_config.js
cat << JSEOF > network_config.js
window.NETWORK_SHARE = {
  localIp: "${LOCAL_IP}",
  port: ${PORT},
  localUrl: "${LOCAL_URL}",
  publicUrl: "${PUBLIC_URL}",
  updatedAt: new Date().toISOString()
};
JSEOF

echo "Updated network_config.js."
echo "--------------------------------------------------"
echo "📱 Share on Mobile/Tablet via Wi-Fi:   ${LOCAL_URL}"
echo "🌍 Share Worldwide via Secure HTTPS:   ${PUBLIC_URL}"
echo "=================================================="
