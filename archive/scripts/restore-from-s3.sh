#!/usr/bin/env bash
# Restore TARA runtime state from S3 via rclone crypt
# Environment variables (RCLONE_CRYPT_PASSWORD, etc.) are loaded by direnv from .enc.env

set -euo pipefail

echo "=== TARA Restore ==="

# Verify rclone crypt password is loaded
if [ -z "${RCLONE_CRYPT_PASSWORD:-}" ]; then
  echo "ERROR: RCLONE_CRYPT_PASSWORD not set. Ensure direnv has loaded .enc.env"
  exit 1
fi

# Check if S3 is configured
if rclone listremotes | grep -q "^tara-crypt:"; then
  echo "Available S3 backups:"
  rclone ls tara-crypt: | sort -k2 || {
    echo "ERROR: Failed to list S3 backups"
    exit 1
  }
  
  read -p "Enter backup date (YYYYMMDD or full timestamp): " DATE
  
  # Try to find the archive
  if rclone ls tara-crypt: | grep -q "tara-runtime-${DATE}"; then
    ARCHIVE=$(rclone ls tara-crypt: | grep "tara-runtime-${DATE}" | awk '{print $2}' | head -1)
  else
    echo "ERROR: No backup found for date: ${DATE}"
    exit 1
  fi
  
  TEMP_DIR="/tmp/tara-restore-${DATE}"
  mkdir -p "${TEMP_DIR}"
  
  echo "Downloading: ${ARCHIVE}..."
  rclone copy "tara-crypt:${ARCHIVE}" "${TEMP_DIR}/"
  
  ARCHIVE_PATH="${TEMP_DIR}/${ARCHIVE}"
else
  echo "S3 remote not configured. Looking for local archives..."
  
  echo "Available local backups:"
  ls -la /tmp/tara-runtime-*.tar.gz 2>/dev/null || {
    echo "ERROR: No local backups found in /tmp/"
    exit 1
  }
  
  read -p "Enter backup date (YYYYMMDD): " DATE
  
  ARCHIVE_PATH=$(ls /tmp/tara-runtime-${DATE}*.tar.gz 2>/dev/null | head -1)
  if [ -z "${ARCHIVE_PATH}" ] || [ ! -f "${ARCHIVE_PATH}" ]; then
    echo "ERROR: No local backup found for date: ${DATE}"
    exit 1
  fi
  
  TEMP_DIR="/tmp/tara-restore-${DATE}"
  mkdir -p "${TEMP_DIR}"
fi

# Extract archive
echo "Extracting: ${ARCHIVE_PATH}..."
cd "${TEMP_DIR}"
tar xzf "${ARCHIVE_PATH}"

echo ""
echo "Extracted contents:"
find . -maxdepth 2 -type f -o -type d | head -20

echo ""
read -p "Overwrite local files? This will replace current bot vault and data. (yes/no): " CONFIRM

if [ "$CONFIRM" = "yes" ]; then
  echo "Restoring..."
  
  if [ -d "${TEMP_DIR}/bot-vault" ]; then
    # Stop anytype server before restoring vault
    if pgrep -f "anytype serve" > /dev/null; then
      echo "Stopping anytype server..."
      pkill -f "anytype serve" || true
      sleep 2
    fi
    
    rm -rf "${HOME}/.config/anytype/data/AArFZ9fimqpTAJ8s1vEUwfJ2EuRaBFbaxy8vBJ8Bc33VQtVu"
    cp -r "${TEMP_DIR}/bot-vault" "${HOME}/.config/anytype/data/AArFZ9fimqpTAJ8s1vEUwfJ2EuRaBFbaxy8vBJ8Bc33VQtVu"
    echo "  ✓ Bot vault restored"
  fi
  
  if [ -f "${TEMP_DIR}/tara_graph.db" ]; then
    cp "${TEMP_DIR}/tara_graph.db" data/
    echo "  ✓ Citation graph restored"
  fi
  
  if [ -d "${TEMP_DIR}/incoming" ]; then
    cp -r "${TEMP_DIR}/incoming" papers/
    echo "  ✓ Incoming papers restored"
  fi
  
  if [ -d "${TEMP_DIR}/processed" ]; then
    cp -r "${TEMP_DIR}/processed" papers/
    echo "  ✓ Processed papers restored"
  fi
  
  echo ""
  echo "=== Restore complete ==="
  echo "Restart anytype server if needed: anytype serve --listen-address 127.0.0.1:31012"
else
  echo "Restore cancelled."
  echo "Extracted files remain in: ${TEMP_DIR}"
fi
