import hashlib
import time
from flask import Flask
from flask import request
from multiprocessing import Process, Pipe

app = Flask(__name__)

@app.route('/unconfirmed_transaction', methods=['POST'])
def add_unconfirmed_transaction():
    data = request.get_json()
    print(data)

max_nonce = 2**32 # ~4 billion

def proof_of_work(header, difficulty_num):
    target = 2**(256-difficulty_num)

    for nonce in xrange(max_nonce):
        hash_result = hashlib.sha256(str(header)+str(nonce)).hexdigest()

        if long(hash_result, 16) < target:
            print ("Found block hash with nonce: %d" % nonce)
            print ("Hash result: %s" % hash_result)

            return (hash_result, nonce)

def mine():
    while True:
        nonce = 0
        hash_result = ''

        for difficulty_num in xrange(32):
            difficulty = 2**difficulty_num

            print ("")
            print ("Difficulty: %ld (current num %d)" % (difficulty, difficulty_num))
            print ("Starting search")
            start = time.time()

            new_block = 'test block header' + hash_result
            (hash_result, nonce) = proof_of_work(new_block, difficulty_num)
            end = time.time()
            elapsed_time = end-start

        print ("Elapsed time: %.2f seconds" % elapsed_time)

# tester -- just to make sure the above code works. won't be part of the final thing
if __name__ == '__main__':
    p0 = Process(target=mine)
    p0.start()
    p1 = Process(target=app.run(host='0.0.0.0'))
    p1.start()
