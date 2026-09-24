import datetime as dt
import io
import unittest
from contextlib import redirect_stdout
from unittest import mock

from scripts import weekly_report_email


class TestEmailModeTests(unittest.TestCase):
    def test_env_flag_accepts_common_true_values(self):
        for value in ("1", "true", "TRUE", "yes", "on"):
            with self.subTest(value=value), mock.patch.dict(
                "os.environ", {"TEST_EMAIL": value}, clear=True
            ):
                self.assertTrue(weekly_report_email._env_flag("TEST_EMAIL"))

    @mock.patch("scripts.weekly_report_email._send_email")
    @mock.patch("scripts.weekly_report_email._utc_now")
    def test_test_mode_sends_diagnostic_without_github_credentials(self, now, send):
        now.return_value = dt.datetime(2026, 9, 24, 12, 30, tzinfo=dt.timezone.utc)

        stdout = io.StringIO()
        with mock.patch.dict("os.environ", {"TEST_EMAIL": "true"}, clear=True):
            with redirect_stdout(stdout):
                result = weekly_report_email.main()

        self.assertEqual(result, 0)
        send.assert_called_once()
        subject, body = send.call_args.args
        self.assertEqual(subject, "[TEST] AI Security Radar email (2026-09-24 12:30:00 UTC)")
        self.assertIn("completed an SMTP send", body)
        self.assertIn("Test email sent successfully.", stdout.getvalue())

    @mock.patch("scripts.weekly_report_email.smtplib.SMTP")
    def test_send_email_uses_tls_login_and_multipart_message(self, smtp):
        server = smtp.return_value.__enter__.return_value
        env = {
            "EMAIL_TO": "recipient@example.com",
            "EMAIL_FROM": "radar@example.com",
            "SMTP_HOST": "smtp.example.com",
            "SMTP_PORT": "2525",
            "SMTP_USER": "radar-user",
            "SMTP_PASS": "secret",
            "SMTP_TLS": "true",
        }

        with mock.patch.dict("os.environ", env, clear=True):
            weekly_report_email._send_email("Test subject", "Test body")

        smtp.assert_called_once_with("smtp.example.com", 2525, timeout=30)
        server.starttls.assert_called_once()
        server.login.assert_called_once_with("radar-user", "secret")
        message = server.send_message.call_args.args[0]
        self.assertEqual(message["To"], "recipient@example.com")
        self.assertEqual(message["Subject"], "Test subject")
        self.assertTrue(message.is_multipart())


if __name__ == "__main__":
    unittest.main()
