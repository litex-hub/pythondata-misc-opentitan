import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11045"
version_tuple = (0, 0, 11045)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11045")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10919"
data_version_tuple = (0, 0, 10919)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10919")
except ImportError:
    pass
data_git_hash = "d6a93fc8348f09ab316e59baeb1815e53c1463cc"
data_git_describe = "v0.0-10919-gd6a93fc83"
data_git_msg = """\
commit d6a93fc8348f09ab316e59baeb1815e53c1463cc
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Mar 15 15:28:33 2022 -0700

    [pwrmgr] Add documentation on a few countermeasures.
    
    - addresses a few items in #11452
    - add documentation about escalate timeout
    - add documentation about fsm sparse error
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
