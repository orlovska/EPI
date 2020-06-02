import os
import sys
# fix path to allow tests easier access to the python code - see https://docs.python-guide.org/writing/structure/
current_folder_name = os.path.dirname(__file__)
step_one_directory_up = '..'
project_root = os.path.abspath(os.path.join(current_folder_name, step_one_directory_up))
before_other_code_search_places = 0
sys.path.insert(before_other_code_search_places, project_root)

from python_code import rectangle_intersection
from python_code import recursion_phone_mnemonics