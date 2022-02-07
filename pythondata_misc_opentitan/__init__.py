import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10095"
version_tuple = (0, 0, 10095)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10095")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9971"
data_version_tuple = (0, 0, 9971)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9971")
except ImportError:
    pass
data_git_hash = "62fca6299474fe9b75124952d46ac6defa2e2ad7"
data_git_describe = "v0.0-9971-g62fca6299"
data_git_msg = """\
commit 62fca6299474fe9b75124952d46ac6defa2e2ad7
Author: Nikola Miladinovic <nikola.miladinovic@ensilica.com>
Date:   Sun Feb 6 11:17:21 2022 +0000

    [flash_ctrl] SMALL SCOREBOARD KNOB CHANGE
    
    Add small knob change for control of host read operations.
    Change name of knob and invert value. Change tests host read
    direct and read buffer evict since they are affected.
    
    Signed-off-by: Nikola Miladinovic <nikola.miladinovic@ensilica.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
