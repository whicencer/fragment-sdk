process_transaction()
=====================

Processes a TON transfer by validating wallet connection, checking balance, decoding the payload (``base64``), and sending the transaction to the specified destination.

**Returns:**  

tx_hash — ``str``

Example
-------

.. code-block:: python

  tx_hash = await WalletClient.process_transaction(
    destination=transaction_msg.address,
    amount=transaction_msg.amount,
    body=transaction_msg.payload # only base64 payload
  )
