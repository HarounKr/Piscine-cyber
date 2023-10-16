import subprocess

cmds = {"Execute docker-compose":["docker-compose", "up", "-d"], 
        "Copy sshd_config file": ["cp", "./sshd_config", "/etc/ssh/"], 
        "Restart sshd": ["systemctl", "restart", "sshd"]}

for key, cmd in cmds.items():
    print(key)
    subprocess.run(cmd)