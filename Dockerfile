FROM containers.github.scch.at/cvrlpbs/cvrlpbswptextanalysis/torch:2.0.1

ENV MINIO_ENDPOINT bigdata.scch.at:9000
ARG MINIO_ACCESS_KEY
ENV MINIO_ACCESS_KEY $MINIO_ACCESS_KEY
ARG MINIO_SECRET_KEY
ENV MINIO_SECRET_KEY $MINIO_SECRET_KEY

ADD . /workspace
WORKDIR /workspace/
RUN pip install .