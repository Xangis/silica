from fabric.api import env, local, run, put, get, cd
import datetime

env.hosts = ['xangis@zetacentauri.com:722']
code_dir = '/var/django/'
app_name = 'silica'
db_name = 'silica'
init_name = 'uwsgi.silica'

def test():
    local("./manage.py test")

def pack():
    local('tar czf /tmp/django-' + app_name + '.tgz .')

def deploy():
    pack()
    put('/tmp/django-' + app_name + '.tgz', '/tmp/')
    with cd(code_dir + app_name):
        run('tar xzf /tmp/django-' + app_name +'.tgz')
        run('rm /tmp/django-' + app_name + '.tgz')
        run('sudo service ' + init_name + ' restart')
    local('rm /tmp/django-' + app_name + '.tgz')

def getdb():
    run('sudo -u postgres pg_dump ' + db_name + ' > /tmp/' + db_name + '.sql')
    get('/tmp/' + db_name + '.sql', './' + db_name + '.sql')
    local('./manage.py reset')
    local('psql ' + db_name + ' < ' + db_name + '.sql')

def getcode():
    local('mkdir -p ../bak')
    local('tar czf ../bak/' + app_name + '_' + str(datetime.date.today()) + '.tgz .')
    with cd(code_dir + app_name):
        run('tar czf /tmp/django-' + app_name + '.tgz . --exclude=images')
    get('/tmp/django-' + app_name + '.tgz', './django-' + app_name + '.tgz')
    run('rm /tmp/django-' + app_name + '.tgz')
    local('tar xzf ./django-' + app_name + '.tgz')
    local('rm ./django-' + app_name + '.tgz')
