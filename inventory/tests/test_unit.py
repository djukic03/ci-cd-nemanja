import pytest
from unittest.mock import MagicMock, patch
from inventory.main import format_product

def test_format_product():
    mock_product = MagicMock()
    mock_product.pk = "test-id-123"
    mock_product.name = "Leskovacki cevap kod komse"
    mock_product.price = 500.0
    mock_product.quantity = 200
    
    with patch('inventory.main.Product.get') as mocked_get:
        mocked_get.return_value = mock_product
        result = format_product("test-id-123")
        assert result == {'id': 'test-id-123', 'name': 'Leskovacki cevap kod komse', 'price': 500.0, 'quantity': 200}
        
        mocked_get.assert_called_once_with("test-id-123")