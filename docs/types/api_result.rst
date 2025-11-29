ApiResult
=========

Basic response for all methods.

.. code-block:: python
  
  class ApiResult(Generic[T]):
    success: bool
    data: Optional[T] = None
    error: Optional[str] = None
    
    @classmethod
    def ok(cls, data: T) -> "ApiResult[T]":
      return cls(success=True, data=data)

    @classmethod
    def fail(cls, error: str) -> "ApiResult[T]":
      return cls(success=False, error=error)

    def __bool__(self) -> bool:
      return self.success
