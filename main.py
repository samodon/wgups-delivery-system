from hashtable import HashTable
import pandas
from package import Package
from delivery import delivery


class Truck:
    def __init__(self):
        self.packages = []
        self.current_location = None

    def load_truck(self, package):
        package.delivery_status = "Loaded into Truck"
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

    print(truck1.packages[1].package_weight)
    delivery1 = delivery(800)
    delivery1.nearest_neighbor(truck3.packages)
    route = delivery1.route
    print("Deliverying from Truck 1:")
    delivery1.deliver(route, truck3.packages)

    delivery2 = delivery(800)
    delivery2.nearest_neighbor(truck2.packages)
    route2 = delivery2.route
    print("Deliverying from Truck 2:")
    delivery2.deliver(route2, truck2.packages)
    # The first driver that returns to the hub first then that driver will take the remaining packages

    if delivery1.delivery_time < delivery2.delivery_time:
        # Calculate the distance from the last delivery to the hub and add it to the current time
        distance_to_hub = delivery1.get_distances(
            truck1.packages[route[-1]].delivery_address, "4001 South 700 East"
        )

        delivery1._get_time(distance_to_hub)
        print("Driver from Truck 1 will return to the hub first")
        delivery3 = delivery(delivery1.delivery_time)

        delivery3.nearest_neighbor(truck3.packages)

        route3 = delivery3.route
        print("Deliverying from Truck 3:")
        delivery3.deliver(route3, truck3.packages)
    else:
        print("Driver from Truck 2 will return to the hub first")
        distance_to_hub = delivery2.get_distances(
            truck1.packages[route[-1]].delivery_address, "4001 South 700 East"
        )

        delivery2._get_time(distance_to_hub)

        delivery3 = delivery(delivery1.delivery_time)
        delivery3.nearest_neighbor(truck3.packages)
        route3 = delivery3.route
        print("Deliverying from Truck 3:")
        delivery3.deliver(route3, truck3.packages)


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
