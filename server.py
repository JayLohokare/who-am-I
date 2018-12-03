from flask import Flask, request, redirect


app = Flask(__name__)

@app.route('/search' , methods=['POST', 'GET'])
def search():
    query  = "+".join(request.values.get('id').strip().split(" "))
    print (query)
    return "https://www.google.com/search?q=" + query
    
@app.route('/' , methods=['POST', 'GET'])
def test():
    return "Server is alive"

if __name__ == '__main__':
    app.run(debug=True)