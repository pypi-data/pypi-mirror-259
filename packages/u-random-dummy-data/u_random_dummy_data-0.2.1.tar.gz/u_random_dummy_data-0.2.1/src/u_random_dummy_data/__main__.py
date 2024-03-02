import argparse

from u_random_dummy_data.format import format_data, FormatStyle
from . import generate_dummy_data


def main():
    parser = argparse.ArgumentParser(
        description="これは様々なフィールドのランダムダミーデータを生成するためのPythonアプリケーションです。")
    parser.add_argument("-c", "--count", type=int, default=1, help="Number of times to generate dummy data")
    parser.add_argument("-f", "--format", choices=["csv", "tsv", "json", "yaml", "scala"], default="csv",
                        help="Output format. 'csv' for comma-separated values, 'tsv' for tab-separated values, "
                             "'json' for JSON format, 'yaml' for YAML format, 'scala' for List of scala case class.")
    args = parser.parse_args()

    data_list = [generate_dummy_data.generate() for _ in range(args.count)]
    result = format_data(data_list, FormatStyle[args.format])
    print(result)


if __name__ == '__main__':
    main()
