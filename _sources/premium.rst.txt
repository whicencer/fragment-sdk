Telegram Premium
================

Working with Telegram Premium

The ``fragment.premium`` module allows you to buy Premium for any user.

Instant purchase
----------------

Using the ``buy_premium`` method, the SDK will create a transaction to pay for Premium and immediately pay for it from your wallet defined during initialization.

.. code-block:: python

  await fragment.premium.buy_premium(username="whicencer", months=12)

Create a purchase transaction
-----------------------------

.. code-block:: python

  recipient = fragment.premium.search_premium_recipient(recipient_username="whicencer")
  transaction = fragment.premium.create_premium_transaction(
    recipient_id=recipient.data.recipient_id,
    months=12
  )

  return transaction.data

Advanced
--------

.. code-block:: python

  # Search recipient
  recipient = fragment.premium.search_premium_recipient(recipient_username="whicencer")

  # Init gift request
  init_gift = fragment.premium.init_gift_premium_request(
    recipient_id=recipient.data.recipient_id,
    months=12
  )

  # Create transaction
  transaction = fragment.premium.get_gift_premium_link(
    account=wallet.get_wallet_data(),
    req_id=init_gift.data.req_id
  )

  return transaction.data
