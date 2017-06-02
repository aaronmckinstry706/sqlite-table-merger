
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
        database_paths = merge.get_relative_database_paths(self._resource_directory)
        merged_path = self._resource_directory + "/merged_names.db"
        
        connection = sqlite3.connect(merged_path)
        cursor = connection.cursor()
        merge.initialize_by_merge(database_paths[0], cursor, "names")
        for database_path in database_paths[1:]:
            merge.merge(database_path, cursor, "names")
        
        cursor.execute("SELECT * FROM names")
        rows = sorted(cursor.fetchall())
        
        connection.close()
        os.remove(merged_path)
        
        expected_rows = sorted(
            [("anassi", "bari"), ("henry", "lin"), ("aaron", "mckinstry"), ("gen", "xiang")])
        self.assertListEqual(expected_rows, rows)
    
    def test_initialize_by_merge(self):
        database_path = self._resource_directory + "/professor_names.db"
        initialized_path = self._resource_directory + "/initialized_names.db"
        
        connection = sqlite3.connect(initialized_path)
        cursor = connection.cursor()
        merge.initialize_by_merge(database_path, cursor, "names")
        
        cursor.execute("SELECT * FROM names")
        rows = sorted(cursor.fetchall())
        
        connection.close()
        os.remove(initialized_path)
        
        expected_rows = sorted([("anassi", "bari")])
        self.assertListEqual(expected_rows, rows)

if __name__ == '__main__':
    unittest.main()
