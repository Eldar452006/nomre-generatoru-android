[app]

title = Nömrə Generatoru
package.name = nomregeneratoru
package.domain = org.eldar

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0

[buildozer]

log_level = 2

warn_on_root = 1

android.api = 33
android.minapi = 21
android.archs = arm64-v8a
android.accept_sdk_license = True
android.permissions = INTERNET
