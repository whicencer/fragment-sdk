buy_stars()
===========

``FragmentStarsAPI.buy_stars()``

Purchase stars. Instant payment.


**Parameters:**  

- **username** (``str``) — Recipient username (without @).
- **quantity** (``int``) — Quantity of stars to purchase.


**Returns:**  

``ApiResult[str]``

Example
-------

.. code-block:: python

  tx_hash = await FragmentStarsAPI.buy_stars(username="whicencer", quantity=50)
  return tx_hash
