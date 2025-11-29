get_buy_stars_link()
========================


``FragmentStarsAPI.get_buy_stars_link()``

Get buy stars transaction.


**Parameters:**  

- **account** — Wallet data. To obtain use ``WalletClient.get_wallet_data()`` method.
- **req_id** (``str``) — ``InitPurchaseResponseData.req_id``. To obtain use ``FragmentStarsAPI.init_buy_stars_request`` method.


**Returns:**  

``ApiResult[Transaction]``

Example
-------

.. code-block:: python
  
  # Get buy stars transaction
  transaction = self.get_buy_stars_link(
    account=wallet.get_wallet_data(),
    req_id=req_id
  )
  
  if transaction.error:
    # Handle error

  print(transaction.data)
