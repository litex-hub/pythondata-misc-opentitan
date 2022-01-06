import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9349"
version_tuple = (0, 0, 9349)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9349")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9232"
data_version_tuple = (0, 0, 9232)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9232")
except ImportError:
    pass
data_git_hash = "3dab726bc1ece248cba95611400ca55ceaa5a848"
data_git_describe = "v0.0-9232-g3dab726bc"
data_git_msg = """\
commit 3dab726bc1ece248cba95611400ca55ceaa5a848
Author: Palmer Dabbelt <palmer@rivosinc.com>
Date:   Wed Jan 5 16:36:02 2022 -0800

    [doc] Fix a grammatical error in ug/design
    
    Signed-off-by: Palmer Dabbelt <palmer@rivosinc.com>

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
