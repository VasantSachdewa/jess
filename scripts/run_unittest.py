import pytest
import django

django.setup()

retcode = pytest.main(["-m", "not integration_test"])