FragmentClient
==============

This page is about the FragmentClient class, which exposes high-level methods for an easy access to the Fragment API.

.. code-block:: python

  from fragment_sdk import FragmentClient

  fragment = FragmentClient(cookies, wallet)

-------
Details
-------
``class fragment_sdk.FragmentClient``

**Parameters:**

- **cookies** (``str``) — Fragment auth cookies in Header string format (only accounts with KYC).
- **wallet** (``WalletClient``) — Wallet client.

------
Fields
------

- **FragmentClient.stars** — :doc:`FragmentStarsAPI <fragment_stars_api/index>`
- **FragmentClient.premium** — :doc:`FragmentPremiumAPI <fragment_premium_api/index>`

.. toctree::
  :hidden:

  fragment_stars_api/index
  fragment_premium_api/index
