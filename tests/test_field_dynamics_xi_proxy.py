# HESPERIA — Ξ proxy (TRIZ rows → contradiction_signal boost).

from __future__ import annotations

import pytest

from hesperia.engine.field_dynamics.xi_proxy import (
    apply_xi_to_contradiction_signal,
    field_dynamics_xi_enabled,
    xi_proxy_from_triz_rows,
)


def test_xi_proxy_empty_rows() -> None:
    g, per = xi_proxy_from_triz_rows([])
    assert g == 0.0
    assert per == [0.0] * 12


def test_xi_proxy_single_row_areas() -> None:
    rows = [{"score": 1.0, "area_a": 0, "area_b": 1}]
    g, per = xi_proxy_from_triz_rows(rows)
    assert 0 < g <= 1.0
    assert per[0] == pytest.approx(1.0)
    assert per[1] == pytest.approx(1.0)
    assert max(per) == pytest.approx(1.0)


def test_apply_xi_empty_rows_no_change() -> None:
    c0 = [0.1] * 12
    out, meta = apply_xi_to_contradiction_signal(c0, [], xi_scale=0.2)
    assert out == c0
    assert meta["xi_proxy_global"] == 0.0


def test_apply_xi_boosts_localized_areas() -> None:
    rows = [{"score": 1.0, "area_a": 3, "area_b": 3}]
    c0 = [0.0] * 12
    out, meta = apply_xi_to_contradiction_signal(c0, rows, xi_scale=0.1)
    assert meta["xi_scale"] == 0.1
    assert out[3] > out[0]
    assert all(0.0 <= x <= 1.0 for x in out)


def test_apply_xi_clamps_to_one() -> None:
    rows = [{"score": 1.0, "area_a": 0, "area_b": 0}]
    c0 = [0.95] * 12
    out, _ = apply_xi_to_contradiction_signal(c0, rows, xi_scale=0.5)
    assert out[0] == pytest.approx(1.0)


def test_field_dynamics_xi_enabled_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("HESPERIA_FIELD_DYNAMICS_XI", raising=False)
    assert field_dynamics_xi_enabled() is True
    monkeypatch.setenv("HESPERIA_FIELD_DYNAMICS_XI", "0")
    assert field_dynamics_xi_enabled() is False


def test_xi_scale_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    rows = [{"score": 0.5, "area_a": 5, "area_b": 5}]
    c0 = [0.0] * 12
    monkeypatch.setenv("HESPERIA_FIELD_DYNAMICS_XI_SCALE", "0.2")
    out_env, _ = apply_xi_to_contradiction_signal(c0, rows, xi_scale=None)
    monkeypatch.delenv("HESPERIA_FIELD_DYNAMICS_XI_SCALE", raising=False)
    out_default, _ = apply_xi_to_contradiction_signal(c0, rows, xi_scale=None)
    assert out_env[5] > out_default[5]
