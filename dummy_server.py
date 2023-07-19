from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Fetch data from the dummy server
    server1_cpu = requests.get('http://localhost:3000/api/cpu').json()['cpuUsage']
    server1_memory = requests.get('http://localhost:3000/api/memory').json()['memoryUsage']
    server2_cpu = requests.get('http://localhost:3000/api/cpu').json()['cpuUsage']
    server2_memory = requests.get('http://localhost:3000/api/memory').json()['memoryUsage']
    server3_cpu = requests.get('http://localhost:3000/api/cpu').json()['cpuUsage']
    server3_memory = requests.get('http://localhost:3000/api/memory').json()['memoryUsage']
    server4_cpu = requests.get('http://localhost:3000/api/cpu').json()['cpuUsage']
    server4_memory = requests.get('http://localhost:3000/api/memory').json()['memoryUsage']
    num_vms1 = requests.get('http://localhost:3000/api/vms').json()['numVMs']
    num_hosted_items1 = requests.get('http://localhost:3000/api/hosted-items').json()['numHostedItems']
    num_vms2 = requests.get('http://localhost:3000/api/vms').json()['numVMs']
    num_hosted_items2 = requests.get('http://localhost:3000/api/hosted-items').json()['numHostedItems']
    num_vms3 = requests.get('http://localhost:3000/api/vms').json()['numVMs']
    num_hosted_items3 = requests.get('http://localhost:3000/api/hosted-items').json()['numHostedItems']
    num_vms4 = requests.get('http://localhost:3000/api/vms').json()['numVMs']
    num_hosted_items4 = requests.get('http://localhost:3000/api/hosted-items').json()['numHostedItems']


    return render_template('dashboard.html',
                           server1Cpu=server1_cpu,
                           server1Memory=server1_memory,
                           server2Cpu=server2_cpu,
                           server2Memory=server2_memory,
                           server3Cpu=server3_cpu,
                           server3Memory=server3_memory,
                           server4Cpu=server4_cpu,
                           server4Memory=server4_memory,
                           numVMs1=num_vms1,
                           numHostedItems1=num_hosted_items1,
                           numVMs2=num_vms2,
                           numHostedItems2=num_hosted_items2,
                           numVMs3=num_vms3,
                           numHostedItems3=num_hosted_items3,
                           numVMs4=num_vms4,
                           numHostedItems4=num_hosted_items4)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
