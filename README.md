# Database Merger

This script merges one table from different databases into a single database with one table. 

## Setup

Each database must be an sqlite3 database, stored in directory <DB_DIR>, with a table called <TABLE_NAME>. Every table called <TABLE_NAME> contained in these databases must have the same schema. 

## Usage

`python merge.py <DB_DIR> <TABLE_NAME> <OUTPUT_FILE>`

The output is a new sqlite3 database in the file <OUTPUT_FILE> with a single table named <TABLE_NAME>, which contains the result of the merge. 

