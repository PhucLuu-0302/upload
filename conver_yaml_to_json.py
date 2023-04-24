# Import thư viện
import ruamel.yaml as yaml
import json

if __name__ == "__main__":
    with open("user.yaml", "r") as a:
        user_yaml = yaml.safe_load(a)

    print(user_yaml)
    print(type(user_yaml))

    user_json = json.dumps(user_yaml, default=str, indent=4)
    print(user_json)
    print(type(user_json))

    file = open("user1.json","w")
    file.write(user_json)
    file.close()
