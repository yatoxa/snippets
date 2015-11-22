from itertools import zip_longest


def get_iterator_by_chunk(iter_obj, chunk):
    return zip_longest(*([iter(iter_obj)] * chunk))
