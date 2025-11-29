search_stars_recipient()
========================


``FragmentStarsAPI.search_stars_recipient()``

Search stars recipient.


**Parameters:**  
- **recipient_username** (``str``) — Recipient Telegram username (without @).


**Returns:**  
``ApiResult[SearchRecipientResponseData]``

Example
-------

.. code-block:: python
  
  # Search recipient
  recipient = self.search_stars_recipient(recipient_username="whicencer")
  if recipient.error:
    # Handle error
  
  print(recipient.data)
