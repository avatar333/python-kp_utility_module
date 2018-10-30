import sys
from colorama import Fore
from colorama import Style
from colorama import init
init()

# Check 'argparse' and 'docopt' for advanced argument parsing


def check_args(expected_arg_num: 0):
    """
    Check and confirm that the required amount of arguments have been passed
    Args:
        Uses arguments passed to the script itself, using sys.argv
    Returns:
        bool: True if argument count
    Raises:
        Exception: ?????
    """

    if len(sys.argv[1:]) >= expected_arg_num:
        return True
    else:
        print(f'Less than the expected{Fore.YELLOW}', expected_arg_num, \
              f'{Style.RESET_ALL}arguments passed to{Fore.GREEN}', sys.argv[0])
        return False


def print_args():
    """
    Just some practice stuff for basics
    Args:
        Uses arguments passed to the script itself, using sys.argv
    Returns:
        bool: N/A
    Raises:
        Exception: ?????
    """


'''
    print("All the arguments passed to the script are:", sys.argv[1:], "\n")
    print("web-hook_url: ", sys.argv[1])
'''

# TEST
# ZZZZZZZZZZZZZZZZZZZZZ
