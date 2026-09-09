[app]

# (str) Title of your application
title = Sudan Relief Manager

# (str) Package name
package.name = sudanrelief

# (str) Package domain (needed for android packaging)
package.domain = org.sudan.relief

# (list) Source files to include (let it include python files and assets)
source.exts = py,png,jpg,kv,atlas,csv

# (list) Source files to exclude (optional)
#source.exclude_exts = spec

# (list) List of inclusion/exclusion patterns
#source.include_patterns = assets/*,images/*.png

# (str) Application source directory
# Here is the fix for the missing source.dir error
source.dir = .

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy,pandas

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
