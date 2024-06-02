# configure_buildozer_spec.py
import configparser
import sys

# Récupérer les arguments de ligne de commande
sdk_path = sys.argv[1]
ndk_path = sys.argv[2]

config = configparser.ConfigParser()
config.read('buildozer.spec')

config.set('app', 'android.sdk_path', sdk_path)
config.set('app', 'android.ndk_path', ndk_path)

with open('buildozer.spec', 'w') as configfile:
    config.write(configfile)
