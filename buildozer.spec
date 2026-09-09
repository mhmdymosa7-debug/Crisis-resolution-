[app]

# (str) Title of your application
title = Sudan Relief Manager

# (str) Package name
package.name = sudanrelief

# (str) Package domain (needed for android packaging)
package.domain = org.sudan.relief

# (list) Source files to include
source.exts = py,png,jpg,csv

# (str) Application source directory
source.dir = .

# (str) Application versioning
version = 1.0

# (list) Application requirements - FIXED: Changed from kivy to flet
requirements = python3,flet

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (str) Supported Android API
android.api = 31

# (str) Minimum API your APK will support
android.minapi = 21

# (int) Automatically accept Android SDK licenses
android.accept_sdk_license = True

# (list) Supported architectures (single architecture to speed up build and prevent errors)
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
