"""Unit tests for agent_test_runner."""
import unittest
from agent_test_runner.runner import run_test_module

class TestRunnerSelf(unittest.TestCase):
    def test_pass_and_fail(self):
        class DummyPass(unittest.TestCase):
            def test_p(self):
                self.assertEqual(1, 1)

        class DummyFail(unittest.TestCase):
            def test_f(self):
                self.assertEqual(1, 2)

        r1 = run_test_module(DummyPass)
        self.assertTrue(r1["passed"])
        self.assertEqual(r1["total"], 1)

        r2 = run_test_module(DummyFail)
        self.assertFalse(r2["passed"])
        self.assertEqual(r2["failed_count"], 1)

if __name__ == "__main__":
    unittest.main()
