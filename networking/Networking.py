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

    # def get_peers(self):
    #     for i in self.nodes:
    #         # print(self.nodes[i])
    #         try:
    #             data = requests.get('http://' + self.nodes[i]['address'] + '/my_peers')
    #             json = json.load(data)
    #             for i2 in json
    #                 if data[i2]['address'] in json
    #
    #         except Exception as e:
    #             print(e)
    def propagate_unverified_transaction(self, trans):
        print(trans)
        for i in self.nodes:
            data = requests.post('http://' + self.nodes[i]['address'] + '/transaction', json=trans)
            print(data.text)
    def get_bal(self, address):
        print(address)
        data = requests.post('http://' + self.nodes['0']["address"] + '/get_bal', data=address)
        return data.data
    def get_latest_block(self):
        data = requests.post('http://' + self.nodes['0']['address'] + '/blockchain/latest')
        return data.text
    def append_blockchain(self, block):
        data = requests.post('http://' + self.nodes['0']['address'] + '/blockchain/append', json=block)
        return data
