import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11188"
version_tuple = (0, 0, 11188)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11188")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11062"
data_version_tuple = (0, 0, 11062)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11062")
except ImportError:
    pass
data_git_hash = "5ef8a53859e089c6b0a7ef60319441a6316db371"
data_git_describe = "v0.0-11062-g5ef8a5385"
data_git_msg = """\
commit 5ef8a53859e089c6b0a7ef60319441a6316db371
Author: Timothy Trippel <ttrippel@google.com>
Date:   Tue Mar 29 09:55:03 2022 -0700

    [bazel] rename sim_dv SW log extraction flag
    
    This renames the sim_dv SW log extraction flag to make it clear the
    Python script that is processing an ELF file is just building a custom
    database file to pass to a testbench, which will extract SW logs on the
    fly.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
