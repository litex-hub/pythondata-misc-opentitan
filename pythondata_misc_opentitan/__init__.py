import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8806"
version_tuple = (0, 0, 8806)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8806")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8694"
data_version_tuple = (0, 0, 8694)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8694")
except ImportError:
    pass
data_git_hash = "d8cc3a18e6bdbe4ffe160bd92e0d750cf6853c61"
data_git_describe = "v0.0-8694-gd8cc3a18e"
data_git_msg = """\
commit d8cc3a18e6bdbe4ffe160bd92e0d750cf6853c61
Author: Eitan Shapira <eitanshapira89@gmail.com>
Date:   Wed Nov 17 12:02:55 2021 +0200

    [flash_ctrl/dv] Checking fix of bug #8934 and small addition to seq_cfg
    
    Signed-off-by: Eitan Shapira <eitanshapira89@gmail.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
