import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5670"
version_tuple = (0, 0, 5670)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5670")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5575"
data_version_tuple = (0, 0, 5575)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5575")
except ImportError:
    pass
data_git_hash = "b398b1181febe5acbdfd084dbe31818f520ecabd"
data_git_describe = "v0.0-5575-gb398b1181"
data_git_msg = """\
commit b398b1181febe5acbdfd084dbe31818f520ecabd
Author: Eitan Shapira <eitan.shapira@nuvoton.com>
Date:   Wed Mar 31 18:42:57 2021 +0300

    [dv/flash] Small changes to improve integration with partner env
    
    Signed-off-by: Eitan Shapira <eitan.shapira@nuvoton.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
