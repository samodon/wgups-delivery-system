import csv
from package import Package


class delivery:
    def __init__(self, delivery_time):
        self.delivery_time = delivery_time
        self.file_path = "WGUPS_Distance_Table.csv"
        self.route = []
        self.distances = {}
        self.addresses = []
        self._read_distances(self.file_path)

    # O(n^2)
    # Helper to read the distance table from the CSV file
    def _read_distances(self, file_path):
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            self.addresses = [address.strip() for address in next(reader)[1:]]

            for row in reader:
                from_address = row[0].strip()
                self.distances[from_address] = {}
                for i, distance in enumerate(row[1:]):
                    to_address = self.addresses[i]
                    self.distances[from_address][to_address] = float(distance)

    # O(1)
    # Get the distance between two addresses
    def get_distances(self, from_address, to_address):
        from_address = from_address.strip()
        to_address = to_address.strip()
        return self.distances[from_address][to_address]

    # O(n)
    # Delivers the packages in the route
    def deliver(self, route, locations, truck):
        distance = 0
        for index in route:
            if index == 0:
                self._get_time(0)
            else:
                #  Keep the package with the wrong address until the correct address is avaialble
                if truck.packages[route[index]].id == 9:
                    time_to_add = 1067 - self.delivery_time
                    truck.packages[route[index]].delivery_address = "410 S State St"
                    self.delivery_time += time_to_add
                distance = self.get_distances(
                    locations[route[index - 1]].delivery_address,
                    locations[route[index]].delivery_address,
                )
                # Get the time it takes to travel the distance
                self._get_time(distance)

                locations[route[index]].delivery_time = self.delivery_time
                truck.total_distance += distance

    # O(1)
    # Helper to get the time it takes to travel a distance
    def _get_time(self, distance):
        time = distance / 18
        self.delivery_time += time * 60

    # O(n^2)
    # Nearest neighbor algorithm to find the shortest route
    def nearest_neighbor(self, locations):
        # Sets the starting location to the hub
        hub = Package(
            0, "4001 South 700 East", 0, "Salt Lake City", "84107", 0, "At Hub"
        )
        locations.insert(0, hub)
        visited = [False] * len(locations)
        visited[0] = True
        self.route.append(0)
        current_index = 0

        # Iterates through the locations to find the nearest neighbor
        for _ in range(1, len(locations)):
            min_distance = float("inf")
            nearest = None

            # Finds the nearest neighbor by comparing the distances between the current location and the other locations
            for j in range(len(locations)):
                if not visited[j]:
                    distance = self.get_distances(
                        locations[current_index].delivery_address,
                        locations[j].delivery_address,
                    )
                    if distance < min_distance:
                        min_distance = distance
                        nearest = j

            # If a nearest neighbor is found, it is added to the route
            if nearest is not None:
                visited[nearest] = True
                self.route.append(nearest)
                current_index = nearest
