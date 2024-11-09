# LLIB 1.1
# Authors: lcl692, chatgpt, Romus228

import minecraft_launcher_lib
import subprocess
import argparse

launcherfolder = "launcher"
launchername = "MyLauncher"
launcherver = "1.0"

parser = argparse.ArgumentParser(description='Launch Minecraft with specific version and username')
parser.add_argument('--username', required=True, help='Minecraft Username')
parser.add_argument('--version', required=True, help='Minecraft Version')

args = parser.parse_args()

minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory().replace('minecraft', launcherfolder)

# Получение версии и имени пользователя из аргументов
version = args.version
username = args.username

# Установка версии Minecraft с необходимыми зависимостями
minecraft_launcher_lib.install.install_minecraft_version(versionid=version, minecraft_directory=minecraft_directory)

# Определение опций запуска
options = {
    'username': username,
    'uuid': '',
    'token': '',
    'launcherName': launchername,
    'launcherVersion': launcherver
}

# Запуск Minecraft
subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=version, minecraft_directory=minecraft_directory, options=options))
