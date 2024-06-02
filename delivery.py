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

    # The solution might be to add the name of the corresponding addressses to the dictionary

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

    def get_distances(self, from_address, to_address):
        from_address = from_address.strip()
        to_address = to_address.strip()
        return self.distances[from_address][to_address]

    # TODO add a way to print the status of the packages at the times specified
    def deliver(self, route, locations, truck):
        distance = 0
        for index in route:
            if index == 0:
                self._get_time(0)
            else:
                distance = self.get_distances(
                    locations[route[index - 1]].delivery_address,
                    locations[route[index]].delivery_address,
                )
                self._get_time(distance)
                hours = int(self.delivery_time // 100)
                minutes = int(self.delivery_time % 60)
                locations[
                    route[index]
                ].delivery_status = f"Delivered at {hours}:{minutes:02d}"
                locations[route[index]].delivery_time = self.delivery_time
                truck.total_distance += distance

    def _get_time(self, distance):
        time = distance / 18
        self.delivery_time += time * 60

    def nearest_neighbor(self, locations):
        hub = Package(
            0, "4001 South 700 East", 0, "Salt Lake City", "84107", 0, "At Hub"
        )
        locations.insert(0, hub)
        visited = [False] * len(locations)
        visited[0] = True
        self.route.append(0)
        current_index = 0

        for _ in range(1, len(locations)):
            min_distance = float("inf")
            nearest = None

            for j in range(len(locations)):
                if not visited[j]:
                    distance = self.get_distances(
                        locations[current_index].delivery_address,
                        locations[j].delivery_address,
                    )
                    if distance < min_distance:
                        min_distance = distance
                        nearest = j

            if nearest is not None:
                visited[nearest] = True
                self.route.append(nearest)
                current_index = nearest
