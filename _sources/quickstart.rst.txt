Quickstart
===========
How to use Fragment SDK. Creating a simple script to buy Telegram premium.

1. Install Fragment SDK with ``pip3 install fragment-sdk``.
2. Get Tonapi key from https://tonapi.io.
3. Make sure you have TON wallet V5R1 or V4R2.
4. Get a Fragment verificated account auth cookies in Header String format (use `Cookie-Editor <https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm>`_).
5. Use the following code:

.. code-block:: python
  :emphasize-lines: 18
  
  from fragment_sdk import WalletClient
  from fragment_sdk import FragmentClient

  TONAPI_KEY = "<your-tonapi-key>"
  MNEMONIC = "WORD1 WORD2 WORD3 ..."
  WALLET_VERSION = "v4r2"
  FRAGMENT_COOKIES = "<your-fragment-cookies>"

  async def main():
    wallet = WalletClient(
      tonapi_key=TONAPI_KEY,
      mnemonic=MNEMONIC,
      version=WALLET_VERSION # v5r1 by default
    )
    fragment = FragmentClient(cookies=FRAGMENT_COOKIES, wallet=wallet)
    
    response = await fragment.premium.buy_premium(username="whicencer", months=3)
    print(response.data, response.error) # tx_hash string, error string

6. The required amount of TON will be debited from your wallet and Telegram Premium will be sent to the recipient.
