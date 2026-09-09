[app]

# (str) Title of your application
title = Sudan Relief Manager

# (str) Package name
package.name = sudanrelief

# (str) Package domain (needed for android packaging)
package.domain = org.sudan.relief

# (list) Source files to include (let it include python files and assets)
source.exts = py,png,jpg,kv,atlas,csv

# (str) Application source directory (هذا هو السطر الذي يمنع خطأ missing source.dir)
source.dir = .

# (str) Application versioning
version = 1.0

# (list) Application requirements
# تحديد إصدارات واضحة ومتوافقة لأندرويد
requirements = python3,kivy,pandas,numpy,certifi

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (str) Supported Android API
android.api = 33

# (str) Minimum API your APK will support
android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 1
bin_dir = ./bin
