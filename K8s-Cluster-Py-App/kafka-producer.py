from confluent_kafka import Producer
from flask import Flask

# this application will push message to the kafka topic names test.

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        p = Producer({'bootstrap.servers': '10.106.20.185:9092'})
        #since kafka is ClusterIP service, check for the IP when you describe the service
        p.produce('test', key='hello', value='world')
        p.flush(30)
        return('pushed to kafka topic')

    except Exception as e:
        return e

if __name__ == "__main__":
    app.run(host='0.0.0.0')
