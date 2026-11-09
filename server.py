# FIZ Game — сынып желісінде ашуға арналған қарапайым сервер.
# Компьютер мен телефондар бір Wi-Fi-да болса, телефондар QR арқылы ойынға қосылады.
import http.server, socket, socketserver, sys, os, webbrowser, threading

PORT = 8080
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        return s.getsockname()[0]
    except OSError:
        return '127.0.0.1'
    finally:
        s.close()

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

class Server(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True

ip = lan_ip()
url = f'http://{ip}:{PORT}/'
with Server(('0.0.0.0', PORT), Handler) as srv:
    print('FIZ Game іске қосылды')
    print('Компьютерде:  ', url)
    print('Телефондар осы Wi-Fi желісіне қосылуы керек.')
    print('Тоқтату үшін осы терезені жабыңыз.')
    threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    srv.serve_forever()
