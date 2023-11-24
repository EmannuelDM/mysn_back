import json
from db.hashing import Hash
from db.database import get_db
from users.models import DbUser


def read_json_users(file_path):
  with open(file_path, 'r') as f:
    users_json = json.load(f)
  users = []
  for user_json in users_json:
    user = DbUser(
      username=user_json["email"],
      password=Hash.bcrypt(user_json["email"]),
      **user_json)
    users.append(user)
  return users

def save_users_to_db(users):
  session = next(get_db())

  for user in users:
    session.add(user)

  session.commit()
  session.close()
