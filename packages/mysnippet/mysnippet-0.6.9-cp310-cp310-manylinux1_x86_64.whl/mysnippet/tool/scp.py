import os
import click
import paramiko
from scp import SCPClient


class ToolSsh:
    def __init__(self, host, port, user, passwd):
        self._ssh = paramiko.SSHClient()
        self._ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._ssh.connect(host, port=int(port), username=user, password=passwd, timeout=20, look_for_keys=False)
        self._scp = SCPClient(self._ssh.get_transport())
        print("connecting to %s success" % host)

    def put(self, filename, remote_dir):
        self._scp.put(filename, remote_dir)

    def send_command(self, command):
        stdin, stdout, stderr = self._ssh.exec_command(command)
        while not stdout.channel.exit_status_ready():
            # Print data when available
            if stdout.channel.recv_ready():
                alldata = stdout.channel.recv(1024)
                prevdata = b"1"
                while prevdata:
                    prevdata = stdout.channel.recv(1024)
                    alldata += prevdata
                print("---- command: %s -----" % command)
                print(alldata.decode())
                print()


@click.command()
@click.argument("host", type=str)
@click.argument("port", type=str)
@click.argument("user", type=str)
@click.argument("passwd", type=str)
@click.argument("filename", type=str)
@click.option("--remote-dir", "-d", type=str, default="~/Downloads")
def main(host, port, user, passwd, filename, remote_dir):
    if not os.path.exists(filename):
        print(f"warning: {filename} not exist")
        return

    obj = ToolSsh(host, port, user, passwd)
    print("put", filename, "to", remote_dir)
    obj.put(filename, remote_dir)
    print("finish")


if __name__ == "__main__":
    main()
