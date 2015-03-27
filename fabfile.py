from fabric.api import local
import urllib

local_absolute_path = '/Users/Tom/projects/land-records/repo/scripts/'
server_absolute_path = '/apps/land-records/repo/scripts'

server_scraper_path = '/scrapers/land-records'

s3_path = 's3://lensnola/land-records/'
server_name = '162.243.152.217'
server_name = 'vault.thelensnola.org'


def scrape():
    local('scp %sscrape.py '
          'tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))


def cleanup():
    local('scp %sCleanup.py '
          'tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))


def app_config():
    local('scp %sapp_config.py '
          'tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))


def init():
    local('scp %sinitialize.py '
          'tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))


def app():
    local('scp %sapp.py '
          'tom@%s:%s' % (
            local_absolute_path,
            server_name,
            server_absolute_path))


def run_trifecta():
    local('python databasedeleter.py')
    local('python databasemaker.py')
    local('python initialize.py')


def four():
    local('scp %sapp.py '
          'tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sinitialize.py '
          'tom@%s:%s' % (
            local_absolute_path,
            server_name,
            server_absolute_path))
    local('scp %sdatabasedeleter.py '
          'tom@%s:%s' % (
            local_absolute_path,
            server_name,
            server_absolute_path))
    local('scp %sdatabasemaker.py '
          'tom@%s:%s' % (
            local_absolute_path,
            server_name,
            server_absolute_path))


def templates():
    local('scp %stemplates/404.html '
          'tom@%s:%s/templates' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %stemplates/banner.html   tom@%s:%s/templates' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %stemplates/dashboard.html   tom@%s:%s/templates' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %stemplates/footer.html   tom@%s:%s/templates' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %stemplates/head.html   tom@%s:%s/templates' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %stemplates/index.html       tom@%s:%s/templates' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %stemplates/js.html   tom@%s:%s/templates' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %stemplates/sale.html        tom@%s:%s/templates' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %stemplates/search.html      tom@%s:%s/templates' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %stemplates/searchArea.html   tom@%s:%s/templates' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %stemplates/table.html       tom@%s:%s/templates' % (local_absolute_path, server_name, server_absolute_path))


def scripts():
    local('scp %sapp.py                 tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sbackup.sh              tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %scheck_assessor_urls.py tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sCleanup.py             tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sdatabasedeleter.py     tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sdatabasemaker.py       tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sfabfile.py             tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %sgeocoder-commands.txt  tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sgmail.py               tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sinitialize.py          tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %skey.json          tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %sneighborhoods-topo.json tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %sneighborhoods.json     tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %sphantomjs              tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %spythonEmail.py            tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %srequirements.txt       tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sscrape.sh              tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sscrape.py              tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %sscreen.js              tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sscrape-mechanize.py             tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %ssquares-topo.json      tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %ssquares.json           tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %stserver.py             tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %stwitter.py             tom@%s:%s' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp /Users/Tom/projects/land-records/repo/.gitignore             tom@%s:%s' % (server_name, server_absolute_path))


def geographicData():
    # Neighborhoods
    local('scp /Users/Tom/projects/land-records/repo/data/neighborhoods/102682.prj tom@%s:/apps/land-records/repo/data/neighborhoods' % (server_name))
    local('scp /Users/Tom/projects/land-records/repo/data/neighborhoods/Neighborhood_Statistical_Areas.dbf tom@%s:/apps/land-records/repo/data/neighborhoods' % (server_name))
    local('scp /Users/Tom/projects/land-records/repo/data/neighborhoods/Neighborhood_Statistical_Areas.json tom@%s:/apps/land-records/repo/data/neighborhoods' % (server_name))
    local('scp /Users/Tom/projects/land-records/repo/data/neighborhoods/Neighborhood_Statistical_Areas.prj tom@%s:/apps/land-records/repo/data/neighborhoods' % (server_name))
    local('scp /Users/Tom/projects/land-records/repo/data/neighborhoods/Neighborhood_Statistical_Areas.sbn tom@%s:/apps/land-records/repo/data/neighborhoods' % (server_name))
    local('scp /Users/Tom/projects/land-records/repo/data/neighborhoods/Neighborhood_Statistical_Areas.sbx tom@%s:/apps/land-records/repo/data/neighborhoods' % (server_name))
    local('scp /Users/Tom/projects/land-records/repo/data/neighborhoods/Neighborhood_Statistical_Areas.shp tom@%s:/apps/land-records/repo/data/neighborhoods' % (server_name))
    local('scp /Users/Tom/projects/land-records/repo/data/neighborhoods/Neighborhood_Statistical_Areas.shp.xml tom@%s:/apps/land-records/repo/data/neighborhoods' % (server_name))
    local('scp /Users/Tom/projects/land-records/repo/data/neighborhoods/Neighborhood_Statistical_Areas.shx tom@%s:/apps/land-records/repo/data/neighborhoods' % (server_name))

    # Squares
    local('scp /Users/Tom/projects/land-records/repo/data/squares/102682.prj tom@%s:/apps/land-records/repo/data/squares' % (server_name))
    local('scp /Users/Tom/projects/land-records/repo/data/squares/NOLA_Squares_20140221.dbf tom@%s:/apps/land-records/repo/data/squares' % (server_name))
    local('scp /Users/Tom/projects/land-records/repo/data/squares/NOLA_Squares_20140221.prj tom@%s:/apps/land-records/repo/data/squares' % (server_name))
    local('scp /Users/Tom/projects/land-records/repo/data/squares/NOLA_Squares_20140221.sbn tom@%s:/apps/land-records/repo/data/squares' % (server_name))
    local('scp /Users/Tom/projects/land-records/repo/data/squares/NOLA_Squares_20140221.sbx tom@%s:/apps/land-records/repo/data/squares' % (server_name))
    local('scp /Users/Tom/projects/land-records/repo/data/squares/NOLA_Squares_20140221.shp tom@%s:/apps/land-records/repo/data/squares' % (server_name))
    local('scp /Users/Tom/projects/land-records/repo/data/squares/NOLA_Squares_20140221.shp.xml tom@%s:/apps/land-records/repo/data/squares' % (server_name))
    local('scp /Users/Tom/projects/land-records/repo/data/squares/NOLA_Squares_20140221.shx tom@%s:/apps/land-records/repo/data/squares' % (server_name))


def css():
    # S3
    # local('aws s3 cp %sstatic/css/font-awesome.css                %scss/font-awesome.css --acl public-read' % (local_absolute_path, s3_path))
    # local('aws s3 cp %sstatic/css/foundation.css                  %scss/foundation.css --acl public-read' % (local_absolute_path, s3_path))
    # local('aws s3 cp %sstatic/css/foundation.min.css              %scss/foundation.min.css --acl public-read' % (local_absolute_path, s3_path))
    # local('aws s3 cp %sstatic/css/jquery-ui-1.9.2.custom.css      %scss/jquery-ui-1.9.2.custom.css --acl public-read' % (local_absolute_path, s3_path))
    # local('aws s3 cp %sstatic/css/jquery-ui.css                   %scss/jquery-ui.css --acl public-read' % (local_absolute_path, s3_path))
    # local('aws s3 cp %sstatic/css/jquery.tablesorter.pager.css    %scss/jquery.tablesorter.pager.css --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/lens.css                        %scss/lens.css --acl public-read' % (local_absolute_path, s3_path))
    # local('aws s3 cp %sstatic/css/lenstablesorter.css             %scss/lenstablesorter.css --acl public-read' % (local_absolute_path, s3_path))
    # local('aws s3 cp %sstatic/css/mapbox.css                      %scss/mapbox.css --acl public-read' % (local_absolute_path, s3_path))
    # local('aws s3 cp %sstatic/css/tablesorter.css                 %scss/tablesorter.css --acl public-read' % (local_absolute_path, s3_path))
    # local('aws s3 cp %sstatic/css/theme.blue.css                  %scss/theme.blue.css --acl public-read' % (local_absolute_path, s3_path))
    
    #Server
    # local('scp %sstatic/css/font-awesome.css              tom@%s:%s/static/css' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %sstatic/css/foundation.css                tom@%s:%s/static/css' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %sstatic/css/foundation.min.css            tom@%s:%s/static/css' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %sstatic/css/jquery-ui-1.9.2.custom.css    tom@%s:%s/static/css' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %sstatic/css/jquery-ui.css                 tom@%s:%s/static/css' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %sstatic/css/jquery.tablesorter.pager.css  tom@%s:%s/static/css' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sstatic/css/lens.css                        tom@%s:%s/static/css' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %sstatic/css/lenstablesorter.css           tom@%s:%s/static/css' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %sstatic/css/mapbox.css                    tom@%s:%s/static/css' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %sstatic/css/tablesorter.css               tom@%s:%s/static/css' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %sstatic/css/theme.blue.css                tom@%s:%s/static/css' % (local_absolute_path, server_name, server_absolute_path))


def images():
    # S3
    local('aws s3 cp %sstatic/css/images/ajax-loader.gif                      %scss/images/ajax-loader.gif --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/black-asc.gif                        %scss/images/black-asc.gif --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/black-desc.gif                       %scss/images/black-desc.gif --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/black-unsorted.gif                   %scss/images/black-unsorted.gif --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/favicon.ico                            %scss/images/favicon.ico --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/first.png                            %scss/images/first.png --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/icons-000000.png                     %scss/images/icons-000000.png --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/icons-000000@2x.png                  %scss/images/icons-000000@2x.png --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/info-i.png                           %scss/images/info-i.png --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/last.png                             %scss/images/last.png --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/lens-logo-retina.png                   %scss/images/lens-logo-retina.png --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/lens-logo-magnifying-glass-only.png    %scss/images/lens-logo-magnifying-glass-only.png --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/next.png                             %scss/images/next.png --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/prev.png                             %scss/images/prev.png --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/ui-bg_flat_75_ffffff_40x100.png      %scss/images/ui-bg_flat_75_ffffff_40x100.png --acl public-read' % (local_absolute_path, s3_path))

    # Server
    local('scp %sstatic/css/images/ajax-loader.gif '
          'tom@%s:%s/static/css/images' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sstatic/css/images/black-asc.gif '
          'tom@%s:%s/static/css/images' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sstatic/css/images/black-desc.gif '
          'tom@%s:%s/static/css/images' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sstatic/css/images/black-unsorted.gif                 tom@%s:%s/static/css/images' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sstatic/css/images/favicon.ico                          tom@%s:%s/static/css/images' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sstatic/css/images/first.png                          tom@%s:%s/static/css/images' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sstatic/css/images/icons-000000.png                   tom@%s:%s/static/css/images' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sstatic/css/images/icons-000000@2x.png                tom@%s:%s/static/css/images' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sstatic/css/images/info-i.png                         tom@%s:%s/static/css/images' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sstatic/css/images/last.png                           tom@%s:%s/static/css/images' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sstatic/css/images/lens-logo-retina.png                 tom@%s:%s/static/css/images' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sstatic/css/images/lens-logo-magnifying-glass-only.png  tom@%s:%s/static/css/images' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sstatic/css/images/next.png                           tom@%s:%s/static/css/images' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sstatic/css/images/prev.png                           tom@%s:%s/static/css/images' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sstatic/css/images/ui-bg_flat_75_ffffff_40x100.png    tom@%s:%s/static/css/images' % (local_absolute_path, server_name, server_absolute_path))


def fonts():
    # S3
    local('aws s3 cp %sstatic/fonts/fontawesome-webfont.eot   %sfonts/fontawesome-webfont.eot --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/fonts/fontawesome-webfont.svg   %sfonts/fontawesome-webfont.svg --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/fonts/fontawesome-webfont.ttf   %sfonts/fontawesome-webfont.ttf --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/fonts/fontawesome-webfont.woff  %sfonts/fontawesome-webfont.woff --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/fonts/FontAwesome.otf           %sfonts/FontAwesome.otf --acl public-read' % (local_absolute_path, s3_path))

    # Server
    local('scp %sstatic/fonts/fontawesome-webfont.eot   tom@%s:%s/static/fonts' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sstatic/fonts/fontawesome-webfont.svg   tom@%s:%s/static/fonts' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sstatic/fonts/fontawesome-webfont.ttf   tom@%s:%s/static/fonts' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sstatic/fonts/fontawesome-webfont.woff  tom@%s:%s/static/fonts' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sstatic/fonts/FontAwesome.otf           tom@%s:%s/static/fonts' % (local_absolute_path, server_name, server_absolute_path))


def js():
    # S3
    local('aws s3 cp %sstatic/js/dashboard.js                     %sjs/dashboard.js --acl public-read' % (local_absolute_path, s3_path))
    # local('aws s3 cp %sstatic/js/foundation.min.js                %sjs/foundation.min.js --acl public-read' % (local_absolute_path, s3_path))
    # local('aws s3 cp %sstatic/js/foundation.tooltip.js            %sjs/foundation.tooltip.js --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/js/index.js                         %sjs/index.js --acl public-read' % (local_absolute_path, s3_path))
    # local('aws s3 cp %sstatic/js/jquery-1.11.0.min.js             %sjs/jquery-1.11.0.min.js --acl public-read' % (local_absolute_path, s3_path))
    # local('aws s3 cp %sstatic/js/jquery-ui.js                     %sjs/jquery-ui.js --acl public-read' % (local_absolute_path, s3_path))
    # local('aws s3 cp %sstatic/js/jquery.tablesorter.min.js        %sjs/jquery.tablesorter.min.js --acl public-read' % (local_absolute_path, s3_path))
    # local('aws s3 cp %sstatic/js/jquery.tablesorter.pager.min.js  %sjs/jquery.tablesorter.pager.min.js --acl public-read' % (local_absolute_path, s3_path))
    # local('aws s3 cp %sstatic/js/leaflet.js                       %sjs/leaflet.js --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/js/lens.js                          %sjs/lens.js --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/js/map.js                        %sjs/map.js --acl public-read' % (local_absolute_path, s3_path))
    # local('aws s3 cp %sstatic/js/mapbox.uncompressed.js           %sjs/mapbox.uncompressed.js --acl public-read' % (local_absolute_path, s3_path))
    # local('aws s3 cp %sstatic/js/modernizr.js                     %sjs/modernizr.js --acl public-read' % (local_absolute_path, s3_path))
    # local('aws s3 cp %sstatic/js/neighborhoods-topo.js            %sjs/neighborhoods-topo.js --acl public-read' % (local_absolute_path, s3_path))
    # local('aws s3 cp %sstatic/js/neighborhoods-topo.min.js        %sjs/neighborhoods-topo.min.js --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/js/sale.js                          %sjs/sale.js --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/js/search.js                        %sjs/search.js --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/js/searchArea.js                        %sjs/searchArea.js --acl public-read' % (local_absolute_path, s3_path))
    # local('aws s3 cp %sstatic/js/squares-topo.js                  %sjs/squares-topo.js --acl public-read' % (local_absolute_path, s3_path))

    # Server
    local('scp %sstatic/js/dashboard.js                     tom@%s:%s/static/js' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %sstatic/js/foundation.min.js                tom@%s:%s/static/js' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %sstatic/js/foundation.tooltip.js            tom@%s:%s/static/js' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sstatic/js/index.js                         tom@%s:%s/static/js' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %sstatic/js/jquery-1.11.0.min.js             tom@%s:%s/static/js' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %sstatic/js/jquery-ui.js                     tom@%s:%s/static/js' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %sstatic/js/jquery.tablesorter.min.js        tom@%s:%s/static/js' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %sstatic/js/jquery.tablesorter.pager.min.js  tom@%s:%s/static/js' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %sstatic/js/leaflet.js                       tom@%s:%s/static/js' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sstatic/js/lens.js                          tom@%s:%s/static/js' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %sstatic/js/mapbox.uncompressed.js           tom@%s:%s/static/js' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %sstatic/js/modernizr.js                     tom@%s:%s/static/js' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %sstatic/js/neighborhoods-topo.js            tom@%s:%s/static/js' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %sstatic/js/neighborhoods-topo.min.js        tom@%s:%s/static/js' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sstatic/js/sale.js                          tom@%s:%s/static/js' % (local_absolute_path, server_name, server_absolute_path))
    local('scp %sstatic/js/search.js                        tom@%s:%s/static/js' % (local_absolute_path, server_name, server_absolute_path))
    # local('scp %sstatic/js/squares-topo.js                  tom@%s:%s/static/js' % (local_absolute_path, server_name, server_absolute_path))


def neighborhoodsJSON():
    local('aws s3 cp {0}static/neighborhood-geojson/ALGIERS POINT.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("ALGIERS POINT", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/AUDUBON.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("AUDUBON", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/B. W. COOPER.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("B. W. COOPER", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/BAYOU ST. JOHN.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("BAYOU ST. JOHN", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/BEHRMAN.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("BEHRMAN", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/BLACK PEARL.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("BLACK PEARL", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/BROADMOOR.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("BROADMOOR", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/BYWATER.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("BYWATER", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/CENTRAL BUSINESS DISTRICT.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("CENTRAL BUSINESS DISTRICT", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/CENTRAL CITY.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("CENTRAL CITY", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/CITY PARK.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("CITY PARK", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/DESIRE AREA.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("DESIRE AREA", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/DILLARD.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("DILLARD", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/DIXON.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("DIXON", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/EAST CARROLLTON.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("EAST CARROLLTON", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/EAST RIVERSIDE.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("EAST RIVERSIDE", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/FAIRGROUNDS.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("FAIRGROUNDS", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/FILLMORE.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("FILLMORE", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/FISCHER DEV.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("FISCHER DEV", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/FLORIDA AREA.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("FLORIDA AREA", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/FLORIDA DEV.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("FLORIDA DEV", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/FRENCH QUARTER.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("FRENCH QUARTER", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/FRERET.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("FRERET", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/GARDEN DISTRICT.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("GARDEN DISTRICT", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/GENTILLY TERRACE.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("GENTILLY TERRACE", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/GENTILLY WOODS.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("GENTILLY WOODS", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/GERT TOWN.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("GERT TOWN", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/HOLLYGROVE.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("HOLLYGROVE", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/HOLY CROSS.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("HOLY CROSS", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/IBERVILLE.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("IBERVILLE", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/IRISH CHANNEL.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("IRISH CHANNEL", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/LAKE CATHERINE.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("LAKE CATHERINE", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/LAKE TERRACE & OAKS.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("LAKE TERRACE & OAKS", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/LAKESHORE - LAKE VISTA.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("LAKESHORE - LAKE VISTA", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/LAKEVIEW.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("LAKEVIEW", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/LAKEWOOD.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("LAKEWOOD", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/LEONIDAS.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("LEONIDAS", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/LITTLE WOODS.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("LITTLE WOODS", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/LOWER GARDEN DISTRICT.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("LOWER GARDEN DISTRICT", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/LOWER NINTH WARD.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("LOWER NINTH WARD", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/MARIGNY.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("MARIGNY", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/MARLYVILLE - FONTAINBLEAU.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("MARLYVILLE - FONTAINBLEAU", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/McDONOGH.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("McDONOGH", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/MID-CITY.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("MID-CITY", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/MILAN.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("MILAN", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/MILNEBURG.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("MILNEBURG", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/NAVARRE.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("NAVARRE", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/NEW AURORA - ENGLISH TURN.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("NEW AURORA - ENGLISH TURN", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/OLD AURORA.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("OLD AURORA", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/PINES VILLAGE.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("PINES VILLAGE", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/PLUM ORCHARD.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("PLUM ORCHARD", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/PONTCHARTRAIN PARK.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("PONTCHARTRAIN PARK", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/READ BLVD EAST.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("READ BLVD EAST", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/READ BLVD WEST.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("READ BLVD WEST", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/SEVENTH WARD.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("SEVENTH WARD", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/ST.  ANTHONY.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("ST.  ANTHONY", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/ST. BERNARD AREA.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("ST. BERNARD AREA", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/ST. CLAUDE.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("ST. CLAUDE", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/ST. ROCH.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("ST. ROCH", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/ST. THOMAS DEV.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("ST. THOMAS DEV", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/TALL TIMBERS - BRECHTEL.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("TALL TIMBERS - BRECHTEL", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/TOURO.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("TOURO", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/TREME - LAFITTE.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("TREME - LAFITTE", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/TULANE - GRAVIER.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("TULANE - GRAVIER", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/U.S. NAVAL BASE.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("U.S. NAVAL BASE", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/UPTOWN.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("UPTOWN", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/VIAVANT - VENETIAN ISLES.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("VIAVANT - VENETIAN ISLES", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/VILLAGE DE LEST.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("VILLAGE DE LEST", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/WEST END.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("WEST END", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/WEST LAKE FOREST.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("WEST LAKE FOREST", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/WEST RIVERSIDE.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("WEST RIVERSIDE", '') + '.json' + ' --acl public-read')
    local('aws s3 cp {0}static/neighborhood-geojson/WHITNEY.json'.format(local_absolute_path) + ' {0}neighborhood-geojson/'.format(s3_path) + urllib.quote("WHITNEY", '') + '.json' + ' --acl public-read')


def doitall():
    scripts()
    templates()
    js()
    css()
    # images()
    # fonts()
    # geographicData()
    # app_config()


def s3():
    local('aws s3 cp %sstatic/css/font-awesome.css                %scss/font-awesome.css --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/foundation.css                  %scss/foundation.css --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/foundation.min.css              %scss/foundation.min.css --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/jquery-ui-1.9.2.custom.css      %scss/jquery-ui-1.9.2.custom.css --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/jquery-ui.css                   %scss/jquery-ui.css --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/jquery.tablesorter.pager.css    %scss/jquery.tablesorter.pager.css --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/lens.css                        %scss/lens.css --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/lenstablesorter.css             %scss/lenstablesorter.css --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/mapbox.css                      %scss/mapbox.css --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/tablesorter.css                 %scss/tablesorter.css --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/theme.blue.css                  %scss/theme.blue.css --acl public-read' % (local_absolute_path, s3_path))

    local('aws s3 cp %sstatic/css/images/ajax-loader.gif                  %scss/images/ajax-loader.gif --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/black-asc.gif                    %scss/images/black-asc.gif --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/black-desc.gif                   %scss/images/black-desc.gif --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/black-unsorted.gif               %scss/images/black-unsorted.gif --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/favicon.ico                      %scss/images/favicon.ico --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/first.png                        %scss/images/first.png --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/icons-000000.png                 %scss/images/icons-000000.png --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/icons-000000@2x.png              %scss/images/icons-000000@2x.png --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/info-i.png                       %scss/images/info-i.png --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/last.png                         %scss/images/last.png --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/lens-info.png                    %scss/images/lens-info.png --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/lens-logo.png                    %scss/images/lens-logo.png --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/next.png                         %scss/images/next.png --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/prev.png                         %scss/images/prev.png --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/css/images/ui-bg_flat_75_ffffff_40x100.png  %scss/images/ui-bg_flat_75_ffffff_40x100.png --acl public-read' % (local_absolute_path, s3_path))

    local('aws s3 cp %sstatic/fonts/fontawesome-webfont.eot   %sfonts/fontawesome-webfont.eot --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/fonts/fontawesome-webfont.svg   %sfonts/fontawesome-webfont.svg --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/fonts/fontawesome-webfont.ttf   %sfonts/fontawesome-webfont.ttf --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/fonts/fontawesome-webfont.woff  %sfonts/fontawesome-webfont.woff --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/fonts/FontAwesome.otf           %sfonts/FontAwesome.otf --acl public-read' % (local_absolute_path, s3_path))

    local('aws s3 cp %sstatic/js/dashboard.js                     %sjs/dashboard.js --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/js/foundation.min.js                %sjs/foundation.min.js --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/js/foundation.tooltip.js            %sjs/foundation.tooltip.js --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/js/index.js                         %sjs/index.js --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/js/jquery-1.11.0.min.js             %sjs/jquery-1.11.0.min.js --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/js/jquery-ui.js                     %sjs/jquery-ui.js --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/js/jquery.tablesorter.min.js        %sjs/jquery.tablesorter.min.js --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/js/jquery.tablesorter.pager.min.js  %sjs/jquery.tablesorter.pager.min.js --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/js/leaflet.js                       %sjs/leaflet.js --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/js/lens.js                          %sjs/lens.js --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/js/mapbox.uncompressed.js           %sjs/mapbox.uncompressed.js --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/js/modernizr.js                     %sjs/modernizr.js --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/js/neighborhoods-topo.js            %sjs/neighborhoods-topo.js --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/js/neighborhoods-topo.min.js        %sjs/neighborhoods-topo.min.js --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/js/sale.js                          %sjs/sale.js --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/js/search.js                        %sjs/search.js --acl public-read' % (local_absolute_path, s3_path))
    local('aws s3 cp %sstatic/js/squares-topo.js                  %sjs/squares-topo.js --acl public-read' % (local_absolute_path, s3_path))
