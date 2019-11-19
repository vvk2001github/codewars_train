import re

def domain_name(url):

    result = re.findall(r"(?:\/\/|[^\/]+)", url)
    if('http:' in result):
        result.remove('http:')
    if('https:' in result):
        result.remove('https:')
    if('//' in result):
        result.remove('//')
    result = result[0].split('.')
    if result[0] == 'www':
        result.remove('www')
    return result[0]

if __name__ == '__main__':
    print(domain_name('https://www.google.co.jp/abc'))