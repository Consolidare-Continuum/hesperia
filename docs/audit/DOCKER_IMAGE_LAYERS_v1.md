# Docker image layers verification v1

**Purpose:** Confirm only the final runtime stage is shipped. Multi-stage builds should leave no build layers in the image; verification catches mistakes.

---

## Procedure

After building the API image:

```bash
docker build -f Dockerfile.shipping -t hesperia-api:latest .
docker history hesperia-api:latest
```

## What to confirm

- **Final image** should show a small number of layers (e.g. base image + app copy + CMD).
- **No build tooling** in the final history: no gcc, no pip install of build deps in the last layer.
- **No source tree** in the last layer: only `/app` with runtime code, not full repo.

Multi-stage Dockerfiles use a `builder` stage and a `final` stage; only the `final` stage is kept. So `docker history` should not show intermediate build steps—only the final stage layers.

If you see many layers (e.g. apt-get, pip install, COPY . .), the image may have been built without multi-stage or the wrong stage is being tagged. Re-check `Dockerfile.shipping` that the final stage starts from a slim base and only copies built artifacts.

---

## In the release gate

`tools/run_release_gate.sh` prints `docker history hesperia-api:latest` after loading the image so reviewers can confirm the final stage is the only one shipped.

---

*See Dockerfile.shipping and SEALED_RUNTIME_RELEASE_PROCESS_v1.md.*
