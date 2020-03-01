"""Create a simple REST API."""
import json


class RestAPI:
    """A simple API for IOU."""

    def __init__(self, database: None) -> None:
        """Initialize."""
        self.database = {user["name"]: user for user in database["users"]}

    def get(self, url: str, payload=None) -> None:
        """Get users."""
        if url != "/users":
            raise ValueError("API not exists.")
        if not payload:
            return json.dumps({"users": [data for user, data in self.database.items()]})
        payload = json.loads(payload)
        return json.dumps({"users": self.get_users(payload["users"])})

    def post(self, url: str, payload=None) -> None:
        """Post users or IOUs."""
        payload = json.loads(payload)
        if url == "/add":
            user = {"name": payload["user"], "owes": {}, "owed_by": {}, "balance": 0.0}
            self.database[payload["user"]] = user
            return json.dumps(user)
        if url == "/iou":
            lender, borrower = payload["lender"], payload["borrower"]
            new_balance = (
                payload["amount"]
                + self.database[lender]["owed_by"].setdefault(borrower, 0)
                - self.database[lender]["owes"].setdefault(borrower, 0)
            )
            self.database[lender]["balance"] += payload["amount"]
            self.database[borrower]["balance"] -= payload["amount"]
            self.cleanup(lender, borrower)
            if new_balance > 0:
                self.database[lender]["owed_by"][borrower] = new_balance
                self.database[borrower]["owes"][lender] = new_balance
            if new_balance < 0:
                self.database[lender]["owes"][borrower] = -new_balance
                self.database[borrower]["owed_by"][lender] = -new_balance
            return json.dumps({"users": self.get_users(sorted([lender, borrower]))})
        raise ValueError("API not exists.")

    def get_users(self, users):
        """Return a list of users' balances."""
        return [self.database[user] for user in users]

    def cleanup(self, lender, borrower):
        """Delete old data before updating."""
        self.database[lender]["owes"].pop(borrower, None)
        self.database[lender]["owed_by"].pop(borrower, None)
        self.database[borrower]["owes"].pop(lender, None)
        self.database[borrower]["owed_by"].pop(lender, None)
