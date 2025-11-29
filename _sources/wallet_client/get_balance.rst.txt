get_balance()
=============

Get connected wallet balance in TON.

**Returns:**  

``float``

Example
-------

.. code-block:: python

  wallet_balance = WalletClient.get_balance()

  if wallet_balance < 10:
    print("Wallet balance is less than 10 TON")
