class Connection:
    def __init__(db, timeout=60):
        print("new connection created")
        pass

    def write(data):
        print("w")
        pass

    def rewrite(data, by_parameter, key):
        print("rw")
        pass

    def get(by_parameter, key):
        print(f"get request (by_parameter) {key}")
        pass


class DBHandler:
    def __init__(db)
        self.db = db
    

    def connection(**kvargs):
        return Connection(self.db, **kvargs)

