ARG PG_MAJOR=12
ARG PG_MINOR=11

FROM image-registry.openshift-image-registry.svc:5000/openshift/postgresql@sha256:d99bb8c63bbdbbfb1bd1a1f4e1a5f114dc5a0d972cdd9d27ca9e69c16cb98089

USER root

RUN yum install postgresql12-pglogical

USER postgres
