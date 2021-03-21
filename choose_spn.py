def spn(organization):
    a = organization['geometry']['properties']['boundedBy']
    return f'{abs(a[0][0] - a[0][1])},{abs(a[1][0] - a[1][1])}'