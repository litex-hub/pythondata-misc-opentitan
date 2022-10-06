import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14583"
version_tuple = (0, 0, 14583)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14583")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14441"
data_version_tuple = (0, 0, 14441)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14441")
except ImportError:
    pass
data_git_hash = "b9d3d8f858e828dc39a28ab4e877c77fc1663e89"
data_git_describe = "v0.0-14441-gb9d3d8f858"
data_git_msg = """\
commit b9d3d8f858e828dc39a28ab4e877c77fc1663e89
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Wed Oct 5 02:26:01 2022 -0700

    added mubi cov if to esc_en issue#13579
    
    Signed-off-by: Rasmus Madsen <rasmus.madsen@wdc.com>

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
