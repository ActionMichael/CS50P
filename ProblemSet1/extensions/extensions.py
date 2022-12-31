require = input("File name: ")
newrequire = require.lower().strip()

def checkpoint(newrequire):
    value = newrequire.split(".")[-1]
    return value

if "." not in newrequire:
    print("application/octet-stream")

elif(checkpoint(newrequire) in ["gif" , "jpg" , "jpeg" , "png"]):
    print("image/"+checkpoint(newrequire))    
elif(checkpoint(newrequire) in ["pdf" , "zip"]):
    print("application/"+checkpoint(newrequire))
elif(checkpoint(newrequire)=="txt"):
    print("text/plain")
else:
    print("application/octet-stream")
