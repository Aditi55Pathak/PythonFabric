from fabric import task, Connection, SerialGroup
import platform

@task
def greeting(c, msg):
    print(f"Good {msg}")

@task
def systeminfo(c):
    info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
    }
    for key, value in info.items():
        print(f"{key}: {value}")

@task
def hostname(c):
    c.run('hostname')

@task
def update_system(c):
    c.sudo('apt-get update && apt-get upgrade -y')

@task
def upload_file(c, src, dest):
    c.put(src, dest)

@task
def download_file(c, remote_path, local_path):
    c.get(remote_path, local_path)

@task
def deploy(c):
    c.put('my_app.py', '/remote/path/my_app.py')
    c.sudo('systemctl restart my_app')

@task
def multi_host_task(c):
    group = SerialGroup('host1', 'host2', 'host3')
    for conn in group:
        conn.run('uname -s')

@task
def local_time(c):
    c.local('date')
