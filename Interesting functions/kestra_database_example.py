# Introduction

## Workflow Automation and Task Scheduling:
1. ** Kestra **:
- `Kestra` is a
modern
orchestration and scheduling
platform
used
for running and managing workflows.
- It
allows
you
to
define
tasks
that
can
be
run in parallel or sequentially, as well as manage
dependencies and process
data
using
various
plugins.
- The
example
below
demonstrates
downloading
tables
concurrently
from a PostgreSQL

database and processing
them
using
Python
's `pandas` library.

## Code Explanation:
- The
workflow
defines
tasks
that
run in parallel, downloading
tables
from PostgreSQL and processing
them
with `pandas` in a Docker container.
- The
tables
are
processed
based
on
triggers
that
execute
the
workflow
on
a
defined
schedule.

```yaml
tasks:
- id: getTables
type: io.kestra.core.tasks.flows.Parallel
concurrent: 2
tasks:
- id: products
type: io.kestra.plugin.jdbc.postgresql.CopyOut
sql: SELECT * FROM
products

- id: orders
type: io.kestra.plugin.jdbc.postgresql.CopyOut
sql: SELECT * FROM
orders

- id: pandas
type: io.kestra.plugin.scripts.python.Script
docker:
image: ghcr.io / kestra - io / pydata:latest
inputFiles:
products.csv: "{{outputs.products.uri}}"
orders.csv: "{{outputs.orders.uri}}"
script: |
import pandas as pd

# Read CSV files containing products and orders data
products = pd.read_csv("products.csv")
orders = pd.read_csv("orders.csv")

# Merge the products and orders data on the "product_id" column
df = orders.merge(products, on="product_id", how="left")

triggers:
- id: everyMorning
type: io.kestra.core.models.triggers.types.Schedule
cron: 0
9 * * *