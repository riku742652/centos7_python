from xmlrpc.client import ServerProxy

proxy = ServerProxy("http://localhost:5000/api")
# print(client.new_post("sample"))
print(proxy.flaskr.newPost("aaa"))
