def preproc_location(hiking_data):
    for record in hiking_data:
        for location in record.locations:
            location.latitude = round(location.latitude, 4)
            location.longitude = round(location.longitude, 4)
    return hiking_data
