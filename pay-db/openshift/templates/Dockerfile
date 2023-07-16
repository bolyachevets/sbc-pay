ARG PG_MAJOR=12
ARG PG_MINOR=11

#FROM image-registry.openshift-image-registry.svc:5000/openshift/postgresql@sha256:d99bb8c63bbdbbfb1bd1a1f4e1a5f114dc5a0d972cdd9d27ca9e69c16cb98089
#FROM image-registry.apps.silver.devops.gov.bc.ca/openshift/postgresql@sha256:d99bb8c63bbdbbfb1bd1a1f4e1a5f114dc5a0d972cdd9d27ca9e69c16cb98089
FROM redhat/ubi8

USER root

WORKDIR /tmp

RUN yum -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm

RUN yum -y install --skip-broke postgresql12-server postgresql12-contrib

RUN curl https://access.2ndquadrant.com/api/repository/dl/default/release/12/rpm | bash

RUN yum -y install postgresql12-pglogical

USER 26

CMD ["run-postgresql"]

ENTRYPOINT ["container-entrypoint"]  
