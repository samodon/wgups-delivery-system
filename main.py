from hashtable import HashTable
import pandas
from package import Package
from delivery import delivery


# Trruck class, used to create truck objects and load packages into them
class Truck:
    def __init__(self):
        self.packages = []
        self.current_location = None
        self.total_distance = 0

    def load_truck(self, package):
        # Update the package status to "Loaded into Truck"
        package.delivery_status = "Loaded into Truck"
        self.packages.append(package)


def main():
    # Create a hash table to store the packages
    package_table = HashTable()

    # Read the package file and load the packages into the hash table

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

    # Set the delivery address for package 9 to the correct address
    package_table.search(9).delivery_address = "410 S State St"

    # Create truck objects
    truck1 = Truck()
    truck2 = Truck()
    truck3 = Truck()
    user_input = 0

    # Main menu for the delivery system
    print("Welcome to the WGUPS delivery system. What would you like to do?")
    while user_input != 5:
        print("1. Load Trucks")
        print("2. Deliver Packages")
        print("3. Check Package Status")
        print("4. Get Truck Distance")
        print("5. Exit")
        user_input = int(input("Select an option: "))

        if user_input == 1:
            # Check if the trucks have already been loaded
            if (
                len(truck1.packages) > 0
                or len(truck2.packages) > 0
                or len(truck3.packages) > 0
            ):
                print("Trucks have already been loaded")
                continue
            # Load the trucks with the packages
            load_trucks(package_table, truck1, truck2, truck3)
        elif user_input == 2:
            # Confirms that the trucks have been loaded before delivering packages
            if len(truck1.packages) == 0:
                print("Trucks have not been loaded yet")
            else:
                # initialize the delivery objects, 800 is the start time for the first trucks
                delivery1 = delivery(800)
                delivery2 = delivery(800)
                print("Truck 1 and Truck 2 out delivering packages!")

                # runs the nearest neighbor algorithm on the packages for each truck``
                delivery2.nearest_neighbor(truck2.packages)
                delivery1.nearest_neighbor(truck1.packages)

                # Adds the address of the wrong address package to the route at the last index in anticipation of receiving the correct address
                delivery2.route[5], delivery2.route[12] = (
                    delivery2.route[12],
                    delivery2.route[5],
                )
                # Adds the package with a delayed delivery time to the route at the end
                delivery2.route[5], delivery2.route[11] = (
                    delivery2.route[11],
                    delivery2.route[5],
                )

                # Delivers the packages for each truck
                delivery1.deliver(delivery1.route, truck1.packages, truck1)
                delivery2.deliver(delivery2.route, truck2.packages, truck2)

                # Checks the delivery time of the last package delivered by each truck to the hub
                truck1_distance_to_hub = delivery1.get_distances(
                    truck1.packages[delivery1.route[-1]].delivery_address,
                    "4001 South 700 East",
                )
                truck1_time_to_hub = (truck1_distance_to_hub / 18) * 60

                # Determines the truck that will leave the hub next based on which one arrives back first
                if delivery1.delivery_time < delivery2.delivery_time:
                    print("Truck 3 out for delivery")
                    delivery3 = delivery(delivery1.delivery_time + truck1_time_to_hub)
                    delivery3.nearest_neighbor(truck3.packages)
                    delivery3.deliver(delivery3.route, truck3.packages, truck3)
                else:
                    print("Truck 3 out for delivery")
                    delivery3 = delivery(delivery2.delivery_time)

                    delivery3.nearest_neighbor(truck3.packages)
                    delivery3.deliver(delivery3.route, truck3.packages, truck3)

                # Updates the delivery status of the packages in the hash table
                truck1.packages[
                    0
                ].delivery_status = f"Delivered at {delivery1.delivery_time}"

                # Updates the delivery status and time of the packages in the hash table
                for i in range(package_table.size):
                    package_in_table = package_table.search(i)

                    if package_in_table:
                        # Check packages in truck 1
                        for truck_package in truck1.packages:
                            if truck_package.id == package_in_table.id:
                                hours = int(truck_package.delivery_time // 100)
                                minutes = int(truck_package.delivery_time % 60)

                                package_in_table.delivery_status = (
                                    f"Delivered at {hours}:{minutes:02}"
                                )
                                package_in_table.delivery_time = (
                                    truck_package.delivery_time
                                )
                                break  # Found the package, no need to check further.

                        # Check packages in truck 2
                        for truck_package in truck2.packages:
                            if truck_package.id == package_in_table.id:
                                hours = int(truck_package.delivery_time // 100)
                                minutes = int(truck_package.delivery_time % 60)

                                package_in_table.delivery_status = (
                                    f"Delivered at {hours}:{minutes:02}"
                                )
                                package_in_table.delivery_time = (
                                    truck_package.delivery_time
                                )
                                break  # Found the package, no need to check further.

                        # Check packages in truck 3
                        for truck_package in truck3.packages:
                            if truck_package.id == package_in_table.id:
                                hours = int(truck_package.delivery_time // 100)
                                minutes = int(truck_package.delivery_time % 60)

                                package_in_table.delivery_status = (
                                    f"Delivered at {hours}:{minutes:02}"
                                )
                                package_in_table.delivery_time = (
                                    truck_package.delivery_time
                                )
                                break  # Found the package, no need to check further.

        # Checks the status of the packages
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

            # Checks the status of the packages based on the time delivered
            elif option == 3:
                print("1. 8:35 - 9:25")
                print("2. 9:35 - 10:25")
                print("3. 12:03 - 1:12")
                time = int(input("Select a time period: "))
                if time == 1:
                    print(package_table.search(1).delivery_time)
                    for i in range(1, (package_table.size)):
                        if (
                            package_table.search(i).delivery_time >= 859.0
                            and package_table.search(i).delivery_time <= 942.0
                        ):
                            print(package_table.search(i))
                            print(package_table.search(i).delivery_time)
                elif time == 2:
                    for i in range(1, (package_table.size)):
                        if (
                            package_table.search(i).delivery_time >= 959
                            and package_table.search(i).delivery_time <= 1042
                        ):
                            print(package_table.search(i).delivery_time)

                elif time == 3:
                    for i in range(1, (package_table.size)):
                        if (
                            package_table.search(i).delivery_time >= 1205
                            and package_table.search(i).delivery_time <= 1320
                        ):
                            print(package_table.search(i))
        elif user_input == 4:
            # Prints the total distance traveled by each truck
            print(f"Truck 1 total distance: {truck1.total_distance:.2f} miles")
            print(f"Truck 2 total distance: {truck2.total_distance:.2f} miles")
            print(f"Truck 3 total distance: {truck3.total_distance:.2f} miles")

        # Bye Bye
        elif user_input == 5:
            print("Goodbye!")
        else:
            print("Invalid input. Please try again.")


# Loading the trucks with the packages that need to be delivered, ordering them as needed
def load_trucks(package, truck1, truck2, truck3):
    truck1_ids = [13, 14, 15, 16, 19, 20, 27, 29, 30, 31, 34, 37, 40]
    truck2_ids = [2, 3, 4, 5, 9, 18, 26, 28, 32, 35, 36, 38]
    truck3_ids = [6, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24, 25, 33, 39, 1]

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
