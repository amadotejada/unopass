import shutil
import subprocess


def op_path() -> str:
    """
    It checks if the op command is installed and returns the path to the op command.
    :return: The location of the op binary.
    """
    try:
        cmd = "op"
        locate = shutil.which(cmd)
        if locate is not None:
            return locate
        else:
            raise FileNotFoundError("error: op cli not found\nhttps://github.com/amadotejada/unopass")
    except Exception as e:
        print(e)
        exit(1)


def unopass(vault, item, field, deauthorize=None) -> str:
    """
    `Requires the 1Password CLI v2.4.1 or higher with Biometrics enabled`

    `unopass` is a function that takes a vault, item, and field as arguments and returns the value of
    the field

    :param vault: The name of the vault you want to access
    :param item: The name of the item you want to retrieve
    :param field: The field you want to retrieve
    :param deauthorize: The boolean value that determines if 1Password should signout
    :return: The results of the command.
    """
    try:
        op = op_path()
        cmd = (op, "read", f"op://{vault}/{item}/{field}")
        results = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        signout(deauthorize)
        if results.strip().decode("utf-8") is not None:
            return results.strip().decode("utf-8")
    except subprocess.CalledProcessError as e:
        signout(deauthorize)
        print((e.output).decode("utf-8"))
        exit(1)


def signout(deauthorize=None) -> None:
    """
    It signs out of the 1Password CLI session

    :param deauthorize: The boolean value that determines if 1Password should signout
    :return: The output of the command.
    """
    try:
        if deauthorize:
            op = op_path()
            results = subprocess.check_output([op, "signout"], stderr=subprocess.STDOUT)
            return results.strip().decode("utf-8")
    except subprocess.CalledProcessError as e:
        print(e.output.decode("utf-8"))
        exit(1)
