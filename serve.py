"""
HTTP POST "/" 

Once receive the POST request, your server program should create a 
separate process for running "stress_cpu.py" (attached below). 
"stress_cpu.py" runs an intensive computation loop to stress the
CPUs to 100% utilization. This script is for triggering the auto 
scaling policy that you will setup later. 

In Python, use subprocess.Popen() to create a separate process so 
that your HTTP server is non-blocking. That is to say, after 
receiving a POST request for stressing the CPU on your EC2 
instance, your server program should still be able to handle 
further POST/GET requests.

HTTP GET "/"

Your server program should return the private IP address of the 
EC2 instance. In Python, you can import socket and use 
socket.gethostname() to get the IP address. 
"""

from flask import Flask,   request
import socket
import subprocess
app = Flask(__name__)



@app.route('/', methods = ['POST'])
def seeding():
    subprocess.Popen(["python3" ,"stress_cpu.py"])
    return ""

@app.route('/', methods = ['GET'])
def get_ip():
    return socket.gethostname()


@app.route('/health')
def check_health():
    try:
        with open(seed_file,"r") as f:
            return ""
    except:
        return "Health check failed"


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
