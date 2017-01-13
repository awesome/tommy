"""
Tommy settings
"""
import os

# Tommy root
TOOMY_ROOT = os.path.dirname(os.path.realpath(__file__)) + "/.."

LANG = 'en'

# Modules settings

LOAD_MODULES = [
	'tommy_date',
	'tommy_macos_url',
	'tommy_hello'
]

MODULES_FOLDER = 'modules'
