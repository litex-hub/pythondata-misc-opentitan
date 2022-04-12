import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11520"
version_tuple = (0, 0, 11520)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11520")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11394"
data_version_tuple = (0, 0, 11394)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11394")
except ImportError:
    pass
data_git_hash = "18f93dba829de0f6cc21516896b014713bdf37f3"
data_git_describe = "v0.0-11394-g18f93dba8"
data_git_msg = """\
commit 18f93dba829de0f6cc21516896b014713bdf37f3
Author: Jade Philipoom <jadep@google.com>
Date:   Fri Apr 8 10:24:16 2022 +0100

    [sw,rom_ext] Replace exponent with address translation in manifest.
    
    We needed to make two changes to the manifest:
    * remove the exponent field (since only one exponent, 65537, is now
      supported), and
    * add a field to indicate whether the `ROM_EXT` expects address
      translation.
    
    Since the two fields are the same size, it causes minimum disruption in
    padding/offsets to simply replace one with the other.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
