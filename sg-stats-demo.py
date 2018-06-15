#!/usr/bin/python

import json
import urllib2
import time
import datetime
import base64
import os
import webbrowser


from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

class S(BaseHTTPRequestHandler):

    debug = False

    def httpGet(self, url='', retry=0):
        try:
           # base64string = base64.encodestring('%s:%s' % (self.username, self.password)).replace('\n', '')
            request = urllib2.Request(url)
            #request.add_header("Authorization", "Basic %s" % base64string)
            result = urllib2.urlopen(request)
            data = result.read()
            r = self.jsonChecker(data)
            return r
        except Exception, e:
            if e:
                if hasattr(e, 'code'):
                    print "Error: HTTP GET: " + str(e.code)
            if retry == 3:
                if self.debug == True:
                    print "DEBUG: Tried 3 times could not execute: GET"
                if e:
                    if hasattr(e, 'code'):
                        if self.debug == True:
                            print "DEBUG: HTTP CODE ON: GET - " + str(e.code)
                        return e.code
                    else:
                        return False
            time.sleep(1.0)
            return self.httpGet(url, retry + 1)

    def jsonChecker(self, data=''):
        # checks if its good json and if so return back Python Dictionary
        try:
            checkedData = json.loads(data)
            return checkedData
        except Exception, e:
            return False

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        #json.dumps(self.pullSGStats())
        web = open("index.html", "r").read()
        #print(web)
        self.wfile.write(web)

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write(json.dumps(self.pullSGStats()))
        

    def pullSGStats(self):
        url = "http://localhost:4985/_expvar"
        if self.debug == True:
            print("DEBUG: ", url)

        data = self.httpGet(url)

        if data == False or None:
            now = time.strftime("%Y-%m-%d %H:%M:%S")
            data = now + " error=could not get stats \n"
            self.writeLog(data)
            return False

        if self.debug == True:
            print("DEBUG: ", data)
        data["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")
        return data
        
def run(server_class=HTTPServer, handler_class=S, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv
    webbrowser.open('http://localhost:8000', new=2)
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
