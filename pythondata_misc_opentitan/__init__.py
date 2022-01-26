import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9808"
version_tuple = (0, 0, 9808)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9808")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9686"
data_version_tuple = (0, 0, 9686)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9686")
except ImportError:
    pass
data_git_hash = "d4457de7e3c5a0509d7640e13081d4daf5060750"
data_git_describe = "v0.0-9686-gd4457de7e"
data_git_msg = """\
commit d4457de7e3c5a0509d7640e13081d4daf5060750
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Jan 25 17:35:31 2022 -0800

    [dv] Update reset probing to match ast update
    
    - por_ni no longer causes ast to asynchronously reset.
    - Tweak the sequence to first look for reset de-assertion before
      looking for assertion
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
