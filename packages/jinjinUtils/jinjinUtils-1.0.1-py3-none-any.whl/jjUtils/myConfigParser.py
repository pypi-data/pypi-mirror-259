import configparser
import os

config = configparser.ConfigParser()

session_path = f"{os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))}\\config.ini"

def add_section(section:str, options:dict, session_path:str="config.ini"):
    """
    
    """
    config.read(session_path, encoding="utf-8")
    if config.has_section(section):
        return
    config.add_section(section)
    for k, v in options.items():
        config.set(section, k, v)
    with open(session_path, "w") as f:
        config.write(f)
        f.close()

def get_section(section, session_path=session_path):
    config.read(session_path, encoding="utf-8")
    options = config.options(section)
    return {o:config.get(section, o) for o in options}


def remove_section(section, session_path=session_path):
    config.read(session_path, encoding="utf-8")
    has = config.has_section(section)
    if has:
        config.remove_section(section)
        with open(session_path, "w") as f:
            config.write(f)
            f.close()


if __name__ == "__main__":
    # add_section("zyxd", {'host': '192.168.0.12', 'user': 'root', 'passwd': 'zyxd123', 'db': 'court_couple', 'charset': 'utf8'})
    # add_section("ngfyy", {'host': '192.168.0.12', 'user': 'root', 'passwd': 'zyxd123', 'db': 'court_couple', 'charset': 'utf8'})
    add_section("ceshi", {'host': 'rm-bp14vpw6r5tzrer6bmo.mysql.rds.aliyuncs.com', 'user': 'dev', 'passwd': 'Zyxd123dev#$#$', 'db': 'test', 'charset': 'utf8'})
    # print(get_section("zyxd"))
    # remove_section("ngfyy")