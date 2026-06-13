#!/usr/bin/env bash
# Backup TARA runtime state to S3 via rclone crypt
# Environment variables (RCLONE_CRYPT_PASSWORD, etc.) are loaded by direnv from .enc.env

set -euo pipefail

DATE=$(date +%Y%m%d-%H%M%S)
BACKUP_DIR="/tmp/tara-backup-${DATE}"
ARCHIVE="tara-runtime-${DATE}.tar.gz"
BOT_VAULT_DIR="${HOME}/.config/anytype/data/AArFZ9fimqpTAJ8s1vEUwfJ2EuRaBFbaxy8vBJ8Bc33VQtVu"

echo "=== TARA Backup: ${DATE} ==="

# Verify rclone crypt password is loaded
if [ -z "${RCLONE_CRYPT_PASSWORD:-}" ]; then
  echo "ERROR: RCLONE_CRYPT_PASSWORD not set. Ensure direnv has loaded .enc.env"
  exit 1
fi

# Create backup staging directory
mkdir -p "${BACKUP_DIR}"

# Collect runtime state
echo "Collecting runtime state..."
if [ -d "${BOT_VAULT_DIR}" ]; then
  cp -r "${BOT_VAULT_DIR}" "${BACKUP_DIR}/bot-vault"
else
  echo "WARNING: Bot vault directory not found at ${BOT_VAULT_DIR}"
fi

if [ -f "data/tara_graph.db" ]; then
  cp data/tara_graph.db "${BACKUP_DIR}/"
else
  echo "WARNING: Citation graph database not found"
fi

if [ -d "papers/incoming" ]; then
  cp -r papers/incoming "${BACKUP_DIR}/" 2>/dev/null || true
fi

if [ -d "papers/processed" ]; then
  cp -r papers/processed "${BACKUP_DIR}/" 2>/dev/null || true
fi

# Create tar archive
cd /tmp
echo "Creating archive: ${ARCHIVE}..."
tar czf "${ARCHIVE}" -C "${BACKUP_DIR}" .

# Check if S3 is configured (placeholder detection)
if rclone listremotes | grep -q "^tara-crypt:"; then
  echo "Uploading to S3 (encrypted via rclone crypt)..."
  rclone copy "${ARCHIVE}" tara-crypt: --progress
  
  echo "Verifying backup integrity..."
  rclone cryptcheck "${ARCHIVE}" "tara-crypt:${ARCHIVE}" || {
    echo "ERROR: Backup verification failed"
    exit 1
  }
  
  echo "Backup completed: ${ARCHIVE} → tara-crypt:"
else
  echo "WARNING: tara-crypt remote not configured. Archive saved locally:"
  echo "  /tmp/${ARCHIVE}"
  echo ""
  echo "To configure S3, update .enc.env with your S3 credentials and run:"
  echo "  rclone config"
  echo ""
  # Keep the archive in /tmp for manual upload
  ARCHIVE_PATH="/tmp/${ARCHIVE}"
fi

# Cleanup staging directory
rm -rf "${BACKUP_DIR}"

# Optional: keep only last N local backups
ls -t /tmp/tara-runtime-*.tar.gz 2>/dev/null | tail -n +4 | xargs -r rm -f

echo "=== Backup finished at $(date +%Y%m%d-%H%M%S) ==="
