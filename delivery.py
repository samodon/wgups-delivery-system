import csv


class delivery:
    def __init__(self):
        self.delivery_time = 800
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

    # THIS NEEDS TO BE REDONE

    def deliver(self, route, locations):
        for index in route:
            if index == 0:
                self._get_time(0)
            else:
                distance = self.get_distances(
                    locations[route[index - 1]].delivery_address,
                    locations[route[index]].delivery_address,
                )
                print()
                self._get_time(distance)
                hours = int(self.delivery_time // 100)
                minutes = int(self.delivery_time % 100)
                print(f"{hours}:{minutes}")
                # print(distance)

    # THIS NEEDS TO BE REDONE
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
                    distance = self.get_distances(
                        locations[i].delivery_address, locations[j].delivery_address
                    )
                    if distance < min_distance:
                        min_distance = distance
                        nearest = j
            visited[nearest] = True
            self.route.append(nearest)
