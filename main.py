from hashtable import HashTable
import pandas
from package import Package
from delivery import delivery


class Truck:
    def __init__(self):
        self.packages = []
        self.current_location = None

    def load_truck(self, package):
        self.packages.append(package)


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

    delivery1 = delivery()
    delivery1.nearest_neighbor(truck3.packages)
    route = delivery1.route
    delivery1.deliver(route, truck3.packages)


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
