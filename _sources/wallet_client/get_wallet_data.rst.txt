get_wallet_data()
=================

Returns wallet data (wallet account).

**Returns:**  

``dict[str, Any]``

Example
-------

.. code-block:: python

  wallet_account = WalletClient.get_wallet_data()

  FragmentClient.stars.create_stars_transaction(
    recipient_id,
    quantity,
    wallet_account=wallet_account
  )
