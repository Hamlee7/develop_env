# -*- coding: utf-8 -*-
import sys
from optparse import OptionParser
from http_server import HttpServer

def main(argv):

    try:
        parser = OptionParser()
        parser.add_option("-P", "--Port", dest="Port", default=2777,
                            help="HTTP server listen port")
        (options, args) = parser.parse_args()
        print("Startup Server")
        print("cmd args: %s" % str(options))

        server = HttpServer(options.Port)
        #启动Http server服务，监听端口，blocking
        server.start()

    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
        server.stop()
        print("Exiting Server")
        sys.exit(0)


if __name__ == "__main__":
    main(sys.argv[1:])
