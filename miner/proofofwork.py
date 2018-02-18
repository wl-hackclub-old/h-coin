import hashlib
import time
from flask import Flask, render_template, request, send_from_directory
from multiprocessing import Process, Pipe
import os
from subprocess import Popen, PIPE

dir_path = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)

@app.route('/unconfirmed_transaction', methods=['POST'])
def add_unconfirmed_transaction():
    data = request.get_json()
    print(data)
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)
@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)
@app.route('/admin')
def admin():
    process = Popen(["istats", "cpu", "temp"], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    return render_template('status.html', cpu=output.split('\xc2\xb0', 1)[0])

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
