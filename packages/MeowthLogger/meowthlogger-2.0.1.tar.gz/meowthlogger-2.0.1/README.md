# MeowthPxnk Cxstom logger for python!
---
### How this works:

Logs will be steram to console and save to rollover every hour at 00 minutes:
***savepath ->*** ./Logs/`YYYY-MM-DD`/`HH.00-HH.00`.log

---
### Usage:
```python
from MeowthLogger import Logger

logger = Logger()

# usage logger ---->

logger.info("INFO")
logger.error("ERROR")
logger.debug("DEBUG")
logger.warning("WARNING")
logger.critical("CRITICAL")
```
---
### Initialisation arguments:
- **logger_level** - level of logging
- **path** - logs folder path
- **filename** - logging filename
- **encoding** - encoding for log ro files
- **use_uvicorn** - bool argument, need to use logger with uvicorn
##### Example:
```python
logger = Logger(
    path="user/logs",
    filename="logging.log",
    encoding="utf-8"
)
```
---
### Usage with dependencies:
##### Uvicorn - 
```python
logger = Logger(use_uvicorn=True)
```
---
$XOXO$
*meowthpxnk*