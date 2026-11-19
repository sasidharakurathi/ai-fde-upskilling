import os

with open(".env", "r") as fp:
    lines = fp.readlines()
    for line in lines:
        hash_in_line = line.index("#")
        if hash_in_line:
            line = line[:hash_in_line].strip()
        if line == "\n" or "=" not in line:
            continue
        name, value = line.split("=")
        # print(f"{name=}, {value=}")
        os.environ[name] = value.strip('"')

val = os.environ.get("DEMO_SECRET")
print(val[:3] + "*"*(len(val)-3))