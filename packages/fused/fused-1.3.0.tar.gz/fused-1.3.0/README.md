<h1 align="center">
  Fused Public Python package
</h1>
<h3 align="center">
  🌎 Code to Map. Instantly.
</h3>
<br><br>

![version](https://img.shields.io/badge/version-1.1.2-blue)

**Fused** is a Python library to code, scale, and ship geospatial workflows of any size. Express workflows as shareable UDFs (user defined functions) without thinking about the underlying compute. The Fused Python library is maintained by [Fused.io](https://fused.io).

## Prerequisites

Python >= 3.8

## Install

Fused is currently in private beta. Email info@fused.io for access.

```
pip install fused
```

## Quickstart

```python3
import fused


# Load data
census = 's3://fused-asset/infra/census_bg_us/'
buildings = 's3://fused-asset/infra/building_msft_us/'

# Declare UDF
@fused.udf()
def census_buildings_join(left, right):
    import fused
    df_joined = fused.utils.geo_join(left.data, right.data)
    df_cnt = df_joined.groupby(['fused_index','GEOID']).size().to_frame('count_building').reset_index()
    return df_cnt

# Instantiate job configuration that runs the data against the UDF
job = census_buildings_join(census, buildings)

# Run locally
job.run_local()

# Run on remote compute managed by Fused and view logs
job_id = job.run_remote(output_table='s3://my-s3-bucket/census_buildings_join')
job_id.tail_logs()

# Export job to local directory
job.export('census_buildings_join', overwrite=True)

# Re-import job
fused.experimental.load_job('census_buildings_join')
```

## Changelog
See the [changelog](https://docs.fused.io/fused_py/changelog/) for the latest changes.
