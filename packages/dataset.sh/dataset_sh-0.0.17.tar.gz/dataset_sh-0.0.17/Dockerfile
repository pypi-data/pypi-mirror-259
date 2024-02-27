FROM python:3

RUN adduser --disabled-password --gecos '' runner

WORKDIR /dataset-sh-storage

RUN mkdir -p /dataset-sh-storage/data && chown -R runner:runner /dataset-sh-storage

RUN pip install dataset.sh['all']
RUN pip install gunicorn

USER runner
WORKDIR /dataset-sh-storage

RUN mkdir -p /dataset-sh-storage/data && chown -R runner:runner /dataset-sh-storage
RUN mkdir -p /dataset-sh-storage/posts && chown -R runner:runner /dataset-sh-storage
RUN mkdir -p /dataset-sh-storage/uploader && chown -R runner:runner /dataset-sh-storage


ENV DATASET_APP_STORAGE_LOCATION=/dataset-sh-storage/data
ENV DATASET_APP_ARTICLE_LOCATION=/dataset-sh-storage/posts
ENV DATASET_APP_UPLOADER_DIR=/dataset-sh-storage/uploader
ENV DATASET_SH_SERVER_CONFIG_FILE=/dataset-sh-storage/dataset-sh-server-config.json
ENV SERVER_NAME=localhost:8989

RUN dataset-sh-server-cli init

CMD ["gunicorn"  , "-b", "0.0.0.0:8989", "dataset_sh.server.app:create_app()"]
