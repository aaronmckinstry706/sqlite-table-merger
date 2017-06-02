
import os
import sqlite3
import unittest

import merge

class MergeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._resource_directory = "unit_test_resources"
    
    def test_get_relative_database_paths(self):
        actual_paths = set(merge.get_relative_database_paths(self._resource_directory))
        expected_paths = set(
            [self._resource_directory + "/" + name
             for name in ["student_names.db", "professor_names.db", "mixed_names.db"]])
        self.assertSetEqual(expected_paths, actual_paths)
    
    def test_merge(self):
        pass
    
    def test_initialize_by_merge(self):
        database_path = self._resource_directory + "/professor_names.db"
        merged_path = self._resource_directory + "/merged_names.db"
        
        connection = sqlite3.connect(merged_path)
        cursor = connection.cursor()
        merge.initialize_by_merge(database_path, cursor, "names")
        
        cursor.execute("SELECT * FROM names")
        rows = cursor.fetchall()
        
        connection.close()
        os.remove(merged_path)
        
        self.assertListEqual([("anassi", "bari")], rows)

if __name__ == '__main__':
    unittest.main()
