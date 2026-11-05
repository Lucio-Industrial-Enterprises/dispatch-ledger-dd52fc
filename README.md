# Warehouse tools

Small Python utilities for warehouse order and shipping workflows.

Run the tests with `python3 -m unittest discover -s tests -v`.

## Shipping

`shipping_quote(weight_kg, zone, service="standard")` returns a delivery quote
in dollars. Zones are `local` and `regional`; weights must be positive.
Service levels are `standard` (default) and `express` — express adds $7.00 to
the standard rate for either zone.

```python
from warehouse.rates import shipping_quote

shipping_quote(2, "local")               # 8.0  (standard)
shipping_quote(2, "local", "express")    # 15.0 (express)
```

The command-line entry point accepts an optional `--service` flag:

```
python -m warehouse.cli 2 local --service express   # $15.00
```
