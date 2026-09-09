[app]

# (str) Title of your application
title = Sudan Relief Manager

# (str) Package name
package.name = sudanrelief

# (str) Package domain (needed for android packaging)
package.domain = org.sudan.relief

# (list) Source files to include (let it include python files and assets)
source.exts = py,png,jpg,kv,atlas,csv

# (str) Application source directory
source.dir = .

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (str) Supported Android API, default is to have to
android.api = 31

# (str) Minimum API your APK will support
android.minapi = 21

# (int) Automatically accept Android SDK licenses (هذا هو الحل الحاسم لمنع توقف التثبيت)
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
