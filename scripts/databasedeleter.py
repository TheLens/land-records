#https://bitbucket.org/zzzeek/sqlalchemy/wiki/UsageRecipes/DropEverything

from sqlalchemy.engine import reflection
from sqlalchemy import create_engine
from sqlalchemy.schema import (
    MetaData,
    Table,
    DropTable,
    ForeignKeyConstraint,
    DropConstraint,
    )
from app_config import server_engine, backup_directory
from subprocess import call

engine = create_engine('%s' % (server_engine))

conn = engine.connect()

# the transaction only applies if the DB supports
# transactional DDL, i.e. Postgresql, MS SQL Server
trans = conn.begin()

inspector = reflection.Inspector.from_engine(engine)

# gather all data first before dropping anything.
# some DBs lock after things have been dropped in 
# a transaction.

metadata = MetaData()

tbs = []
all_fks = []

# Backup dashboard table
call('pg_dump -Fc landrecords -t dashboard > ' + backup_directory + '/dashboard_table_$(date +%Y-%m-%d).sql', shell=True)

for table_name in inspector.get_table_names():
    fks = []
    for fk in inspector.get_foreign_keys(table_name):
        if not fk['name']:
            continue
        fks.append(
            ForeignKeyConstraint((),(),name=fk['name'])
            )
    t = Table(table_name,metadata,*fks)
    tbs.append(t)
    all_fks.extend(fks)

for fkc in all_fks:
    conn.execute(DropConstraint(fkc))
print tbs
for table in tbs:
    if table.name == 'spatial_ref_sys': # This table is part of PostGIS extension.
        continue
    conn.execute(DropTable(table))

trans.commit()