# TARA Backup & Restore Guide

This guide explains how to configure S3 backup and run the backup/restore scripts.

## Prerequisites

- A working S3-compatible endpoint (e.g., self-hosted Garage, MinIO, AWS S3, etc.)
- `rclone` configured with a crypt remote
- Direnv loaded (`.envrc` loads secrets from `.enc.env`)

## 1. Update S3 Credentials

Edit the encrypted `.enc.env` file with your S3 endpoint details:

```bash
sops .enc.env
```

Replace the placeholders:

```bash
RCLONE_S3_ACCESS_KEY_ID="your-access-key"
RCLONE_S3_SECRET_ACCESS_KEY="your-secret-key"
S3_ENDPOINT="https://your-s3-endpoint.com"
```

Save and exit. SOPS will encrypt the file automatically.

## 2. Configure Rclone

Create the S3 and crypt remotes:

```bash
rclone config
```

Follow the prompts:

1. Create `tara-s3` (S3-compatible remote):
   - Choose `5) Amazon S3`
   - Set `provider` to `Other`
   - Set `env_auth` to `false`
   - Enter `access_key_id` and `secret_access_key` from `.enc.env`
   - Set `endpoint` to your S3 endpoint URL
   - Set `region` to your region

2. Create `tara-crypt` (crypt remote wrapping tara-s3):
   - Choose `12) Crypt`
   - Set `remote` to `tara-s3:tara-backups/brad-vener/laptop/`
   - Set `filename_encryption` to `standard`
   - Set `directory_name_encryption` to `true`
   - Enter the password from `RCLONE_CRYPT_PASSWORD` (get it with `echo $RCLONE_CRYPT_PASSWORD` inside the devenv)
   - Enter the salt from `RCLONE_CRYPT_PASSWORD2` (get it with `echo $RCLONE_CRYPT_PASSWORD2`)

Verify the remotes:

```bash
rclone listremotes
```

## 3. Run a Backup

Inside the devenv (direnv loads secrets automatically):

```bash
./scripts/backup-to-s3.sh
```

The script will:
1. Collect the bot vault, citation graph, and papers
2. Create a tar archive
3. Encrypt it via rclone crypt
4. Upload to S3
5. Verify the upload with `rclone cryptcheck`

## 4. Restore from Backup

List available backups:

```bash
rclone ls tara-crypt:
```

Run the restore script:

```bash
./scripts/restore-from-s3.sh
```

Follow the prompts:
1. Enter the backup date (YYYYMMDD)
2. Review the extracted files
3. Confirm to overwrite local files

## 5. Automate Weekly Backups

Add a cron job that runs every Sunday at 3 AM:

```bash
0 3 * * 0 cd ~/Documents/Research && eval "$(direnv export bash)" && ./scripts/backup-to-s3.sh >> /tmp/tara-backup.log 2>&1
```

Or use a systemd timer:

```bash
# ~/.config/systemd/user/tara-backup.service
[Unit]
Description=TARA weekly backup

[Service]
Type=oneshot
ExecStart=%h/Documents/Research/scripts/backup-to-s3.sh
WorkingDirectory=%h/Documents/Research
Environment="RCLONE_CRYPT_PASSWORD=%h/.config/rclone/rclone.conf"

# ~/.config/systemd/user/tara-backup.timer
[Unit]
Description=TARA weekly backup timer

[Timer]
OnCalendar=weekly
Persistent=true

[Install]
WantedBy=timers.target
```

Enable:
```bash
systemctl --user daemon-reload
systemctl --user enable tara-backup.timer
systemctl --user start tara-backup.timer
```

## Troubleshooting

### RCLONE_CRYPT_PASSWORD not set

Ensure direnv has loaded:
```bash
direnv exec . ./scripts/backup-to-s3.sh
```

Or check the variable:
```bash
echo $RCLONE_CRYPT_PASSWORD
```

### S3 connection errors

Verify the `tara-s3` remote:
```bash
rclone lsd tara-s3:
```

### Backup fails verification

The `rclone cryptcheck` step may fail if the upload was interrupted. Check the S3 bucket and retry:
```bash
rclone ls tara-crypt:
```

## Security Notes

- The rclone crypt password is stored in `.enc.env` (SOPS-encrypted with age)
- The password is loaded into memory by direnv when you enter the directory
- S3 credentials are also encrypted in `.enc.env`
- The `rclone.conf` file contains no passwords — they come from the environment
- Backups are encrypted at rest in S3 (NaCl SecretBox)

## Files

- `scripts/backup-to-s3.sh` — backup script
- `scripts/restore-from-s3.sh` — restore script
- `.enc.env` — encrypted secrets (SOPS + age)
- `.sops.yaml` — SOPS configuration
- `.envrc` — direnv auto-loader
