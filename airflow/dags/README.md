# Airflow DAGs

This directory contains examples of different ways to create Airflow DAGs and use various operators.

## Methods for Creating DAGs

There are two primary ways to define a DAG in Airflow:

1.  **Traditional `DAG` object instantiation**: This involves creating a `DAG` object and then defining tasks that belong to that DAG. The `python_opeator_dag.py` file shows an example of this approach.

2.  **Decorator-based DAGs**: Airflow's `@dag` decorator provides a more Pythonic and concise way to define a DAG. You can see this in action in the `decorator_dag.py` file.

## Airflow Operators

Operators are the building blocks of Airflow DAGs, representing a single task.

### Operator Examples in this Directory

*   **`@task` decorator (TaskFlow API)**: The `decorator_dag.py` example uses the `@task` decorator, which is part of the TaskFlow API. This simplifies the process of passing data between tasks.

*   **`PythonOperator`**: The `python_opeator_dag.py` example uses the `PythonOperator` to execute a Python callable.

### Other Common Operators

Airflow has a wide variety of pre-built operators to interact with different systems:

*   `BashOperator`: Executes a bash command.
*   `PostgresOperator`: Executes a SQL command in a PostgreSQL database.
*   `SnowflakeOperator`: Executes a SQL command in a Snowflake warehouse.
*   `SimpleHttpOperator`: Makes an HTTP request.
*   `DockerOperator`: Runs a command inside a Docker container.
*   And many more for services like Kubernetes, Databricks, Spark, etc.

## Task Dependencies

You can define the order in which tasks should execute by setting dependencies.

### Bit-shift operators

The most common way to set dependencies is using the bit-shift operators `>>` (downstream) and `<<` (upstream).

```python
# task1 will run before task2, which will run before task3
task1 >> task2 >> task3

# task3 will run after task2, which will run after task1
task3 << task2 << task1
```

### `set_downstream()` and `set_upstream()`

You can also use the `set_downstream()` and `set_upstream()` methods.

```python
task1.set_downstream(task2) # task1 runs before task2
task3.set_upstream(task2)   # task3 runs after task2
```

## Trigger Rules

The `trigger_rule` parameter in a task determines when it runs based on the status of its upstream tasks.

Common trigger rules include:

*   `all_success` (default): The task runs only when all upstream tasks have succeeded.
*   `all_failed`: The task runs only when all upstream tasks have failed.
*   `all_done`: The task runs when all upstream tasks are done (succeeded, failed, or skipped).
*   `one_success`: The task runs as soon as one upstream task succeeds.
*   `one_failed`: The task runs as soon as one upstream task fails.
*   `none_failed`: The task runs if no upstream tasks have failed (i.e., all have succeeded or been skipped).
*   `none_failed_min_one_success`: The task runs if no upstream tasks have failed and at least one has succeeded.
*   `dummy`: Dependencies are just for show, trigger at will.

Example:
```python
my_task = BashOperator(
    task_id='my_task',
    bash_command='echo "This will run even if some upstream tasks fail"',
    trigger_rule='one_success',
    dag=my_dag
)
```
