################################################################################
##                                 BASE IMAGE                                 ##
################################################################################

FROM python:3.10-buster AS base


# install Python Packages
#RUN poetry install  --no-interaction --no-ansi --no-root
RUN groupadd -r feast && useradd --no-log-init -u 1000 -r -g feast feast

RUN mkdir /feature_repo && chown feast:feast /feature_repo

# Install Poetry
RUN pip install feast[redis]

COPY . .

WORKDIR /feature_repo

################################################################################
##                               IMAGE                                 ##
################################################################################


FROM base as feast

# convert csv to parquet
#RUN python convert_csv_to_parquet.py sample_products
#RUN python convert_csv_to_parquet.py test_products


CMD feast serve