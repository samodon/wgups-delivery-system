from hashtable import HashTable
import numpy as np
import pandas
from package import Package


class Truck:
    def __init__(self):
        self.packages = []
        self.current_location = None

    def load_truck(self, package):
        self.packages.append(package)


class delivery:
    def __init__(self):
        self.delivery_time = 800
        self.df = self.clean_df("WGUPS_Distance_Table.csv")

    def clean_df(self, csv_file):
        df = pandas.read_csv(csv_file)
        df[df.columns[0]] = df[df.columns[0]].str.strip()
        df.columns = df.columns.str.strip()

        return df

    def deliver(self, truck):
        pass

    def get_distance(self, start_address, end_address):
        row, col = np.where(self.df == start_address)
        print(self.df.at[row[0], end_address])
        return self.df.at[row[0], end_address]

    def _get_time(self, distance):
        time = distance / 18
        self.time = (time * 60) + self.time
        return


def main():
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

    truck1 = Truck()
    truck2 = Truck()
    truck3 = Truck()

    load_trucks(package_table, truck1, truck2, truck3)

    # print(truck1.packages[0].delivery_address)
    delivery1 = delivery()
    delivery1.get_distance("1060 Dalton Ave S", "4001 South 700 East")


def load_trucks(package, truck1, truck2, truck3):
    for i in range(1, package.size):
        if len(truck2.packages) < 16:
            if package.search(i).id == 3:
                truck2.load_truck(package.search(i))
            elif package.search(i).id == 18:
                truck2.load_truck(package.search(i))
            elif package.search(i).id == 36:
                truck2.load_truck(package.search(i))
            elif package.search(i).id == 38:
                truck2.load_truck(package.search(i))
            elif (
                package.search(i).id == 15
                or package.search(i).id == 19
                or package.search(i).id == 13
            ):
                truck2.load_truck(package.search(i))
            else:
                truck2.load_truck(package.search(i))
        elif len(truck1.packages) < 16:
            truck1.load_truck(package.search(i))
        else:
            truck3.load_truck(package.search(i))


if __name__ == "__main__":
    main()
