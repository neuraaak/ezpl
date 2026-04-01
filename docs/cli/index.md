# CLI reference

Command and option reference for the ezplog command-line interface.

## 💻 Usage

```bash
ezpl [OPTIONS] COMMAND [ARGS]...
```

## ⚙️ Global options

| Option      | Short | Description            |
| :---------- | :---- | :--------------------- |
| `--help`    | `-h`  | Show help and exit.    |
| `--version` | `-v`  | Show version and exit. |

## 📋 Command groups

| Group    | Description                                   |
| :------- | :-------------------------------------------- |
| `logs`   | View, search, analyze, and export log files.  |
| `config` | Read, update, and reset configuration values. |

## ⚙️ logs commands

| Command            | Key options                                                      |
| :----------------- | :--------------------------------------------------------------- |
| `ezpl logs view`   | `--file/-f`, `--lines/-n`, `--level/-l`, `--follow/-F`           |
| `ezpl logs search` | `--file/-f`, `--pattern/-p`, `--level/-l`, `--case-sensitive/-c` |
| `ezpl logs stats`  | `--file/-f`, `--format/-F`                                       |
| `ezpl logs tail`   | `--file/-f`, `--lines/-n`, `--follow/-F`                         |
| `ezpl logs list`   | `--dir/-d`                                                       |
| `ezpl logs clean`  | `--file/-f`, `--days/-d`, `--size/-s`, `--confirm/-y`            |
| `ezpl logs export` | `--file/-f`, `--format/-F`, `--output/-o`                        |

## ⚙️ config commands

| Command                     | Key options     |
| :-------------------------- | :-------------- |
| `ezpl config get [KEY]`     | `--show-env/-e` |
| `ezpl config set KEY VALUE` | `--env/-e`      |
| `ezpl config reset`         | `--confirm/-y`  |

## 📋 Standalone commands

| Command        | Description                                 |
| :------------- | :------------------------------------------ |
| `ezpl version` | Show package version details.               |
| `ezpl info`    | Show package and configuration information. |
| `ezpl docs`    | Open the online documentation website.      |

## 🧪 Examples

```bash
ezpl --help
ezpl -v
ezpl config get --show-env
ezpl config set log-level DEBUG --env
ezpl logs view --lines 100
ezpl logs search --pattern "error|exception" --level ERROR
ezpl logs export --format json --output logs.json
ezpl docs
```
