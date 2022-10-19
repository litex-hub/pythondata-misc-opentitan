import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14816"
version_tuple = (0, 0, 14816)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14816")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14674"
data_version_tuple = (0, 0, 14674)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14674")
except ImportError:
    pass
data_git_hash = "08ee604e37ff2be3e38ed7f4f826b40b9d6d54d0"
data_git_describe = "v0.0-14674-g08ee604e37"
data_git_msg = """\
commit 08ee604e37ff2be3e38ed7f4f826b40b9d6d54d0
Author: Weicai Yang <weicai@google.com>
Date:   Mon Oct 17 22:42:50 2022 -0700

    [chip, dv] update testplan for chip_sw_data_integrity test
    
    As discussed, we have chip_sw_all_escalation_resets to test integrity errors due to wr_en violation
    for all the IPs. This chip_sw_data_integrity test only needs to inject integrity error on a memory to
    test memory e2e integrity scheme.
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
