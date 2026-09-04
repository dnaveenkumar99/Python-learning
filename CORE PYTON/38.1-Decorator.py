def main():
    str="Pentagon"
    return str
def outer(ptr):
    print("Inside outer")
    def inner():
        print("Inside inner")
        res=ptr()
        ans=res.upper()
        print(ans)
    return inner
ref=outer(main)
ref()