"""Command line interface for agent-test-runner."""
import unittest
from .runner import run_test_module

class SampleTest(unittest.TestCase):
    def test_ok(self):
        self.assertTrue(True)

def main():
    res = run_test_module(SampleTest)
    print("Test Runner Result:", res)

if __name__ == "__main__":
    main()
