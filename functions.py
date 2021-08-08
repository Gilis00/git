'''All functions will be here'''
import yaml

'''Data Functions'''
def extract(file):
    with open(file) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        n = []
        Pn = []
        EPn = []
        for x in data['independent_variables'][0]['values']:
            n.append((x['high'] + x['low'])/2)
        for y in data['dependent_variables'][0]['values']:
            Pn.append(y['value'])
            try:
                EPn.append(y['errors'][1]['symerror'])
            except:
                x = max(y['errors'][1]['asymerror']['plus'],y['errors'][1]['asymerror']['minus'])
                EPn.append(x)
    return (n, Pn, EPn)