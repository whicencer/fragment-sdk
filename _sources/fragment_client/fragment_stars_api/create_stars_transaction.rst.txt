create_stars_transaction()
==========================

``FragmentStarsAPI.create_stars_transaction()``

Creates buy stars transaction.

**Parameters:**  

- **recipient_id** (``str``) — Recipient ID. To obtain use ``FragmentStarsAPI.search_stars_recipient()`` method.
- **quantity** (``int``) — Stars quantity.
- **wallet_account** (``int``) — Wallet data. To obtain use ``WalletClient.get_wallet_data()`` method.

**Returns:**  

``ApiResult[Transaction]``

Example
-------

.. code-block:: python

  transaction = self.create_stars_transaction(
    recipient_id=recipient_id,
    quantity=quantity,
    wallet_account=wallet_account
  )

  if transaction.error:
    # Handle error

  # Get transaction message
  transaction_msg = transaction.data.messages[0]

  # Send transaction to pay stars
  tx_hash = await WalletClient.process_transaction(
    destination=transaction_msg.address,
    amount=transaction_msg.amount,
    body=transaction_msg.payload
  )