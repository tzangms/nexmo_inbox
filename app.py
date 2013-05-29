from flask import Flask, request
app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"

@app.route("callback")
def callback():
    type = request.args.get('type')
    to = request.args.get('to')
    msisdn = request.args.get('msisdn')
    network_code = request.args.get('network-code')
    message_id = request.args.get('messageId')
    message_timestamp = request.args.get('message-timestamp')
    text = request.args.get('text')
    concat = request.args.get('concat')

    if concat:
        concat_ref = request.args.get('concat-ref')
        concat_total = request.args.get('concat-total')
        concat_part = request.args.get('concat-part')


    if type == 'binary':
        data = request.args.get('data')
        udh = request.args.get('udh')

    return "OK"

if __name__ == "__main__":
    app.debug = True
    app.run()
