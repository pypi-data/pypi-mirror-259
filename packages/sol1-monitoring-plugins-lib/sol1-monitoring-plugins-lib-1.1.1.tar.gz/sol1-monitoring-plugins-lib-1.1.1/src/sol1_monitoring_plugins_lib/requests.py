import os

def initRequestsCache(cache_file, expire_after = 30):
    """Initalize requests cache for monitoring checks. Cleans up stale cache entries and 
    the same cache file can be access by multiple check at the same time.

    Args:
        cache_file (str): full path to cache file
        expire_after (int, optional): seconds till the cache expires. Defaults to 30.

    Returns:
        tuple: (bool, str) the boolan value is success/failure, the string is the message which can be logged and/or passed to plugin output
    """    
    try:
        import requests_cache
        if os.path.isfile(cache_file):
            if not os.access(cache_file, os.W_OK):
                return (False, f"Permissions error, unable to write to requests cache file ({cache_file})")

        backend = requests_cache.SQLiteCache(cache_file, check_same_thread=False)
        requests_cache.install_cache(cache_file, backend=backend, expire_after=expire_after)
        requests_cache.patcher.remove_expired_responses()
        return (True, f'Successfully initalized requests cache file ({cache_file}) with age ({expire_after})')
    except Exception as e:
        return (False, f'Error initalizing requests cache file ({cache_file}): {e}')