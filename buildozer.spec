[app]
title = fulmkartoj
package.name = fulmkartoj
package.domain = org.fulmkartoj
source.dir = .
source.include_exts = py,png,jpg,kv,json
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.add_assets = vocab.json
android.archs = arm64-v8a, armeabi-v7a

android.accept_sdk_license = True
android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.2

# Prevent GitHub Buildozer from “helpfully” choosing 36.x
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1
