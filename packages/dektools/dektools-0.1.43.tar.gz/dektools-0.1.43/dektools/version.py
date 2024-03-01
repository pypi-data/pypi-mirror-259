import re

version_pattern = '[0-9]+.[0-9]+.[0-9]+'


def version_to_tuple(version, sep='.'):
    array = []
    for x in version.split(sep):
        try:
            x = int(x)
        except ValueError:
            pass
        array.append(x)
    return tuple(array)


def version_digits(version):
    return re.search(version_pattern, version).group()


def version_is_pure(version):
    span = re.search(version_pattern, version).span()[-1]
    return not version[span:]


def version_sorted(versions, reverse=False):
    keys = {x: version_to_tuple(x) for x in versions}
    return sorted(keys, key=lambda x: keys[x], reverse=reverse)
