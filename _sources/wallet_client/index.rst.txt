WalletClient
============

You have entered the API Reference section where you can find detailed information about Fragment SDK API.

This page is about the ``WalletClient`` class — simple wrapper over the original TON wallet client.

.. code-block:: python
  
  from fragment_sdk import WalletClient

  wallet = WalletClient(
    tonapi_key="<your-tonapi-key>",
    mnemonic="<your-wallet-seed-phrases>",
  )

-------
Details
-------

``class fragment_sdk.WalletClient``

**Parameters:**

- **tonapi_key** (``str``) — Your Tonapi API key you got on `Tonapi.io <https://tonapi.io>`_.
- **mnemonic** (``str``) — Your 24-word wallet seed phrases. Supports only wallets ``V4R2`` and ``V5R1``.
- **version** (``str``) — Wallet version you want to use (only ``V4R2`` and ``V5R1`` – default).

**Fields:**

- **address** (``str``) — User-friendly, non-bouncable wallet address.

Methods
-------

.. toctree::
  :titlesonly:

  get_balance
  get_wallet_data
  process_transaction
