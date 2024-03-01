# Restore using the same container

To restore using the same backup container, replace $BACKUPFILE, $CONTAINER, $USERNAME and $DBNAME from the following command:

```
docker exec --tty --interactive $CONTAINER /bin/sh -c "zcat $BACKUPFILE | psql --username=$USERNAME --dbname=$DBNAME -W"
```

# Restore using a new container

Replace $BACKUPFILE, $HOSTNAME, $PORT, $USERNAME and $DBNAME from the following command:

```
docker run --rm --tty --interactive -v $BACKUPFILE:/tmp/backupfile.sql.gz postgres:16.1 /bin/sh -c "zcat /tmp/backupfile.sql.gz | psql --host=$HOSTNAME --port=$PORT --username=$USERNAME --dbname=$DBNAME -W"
```