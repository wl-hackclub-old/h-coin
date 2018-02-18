import hashlib
import time
from flask import Flask, render_template, request, send_from_directory
from multiprocessing import Process, Pipe
import os
from subprocess import Popen, PIPE
from blockchain.blockchain import Blockchain
from blockchain.block import Block

dir_path = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
BLOCKCHAIN = []
PENDING_TX = []

@app.route('/diff')
def get_diff():
    return str(difficulty)

@app.route('/transaction', methods=['POST'])
def add_unconfirmed_transaction():
    data = request.get_json()
    PENDING_TX.append(data)
    print(data)
@app.route('/blockchain/create_genesis', methods=['POST'])
def create_genesis():
    chain = Blockchain(BLOCKCHAIN)
    genesis = chain.create_genesis()
    BLOCKCHAIN.append(genesis)

# create_genesis()

@app.route('/blockchain/index')
def get_previous_index(block):
    l_index = int(block.get_index())
    if l_index >= 1:
        return l_index - 1
    else:
        return l_index
@app.route('/blockchain/hash')
def get_previous_hash(block):
    if block.get_index() == 0:
        return 0
    else:
        return block.get_prev_hash()
@app.route('/blockchain/latest')
def get_latest_block():
    chain = Blockchain(BLOCKCHAIN)
    return chain.get_latest_block()
#@app.route('/blockchain/mined_block')
#def mined_block():

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)
@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)
@app.route('/temp')
def send_temp():
    temp_process = Popen(["istats", "cpu", "temp"], stdout=PIPE)
    (temp_output, temp_err) = temp_process.communicate()
    temp_exit_code = temp_process.wait()
    return temp_output.split('\xc2\xb0', 1)[0]
@app.route('/fan')
def send_fan():
    fan_process = Popen(["istats", "fan"], stdout=PIPE)
    (fan_output, fan_err) = fan_process.communicate()
    fan_exit_code = fan_process.wait()
    fan_output = fan_output.split('speed: ')[1]
    return fan_output.split('RPM')[0]
@app.route('/admin')
def admin():
    return render_template('status.html')

max_nonce = 2**32 # ~4 billion

def proof_of_work(header, difficulty_num):
    target = 2**(256-difficulty_num)

    for nonce in range(max_nonce):
        combined = (str(header) + str(nonce)).encode()
        hash_result = hashlib.sha256(combined).hexdigest()

        if int(hash_result, 16) < target:
            print ("Found block hash with nonce: %d" % nonce)
            print ("Hash result: %s" % hash_result)

            return (hash_result, nonce)

def mine():
    while True:
        nonce = 0
        hash_result = ''

        for difficulty_num in range(32):
            difficulty = 2**difficulty_num

            print ("")
            print ("Difficulty: %ld (current num %d)" % (difficulty, difficulty_num))
            print ("Starting search")
            start = time.time()

            new_block = Block(get_latest_block(), time.time(), get_latest_block(), {"nonce": nonce, "transactions": None}, nonce, difficulty)
            BLOCKCHAIN.append(new_block)
            (hash_result, nonce) = proof_of_work(new_block, difficulty_num)
            end = time.time()
            elapsed_time = end-start

        print ("Elapsed time: %.2f seconds" % elapsed_time)

if __name__ == '__main__':
    p0 = Process(target=mine)
    p0.start()
    p1 = Process(target=app.run(host='0.0.0.0'))
    p1.start()
