import unittest

from functions.get_files_info import get_files_info


class TestGetFilesInfo(unittest.TestCase):
    def test_current_directory(self):
        result = get_files_info("calculator", ".")
        print("Test 1: get_files_info('calculator', '.')\n" + result)
        self.assertIsInstance(result, str)
        self.assertNotIn("Error:", result)

    def test_pkg_directory(self):
        result = get_files_info("calculator", "pkg")
        print("Test 2: get_files_info('calculator', 'pkg')\n" + result)
        self.assertIsInstance(result, str)
        self.assertNotIn("Error:", result)

    def test_bin_directory(self):
        result = get_files_info("calculator", "/bin")
        print("Test 3: get_files_info('calculator', '/bin')\n" + result)
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("Error:"))

    def test_parent_directory(self):
        result = get_files_info("calculator", "../")
        print("Test 4: get_files_info('calculator', '../')\n" + result)
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("Error:"))


if __name__ == "__main__":
    unittest.main()
