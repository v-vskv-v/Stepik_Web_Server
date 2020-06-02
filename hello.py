def WSGIScript(env, start_responce):
    source = env['QUERY_STRING'].split('&')
    start_responce('200 OK', [('Content-Type', 'text/plain')])
    return ''.join([token + '\n' for token in source])
