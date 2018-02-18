import hashlib
import time
from flask import Flask, render_template, request, send_from_directory
from multiprocessing import Process, Pipe
import os
from subprocess import Popen, PIPE

dir_path = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
difficulty_ = 0

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
    temp_process = Popen(["istats", "cpu", "temp"], stdout=PIPE)
    (temp_output, temp_err) = temp_process.communicate()
    temp_exit_code = temp_process.wait()
    fan_process = Popen(["istats", "fan"], stdout=PIPE)
    (fan_output, fan_err) = fan_process.communicate()
    fan_exit_code = fan_process.wait()
    print(fan_output.split(' ')[18])
    return render_template('status.html', cpu=temp_output.split('\xc2\xb0', 1)[0], fan=fan_output.split(' ')[18], diff=difficulty_)

max_nonce = 2**32 # ~4 billion

def proof_of_work(header, difficulty_num):
    target = 2**(256-difficulty_num)

    for nonce in xrange(max_nonce):
        hash_result = hashlib.sha256(str(header)+str(nonce)).hexdigest()

        if long(hash_result, 16) < target:
            print ("Found block hash with nonce: %d" % nonce)
            print ("Hash result: %s" % hash_result)

            return (hash_result, nonce)

def mine(d):
    while True:
        nonce = 0
        hash_result = ''

        for difficulty_num in xrange(32):
            difficulty = 2**difficulty_num

            d = difficulty

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
    p0 = Process(target=mine, args=(difficulty_,))
    p0.start()
    p1 = Process(target=app.run(host='0.0.0.0'))
    p1.start()
