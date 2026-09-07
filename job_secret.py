import os

secret = os.environ.get("SECRET_API_TOKEN")

if secret:
    print("Le secret est bien accessible")
else:
    print("Le secret n'est pas accessible")