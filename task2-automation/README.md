# Automated CSV Report Generator

Redynox Python Developer Internship — Task 2: Automation Script for a Real-World Problem

## Problem statement

HR and admin teams often receive employee data as CSV files and then calculate totals, salary ranges, and department summaries by hand. Doing this repeatedly is slow and easy to get wrong.

## Objective

Build a simple Python automation tool that:

1. Reads an employee CSV file
2. Validates the data
3. Calculates useful statistics
4. Writes a professional text report automatically
5. Logs every important step so the run can be reviewed later

This project solves **automated report generation**. It is not a file organizer, email sender, or web scraper.

## Solution approach

The script uses **Pandas** to load and clean CSV data, then writes a readable report with Python’s built-in libraries.

Typical flow:

1. Accept `--input` (and optional `--output`) from the command line
2. Start logging to `logs/automation.log`
3. Load the CSV
4. Check required columns and salary values
5. Calculate overall, department-wise, and performance-wise statistics
6. Save the report to `output/employee_report.txt`
7. Print a short success or error message in the terminal

## Features

- CSV input with command-line arguments
- Validation for missing files, empty files, missing columns, and invalid salaries
- Statistics: total records, average/min/max salary, department counts, department average salary, performance counts
- Professional text report with date and time
- Logging with INFO, WARNING, and ERROR
- Clear terminal messages after success or failure
- Extra sample files for testing error cases

## Technologies used

- Python 3
- Pandas
- argparse (command-line arguments)
- logging (execution logs)
- datetime and os (standard library)

## Project structure

```
task2-automation/
├── input/
│   ├── sample_data.csv          # Main demo dataset
│   ├── empty.csv                # Test: empty file
│   ├── missing_column.csv       # Test: Salary column missing
│   └── invalid_salary.csv       # Test: non-numeric salary
├── output/
│   └── employee_report.txt      # Generated report
├── logs/
│   └── automation.log           # Execution log
├── report_generator.py          # Main automation script
├── sample_data.csv              # Copy of the demo dataset
├── requirements.txt
└── README.md
```

Use `input/sample_data.csv` as the main input file.

## How to run the project

Open a terminal in the `task2-automation` folder.

```bash
cd task2-automation
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
python3 report_generator.py --input input/sample_data.csv
```

Optional custom output path:

```bash
python3 report_generator.py --input input/sample_data.csv --output output/employee_report.txt
```

You can also pass the copy in the project root:

```bash
python3 report_generator.py --input sample_data.csv
```

## Command examples

**Successful run (use this for your demo):**

```bash
python3 report_generator.py --input input/sample_data.csv --output output/employee_report.txt
```

**Empty CSV:**

```bash
python3 report_generator.py --input input/empty.csv
```

**Missing required column:**

```bash
python3 report_generator.py --input input/missing_column.csv
```

**Invalid salary values:**

```bash
python3 report_generator.py --input input/invalid_salary.csv
```

**File does not exist:**

```bash
python3 report_generator.py --input input/does_not_exist.csv
```

## Expected output

After a successful run, the terminal shows:

```text
Report generated successfully!
Input: input/sample_data.csv
Output: output/employee_report.txt
Records processed: 12
```

The report file includes:

- Report title
- Generation date and time
- Total employees
- Average, minimum, and maximum salary
- Department summary (count and average salary)
- Performance summary (count by rating)

## Testing scenarios

| Scenario | Command / file | Expected result |
|----------|----------------|-----------------|
| Valid CSV | `input/sample_data.csv` | Report created, 12 records processed |
| Empty CSV | `input/empty.csv` | Error: no employee records |
| Missing column | `input/missing_column.csv` | Error: missing `Salary` column |
| Invalid salary | `input/invalid_salary.csv` | Error: no valid numeric salary values |
| Missing file | `input/does_not_exist.csv` | Error: input CSV does not exist |

## Error handling

The program does not crash with a confusing traceback for normal user mistakes. It prints a short error message and writes details to `logs/automation.log`.

Handled cases:

- Input CSV does not exist
- Invalid CSV format
- Empty CSV
- Missing required columns
- Invalid numeric salary values
- Unexpected exceptions (logged as ERROR)

## How this meets Redynox Task 2

| Task 2 requirement | How this project covers it |
|--------------------|----------------------------|
| Real repetitive task | Employee CSV report generation |
| Input from files | `--input` CSV path |
| Data processing | Pandas load, clean, and group-by stats |
| Automated output | `output/employee_report.txt` |
| Logging | `logs/automation.log` |
| Error handling | User-friendly messages for common failures |
| Command-line arguments | `argparse` with `--input` and `--output` |
| Easy to demonstrate | One command produces a readable report |

## Future improvements

- Export the same summary as PDF or Excel
- Support extra columns such as joining date or bonus
- Watch a folder and generate a report whenever a new CSV arrives
- Add charts for department salary comparison
