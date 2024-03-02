# Project description

Module for report generation. Takes logs of start and end time, assing values by key to data from abbrevations.txt and provide records recults.

## Installation

To use the package, you need to install it first. You can do this using `pip`:

```pip install report_volo```

## A Simple Example
"""
from report_volo import record_report

args = ["--files", "path/to/data_folder", "--asc"]
record_report(args)
"""

## Methods:

### read_abbr

Reads abbreviations from the specified file, validates the format, and returns a dictionary of `Record` objects.
"""
Example:
>> Record.read_abbr("path/to/folder, records_dict, abbr_file="abbreviations.txt")
"""
### read_logs 

Reads log files, extracts start and end data, and updates the Record objects accordingly.
"""
Example:
>> read_logs("path/to/folder", records_dict, start_file="start.log", end_file="end.log")
"""

### build_report 
Compiles and returns two lists of Record objects representing valid and invalid records based on logs and abbreviations.
"""
Example:
>>  good_records_asc, bad_records = Record.build_report(path=folder_path, order="asc")
"""

### print_report
Formats and prints a report based on ordered lists of valid and invalid records.
"""
Example:
>> print_report(expected_good_records_asc, expected_bad_records, border_line=2)
"""


### cli
Parses command-line arguments using argparse and returns a namespace.
"""
Example:
>> cli("--files", "path/to/folder", "--asc")
"""

### record_report
Orchestrates the report generation process, parsing command-line arguments, generating reports, and printing them.
"""
Example:
>> record_report("--files", "path/to/folder", "--asc")
"""


## License

This package is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
