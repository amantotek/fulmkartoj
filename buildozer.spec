[app]
title = fulmkartoj
package.name = fulmkartoj
package.domain = org.fulmkartoj
source.dir = .
source.include_exts = py,png,jpg,kv,json
version = 0.1

#requirements = python3,kivy,pyjnius==1.4.2
requirements = python3,kivy,pyjnius==1.6.1

orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.add_assets = vocab.json

# 64 then 32 bit 
android.archs = arm64-v8a, armeabi-v7a

android.accept_sdk_license = True
android.api = 33
android.minapi = 21

# Lock NDK (critical for CI reproducibility)
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1
