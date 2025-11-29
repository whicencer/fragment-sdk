Transaction
===========

TON transaction object.

.. code-block:: python

  @dataclass
  class Transaction():
    validUntil: int
    messages: List[TransactionMessage]

:doc:`TransactionMessage <transaction_message>`.
