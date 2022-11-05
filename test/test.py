import os
import subprocess
import unittest

class TestAiEps(unittest.TestCase):

    def test(self):
        test_dir = os.path.dirname(os.path.abspath(__file__))
        script_file = test_dir + '/../aieps_output.py'
        print(script_file)
        
        # run the script with test input
        completed_process = subprocess.run(['python3', script_file, test_dir + '/input.svg'], capture_output=True, text=True)

        if completed_process.returncode != 0:
            print(completed_process.stderr)

        # expect success return code
        self.assertEqual(0, completed_process.returncode)

        # compare to reference file
        expected_file = open(test_dir + '/expected-output.eps', "r")
        expected_output = expected_file.read()
        expected_file.close()

        self.assertEqual(expected_output, completed_process.stdout)

if __name__ == '__main__':
    unittest.main()