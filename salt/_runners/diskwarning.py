def write_log(message):
    with open('/var/log/salt/diskwarning.log', 'a') as logfile:
        logfile.write(str(message)+'\n')

def log(**kwarg):
    try:
        assert type(kwarg['diskusage']) is float
        assert type(kwarg['mount']) is str
        assert type(kwarg['id']) is str
        assert type(kwarg['_stamp']) is str

        write_log("warning disk limit exceeded for minion: {0} {1}".format(kwarg['id'], str(kwarg)))
        return True

    except Exception as e:
        write_log(e)
        return False

