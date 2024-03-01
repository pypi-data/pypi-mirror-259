import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
import argparse

RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def check_requirements_update(library_name: str, required_version: str, verbose: bool = False):
    """Check if there's a newer version of a library available on PyPI.

    Args:
        library_name (str): The name of the library.
        required_version (str): The version specified in the requirements.
        verbose (bool, optional): Whether to print additional information. Defaults to False.

    Returns:
        tuple: A tuple containing (new_version, days_since_release, is_new_version).
    """
    base_url = f'https://pypi.org/rss/project/{library_name}/releases.xml'.strip()
    try:
        response = requests.get(base_url)
    except requests.exceptions.RequestException as e:
        if verbose:
            print(f"{RED}[-]{RESET} CONNECTION ERROR")
            return None, None, False

    if response.status_code == 200:
        root = ET.fromstring(response.text)
        initial_version_found = True
        initial_version = None

        for release_item in root.findall('.//channel/item'):
            release_title = release_item.find('title').text

            if initial_version_found:
                initial_version_found = False
                initial_version = release_title
                if release_title == required_version:
                    initial_version_found = False
                    return release_title, 0, False
            else:
                if release_title == required_version:
                    release_date_unix = convert_time(release_item.find('pubDate').text)
                    time_difference = time_between(release_date_unix)
                    return initial_version, time_difference, True
        return initial_version, None, True
    else:
        return None, None, None

def convert_time(time_rss: str):
    """Convert time from RSS format to Unix timestamp.

    Args:
        time_rss (str): Time (format:  "%a, %d %b %Y %H:%M:%S %Z")

    Returns:
        int: Unix timestamp.
    """
    date_obj = datetime.strptime(time_rss, "%a, %d %b %Y %H:%M:%S %Z")
    date_obj = date_obj.replace(tzinfo=timezone.utc)  # Set the timezone explicitly to UTC
    unixtime = date_obj.timestamp()
    return unixtime

def time_between(date: int):
    """Calculate the number of days between the specified date and the current date.

    Args:
        date (int): Unix timestamp.

    Returns:
        int: Number of days.
    """
    today = datetime.now()
    delta = today - datetime.fromtimestamp(date)
    days = delta.days
    return days

def load_requirements(file_path: str):
    """Load requirements from the specified file.
    
    Args:
        file_path (str): Path to the requirements file.
        
    Returns:
        list: List of requirements.
    """
    try:
        with open(file_path) as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"{RED}[-]{RESET} ERROR: File {file_path} not found")
        exit()

def extract_library_and_version(line: str):
    """Extract the library name, version, and operator from the specified line.
    
    Args:
        line (str): Line from the requirements file.
        
    Returns:
        list: List containing the library name, version, and operator.
    """
    for operator in ['==', '>=', '<=', '>', '<']:
        if operator in line:
            return line.split(operator) + [operator]
    return [line.replace("\n", ""), "", "=="]

def update_requirements(requirements: str, verbose=True):
    """Check and update library versions in the requirements.
    
    Args:
        requirements (str): List of requirements.
        verbose (bool, optional): Whether to print additional information. Defaults to True.
        
    Returns:
        str: Updated requirements.
    """
    updated_elements = ""
    for line in requirements:
        library, version, operator = extract_library_and_version(line)
        version = version.strip()
        new_version, number_day, is_new_version = check_requirements_update(library, version)

        if verbose:
            if is_new_version is None:
                print(f"{RED}[-]{RESET}{BLUE}{library}{RESET} not found")
            elif is_new_version:
                print(f"{YELLOW}[i]{RESET} {library} | Days between versions: {number_day} days ==> {new_version}")
            else:
                print(f"{GREEN}[+]{RESET} {library} == {new_version}{RESET}")

        updated_elements += f"{library}{operator}{new_version}\n" if new_version else line

    return updated_elements

def start(file_requirements: str = "requirements.txt", verbose: bool = False, overwrite: bool = False):
    """Check and update the library versions in the requirements file.

    Args:
        file_requirements (str, optional): Path to the requirements file. Defaults to "requirements.txt".
        verbose (bool, optional): Whether to print additional information. Defaults to False.
        overwrite (bool, optional): Whether to overwrite the requirements file. Defaults to False.

    Returns:
        None: None
    """
    requirements = load_requirements(file_requirements)

    if overwrite:
        output_file = file_requirements
    else:
        output_file = "requirements-updated.txt"

    updated_requirements = update_requirements(requirements)

    save_requirements(updated_requirements, output_file)

def save_requirements(updated_requirements: str, output_file: str):
    """Save updated requirements to the specified file.
    
    Args:
        updated_requirements (str): Updated requirements.
        output_file (str): Path to the output file.
        
    Returns:
        None: None
    """
    with open(output_file, 'w') as file:
        file.writelines(updated_requirements)

def parse_args():
    """Parse command line arguments.

    Args:
        None
        
    Returns:
        argparse.Namespace: Parsed command line arguments.
    """
    parser = argparse.ArgumentParser(
        description='Check if the libraries in the requirements.txt file are up to date')

    parser.add_argument('-p', '--path', dest='file', default='requirements.txt',
                        help='Path of the requirements file')
    parser.add_argument('-v', '--verbose', action='store_true', default=False,
                        help='Display additional information')
    parser.add_argument('-f', '--force', action='store_true', default=False,
                        help='Overwrite the requirements file')

    args = parser.parse_args()

    args.verbose = False if args.verbose else True
    return parser.parse_args()

def main():
    args = parse_args()
    start(args.file, args.verbose, args.force)
    print("Requirements file updated")
    
if __name__ == '__main__':
    main()
