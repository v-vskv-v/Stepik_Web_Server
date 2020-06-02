def WSGIScript(env, start_responce):
    source = env[QUERY_STRING].split('&')
    start_responce('200 OK', [('Content-Type', 'test/plain')])
    return [token + '\r\n' for token in source]
