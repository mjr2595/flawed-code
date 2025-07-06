import unittest

from functions.get_file_content import get_file_content


class TestGetFileContent(unittest.TestCase):
    def test_main_py_content(self):
        content = get_file_content("calculator", "main.py")
        print("Test: get_file_content('calculator', 'main.py')\n" + content)
        self.assertIsInstance(content, str)
        self.assertFalse(content.startswith("Error:"))

    def test_pkg_calculator_py_content(self):
        content = get_file_content("calculator", "pkg/calculator.py")
        print("Test: get_file_content('calculator', 'pkg/calculator.py')\n" + content)
        self.assertIsInstance(content, str)
        self.assertFalse(content.startswith("Error:"))

    def test_bin_cat_error(self):
        content = get_file_content("calculator", "/bin/cat")
        print("Test: get_file_content('calculator', '/bin/cat')\n" + content)
        self.assertIsInstance(content, str)
        self.assertTrue(content.startswith("Error:"))


if __name__ == "__main__":
    unittest.main()
