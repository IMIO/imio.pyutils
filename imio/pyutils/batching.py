# encoding: utf-8
# IMIO <support@imio.be>
#

"""
This module is just a part of imio.helpers.batching module.
https://github.com/IMIO/imio.helpers/blob/master/src/imio/helpers/batching.py

Following function has been put here because imio.pyutils is common to imio.helpers and imio.updates.
"""

from datetime import datetime

import logging
import os


logger = logging.getLogger("imio.pyutils")


# 7) when all the items are treated, we can delete the dictionary file
def batch_delete_files(batch_keys, config, rename=True):
    """Deletes the file containing the batched keys.

    :param batch_keys: the treated keys set
    :param config: a config dict {'bn': batch_number, 'bl': batch_last, 'cn': commit_number, 'll': loop_length,
                                  'lc': loop_count, 'pf': infile, 'cf': config_file, 'kc': keys_count, 'lk': last_key,
                                  'ldk': last_dump_key, 'fr'; first_run_bool}
    :param rename: do not delete but rename
    """
    if batch_keys is None:
        return
    files = [config[key] for key in ("pf", "cf") if config[key] and os.path.exists(config[key])]
    files.extend([fn for fn in config["af"] if os.path.exists(fn)])
    try:
        for filename in files:
            if rename:
                os.rename(filename, "{}.{}".format(filename, datetime.now().strftime("%Y%m%d-%H%M%S")))
            else:
                os.remove(filename)
    except Exception as error:
        logger.exception("Error while renaming/deleting the file %s: %s", filename, error)
