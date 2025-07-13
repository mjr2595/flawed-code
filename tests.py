import unittest

from functions.run_python import run_python_file


class TestRunPythonFile(unittest.TestCase):
    def test_run_python_main_py(self):
        result = run_python_file("calculator", "main.py")
        print("run_python_file('calculator', 'main.py'):")
        print(result)
        self.assertIsInstance(result, str)
        # Accepts any output, but should not be an error about file not found or not a Python file
        self.assertFalse(result.startswith('Error: File "main.py" not found.'))
        self.assertFalse(result.startswith('Error: "main.py" is not a Python file.'))
        self.assertFalse(result.startswith("Error: Cannot execute"))

    def test_run_python_tests_py(self):
        result = run_python_file("calculator", "tests.py")
        print("run_python_file('calculator', 'tests.py'):")
        print(result)
        self.assertIsInstance(result, str)
        # Accepts any output, but should not be an error about file not found or not a Python file
        self.assertFalse(result.startswith('Error: File "tests.py" not found.'))
        self.assertFalse(result.startswith('Error: "tests.py" is not a Python file.'))
        self.assertFalse(result.startswith("Error: Cannot execute"))

    def test_run_python_outside_directory(self):
        result = run_python_file("calculator", "../main.py")
        print("run_python_file('calculator', '../main.py') (should error):")
        print(result)
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("Error: Cannot execute"))

    def test_run_python_nonexistent_file(self):
        result = run_python_file("calculator", "nonexistent.py")
        print("run_python_file('calculator', 'nonexistent.py') (should error):")
        print(result)
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith('Error: File "nonexistent.py" not found.'))


if __name__ == "__main__":
    unittest.main()
