from Feature.FeatureCount import FeatureCount
from Feature.Feature import Feature

class LoginRole_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'LoginRole_freq', 'LoginRole')


class LoginRole_country(Feature):
    def __init__(self):
        Feature.__init__(self, 'LoginRole_country', 'LoginRole')

    def __parse__(self, item):
        return item['raw_info']['country']


class LoginRole_osname(Feature):
    def __init__(self):
        Feature.__init__(self, 'LoginRole_osname', 'LoginRole')

    def __parse__(self, item):
        return item['raw_info']['os_name']


class LoginRole_appchannel(Feature):
    def __init__(self):
        Feature.__init__(self, 'LoginRole_appchannel', 'LoginRole')

    def __parse__(self, item):
        return item['raw_info']['app_channel']


class LoginRole_rolelevel(Feature):
    def __init__(self):
        Feature.__init__(self, 'LoginRole_rolelevel', 'LoginRole')

    def __parse__(self, item):
        return item['raw_info']['role_level']


class LoginRole_pixel(Feature):
    def __init__(self):
        Feature.__init__(self, 'LoginRole_pixel', 'LoginRole')

    def __parse__(self, item):
        return float(item['raw_info']['device_height']) * float(item['raw_info']['device_width'])


class LoginRole_logintime(Feature):
    def __init__(self):
        Feature.__init__(self, 'LoginRole_logintime', 'LoginRole')

    def __parse__(self, item):
        return item['raw_info']['login_time']


class LoginRole_clientsource(Feature):
    def __init__(self):
        Feature.__init__(self, 'LoginRole_clientsource', 'LoginRole')

    def __parse__(self, item):
        return item['raw_info']['client_source']


class LoginRole_clienttype(Feature):
    def __init__(self):
        Feature.__init__(self, 'LoginRole_clienttype', 'LoginRole')

    def __parse__(self, item):
        return item['raw_info']['client_type']
