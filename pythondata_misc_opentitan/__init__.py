import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10206"
version_tuple = (0, 0, 10206)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10206")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10082"
data_version_tuple = (0, 0, 10082)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10082")
except ImportError:
    pass
data_git_hash = "96ec26e144a62986d8be33a3ba1be85d1eab088b"
data_git_describe = "v0.0-10082-g96ec26e14"
data_git_msg = """\
commit 96ec26e144a62986d8be33a3ba1be85d1eab088b
Author: Nikola Miladinovic <nikola.miladinovic@ensilica.com>
Date:   Wed Feb 2 20:03:56 2022 +0000

    [flash_ctrl] ADD TEST FOR PHY ARBITRATION
    
    Add test for arbitration between host reads and controller operations.
    Test has three scenarios: 1. arbitration is tested on the
    different banks, 2. arbitration is tested on the same bank and
    3. lost of host reads priority.
    
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
