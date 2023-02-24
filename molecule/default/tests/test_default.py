from pathlib import Path

import pytest


@pytest.mark.parametrize(
    ("user", "principals"),
    (
        ("admin", ["barack", "joe"]),
        ("service", ["carpool"])
    )
)
def test_hosts_file(host, user: str, principals: list[str]):
    """Validate /etc/hosts file."""
    path = Path("/etc/ssh/auth_principals") / user
    f = host.file(str(path))

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"
    for principal in principals:
        assert f.contains(principal)
