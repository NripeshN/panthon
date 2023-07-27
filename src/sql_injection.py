class SQLInjection:
    def __init__(self, db):
        self.db = db  # a hypothetical database object

    def simulate_attack(self, payload):
        # In a real scenario, the payload would be a malicious SQL query.
        # In this simulation, we simply pass it to the database's query method.
        try:
            result = self.db.query(payload)
            return result
        except Exception as e:
            print(f"Exception occurred while querying the database: {e}")
