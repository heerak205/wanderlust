def foo(given_string,x,y=True):
    if x>5 and y:
        return given_string
    else:
        return"bob"
string = "robert"
result=foo(string,len(string))*3
