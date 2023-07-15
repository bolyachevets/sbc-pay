ARG PG_MAJOR=12
ARG PG_MINOR=11

FROM quay.io/fedora/postgresql-$PG_MAJOR:$PG_MINOR

WORKDIR /

# read env variables
ARG TZ=America/Vancouver

ENV PORT=5432
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV PGDATA=/var/lib/pgsql/data

USER root

# install replication package
RUN dnf install -y postgresql-$PG_MAJOR-pglogical

# set time zone
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

USER 26

EXPOSE $PORT

CMD ["postgres"]
