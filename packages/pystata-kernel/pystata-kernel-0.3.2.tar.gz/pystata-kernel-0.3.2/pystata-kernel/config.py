import os
import sys
from pathlib import Path
from configparser import ConfigParser, NoSectionError
from .utils import find_dir_edition

def get_config():
    """
    Version 1.10:
    First check if a configuration file exists, if not, query the system.    
    """
    global_config_path = Path(os.path.join(sys.prefix,'etc','pystata-kernel.conf'))
    user_config_path = Path('~/.pystata-kernel.conf').expanduser()

    env = {'stata_dir': None, 
            'edition': None, 
            'graph_format': 'png',
            'echo': 'False',
            'splash': 'True',
            'missing': '.'
            }

    for cpath in (global_config_path,user_config_path):
        try:
            if cpath.is_file():
                config = ConfigParser()
                config.read(str(cpath))
                env.update(dict(config.items('pystata-kernel')))
        except:
            pass

    if env['stata_dir']==None or env['edition']==None:     
        stata_dir,stata_ed = find_dir_edition()     
        default_env = {'stata_dir': stata_dir, 'edition': stata_ed}
        env.update(default_env)
    return env