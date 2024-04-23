# Sysbench MySQL Benchmarking Script

This Python script automates the process of running Sysbench benchmarks on a MySQL database. It prepares the database for benchmarking and then runs the benchmark with customizable parameters.

## Prerequisites

Before using this script, make sure you have the following installed:

- [Sysbench](https://github.com/akopytov/sysbench)
- Python 3.x

## Usage

1. Clone the repository to your local machine:

git clone https://github.com/aliaslani/mysql_benchmark.git

css


2. Navigate to the project directory:

cd sysbench-mysql-benchmark

makefile


3. Modify the script `benchmark.py` to set your MySQL database credentials and desired benchmarking parameters:

```python
db_user = "your_mysql_username"
db_password = "your_mysql_password"
db_name = "your_database_name"

    Run the script to execute the benchmarking process:

python benchmark.py

Script Details

    prepare_benchmark: Prepares the MySQL database for benchmarking by initializing the required data.
    run_benchmark: Executes the benchmarking process on the MySQL database with customizable parameters such as the number of threads and duration.

Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or create a pull request.
License

This project is licensed under the MIT License - see the LICENSE file for details.

csharp

