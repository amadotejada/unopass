import shutil
import subprocess


def op_path() -> str:
    """
    Locate the `op` 1Password CLI binary on PATH.

    :return: Absolute path to the `op` binary.
    :raises FileNotFoundError: If `op` is not on PATH.
    """
    op = shutil.which("op")
    if op is None:
        raise FileNotFoundError(
            "error: op cli not found\nhttps://github.com/amadotejada/unopass"
        )
    return op


def unopass(vault, item, field, deauthorize=None) -> str:
    """
    `Requires the 1Password CLI v2.4.1 or higher with Biometrics enabled`

    `unopass` is a function that takes a vault, item, and field as arguments and returns the
    value of the field.

    :param vault: The name of the vault you want to access
    :param item: The name of the item you want to retrieve
    :param field: The field you want to retrieve
    :param deauthorize: If truthy, sign out of the 1Password CLI session after the read
    :return: The retrieved secret value
    :raises FileNotFoundError: If `op` is not on PATH
    :raises subprocess.CalledProcessError: If `op read` fails
    :raises subprocess.TimeoutExpired: If the biometric prompt is not answered within 30s
    """
    op = op_path()
    try:
        result = subprocess.run(
            (op, "read", f"op://{vault}/{item}/{field}"),
            capture_output=True,
            check=True,
            text=True,
            timeout=30,
        )
    except subprocess.CalledProcessError:
        try:
            signout(deauthorize)
        except Exception:
            pass
        raise
    signout(deauthorize)
    return result.stdout.strip()


def signout(deauthorize=None) -> None:
    """
    Sign out of the 1Password CLI session.

    :param deauthorize: If truthy, run `op signout`. Otherwise no-op.
    :raises subprocess.CalledProcessError: If `op signout` fails
    """
    if not deauthorize:
        return
    op = op_path()
    subprocess.run([op, "signout"], capture_output=True, check=True, text=True)
