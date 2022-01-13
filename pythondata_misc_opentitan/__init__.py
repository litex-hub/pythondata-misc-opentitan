import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9506"
version_tuple = (0, 0, 9506)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9506")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9388"
data_version_tuple = (0, 0, 9388)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9388")
except ImportError:
    pass
data_git_hash = "c439fa718ae74a00a4900238a513f239be35bcc8"
data_git_describe = "v0.0-9388-gc439fa718"
data_git_msg = """\
commit c439fa718ae74a00a4900238a513f239be35bcc8
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Wed Jan 12 13:35:54 2022 -0800

    [entropy complex/rtl] change comment on countermeasure
    
    A countermeasure comment was confusing for all entropy blocks doing consecutive bus comparisos.
    The comment has been corrected.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post118"
tool_version_tuple = (0, 0, 118)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post118")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
