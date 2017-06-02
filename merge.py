
import os
import sqlite3
import sys

def get_relative_database_paths(database_directory):
    return [database_directory + '/' + name
            for name in os.listdir(database_directory)
            if os.path.isfile(database_directory + '/' + name)]

def initialize_by_merge(database_path, cursor, table_name):
    cursor.execute("ATTACH '" + database_path + "' AS to_merge")
    cursor.execute("BEGIN")
    cursor.execute("CREATE TABLE " + table_name + " AS SELECT * FROM to_merge." + table_name)
    cursor.execute("COMMIT")
    cursor.execute("DETACH to_merge")
    cursor.commit()

def merge(database_path, cursor, table_name):
    cursor.execute("ATTACH '" + database_path + "' AS to_merge")
    cursor.execute("BEGIN")
    cursor.execute("INSERT INTO " + table_name + " SELECT * FROM to_merge." + table_name)
    cursor.execute("COMMIT")
    cursor.execute("DETACH to_merge")
    cursor.commit()

if __name__ == '__main__':
    
    if len(sys.argv) - 1 != 3:
        print("Usage: python merge.py <DATABASE_DIRECTORY> <TABLE_NAME> <OUTPUT_FILE>")
        exit(0)
    
    database_directory = sys.argv[1]
    table_name = sys.argv[2]
    output_file = sys.argv[3]
    
    merged_connection = sqlite3.connect('merged.db')
    merged_cursor = merged_connection.cursor()
    database_paths = get_relative_database_paths(database_directory)
    
    initialize_by_merge(database_paths[0], merged_cursor, table_name)
    for database_path in database_paths[1:]:
        merge(database_path, merged_cursor, table_name)
    
    merged_connection.close()

