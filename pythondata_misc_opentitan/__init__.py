import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14423"
version_tuple = (0, 0, 14423)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14423")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14281"
data_version_tuple = (0, 0, 14281)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14281")
except ImportError:
    pass
data_git_hash = "f3b5cf89960dc332e12fbe4cb1e04e1b8aa7aa67"
data_git_describe = "v0.0-14281-gf3b5cf8996"
data_git_msg = """\
commit f3b5cf89960dc332e12fbe4cb1e04e1b8aa7aa67
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Fri Sep 23 16:06:55 2022 -0700

    [entropy_src/dv] VCS compatibility
    
    Minor VCS-related bug fix
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

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
