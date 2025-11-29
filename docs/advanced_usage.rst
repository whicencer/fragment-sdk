Advanced Usage
==============

You can also interact with Fragment using ``FragmentClient`` low-level method ``send_fragment_request``.

Example
-------

.. code-block:: python

  from fragment_sdk.methods import FragmentMethod

  # Init buy stars
  data, error = FragmentClient.send_fragment_request(
    method=FragmentMethod.SEARCH_STARS_RECIPIENT,
    body={ 'query': 'whicencer', 'quantity': 50 }
  )

``data`` — JSON response from Fragment.  

``error`` — String error response from Fragment.

Available methods
-----------------

Methods in ``FragmentMethod`` class.

.. code-block:: python
  
  SEARCH_STARS_RECIPIENT = 'searchStarsRecipient'
  INIT_BUY_STARS = 'initBuyStarsRequest'
  GET_BUY_STARS_LINK = 'getBuyStarsLink'

  SEARCH_PREMIUM_RECIPIENT = 'searchPremiumGiftRecipient'
  INIT_GIFT_PREMIUM = 'initGiftPremiumRequest'
  GET_GIFT_PREMIUM_LINK = 'getGiftPremiumLink'

  SEARCH_ADS_RECIPIENT = 'searchAdsTopupRecipient'
  INIT_ADS_TOPUP = 'initAdsTopupRequest'
  GET_ADS_TOPUP_LINK = 'getAdsTopupLink'

Request body
------------

Each method accepts its own request body.

Stars
~~~~~

**searchStarsRecipient** — ``{ quantity: 50, query: str }``

**initBuyStarsRequest** — ``{ quantity: 50, recipient: str }``

**getBuyStarsLink** — ``{ account: wallet_data_object, id: str, show_sender: int }``

Premium
~~~~~~~

**searchPremiumGiftRecipient** — ``{ months: 12, query: str }``

**initGiftPremiumRequest** — ``{ months: 12, recipient: str }``

**getGiftPremiumLink** — ``{ account: wallet_data_object, id: str, show_sender: int }``

Ads
~~~

**searchAdsTopupRecipient** — ``{ query: str }``

**initAdsTopupRequest** — ``{ amount: 100, recipient: str }``

**getAdsTopupLink** — ``{ account: wallet_data_object, id: str, show_sender: int }``
