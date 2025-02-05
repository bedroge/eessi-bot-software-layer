# This file is part of the EESSI build-and-deploy bot,
# see https://github.com/EESSI/eessi-bot-software-layer
#
# The bot helps with requests to add software installations to the
# EESSI software layer, see https://github.com/EESSI/software-layer
#
# author: Bob Droege (@bedroge)
#
# license: GPLv2
#
import datetime
import json
import os
import sys

LOG = os.path.join(os.getenv('HOME'), 'eessi-bot-software-layer.log')

def error(msg, rc=1):
    """
    Print an error and exit
    """
    sys.stderr.write(msg + "\n")
    sys.exit(rc)

def log(msg):
    """
    Log message
    """
    with open(LOG, 'a') as fh:
        timestamp = datetime.datetime.now().strftime("%Y%m%d-T%H:%M:%S")
        fh.write('[' + timestamp + '] ' + msg + '\n')


def log_event(request):
    """
    Log event data
    """
    event_type = request.headers['X-GitHub-Event']
    msg_txt = '\n'.join([
        "Event type: %s" % event_type,
        #"Request headers: %s" % pprint.pformat(dict(request.headers)),
        #"Request body: %s" % pprint.pformat(request.json),
        "Event data (JSON): %s" % json.dumps({'headers': dict(request.headers), 'json': request.json}, indent=4),
        '',
    ])
    log(msg_txt)
