import unittest

from functions.write_file import write_file


class TestWriteFile(unittest.TestCase):
    def test_write_file_in_working_directory(self):
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(
            "Test: write_file('calculator', 'lorem.txt', \"wait, this isn't lorem ipsum\")"
        )
        print(result)
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("Successfully wrote"))

    def test_write_file_with_subdirectory(self):
        result = write_file(
            "calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"
        )
        print(
            "Test: write_file('calculator', 'pkg/morelorem.txt', 'lorem ipsum dolor sit amet')"
        )
        print(result)
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("Successfully wrote"))

    def test_write_file_outside_working_directory(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(
            "Test: write_file('calculator', '/tmp/temp.txt', 'this should not be allowed')"
        )
        print(result)
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("Error:"))


if __name__ == "__main__":
    unittest.main()
