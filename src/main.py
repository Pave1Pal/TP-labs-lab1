# -*- coding: utf-8 -*-
import argparse
import sys

from JsonDataReader import JsonDataReader
from StudyDebtorFinder import StudyDebtorFinder


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    jsonReader = JsonDataReader()
    students = jsonReader.read(path)
    print("Students: ", students)

    debtorFinder = StudyDebtorFinder()
    debtors = debtorFinder.find(students)
    print("Debtors: ", debtors)
    print(len(debtors))


if __name__ == "__main__":
    main()
