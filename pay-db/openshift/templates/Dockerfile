ARG PG_MAJOR=12
ARG PG_MINOR=11

FROM postgres:$PG_MAJOR.$PG_MINOR

# read env variables
ARG TZ=America/Vancouver

ENV PORT=5432
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV PGDATA=/var/lib/pgsql/data

# install replication package
RUN mkdir -p /opt/apps
RUN apt-get -qq update
RUN apt-get -qq install -y --no-install-recommends postgresql-$PG_MAJOR-pglogical
RUN apt-get -qq clean

# set time zone
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

EXPOSE $PORT

CMD ["postgres"]
