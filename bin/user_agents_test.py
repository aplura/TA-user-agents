import os

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_FILE = os.path.abspath(os.path.join(ROOT_DIR, 'uap-core', 'regexes.yaml'))
os.environ['UA_PARSER_YAML'] = DATA_FILE

from ua_parser import user_agent_parser

if __name__ == '__main__':
    http_user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.4; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30'
    results = user_agent_parser.Parse(http_user_agent)
    print(results)
