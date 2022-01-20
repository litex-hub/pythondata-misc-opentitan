import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9641"
version_tuple = (0, 0, 9641)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9641")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9519"
data_version_tuple = (0, 0, 9519)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9519")
except ImportError:
    pass
data_git_hash = "a3a6f0b340543821e2652ab82baf65dfcc95b196"
data_git_describe = "v0.0-9519-ga3a6f0b34"
data_git_msg = """\
commit a3a6f0b340543821e2652ab82baf65dfcc95b196
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Jan 18 18:52:23 2022 -0800

    [rv_core_ibex] Add edn connection to rv_core_ibex
    
    - continuation of #7946
    - rv_core_ibex automatically talks to edn for random data, which is provided
      to ibex through a local register.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
