import os
import datetime
import click
import pandas as pd
import pymysql
import warnings

warnings.filterwarnings("ignore")


@click.group()
def main():
    pass


@main.command()
@click.argument('connect_str', type=str, )
@click.option('-p', '--path', type=str, default=".", help='保存dump文件的文件夹')
@click.option('-t', '--tables', type=str, default=None, help="可选参数，使用空格分割")
def dump(connect_str, dbname, path, tables):

    # connect_str: user:passwd@host:port

    tmp = connect_str.split("@")
    if len(tmp) != 2:
        raise Exception("connect str format must be user:passwd@host:port")

    user, password = tmp[0].split(":")
    host, port = tmp[1].split(":")
    port = int(port)

    path = os.path.abspath(path)
    print(f"connect str = {connect_str}")


    option = ""
    filename_sql = "%s.sql" % dbname
    filename_gz = "%s.%s.sql.tar.gz" % (
        dbname, format(datetime.datetime.now(), "%Y%m%dT%H%M%S"))
    if tables is not None:
        tables = " ".join([v.strip() for v in tables.split(" ") if len(v.strip()) > 0])
        option += f" --tables {tables} "
        filename_sql = f"{dbname}.{tables.replace(' ', '.')}.sql"
        filename_gz = f"{dbname}.{tables.replace(' ', '.')}.{format(datetime.datetime.now(), '%Y%m%dT%H%M%S')}.sql.tar.gz"
    command = f"mysqldump -h {host} -P {port} -u{user} -p{password} --databases {dbname} {option} > {filename_sql} 2>/dev/null"
    print(command)
    os.system(command)
    command = "tar -czf %s/%s %s" % (path, filename_gz, filename_sql)
    print(command)
    os.system(command)
    command = "rm %s" % filename_sql
    print(command)
    os.system(command)
    print("finish")


@main.command()
@click.argument('host', type=str)
@click.argument('port', type=int)
@click.argument('user', type=str)
@click.argument('passwd', type=str)
@click.argument("sql", type=str)
@click.option("--filename", "-f", type=str, default=None)
def export(host, port, user, passwd, sql, filename):
    filetype = None
    if filename:
        filetype = os.path.splitext(filename)[-1].replace(".", "")
        if filetype not in ('csv', 'xlsx'):
            print(f"warning: filetype={filetype} must be csv or xlsx")
            return

        filename = os.path.abspath(filename)
        if not os.path.exists(os.path.split(filename)[0]):
            print(f"warning: path={os.path.split(filename[0])} not exists")
            return

        if os.path.exists(filename):
            print(f"warning: filename={filename} is exists")
            return

    conn = pymysql.connect(host=host, port=int(port), user=user, passwd=passwd)
    data = pd.read_sql(sql, conn)

    if filename:
        if filetype == 'csv':
            data.to_csv(filename, index=False)
        elif filetype == 'xlsx':
            data.to_excel(filename, index=False, engine='xlsxwriter')
        print(f"success export filename={filename}, total_len={len(data)}")
    else:
        print(data)
