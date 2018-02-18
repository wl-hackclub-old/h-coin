import requests
import json
import os
# class Miner:
#     def __init__():
#
#     def broadcast_block_found(block):
#         print('test')
#



class Propagator:
    def __init__(self):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))

        self.nodes = {}

        with open(self.dir_path + "/nodes.json", "r") as json_file:
            self.data = json.load(json_file)
            self.nodes = self.data

    def my_peers(self):
        return self.nodes

    def get_peers(self):
        for i in self.nodes:
            # print(self.nodes[i])
            try:
                data = requests.get('http://' + self.nodes[i]['address'] + '/my_peers')
                print(data)

            except Exception as e:
                print(e)
