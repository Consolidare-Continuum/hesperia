# Hesperia Analyze API — request/response schemas (OpenAI GPT contract)
from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class AnalyzeOptions(BaseModel):
    include_supporting_statements: bool = True
    max_supporting_statements: int = Field(default=10, ge=1, le=50)
    return_region_coordinates: bool = True
    return_metrics: bool = True


class HesperiaAnalyzeRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Natural language text to be analyzed by HESPERIA.")
    options: AnalyzeOptions | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [{"text": "User text here"}],
        }
    }


class SupportingStatement(BaseModel):
    statement_id: str
    text: str
    side_label: str  # pattern A02-F01-H001-S0
    tau: float = Field(..., ge=0, le=1)


class MetricsBlock(BaseModel):
    T: float | None = None
    T_norm: float | None = Field(None, ge=0, le=1)
    C: float | None = Field(None, ge=0, le=1)
    X_A: float | None = Field(None, ge=0, le=1)
    X_F: float | None = Field(None, ge=0, le=1)
    fragIndex: float | None = Field(None, ge=0, le=1)
    areaEntropy: float | None = None
    evidenceQuality: float | None = Field(None, ge=0, le=1)
    causalCoherence: float | None = Field(None, ge=-1, le=1)


class HesperiaAnalyzeResponse(BaseModel):
    dominant_area: str
    dominant_family: str
    area_index: int | None = Field(None, ge=0, le=11)
    family_global_index: int | None = Field(None, ge=0, le=287)
    loopability: float = Field(..., ge=0, le=1)
    tension_energy: float = Field(..., ge=0)
    obstacle_score: float = Field(..., ge=0, le=1)
    governance: Literal["allow", "require_correction", "forbid"]
    metrics: MetricsBlock | None = None
    region_coordinates: list[str] | None = None
    supporting_statements: list[SupportingStatement] | None = None
    timestamp: str  # date-time
    version: str
