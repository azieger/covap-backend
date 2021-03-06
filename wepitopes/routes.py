def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('api_get_fields', '/api/get-fields')
    config.add_route('api_get_fields_limit', '/api/get-fields/limit/{limit}')
    config.add_route('api_get_collection_fields_limit', '/api/get-fields/{collection}/limit/{limit}')
    config.add_route('api_get_data', '/api/get-data')
    config.add_route('home', '/')
