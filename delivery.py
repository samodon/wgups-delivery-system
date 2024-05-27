import numpy as np
import pandas


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
        # print(self.df.at[row[0], end_address])
        return self.df.at[row[0], end_address]

    def _get_time(self, distance):
        time = distance / 18
        self.time = (time * 60) + self.time
        return self.time

    def nearest_neighbor(self, start_address):
        pass
