class Abstract:
    """Base class for all abstract classes providing an abstract method decorator."""
    
    @staticmethod
    def abstractmethod(method):
        """Decorator to mark a method as abstract."""
        def wrapper(*args, **kwargs):
            # If this method is called, it means it has not been overridden
            raise NotImplementedError(f"The method '{method.__name__}' must be implemented in the subclass.")
        
        wrapper.__name__ = method.__name__  # Preserve the original method name
        wrapper.__doc__ = method.__doc__      # Preserve the original docstring
        return wrapper