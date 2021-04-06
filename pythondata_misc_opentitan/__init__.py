import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5724"
version_tuple = (0, 0, 5724)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5724")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5629"
data_version_tuple = (0, 0, 5629)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5629")
except ImportError:
    pass
data_git_hash = "4458f8377c5e0015c81802b321f22873b4097a23"
data_git_describe = "v0.0-5629-g4458f8377"
data_git_msg = """\
commit 4458f8377c5e0015c81802b321f22873b4097a23
Author: Philipp Wagner <phw@lowrisc.org>
Date:   Wed Mar 31 15:51:58 2021 +0100

    [otbn] Move to version 0.2
    
    OTBN is now in a consistent state from a specification, RTL,
    verification, and software perspective. The respective D1/V1/S1 status
    indicates that. We would like to use this opportunity to mark this state
    as version 0.1 before we move out of this consistent state again.
    
    Version 0.1 of OTBN isn't perfect -- there are known bugs and gaps in
    the implementation, in the verification, in the DIF and test software,
    and in the specification, as it would be expected for a design in
    L1/D1/V1/S1 state. However, OTBN in its current state is good enough
    to be synthesized properly, run RSA and ECDSA-P256 on it, and pass basic
    verification. The specification has seen extensive review.
    
    Going forward in version 0.2 we will (re-)open the discussion around some
    aspects of the specification, mostly to add security hardening features,
    and likely to be better suited for workloads we haven't considered so
    far (e.g. SIMD instructions for SHA2).
    
    For now, I'm leaving the D1/V1/S1 status in place (instead of going down
    e.g. to D0), as it is still valid. In the past we were able in OTBN to
    reasonably synchronously add support for new features to DIF, RTL, and
    verification, which would keep the *1 status in place. However, we don't
    have that many examples of version bumps in OpenTitan, and with that not
    that many established guidelines that we could follow.
    
    Finally: The version number does not have any semantic meaning whatsoever.
    
    Documentation on versioning: https://docs.opentitan.org/doc/project/development_stages/#versioning
    
    Signed-off-by: Philipp Wagner <phw@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
