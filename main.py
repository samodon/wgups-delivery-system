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
    user_input = 0

    while user_input != 4:
        print("Welcome to the WGUPS delivery system. What would you like to do?")
        print("1. Load Trucks")
        print("2. Deliver Packages")
        print("3. Check Package Status")
        print("4. Exit")
        user_input = int(input("Select an option: "))
        if user_input == 1:
            load_trucks(package_table, truck1, truck2, truck3)
            print(f"Truck 1 has been loaded with {len(truck1.packages)} packages")
            print(f"Truck 2 has been loaded with {len(truck2.packages)} packages")
            print(f"Truck 3 has been loaded with {len(truck3.packages)} packages")
        elif user_input == 2:
            if len(truck1.packages) == 0:
                print("Trucks have not been loaded yet")
            else:
                delivery1 = delivery(800)
                delivery2 = delivery(800)
                print("Truck 1 and Truck 2 out delivery packages!")
                delivery2.nearest_neighbor(truck2.packages)
                delivery1.nearest_neighbor(truck1.packages)
                delivery1.deliver(delivery1.route, truck1.packages)
                delivery2.deliver(delivery2.route, truck2.packages)
                if delivery1.delivery_time < delivery2.delivery_time:
                    print("Truck 3 out for delivery")
                    distance_to_hub = delivery1.get_distances(
                        truck1.packages[delivery1.route[-1]].delivery_address,
                        "4001 South 700 East",
                    )
                    delivery1._get_time(distance_to_hub)
                    delivery3 = delivery(delivery1.delivery_time)
                    delivery3.nearest_neighbor(truck3.packages)
                    delivery3.deliver(delivery3.route, truck3.packages)
                else:
                    print("Truck 3 out for delivery")
                    distance_to_hub = delivery2.get_distances(
                        truck2.packages[delivery2.route[-1]].delivery_address,
                        "4001 South 700 East",
                    )
                    delivery2._get_time(distance_to_hub)
                    delivery3 = delivery(delivery2.delivery_time)
                    delivery3.nearest_neighbor(truck3.packages)
                    delivery3.deliver(delivery3.route, truck3.packages)
                for i in range(1, (package_table.size)):
                    if i < len(truck1.packages):
                        if truck1.packages[i].id == package_table.search(i).id:
                            package_table.search(i).delivery_status = truck1.packages[
                                i
                            ].delivery_status
                    if i < len(truck2.packages):
                        if truck2.packages[i].id == package_table.search(i).id:
                            package_table.search(i).delivery_status = truck2.packages[
                                i
                            ].delivery_status
                    if i < len(truck3.packages):
                        if truck3.packages[i].id == package_table.search(i).id:
                            package_table.search(i).delivery_status = truck3.packages[
                                i
                            ].delivery_status
        elif user_input == 3:
            print("Choose an option:")
            print("1. Check all packages")
            print("2. Check a specific package")
            option = int(input("Select an option: "))
            if option == 1:
                for i in range(1, (package_table.size)):
                    print(package_table.search(i))
            elif option == 2:
                package_id = int(input("Enter the package ID: "))
                print(package_table.search(package_id))


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
