from dotenv import load_dotenv
import os

load_dotenv()

val = os.environ.get("DEMO_SECRET")
print(val[:3] + "*"*(len(val)-3))