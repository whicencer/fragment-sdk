from fragment_sdk import FragmentClient
from fragment_sdk.wallet import WalletClient

async def main():
  wallet = WalletClient(
    tonapi_key="TONAPI_KEY",
    mnemonic="WORD1 WORD2 WORD3 ...",
    version='v5r1' # v5r1 by default (v4r2 supported)
  )
  fragment = FragmentClient(
    cookies="FRAGMENT_COOKIES_STRING",
    wallet=wallet
  )
  
  response = await fragment.premium.buy_premium(username="whicencer", months=3)
  
  error = response.error
  tx_hash = response.data
  print(tx_hash, error)

# if __name__ == "__main__":
#   import asyncio
#   asyncio.run(main())