from flask import Flask, render_template, request
import query_on_whoosh
import config
import smtp
import math

#turn this file into a web app
app = Flask(__name__)
app.config.update(dict(JSONIFY_PRETTYPRINT_REGULAR=True))

@app.route("/")
def handle_slash():
    requested_name = request.args.get("name")
    return render_template("index.html", name=requested_name)

@app.route("/test/", strict_slashes=False)
def handle_test():
    input = "abc"
    return test_module.test(input)

@app.route("/query", strict_slashes=False)
def handle_query():
    query_term = request.args.get("q")
    return jsonify(query_on_whoosh.query(query_term))
    return jsonify({"query_term": query_term, "search_results": query_on_whoosh.query(query_term, current_page=page_index)})

@app.route("/query_view", strict_slashes=False)
def handle_query_view():
    query_term = request.args.get("q")
    if not query_term:
        query_term = ""
    page_index_arg = request.args.get("p")
    if not page_index_arg:
        page_index_arg = "1"
    page_index = int(request.args.get("p"))
    query_results = query_on_whoosh.query(query_term, current_page=page_index)
    search_results = query_results[0]
    results_cnt = int(query_results[1])
    page_cnt = math.ceil(results_cnt/10)
    return render_template("query.html", results = query_results, page_cnt=page_cnt)

@app.route("/about", strict_slashes=False)
def handle_about():
    return render_template("about.html")

@app.route("/success", strict_slashes=False)
def handle_request():
    new_date = request.args.get("new_data")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.startls()
    server.login("student.a.cosc381.2020fall@gmail.com", "sjian1@emich.edu", "request " + new_data)
    return render_template("success.html", new_data=new_data)