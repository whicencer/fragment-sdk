TransactionMessage
==================

:doc:`Transaction <transaction>` message.

.. code-block:: python

  @dataclass
  class TransactionMessage():
    address: str
    amount: str
    payload: str
