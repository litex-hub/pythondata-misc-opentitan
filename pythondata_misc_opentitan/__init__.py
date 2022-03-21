import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11006"
version_tuple = (0, 0, 11006)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11006")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10880"
data_version_tuple = (0, 0, 10880)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10880")
except ImportError:
    pass
data_git_hash = "93a6f539e151d654820e6ccd2f1477dd0cebd2e0"
data_git_describe = "v0.0-10880-g93a6f539e"
data_git_msg = """\
commit 93a6f539e151d654820e6ccd2f1477dd0cebd2e0
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Mar 17 13:51:10 2022 -0700

    [flash_ctrl] Clarify usage of disable
    
    - state the difference in behavior between the protocl and physical
      controllers
    - make sure host transactions are error'd back as well
    
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
