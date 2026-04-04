# LangChain Flows — Methods & Nodes (brief)

This file lists common node types and runtime methods used when building LangChain Flows (orchestration graphs). Use these as a quick reference — names may vary slightly between LangChain versions.

## Node types / methods
- **Prompt / LLM**: Call an LLM with a prompt template; handles prompt rendering and model invocation.
- **Tool / External Call**: Invoke external APIs, databases, or user-defined tools; returns structured results.
- **Python / Computation**: Run arbitrary Python code for transformations or business logic inside the flow.
- **Chain / Subflow**: Embed an existing chain or nested flow as a reusable node.
- **Agent**: Executes agent logic that decides and calls tools dynamically during a run.
- **Data Loader**: Ingest data from sources (files, DBs, APIs) and normalize it for downstream nodes.
- **Validator / Schema**: Validate and coerce node inputs/outputs against typed schemas.

## Execution & orchestration methods
- **run**: Synchronously execute a flow or node with given inputs; returns final outputs.
- **async_run**: Asynchronous execution variant for non-blocking flows.
- **schedule**: Enqueue or schedule a flow run (delayed or periodic execution).
- **map / batch_run**: Execute a node or flow over a collection (parallel or chunked).
- **parallelize / concurrency**: Execute independent nodes concurrently to improve throughput.
- **retry**: Automatic retry wrapper for transient failures with configurable backoff.
- **timeout**: Enforce time limits on node or flow execution.

## State, caching & persistence
- **context / get_context / set_context**: Access or mutate the per-run context holding inputs and intermediate outputs.
- **cache / memoize**: Store and reuse node results to avoid duplicated work.
- **save_state / load_state**: Persist and restore flow state or artifacts between runs.

## I/O, typing & serialization
- **validate_input / validate_output**: Enforce typed schemas on node inputs/outputs.
- **serialize / deserialize**: Convert typed objects to/from transport formats (JSON, YAML, binary).

## Observability & control
- **trace / get_run_history**: Record execution traces and retrieve run metadata for debugging and auditing.
- **log**: Emit structured logs from nodes and the engine.
- **visualize**: Render the flow graph, node status, and data lineage for inspection.
- **debug**: Interactive hooks or step-through tooling for node execution.

## Deployment & operational methods
- **start / stop / scale**: Manage runtime processes, worker pools, or server deployments.
- **register_tool / unregister_tool**: Add or remove tool adapters available to flows and agents.
- **audit / access_control**: Manage permissions, audit logs, and safe access to external resources.

---

If you'd like, I can:

- Provide a code example (`Flow` YAML or Python) that uses several of these methods.
- Map these to exact API names for a specific LangChain version.

Replace this file or open a PR to adjust wording for your project's conventions.
