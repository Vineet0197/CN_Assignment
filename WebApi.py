import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Computer Networks Assignment</h1>" \
           "<h2>TOPIC:- Implementation of HTTP Protocol using Wireshark</h2>" \
           "<p>Capture and Analyze packet through Wireshark</p>" \
           "<p>By Vineet Aggarwal (BITS ID.:- 2020MT13016)</p>"


app.run()
