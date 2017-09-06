from sylfk import SYLFK
app = SYLFK()
@app.route('/index', methods=['GET'])
def index():
    return '这是一个路由测试页面'
@app.route("/test/js")
def test_js():
   return '<script src="/static/test.js"></script>'
app.run()