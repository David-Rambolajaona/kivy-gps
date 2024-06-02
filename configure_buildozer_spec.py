# configure_buildozer_spec.py
import configparser

config = configparser.ConfigParser()
config.read('buildozer.spec')

config.set('app', 'android.sdk_path', '${{ github.workspace }}/android-sdk')
config.set('app', 'android.ndk_path', '${{ github.workspace }}/android-ndk')

with open('buildozer.spec', 'w') as configfile:
    config.write(configfile)