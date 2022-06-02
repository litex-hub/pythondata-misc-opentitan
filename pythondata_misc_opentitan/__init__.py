import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12471"
version_tuple = (0, 0, 12471)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12471")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12329"
data_version_tuple = (0, 0, 12329)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12329")
except ImportError:
    pass
data_git_hash = "aa91ed9c8c1a464a91828b431d73e73b84cdd218"
data_git_describe = "v0.0-12329-gaa91ed9c8"
data_git_msg = """\
commit aa91ed9c8c1a464a91828b431d73e73b84cdd218
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Thu Jun 2 09:26:49 2022 -0700

    fix(cdc): Typo in waiver file
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
