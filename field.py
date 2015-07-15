from ingrex import Intel, Utils

def main():
    "main function"
    field = {
        'minLngE6': 166071535,
        'maxLngE6': 166793004,
        'minLatE6': 39741368,
        'maxLatE6': 40175495,
    }
    with open('cookies') as cookies:
        cookies = cookies.read().strip()

    minxtile, maxytile = Utils.calc_tile(field['minLngE6']/1E6, field['minLatE6']/1E6, 15)
    maxxtile, minytile = Utils.calc_tile(field['maxLngE6']/1E6, field['maxLatE6']/1E6, 15)
    for xtile in range(minxtile, maxxtile + 1):
        for ytile in range(minytile, maxytile + 1):
            tilekey = '15_{}_{}_8_8_25'.format(xtile, ytile)
            intel = Intel(cookies, field)
            result = intel.fetch_map([tilekey])
            entities = result['map'][tilekey]['gameEntities']
            for entity in entities:
                if entity[0].endswith('.9'):
                    print(entity)

if __name__ == '__main__':
    main()
