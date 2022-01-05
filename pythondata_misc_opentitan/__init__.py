import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9348"
version_tuple = (0, 0, 9348)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9348")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9231"
data_version_tuple = (0, 0, 9231)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9231")
except ImportError:
    pass
data_git_hash = "8288b0163a4d7b7bcf904da84c6d18976ad1ffa0"
data_git_describe = "v0.0-9231-g8288b0163"
data_git_msg = """\
commit 8288b0163a4d7b7bcf904da84c6d18976ad1ffa0
Author: Jes B. Klinke <jbk@chromium.org>
Date:   Mon Nov 8 13:46:08 2021 -0800

    [opentitantool] Support configuration of GPIO pin modes
    
    Replace GPIO direction enum (in/out) with a mode enum
    (input/push pull/open drain).
    
    Also, introduce functionality in TransportWrapper to iterate over pin
    declarations and apply mode and default output level on a set of pins.
    This is intended to be used both on a broad set of pins, as well as
    multiple named combinations on a smaller set of pins strappings.
    
    Signed-off-by: Jes B. Klinke <jbk@chromium.org>
    Change-Id: Ia6b9f392be2c34451bcdfadf82b8864797d5553b

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
