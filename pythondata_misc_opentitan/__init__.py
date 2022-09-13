import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14173"
version_tuple = (0, 0, 14173)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14173")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14031"
data_version_tuple = (0, 0, 14031)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14031")
except ImportError:
    pass
data_git_hash = "de4d178aa78d053ef3bcf166ec6f7322ce1517c5"
data_git_describe = "v0.0-14031-gde4d178aa7"
data_git_msg = """\
commit de4d178aa78d053ef3bcf166ec6f7322ce1517c5
Author: Jorge Prendes <jorge.prendes@gmail.com>
Date:   Tue Sep 13 13:56:07 2022 +0100

    [ottool] Use a constant for the programming speed
    
    Signed-off-by: Jorge Prendes <jorge.prendes@gmail.com>

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
