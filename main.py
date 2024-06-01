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

    package_table.search(9).delivery_address = "410 S State St"
    truck1 = Truck()
    truck2 = Truck()
    truck3 = Truck()
    user_input = 0

    print("Welcome to the WGUPS delivery system. What would you like to do?")
    while user_input != 4:
        print("1. Load Trucks")
        print("2. Deliver Packages")
        print("3. Check Package Status")
        print("4. Exit")
        user_input = int(input("Select an option: "))

        if user_input == 1:
            if (
                len(truck1.packages) > 0
                or len(truck2.packages) > 0
                or len(truck3.packages) > 0
            ):
                print("Trucks have already been loaded")
                continue
            load_trucks(package_table, truck1, truck2, truck3)
        #            print(f"Truck 1 has been loaded with {len(truck1.packages)} packages")
        #           print(f"Truck 2 has been loaded with {len(truck2.packages)} packages")
        #          print(f"Truck 3 has been loaded with {len(truck3.packages)} packages")
        elif user_input == 2:
            if len(truck1.packages) == 0:
                print("Trucks have not been loaded yet")
            else:
                delivery1 = delivery(800)
                delivery2 = delivery(800)
                print("Truck 1 and Truck 2 out delivering packages!")

                delivery2.nearest_neighbor(truck2.packages)
                delivery1.nearest_neighbor(truck1.packages)

                delivery1.deliver(delivery1.route, truck1.packages)
                delivery2.deliver(delivery2.route, truck2.packages)

                if delivery1.delivery_time < delivery2.delivery_time:
                    print("Truck 3 out for delivery")
                    # distance_to_hub = delivery1.get_distances(
                    # truck1.packages[delivery1.route[-1]].delivery_address,
                    # "4001 South 700 East",
                    # )

                    # delivery1._get_time(distance_to_hub)
                    delivery3 = delivery(delivery1.delivery_time)

                    delivery3.nearest_neighbor(truck3.packages)
                    delivery3.deliver(delivery3.route, truck3.packages)
                else:
                    print("Truck 3 out for delivery")
                    # distance_to_hub = delivery2.get_distances(
                    # truck2.packages[delivery2.route[-1]].delivery_address,
                    # "4001 South 700 East",
                    # )

                    # delivery2._get_time(distance_to_hub)
                    delivery3 = delivery(delivery2.delivery_time)

                    delivery3.nearest_neighbor(truck3.packages)
                    delivery3.deliver(delivery3.route, truck3.packages)

                for i in range(1, (package_table.size - 1)):
                    if i < len(truck1.packages):
                        if truck1.packages[i].id == package_table.search(i).id:
                            package_table.search(i).delivery_status = truck1.packages[
                                i
                            ].delivery_status
                            package_table.search(i).delivery_time = truck1.packages[
                                i
                            ].delivery_time

                    if i < len(truck2.packages):
                        if truck2.packages[i].id == package_table.search(i).id:
                            package_table.search(i).delivery_status = truck2.packages[
                                i
                            ].delivery_status
                            package_table.search(i).delivery_time = truck2.packages[
                                i
                            ].delivery_time

                    if i < len(truck3.packages):
                        if truck3.packages[i].id == package_table.search(i).id:
                            package_table.search(i).delivery_status = truck3.packages[
                                i
                            ].delivery_status
                            package_table.search(i).delivery_time = truck3.packages[
                                i
                            ].delivery_time
        elif user_input == 3:
            print("Choose an option:")
            print("1. Check all packages")
            print("2. Check a specific package")
            print("3. Select by time period")
            option = int(input("Select an option: "))
            if option == 1:
                for i in range(1, (package_table.size)):
                    print(package_table.search(i))
            elif option == 2:
                package_id = int(input("Enter the package ID: "))
                if package_id > package_table.size:
                    print("Invalid package ID")
                else:
                    print(package_table.search(package_id))
            elif option == 3:
                time = int(input("Enter the time: "))
                for i in range(1, (package_table.size)):
                    if package_table.search(i).delivery_time <= time:
                        print(package_table.search(i))
                    else:
                        continue
        elif user_input == 4:
            print("Goodbye!")
        else:
            print("Invalid input. Please try again.")


def load_trucks(package, truck1, truck2, truck3):
    truck1_ids = [1, 13, 14, 15, 16, 19, 20, 27, 29, 30, 31, 34, 37, 40]
    truck2_ids = [2, 3, 4, 5, 9, 18, 26, 28, 32, 35, 36, 38]
    truck3_ids = [6, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24, 25, 33, 39]

    for package_id in truck1_ids:
        pkg = package.search(package_id)
        if pkg:
            truck1.load_truck(pkg)

    for package_id in truck2_ids:
        pkg = package.search(package_id)
        if pkg:
            truck2.load_truck(pkg)

    for package_id in truck3_ids:
        pkg = package.search(package_id)
        if pkg:
            truck3.load_truck(pkg)


if __name__ == "__main__":
    main()
