if __name__ == "__main__":

    import requests
    import hashlib
    import sys

    enteredpw = sys.argv[1]

    pw_hashed = hashlib.sha1(bytes(enteredpw, "utf8"))
    pw_hex = pw_hashed.hexdigest().upper()
    pw_5dig = pw_hex[:5]

    hashes = []
    count = []

    url1 = "https://api.pwnedpasswords.com/range/"
    url = url1 + pw_5dig

    r = requests.get(url)

    for line in r.text.splitlines():
        hashes.append(pw_5dig + line.split(":",1)[0])

    for line in r.text.splitlines():
        count.append(line.split(":", 1)[1])


    if pw_hex in hashes:
        index = hashes.index(pw_hex)
        timesfound = count[index]
        print("Hash:%s, %s occurences" % (str(pw_hex), str(timesfound)))



