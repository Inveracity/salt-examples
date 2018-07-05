#!pyobjects

minion_grains = __salt__['grains.items']()

Pkg.installed("nginx")

Service.running("nginx",
                enable  = True,
                require = Pkg("nginx"))

File.managed("/etc/nginx/sites-available/mysite.conf",
          owner  = 'root',
          group  = 'root',
          mode   = '0444',
          source = 'salt://nginx/mysite.conf')

File.managed("/usr/share/nginx/html/index.html",
          owner    = 'root',
          group    = 'root',
          mode     = '0444',
          source   = 'salt://nginx/index.html',
          template = 'jinja',
          context  = {'grains':minion_grains})


File.symlink("/etc/nginx/sites-enabled/mysite.conf",
            target='/etc/nginx/sites-available/mysite.conf')

Cmd.run('service nginx restart')

# salt 'minion' state.show_sls nginx --out=yaml
