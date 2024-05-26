from hashtable import HashTable
import pandas
from package import Package


def main():
    # Create a hashtable
    package_table = HashTable()
    df = pandas.read_csv("WGUPS Package File.csv")
    for index, row in df.iterrows():
        package = Package(
            row["Package\nID"],
            row["Address"],
            row["Delivery\nDeadline"],
            row["City "],
            row["Zip"],
            row["Weight\nKILO"],
            row["page 1 of 1PageSpecial Notes"],
        )
        package_table.insert(package.id, package)

    print(package_table.search(24))


if __name__ == "__main__":
    main()
