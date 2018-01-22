class Urlparameterhandleutil:

def analyze_url_paramters(self, urlParamters):
    paramters = urlParamters.split('&')
    for paramter in paramters:
        paramterMap = paramter.split('=')
        paramterValue = paramterMap[1]
    return paramterValue