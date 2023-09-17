# In-Process Analytical Data Management with DuckDB
by Hannes Mühleisen, Mark Raasveldt
* [Talk info](https://amsterdam2023.pydata.org/cfp/talk/U93EST/)
## Abstract
DuckDB is a novel analytical data management system. DuckDB supports complex queries, has no external dependencies, and is deeply integrated into the Python ecosystem. Because DuckDB runs in the same process, no serialization or socket communication has to occur, making data transfer virtually instantaneous. For example, DuckDB can directly query Pandas data frames faster than Pandas itself. In our talk, we will describe the user values of DuckDB, and how it can be used to improve their day-to-day lives through automatic parallelization, efficient operators and out-of-core operations.
