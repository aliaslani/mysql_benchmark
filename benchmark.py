import subprocess

def prepare_benchmark(db_user, db_password, db_name):
    prepare_command = f"sysbench --db-driver=mysql --mysql-host=localhost --mysql-user={db_user} --mysql-password=\"{db_password}\" --mysql-db={db_name} oltp_read_only prepare"
    subprocess.run(prepare_command, shell=True)

def run_benchmark(db_user, db_password, db_name, threads=4, time=30):
    run_command = f"sysbench --db-driver=mysql --mysql-host=localhost --mysql-user={db_user} --mysql-password=\"{db_password}\" --mysql-db={db_name} --threads={threads} --time={time} --events=0 oltp_read_only run"
    subprocess.run(run_command, shell=True)

if __name__ == "__main__":
    db_user = "database_user"
    db_password = "database_password"
    db_name = "database_name"

    prepare_benchmark(db_user, db_password, db_name)
    run_benchmark(db_user, db_password, db_name)
