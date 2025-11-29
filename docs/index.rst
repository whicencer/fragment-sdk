.. Fragment SDK documentation master file, created by
   sphinx-quickstart on Wed Nov 19 13:22:49 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Fragment SDK
==========================

**Fragment SDK** makes working with `Fragment <https://fragment.com>`_ effortless.
Handle Telegram Stars, Premium, and TON operations in just a few lines of Python — clean, fast, and fully open-source.

.. code-block:: python
   :emphasize-lines: 17

   import asyncio
   from fragment_sdk import FragmentClient
   from fragment_sdk.wallet import WalletClient

   async def main():
      wallet = WalletClient(
         tonapi_key="TONAPI_KEY",
         mnemonic="WORD1 WORD2 WORD3 ..."
      )
      fragment = FragmentClient(
         cookies="FRAGMENT_COOKIES_STRING",
         wallet=wallet
      )
      
      await fragment.stars.buy_stars(username="whicencer", quantity=50)

   asyncio.run(main())

.. toctree::
   :hidden:

   quickstart

.. toctree::
   :caption: Usage
   :hidden:

   stars
   premium
   advanced_usage

.. toctree::
   :caption: API Reference
   :hidden:

   wallet_client/index
   fragment_client/index
   types/index

.. toctree::
   :caption: Contact
   :hidden:

   Telegram <https://t.me/whicencer>
