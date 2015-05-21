import httpagentparser,numbers,itertools
def flatten(value, accum):
    '''Function for flattening IPViking JSON to Splunk fields. Does not convert 
    NoneType values.'''
    output = {}
    if isinstance(value, (basestring, numbers.Number)):
        output[accum] = value
    elif isinstance(value, dict):
        for subk, subv in value.iteritems():
            values = flatten(subv, '')
            for k, v in values.iteritems():
                output['.'.join(itertools.ifilter(lambda x: x, [accum, subk, k]))] = v
    elif isinstance(value, list):
        for num, subv in enumerate(value):
            values = flatten(subv, '')
            for k, v in values.iteritems():
                output['.'.join(itertools.ifilter(lambda x: x, [accum, str(num), k]))] = v
    return output

#
# Main routine - basically it's the standard python recipe for handling
# Splunk lookups
#
if __name__ == '__main__':
	http_user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.4; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30'
	results = []
	results = httpagentparser.detect(http_user_agent)

	# flatten it
	flattened = flatten(results, '')
	print flattened    

