{
  startScript = ''
    uwsgi --http :5000 --gevent 1000 --http-websockets --master --wsgi-file main.py --callable app
  '';
}
