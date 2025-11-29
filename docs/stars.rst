Telegram Stars
==============

Working with Telegram Stars

The ``fragment.stars`` module allows you to buy Stars for any user.

There are different ways to interact with Stars using **Fragment SDK**:

- Create and pay transaction in a single method.
- Create a purchase transaction (without paying)
- And one more way if you want to get full control during purchase Stars.

--------------------------
Create and pay transaction
--------------------------

Using the ``buy_stars`` method, the SDK will create a transaction to pay for Stars and immediately pay for it from your wallet defined during initialization.

.. code-block:: python

  await fragment.stars.buy_stars(username="whicencer", quantity=50)   

-----------------------------
Create a purchase transaction
-----------------------------
This way doesn't include paying and consists of two steps:

1. Search recipient
2. Create a transaction

.. code-block:: python

  recipient = fragment.stars.search_stars_recipient(recipient_username="whicencer")
  transaction = fragment.stars.create_stars_transaction(
    recipient_id=recipient.data.recipient_id,
    quantity=50
  )

  return transaction.data

------------
Full control
------------
This way you use if you want to control the full process of purchasing Stars:

1. Initializing a purchase
2. Creating of a transaction

Use this method only if you know you need it.

.. code-block:: python

  # Search recipient
  recipient = fragment.stars.search_stars_recipient(recipient_username="whicencer")

  # Init buy request
  init_buy = fragment.stars.init_buy_stars_request(
    recipient_id=recipient.data.recipient_id,
    quantity=50
  )

  # Create transaction
  transaction = fragment.stars.get_buy_stars_link(
    account=wallet.get_wallet_data(),
    req_id=init_buy.data.req_id
  )

  return transaction.data
