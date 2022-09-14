import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14181"
version_tuple = (0, 0, 14181)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14181")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14039"
data_version_tuple = (0, 0, 14039)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14039")
except ImportError:
    pass
data_git_hash = "b6f1ac7835b81041dd7e1241efe5c0a4b74ef001"
data_git_describe = "v0.0-14039-gb6f1ac7835"
data_git_msg = """\
commit b6f1ac7835b81041dd7e1241efe5c0a4b74ef001
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Tue Sep 13 16:08:38 2022 -0700

    feat(kmac): Allow ENTROPY SEED update after REGWEN off
    
    _Related Issue: https://github.com/lowRISC/opentitan/issues/14902 _
    
    `ENTROPY_SEED[i]` is being used to issue LFSR seeds in the SW entropy
    mode. The updating of the seeds is one-time event. After the first
    update, SW is not permitted to change the seeds.
    
    The CSRs were also blocked by `CFG_REGWEN`. If SW clears the
    `CFG_REGWEN` before it updates the seeds, the SW is not able to update
    the seeds again until reset.
    
    This commit releases the restriction. It allows the `ENTROPY_SEED[i]`
    can be updated afer the SW clearing of `CFG_REGWEN`.
    
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
