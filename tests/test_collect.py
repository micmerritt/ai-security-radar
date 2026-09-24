import io
import unittest
from contextlib import redirect_stderr
from unittest import mock

from scripts import collect


class FetchWithRetriesTests(unittest.TestCase):
    @mock.patch("scripts.collect.time.sleep")
    @mock.patch("scripts.collect._fetch_arxiv_atom")
    def test_retries_with_backoff_before_succeeding(self, fetch, sleep):
        fetch.side_effect = [OSError("temporary one"), OSError("temporary two"), "atom"]

        stderr = io.StringIO()
        with redirect_stderr(stderr):
            result = collect._fetch_with_retries(
                "query", max_results=5, tries=3, retry_delays=(2, 4)
            )

        self.assertEqual(result, "atom")
        self.assertEqual(fetch.call_count, 3)
        self.assertEqual([call.args[0] for call in sleep.call_args_list], [2, 4])
        self.assertIn("attempt 1/3", stderr.getvalue())
        self.assertIn("attempt 2/3", stderr.getvalue())

    @mock.patch("scripts.collect.time.sleep")
    @mock.patch("scripts.collect._fetch_arxiv_atom", side_effect=OSError("unavailable"))
    def test_raises_last_error_after_final_attempt(self, fetch, sleep):
        with self.assertRaisesRegex(OSError, "unavailable"):
            collect._fetch_with_retries(
                "query", max_results=5, tries=3, retry_delays=(1, 2)
            )

        self.assertEqual(fetch.call_count, 3)
        self.assertEqual([call.args[0] for call in sleep.call_args_list], [1, 2])

    def test_rejects_zero_attempts(self):
        with self.assertRaisesRegex(ValueError, "at least 1"):
            collect._fetch_with_retries("query", max_results=5, tries=0)

    @mock.patch("scripts.collect._fetch_with_retries")
    def test_source_outage_warns_and_keeps_last_good_snapshot(self, fetch):
        fetch.side_effect = OSError("source unavailable")

        stdout = io.StringIO()
        with mock.patch("sys.stdout", stdout):
            result = collect._collect_arxiv_or_warn("query", max_results=5)

        self.assertIsNone(result)
        self.assertIn("::warning title=arXiv collection unavailable::", stdout.getvalue())
        self.assertIn("Keeping the last successful report", stdout.getvalue())

    @mock.patch("scripts.collect._fetch_with_retries", return_value="atom")
    def test_successful_source_fetch_is_returned(self, fetch):
        self.assertEqual(
            collect._collect_arxiv_or_warn("query", max_results=5), "atom"
        )
        fetch.assert_called_once_with("query", max_results=5, tries=3)


class ClassificationTests(unittest.TestCase):
    def test_short_terms_do_not_match_inside_unrelated_words(self):
        entry = {
            "title": "A paragraph about chemical reagents",
            "summary": "A study of language modeling.",
        }

        self.assertFalse(collect._is_security_related(entry))
        self.assertEqual(collect._categorize(entry), "Other (Review)")

    def test_plural_terms_match(self):
        self.assertTrue(collect._contains_term("autonomous agents", "agent"))
        self.assertTrue(collect._contains_term("new vulnerabilities", "vulnerability"))

    def test_weak_terms_still_match_as_words(self):
        entry = {
            "title": "Securing an agent workflow",
            "summary": "A study of tool call abuse and operational controls.",
        }

        self.assertTrue(collect._is_security_related(entry))
        self.assertEqual(collect._categorize(entry), "Agent & Tool Security")

    def test_specific_attack_category_takes_priority_over_agent(self):
        entry = {
            "title": "Prompt injection against an agent",
            "summary": "An indirect prompt can control tool calls.",
        }

        self.assertEqual(collect._categorize(entry), "Prompt Injection")


if __name__ == "__main__":
    unittest.main()
