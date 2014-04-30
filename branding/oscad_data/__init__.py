
def load_data(name):
    import pkg_resources 
    return load_file(pkg_resources.resource_stream(__name__, 'data/%s.yml' % name))


def load_file(fileobj):
    import yaml
    return yaml.safe_load(fileobj)

def update_oslic_data():
    import oscad_data

    oscad_data.licenses = load_data('licenses')
    oscad_data.osuc = load_data('osuc')
    oscad_data.lsuc = load_data('lsuc')

    oscad_data.valid_licenses = sorted(oscad_data.licenses.keys())

    oscad_data.valid_inputs['license'] = oscad_data.valid_licenses
