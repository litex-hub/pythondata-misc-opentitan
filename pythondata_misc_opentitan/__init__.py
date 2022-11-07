import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15269"
version_tuple = (0, 0, 15269)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15269")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15127"
data_version_tuple = (0, 0, 15127)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15127")
except ImportError:
    pass
data_git_hash = "20e9432fe6eb2805766358cb67e971db693424a8"
data_git_describe = "v0.0-15127-g20e9432fe6"
data_git_msg = """\
commit 20e9432fe6eb2805766358cb67e971db693424a8
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Fri Nov 4 17:18:14 2022 -0700

    [top-test] Switch otbn tests to edn auto mode
    
    We want to use OTBN with EDN in auto mode for production use cases. This
    commit updates top-level tests to use EDN auto mode configuration.
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
