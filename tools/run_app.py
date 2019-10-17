# coding=utf-8
#

import sys
sys.path.append('/Users/charles/Documents/projects/myProjects/selfServiceOrder')

from app.web.webapp import run  # noqa
from app.config import CONF     # noqa


if __name__ == '__main__':
    CONF(['--config-file', '/Users/charles/Documents/projects/myProjects/selfServiceOrder/etc/dev/web.conf'])
    run()

