from bhfutils.scutils.log_factory import LogFactory


class ProxyRotateMiddleware(object):
    def __init__(self, settings):
        self.setup(settings)
        self.proxies = settings.get('PROXIES')
        self.proxy_queue = self.get_proxy()

    def get_proxy(self):
        while self.proxies:
            for proxy in self.proxies:
                yield proxy
        raise LookupError('Proxies not found. Set PROXIES in settings! Use format [http://user:password@ip:port] for proxies.')

    def setup(self, settings):
        '''
        Does the actual setup of the middleware
        '''
        # set up the default sc logger
        my_level = settings.get('SC_LOG_LEVEL', 'INFO')
        my_name = settings.get('SC_LOGGER_NAME', 'sc-logger')
        my_output = settings.get('SC_LOG_STDOUT', True)
        my_json = settings.get('SC_LOG_JSON', False)
        my_dir = settings.get('SC_LOG_DIR', 'logs')
        my_bytes = settings.get('SC_LOG_MAX_BYTES', '10MB')
        my_file = settings.get('SC_LOG_FILE', 'main.log')
        my_backups = settings.get('SC_LOG_BACKUPS', 5)

        self.logger = LogFactory.get_instance(json=my_json,
                                         name=my_name,
                                         stdout=my_output,
                                         level=my_level,
                                         dir=my_dir,
                                         file=my_file,
                                         bytes=my_bytes,
                                         backups=my_backups)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_spider_output(self, response, result, spider):
        '''
        Ensures the proxy from the response is passed
        when response status code is 429.
        
        Usage: 

        settings.py ->

        ...
        PROXIES = ['http://127.0.0.1:8080']

        ...

        SPIDER_MIDDLEWARES = {
            ...
            'bhfutils.crawler.proxy_rotate.ProxyRotateMiddleware': 100
        }
        '''
        self.logger.debug("processing proxy rotate middleware")
        if response.status == 429:
            self.logger.debug("proxy rotate required")
            meta = response.request.meta.copy()
            meta['proxy'] = next(self.proxy_queue)
            yield response.request.replace(meta=meta)
        else:
            for x in result:
                yield x
