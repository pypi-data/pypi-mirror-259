import json

class RequestParser():
    def __init__(self, **kargs):
        self.raw_request = kargs.get("raw_request","")
        self.headers = getHeaders(self.raw_request)
        self.body = getBody(self.raw_request, self.headers)
        self.param = getParameter(self.raw_request)
        self.path = getPath(self.raw_request)

def getHeaders(raw_request):
    data = raw_request.split('\n\n')
    data =  data[0].split("\n")[1:]
    headers = {}
    for header in data:
        header_key = header.split(":")[0]
        header_value = header.replace(f"{header_key}: ","")
        headers.update({header_key: header_value})
    return headers

def getRawBody(raw_request):
    data = raw_request.split("\n\n")
    body = raw_request.replace(f"{data[0]}\n\n", "")
    return body

def getBody(raw_request, headers):
    try:
        # data = raw_request.split("\n\n")
        body = getRawBody(raw_request)
        if "json" in headers['Content-Type'].lower():
            return json.loads(body)
        elif "multipart/form-data".lower() in headers['Content-Type'].lower():
            return readMutipartRequest(raw_request)
        else:
            return body
    except:
        pass
    
def getParameter(raw_request):
    data = raw_request.split('\n\n')
    data =  data[0].split("\n")[0]
    if "?" in data:
        param_raw = data.split("?",1)[1].split(" ",1)[0]
        param_arr = param_raw.split("&")
        params = {}
        for data in param_arr:
            data = data.split("=")
            if len(data) > 1:
                params[data[0]] = str(data[1])
            else:
                params[data[0]] = ""
        return params
    return None

def readMutipartRequest(raw_request):
    headers = getHeaders(raw_request)
    content_type = headers.get("Content-Type")
    if "multipart/form-data" in content_type.lower():
        boundary = content_type.split(";")[1].replace("boundary=","").replace(" ","")
        raw_body = getRawBody(raw_request)
        raw_body = raw_body.split(f"--{boundary}")
        multipart_body = {}
        for i in range(1, len(raw_body)-1):
            data = raw_body[i]
            if data != '':
                content_desposition = data.split("\n")[1].split(";")
                for element in content_desposition:
                    if " name=".lower() in element.lower():
                        name = element.lower().replace("name","").replace("\"","").replace(" ","").replace("=","")
                content = data.split("\n")
                content = content[:-1][-1]
                multipart_body[name] = content
        return multipart_body
    return None      
            
    
def getPath(raw_request):
    data = raw_request.split('\n\n')
    headers =  data[0].split("\n")
    return headers[0].split(" ")[1].split("?",1)[0]
    
