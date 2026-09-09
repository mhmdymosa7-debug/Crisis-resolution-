[app]
title = Sudan Relief Manager
package.name = sudanrelief
package.domain = org.sudan.relief

source.include_exts = py,png,jpg,kv,atlas,csv
source.exclude_exts = spec
version = 1.0
requirements = python3,kivy,pandas

orientation = portrait
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
