import logging
import os

from config import LOG_FMT, LOG_LVL, ROOT


log = logging.getLogger('Bot')
log.setLevel(LOG_LVL)
fh = logging.FileHandler(os.path.join(ROOT, 'log', 'app.log'), encoding='utf-8')
fh.setLevel(LOG_LVL)
fh.setFormatter(logging.Formatter(LOG_FMT))
log.addHandler(fh)
