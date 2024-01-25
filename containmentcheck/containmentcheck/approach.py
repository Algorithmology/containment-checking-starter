"""Configuration of the benchmarking tool with an approach."""

from enum import Enum

# TODO: Define the name for the approach for performing containment checking of structured types

class ContainmentCheckApproach(str, Enum):


    list = ""
    set = ""
    tuple = ""
