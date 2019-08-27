# coding=utf-8
#

import sys
from oslo_config import cfg

CONF = cfg.CONF

CONF.register_opts([
    cfg.StrOpt('connection', default='', help='db connection'),
    cfg.IntOpt('pool_size', default=10, help='pool size')
], 'db')


CONF(sys.argv[1:])

