import testinfra

def test_nginx_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed

def test_nginx_running_and_enabled(host):
    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled

def test_http_redirect(host):
    cmd = host.run("curl -I http://localhost")
    assert "301 Moved Permanently" in cmd.stdout

def test_https_accessible(host):
    cmd = host.run("curl -k https://localhost")
    assert "Hello World!" in cmd.stdout
