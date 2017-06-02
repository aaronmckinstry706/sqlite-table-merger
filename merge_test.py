
import os
import unittest

import merge

class MergeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._resource_directory = "unit_test_resources"
    
    def test_get_relative_database_paths(self):
        actual_paths = set(merge.get_relative_database_paths("unit_test_resources"))
        expected_paths = set(
            [self._resource_directory + '/' + name
             for name in ["student_names.db", "professor_names.db", "mixed_names.db"]])
        self.assertSetEqual(expected_paths, actual_paths)
    
    def test_merge(self):
        pass
    
    def test_initialize_by_merge(self):
        pass

if __name__ == '__main__':
    unittest.main()
