# -*- coding: utf-8 -*-

'''
author: christopher baklid
email: christopherb@unity3d.com

This returner only stores grains.items and state.highstate data.
It does not store historical data only the latest data for each minion
'''

# Imports
from __future__ import absolute_import
import json
import logging
import datetime
import traceback
import salt.utils.jid
import salt.returners
import salt.config

# Dependency
try:
    import rethinkdb as r
    HAS_RDB = True
except ImportError:
    HAS_RDB = False

# Logging
log = logging.getLogger(__name__)


# Constants
__virtualname__ = 'rethink'

rethinkdb_conf = salt.config.master_config('/etc/salt/master')
rdbconf = rethinkdb_conf.get('rethinkdb', {})
if not rdbconf:
    log.warning('rethinkdb not in salt master configuration, using defaults')

DB       = rdbconf.get('database', 'salt')
TABLE    = rdbconf.get('table',    'events')
ENDPOINT = rdbconf.get('endpoint', '127.0.0.1')
PORT     = rdbconf.get('port',     '28015')
INDEXES  = rdbconf.get('indexes',  ['state.highstate', 'state.apply', 'grains.items'])


def __virtual__():
    if not HAS_RDB:
        return False
    return __virtualname__


def _connect():
    conn = r.connect(
        host=ENDPOINT,
        port=PORT,
        db=DB)

    return conn

def _upsert_data(data, fun, minion, conn):
    """ insert or update data """
    if fun == 'state.sls':
        fun = 'state.apply'

    rtable = r.db(DB).table(TABLE)
    res = rtable.update(data).run(conn)
    if not res.get('replaced', 0):
        res = rtable.insert(data).run(conn)

    log.debug('rethinkdb - updated {0} data for minion: {1}'.format(fun, minion))


def event_return(events):
    """ main function triggered with every event in the master event bus.
        formats the data before inserting into rethinkdb
    """
    try:
        conn = _connect()

        for event in events:
            fun = event.get('data', {}).get('fun', {})
            minion = event.get('data', {}).get('id', None)
            if minion and isinstance(fun, str):
                data = {'id': minion, fun: event}
                _upsert_data(data, fun, minion, conn)

        conn.close()
    except:
        log.error(traceback.format_exc())

def prep_jid(nocache=False, passed_jid=None):
    ''' If a job id for whatever reason was not generated, generate it here '''
    return str(passed_jid) if passed_jid is not None else salt.utils.jid.gen_jid()


def _initialise():
    log.debug('initializing rethinkdb for highstatestack data')

    try:
        conn = _connect()

        # Check if DB exists, if not create it
        db_exists = r.db_list().contains(DB).run(conn)
        if not db_exists:
            r.db_create(DB).run(conn)

        # Check if events table exist, if not create it
        table_exists = r.db(DB).table_list().contains(TABLE).run(conn)
        if not table_exists:
            result = r.db(DB).table_create(TABLE).run(conn)

        # Check if index exists if not add it
        rtable = r.db(DB).table(TABLE)
        current_indexes = rtable.index_list().run(conn)
        for index in INDEXES:
            if index not in current_indexes:
                log.debug('adding index {0}'.format(index))
                rtable.index_create(index).run(conn)

    except:
        log.error('could not connect to rehinkdb server on {0}:{1}'.format(DB, PORT))
        log.error(traceback.format_exc())

if HAS_RDB:
    _initialise()
