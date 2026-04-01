# App mode vs lib mode

`ezplog` separates responsibilities between host applications and reusable libraries.
This separation prevents conflicting logging setup and keeps integration predictable.

## 📚 Background

Python libraries are expected to emit log records without owning global logging configuration.
Applications, by contrast, are responsible for defining handlers, levels, and routing.

`ezplog` encodes this model with two entry points:

- App mode through `Ezpl`, which owns configuration.
- Lib mode through `get_logger()` and `get_printer()`, which remain passive until a host app initializes `Ezpl`.

## 🔍 Compatibility model

The compatibility layer is explicit and controlled through hooks:

- `hook_logger=True` connects stdlib logging records to the loguru pipeline.
- `hook_printer=True` allows `lib_mode` printer proxies to delegate to the real `EzPrinter`.
- `logger_names=[...]` narrows logger hooking to selected namespaces.

These controls are available at initialization and through `set_compatibility_hooks()`.

## ⚖️ Design trade-offs

Root logger interception maximizes integration and minimizes app/library friction, but broad capture can include third-party noise.
Named logger hooking reduces noise and increases control, but requires explicit namespace management.

Silent behavior in lib mode is deliberate: library code should not fail or reconfigure host logging when no app-level configuration exists.

## 🧠 Why hooks are explicit

Previous implicit compatibility patterns hide behavior and make runtime diagnostics harder.
Explicit hooks create a stable and auditable contract:

- Integration behavior is visible in startup configuration.
- Tests can assert each mode independently.
- Runtime updates can be made intentionally, not accidentally.

## 🔗 Relationship to configuration lock

`lock_config` protects application ownership after bootstrap.
Once locked, runtime changes like `configure()` and level updates are blocked without a valid token.

This complements app/lib separation: applications define policy once, libraries consume it passively.
