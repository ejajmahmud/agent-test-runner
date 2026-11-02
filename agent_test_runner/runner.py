"""Structured test runner returning distilled diagnostic JSON."""
import unittest
import io
from typing import Dict, Any

def run_test_module(test_case_class) -> Dict[str, Any]:
    suite = unittest.TestLoader().loadTestsFromTestCase(test_case_class)
    stream = io.StringIO()
    runner = unittest.TextTestRunner(stream=stream, verbosity=1)
    result = runner.run(suite)

    failures = []
    for test, tb in result.failures + result.errors:
        failures.append({
            "test": str(test),
            "traceback": tb.strip().splitlines()[-1] if tb else "Unknown"
        })

    return {
        "total": result.testsRun,
        "passed": result.wasSuccessful(),
        "failed_count": len(result.failures) + len(result.errors),
        "failures": failures
    }
