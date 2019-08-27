# coding=utf-8
#

from app.web.webapp import run
from app.config import CONF


if __name__ == '__main__':
    CONF(['--config-file', '/Users/charles/Documents/projects/myProjects/selfServiceOrder/etc/dev/web.conf'])
    run()

