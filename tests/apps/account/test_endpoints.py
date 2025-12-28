from appserver.apps.account.endpoints import user_detail
import pytest
from fastapi import HTTPException, status

async def test_user_detail_successfully():
    result = await user_detail("test")
    assert result["id"] == 1
    assert result["username"] == "test"
    assert result["email"] == "test@example.com"
    assert result["display_name"] == "test"
    assert result["is_host"] is True
    assert result["created_at"] is not None
    assert result["updated_at"] is not None
    
async def test_user_detail_not_found():
    with pytest.raises(HTTPException) as exc_info:
        await user_detail("not_found")
    assert exc_info.value.status_code == status.HTTP_404_NOT_FOUND    