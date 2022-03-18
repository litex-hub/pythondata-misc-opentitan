import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10984"
version_tuple = (0, 0, 10984)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10984")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10858"
data_version_tuple = (0, 0, 10858)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10858")
except ImportError:
    pass
data_git_hash = "e586c76f5a728d4a45c7fb28aa0b858cb334a07b"
data_git_describe = "v0.0-10858-ge586c76f5"
data_git_msg = """\
commit e586c76f5a728d4a45c7fb28aa0b858cb334a07b
Author: Alexander Williams <awill@google.com>
Date:   Fri Mar 18 09:45:05 2022 -0700

    [dif/bazel] Fix up adc_ctrl target
    
    Remove duplicated hdrs field.
    
    Signed-off-by: Alexander Williams <awill@google.com>

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
