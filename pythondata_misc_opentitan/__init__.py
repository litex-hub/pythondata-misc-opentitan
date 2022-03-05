import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10730"
version_tuple = (0, 0, 10730)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10730")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10604"
data_version_tuple = (0, 0, 10604)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10604")
except ImportError:
    pass
data_git_hash = "3020470fc56252bd8db4a898a628d1ff761beeab"
data_git_describe = "v0.0-10604-g3020470fc"
data_git_msg = """\
commit 3020470fc56252bd8db4a898a628d1ff761beeab
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Mar 4 11:10:23 2022 +0000

    [ipgen] Mark the --config-file argument as required
    
    The script unconditionally reads the configuration file (not
    unreasonable: this tells it what to do!), so that argument must be
    given.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
