__author__ = "Xupeng Tong"
__copyright__ = "Copyright 2017, subtitle scrawler"
__email__ = "tongxupeng.cpu@gmail.com"

import os
from pyunpack import Archive

files = os.listdir('subtitles')

for f in files:
	Archive(f).extractall('subtitles_decompressed')