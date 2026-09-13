import argparse
import logging
from pathlib import Path
from datetime import datetime

import pandas as pd


REQUIRED_COLUMNS = ["Employee", "Department", "Salary", "Performance"]


def setup_logging(log_file):
    """Configure logging for the automation."""
    log_file.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


def load_csv(input_file):
    """Load the CSV file safely."""
    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    try:
        if input_file.stat().st_size == 0:
            raise ValueError("The CSV file is empty.")

        df = pd.read_csv(input_file)

    except ValueError:
        raise

    except Exception as exc:
        raise ValueError(f"Unable to read CSV file: {exc}") from exc
    
    if df.empty:
        raise ValueError("The CSV file is empty.")

    return df


def validate_data(df):
    """Validate required columns and salary values."""
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {', '.join(missing_columns)}"
        )

    df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

    if df["Salary"].isna().any():
        raise ValueError("Salary contains invalid or missing numeric values.")

    return df


def generate_summary(df):
    """Calculate report statistics."""
    summary = {
        "total_employees": len(df),
        "average_salary": df["Salary"].mean(),
        "minimum_salary": df["Salary"].min(),
        "maximum_salary": df["Salary"].max(),
        "department_count": df["Department"].value_counts(),
        "department_average_salary": df.groupby("Department")["Salary"].mean(),
        "performance_count": df["Performance"].value_counts(),
    }

    return summary


def generate_report(summary, output_file):
    """Generate and save the final text report."""
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write("AUTOMATED EMPLOYEE REPORT\n")
        file.write("=" * 50 + "\n")
        file.write(
            f"Generated on: "
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        )

        file.write("GENERAL SUMMARY\n")
        file.write("-" * 50 + "\n")
        file.write(
            f"Total Employees: {summary['total_employees']}\n"
        )
        file.write(
            f"Average Salary: ₹{summary['average_salary']:,.2f}\n"
        )
        file.write(
            f"Minimum Salary: ₹{summary['minimum_salary']:,.2f}\n"
        )
        file.write(
            f"Maximum Salary: ₹{summary['maximum_salary']:,.2f}\n\n"
        )

        file.write("DEPARTMENT SUMMARY\n")
        file.write("-" * 50 + "\n")

        for department, count in summary["department_count"].items():
            avg_salary = summary["department_average_salary"][department]
            file.write(
                f"{department}: {count} employee(s), "
                f"Average Salary: ₹{avg_salary:,.2f}\n"
            )

        file.write("\nPERFORMANCE SUMMARY\n")
        file.write("-" * 50 + "\n")

        for performance, count in summary["performance_count"].items():
            file.write(f"{performance}: {count} employee(s)\n")

        file.write("\n")
        file.write("Report generated successfully by Automated CSV Report Generator.\n")


def main():
    parser = argparse.ArgumentParser(
        description="Generate an automated employee report from a CSV file."
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to the input CSV file."
    )

    parser.add_argument(
        "--output",
        default="output/employee_report.txt",
        help="Path for the generated report."
    )

    args = parser.parse_args()

    input_file = Path(args.input)
    output_file = Path(args.output)
    log_file = Path("logs/automation.log")

    setup_logging(log_file)

    try:
        logging.info("Automation started.")
        logging.info("Input file: %s", input_file)

        df = load_csv(input_file)
        logging.info("CSV successfully loaded.")

        df = validate_data(df)
        logging.info("Data validation completed successfully.")

        summary = generate_summary(df)
        generate_report(summary, output_file)

        logging.info("Report generated successfully.")
        logging.info("Output file: %s", output_file)
        logging.info("Records processed: %d", len(df))

        print("\nReport generated successfully!")
        print(f"Input: {input_file}")
        print(f"Output: {output_file}")
        print(f"Records processed: {len(df)}")

    except FileNotFoundError as exc:
        logging.error(str(exc))
        print(f"\nERROR: {exc}")

    except ValueError as exc:
        logging.error(str(exc))
        print(f"\nERROR: {exc}")

    except Exception as exc:
        logging.exception("Unexpected error occurred.")
        print(f"\nERROR: Unexpected error occurred: {exc}")


if __name__ == "__main__":
    main()
