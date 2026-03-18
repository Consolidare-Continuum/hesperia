# TRIZ MVP deployment

## Modes

| `TRIZ_DEPLOY_MODE` | Behavior |
|--------------------|----------|
| `dev` | Benchmark fixtures allowed |
| `demo` | Investor/demo reports OK |
| `pilot` | Disable synthetic corpora by default in product UI (enforce in app layer) |

## Services

- **api**: FastAPI (`runtime.api.main`) on 8080
- **worker**: placeholder for async batch jobs
- **Volumes**: `/data/outputs` (tenant tree), `/data/logs`

## Run

```bash
cp env.example .env
docker compose up --build
```

Health: `GET http://localhost:8080/health`  
TRIZ v1: `POST /api/v1/triz/analyze` (Bearer required if `HESPERIA_API_KEY` set)

## Flags

- `TRIZ_ENABLE_COMPARE` — `/api/v1/triz/compare`
- `TRIZ_ENABLE_EXPORT` — `/api/v1/triz/export`
- `TRIZ_ENABLE_BENCHMARKS` — reserved for benchmark endpoints
- `TRIZ_ENABLE_DEMO_MODE` — reserved for demo-only paths
