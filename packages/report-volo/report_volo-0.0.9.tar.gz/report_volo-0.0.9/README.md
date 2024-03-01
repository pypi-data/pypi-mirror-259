# Formula 1 Monaco 2018 Racing Report Generator

This Python package provides a tool for generating reports based on the start and end data of the best lap for each racer of Formula 1 - Monaco 2018 Racing during the first stage of the qualification (Q1).

## Installation

To use the package, you need to install it first. You can do this using `pip`:

```pip install report_volo```

## Usage

The package provides a command-line interface with several options.

### Generating a Report

You can generate a report for the first 20 minutes of the Monaco 2018 Racing by providing the path to the folder containing the data files. The `--asc` or `--desc` flag allows you to specify the sorting order (default is ascending).

```bash (update later)
report.py --files <folder_path> [--asc | --desc]
```

### Driver Statistics

To get statistics about a specific driver, use the `--driver` option along with the folder path.

```bash
report.py --files <folder_path> --driver "Sebastian Vettel"
```

## Package Structure

The package consists of the following components:

- **`Record` Class:** Represents a racer record with start and end times.
- **`FileNotFound` Exception:** Raised when a specified file is not found.
- **`ReportInvalidOrder` Exception:** Raised for an invalid sorting order in the report.
- **`build_report` Function:** Compiles a report summarizing valid and invalid records.
- **`print_report` Function:** Prints a formatted report based on ordered results.
- **`cli` Function:** Parses command-line arguments and orchestrates the report generation process.

## Example

```python
import report.py
#(update later)
# Command-line interface
args = formula1_report.Record.cli()

# Build the report
good_records, bad_records = formula1_report.Record.build_report(args.files, args.sort)

# Filter records if a specific driver is provided
if args.driver:
    good_records = [rec for rec in good_records if rec.driver == args.driver]
    bad_records = [rec for rec in bad_records if rec.driver == args.driver]

# Print the report
print(report.Record.print_report(good_records, bad_records))
```

## License

This package is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
