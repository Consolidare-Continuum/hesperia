import json
from pathlib import Path

from django.test import Client, TestCase, override_settings


class OutputViewsSmokeTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_health(self) -> None:
        r = self.client.get("/health/")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json().get("status"), "ok")

    def test_operator_home(self) -> None:
        r = self.client.get("/")
        self.assertEqual(r.status_code, 200)

    def test_client_preview(self) -> None:
        r = self.client.get("/preview/client/")
        self.assertEqual(r.status_code, 200)


class SessionInspectorMVPTests(TestCase):
    """T13–T21, T30 (partial), T54–T55 docs — fixture-backed inspector."""

    def test_inspector_200(self) -> None:
        r = self.client.get("/inspector/session_inspector_min/")
        self.assertEqual(r.status_code, 200)

    def test_inspector_dropdown_two_iterations(self) -> None:
        r = self.client.get("/inspector/session_inspector_min/")
        body = r.content.decode("utf-8")
        self.assertIn('value="0"', body)
        self.assertIn('value="1"', body)

    def test_deep_link_sentence_active(self) -> None:
        r = self.client.get("/inspector/session_inspector_min/?iteration=1&sentence=s1")
        self.assertEqual(r.status_code, 200)
        self.assertIn("is-active", r.content.decode("utf-8"))

    def test_unknown_bundle_404(self) -> None:
        r = self.client.get("/inspector/does_not_exist_fixture/")
        self.assertEqual(r.status_code, 404)


class SessionInspectorExportTests(TestCase):
    """T22–T25 export.json + proxy gate."""

    def test_export_json_has_messages(self) -> None:
        r = self.client.get("/inspector/session_inspector_min/export.json?iteration=0")
        self.assertEqual(r.status_code, 200)
        data = r.json()
        self.assertIn("messages", data)
        self.assertGreaterEqual(len(data["messages"]), 2)
        disp = r.get("Content-Disposition", "")
        self.assertIn("attachment", disp)
        self.assertIn("segment.json", disp)

    @override_settings(HESPERIA_OUTPUT_VIEWS_OPENAI_PROXY=False)
    def test_openai_proxy_disabled_404(self) -> None:
        r = self.client.post("/inspector/session_inspector_min/openai-proxy/", {"iteration": "0"})
        self.assertEqual(r.status_code, 404)

    @override_settings(HESPERIA_OUTPUT_VIEWS_OPENAI_PROXY=True, OPENAI_API_KEY="")
    def test_openai_proxy_no_key_503(self) -> None:
        r = self.client.post("/inspector/session_inspector_min/openai-proxy/", {"iteration": "0"})
        self.assertEqual(r.status_code, 503)


class IterationSegmentOpenAiV1Tests(TestCase):
    """T04, T29, T63 — segment schema + messages contract."""

    def test_golden_fixture_extract_finalize_validate(self) -> None:
        from segment import (
            extract_iteration_segment,
            finalize_segment_openai_v1,
            validate_iteration_segment_openai_v1,
        )

        root = Path(__file__).resolve().parent.parent.parent
        raw = (root / "tests" / "fixtures" / "session_inspector_min.json").read_text(encoding="utf-8")
        bundle = json.loads(raw)
        base = extract_iteration_segment(bundle, "iter_0")
        final = finalize_segment_openai_v1(base)
        validate_iteration_segment_openai_v1(final)

    def test_t63_messages_roles(self) -> None:
        from segment import (
            extract_iteration_segment,
            finalize_segment_openai_v1,
        )

        root = Path(__file__).resolve().parent.parent.parent
        raw = (root / "tests" / "fixtures" / "session_inspector_min.json").read_text(encoding="utf-8")
        bundle = json.loads(raw)
        base = extract_iteration_segment(bundle, "iter_0")
        final = finalize_segment_openai_v1(base)
        msgs = final["messages"]
        self.assertGreaterEqual(len(msgs), 2)
        self.assertEqual(msgs[0]["role"], "system")
        self.assertEqual(msgs[1]["role"], "user")
        self.assertTrue(msgs[0]["content"].strip())
        self.assertTrue(msgs[1]["content"].strip())
