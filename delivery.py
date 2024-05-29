import csv


class delivery:
    def __init__(self):
        self.delivery_time = 800
        self.file_path = "WGUPS_Distance_Table.csv"
        self.route = []
        self.distances = self._read_distances(self.file_path)

    # The solution might be to add the name of the corresponding addressses to the dictionary
    def _read_distances(self, csv_file):
        distances = {}
        with open(csv_file, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                start_address = row[0].strip()
                distance_values = [float(value) for value in row[1:] if value]
                distances[start_address] = distance_values
        return distances

    def get_distances(self):
        return self.distances

    def _get_distance(self, start_address, end_address):
        return self.distances[start_address][end_address]

    # THIS NEEDS TO BE REDONE

    def deliver(self, route, locations):
        for i in range(len(route)):
            for j in range(len(locations)):
                if route[i] == locations.index(locations[j]):
                    continue
                    print(
                        f"Match found between {route[i]} and {locations.index(locations[j])}"
                    )
                    print(self.distance[i])

    def _get_time(self, distance):
        time = distance / 18
        self.delivery_time += time * 60

    def nearest_neighbor(self, locations):
        visited = [False] * len(locations)
        visited[0] = True
        nearest = None
        self.route.append(locations.index(locations[0]))
        for i in range(len(locations)):
            min_distance = float("inf")
            for j in range(len(locations)):
                if not visited[j]:
                    print(
                        f"Checking distance between {locations[i].delivery_address} and {locations[j].delivery_address}"
                    )
                    distance = self.get_distance(
                        locations[i].delivery_address, locations[j].delivery_address
                    )
                    print(locations[j].delivery_address)
                    if distance < min_distance:
                        min_distance = distance
                        print(min_distance)
                        nearest = j
            visited[nearest] = True
            self.route.append(nearest)
