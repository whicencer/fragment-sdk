init_buy_stars()
========================


``FragmentStarsAPI.init_buy_stars()``

Init buy stars request.


**Parameters:**  

- **recipient_id** (``str``) — Stars ``recipient_id`` obtained from :doc:`FragmentStarsAPI.search_stars_recipient() <search_stars_recipient>`.


**Returns:**  

``ApiResult[InitPurchaseResponseData]``

Example
-------

.. code-block:: python
  
  # Init buy stars request
  init_data = self.init_buy_stars_request(
    recipient_id=recipient_id,
    quantity=quantity
  )
  
  if init_data.error:
    # Handle error

  print(init_data.data)
