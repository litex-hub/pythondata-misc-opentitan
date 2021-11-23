import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8834"
version_tuple = (0, 0, 8834)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8834")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8722"
data_version_tuple = (0, 0, 8722)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8722")
except ImportError:
    pass
data_git_hash = "537937aec1255816352bf0f0806068dc9a61cc9d"
data_git_describe = "v0.0-8722-g537937aec"
data_git_msg = """\
commit 537937aec1255816352bf0f0806068dc9a61cc9d
Author: Nikola Miladinovic <nikola.miladinovic@ensilica.com>
Date:   Mon Nov 22 15:42:23 2021 +0000

    [flash_ctrl] Adding Interface at Environment,fix analog inputs
    
    Signed-off-by: Nikola Miladinovic <nikola.miladinovic@ensilica.com>

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
