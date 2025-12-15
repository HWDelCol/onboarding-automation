from readers.csv_reader import read_employees


def main():
    employees = read_employees("data/employees.csv")
    for emp in employees:
        print(emp)


if __name__ == "__main__":
    main()