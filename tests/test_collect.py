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


if __name__ == "__main__":
    unittest.main()
