import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9553"
version_tuple = (0, 0, 9553)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9553")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9431"
data_version_tuple = (0, 0, 9431)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9431")
except ImportError:
    pass
data_git_hash = "733e3ecf5ccc3fd89755c9e3ec6c3532bc53c12d"
data_git_describe = "v0.0-9431-g733e3ecf5"
data_git_msg = """\
commit 733e3ecf5ccc3fd89755c9e3ec6c3532bc53c12d
Author: Muqing Liu <muqing.liu@wdc.com>
Date:   Wed Jan 5 16:40:55 2022 -0800

    [edn, dv] EDN testplan update
    
      - Update EDN testplan to include alert and error tests
      - Move the ERR_CODE verification from the interrupt test to error test
      - Add a covergroup for interrupt, alert and error test
    
    Signed-off-by: Muqing Liu <muqing.liu@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
