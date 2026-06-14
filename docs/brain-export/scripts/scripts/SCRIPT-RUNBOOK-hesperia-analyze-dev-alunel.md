# SCRIPT-RUNBOOK — Hesperia analyze dev on alunel (:18880)

**Scope:** Dev-only shipping `/analyze` API for tersagor `TERSAGOR_HESPERIA_ENGINE_URL`.  
**Host:** alunel (`127.0.0.1:18880`)  
**Unit:** `cluster/alunel/systemd/hesperia-analyze-dev.service`

---

## Start / enable

```bash
sudo cp cluster/alunel/systemd/hesperia-analyze-dev.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now hesperia-analyze-dev
```

## Health

```bash
systemctl status hesperia-analyze-dev --no-pager
curl -sf http://127.0.0.1:18880/health
```

## Stop

```bash
sudo systemctl stop hesperia-analyze-dev
```

## Logs

```bash
journalctl -u hesperia-analyze-dev -n 50 --no-pager
```

## Post-boot

Included in `scripts/alunel-post-boot-fixups.sh` — enables unit and ensures `/data/hesperia/reflection` + `/data/hesperia/ksi`.

---

SIGNED: Runbook (Liam) | hesperia analyze dev alunel | 2026-06-14 | HFIX-27
