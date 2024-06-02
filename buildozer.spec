[app]
title = LocationApp
package.name = locationapp
package.domain = org.example
source.include_exts = py,png,jpg,kv,atlas
source.exclude_exts = spec
version = 0.1
requirements = python3,kivy,plyer
orientation = portrait
android.permissions = ACCESS_FINE_LOCATION,INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
