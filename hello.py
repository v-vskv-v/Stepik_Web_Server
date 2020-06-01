def application(env, start_responce):
    source = env[QUERY_STRING][2:]
    start_responce('200 OK', [('Content-Type', 'test/plain')])
    return bytes(source.replace('&', '\n'))
