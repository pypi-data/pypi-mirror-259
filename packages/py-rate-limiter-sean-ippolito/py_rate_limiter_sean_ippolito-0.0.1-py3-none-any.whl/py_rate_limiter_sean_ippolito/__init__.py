from db import client
from routes import server

print(client.list_database_names())


if __name__ == '__main__':
    server.run(debug=True)