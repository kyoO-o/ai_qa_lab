# test_email_validation.py
import unittest
from email_valid import is_valid_email  # Функц агуулагдсан файлыг импортлоорой

# =====================
# Positive Test Cases
# =====================
def test_valid_email_normal():
    assert is_valid_email("user@example.com") == True

def test_valid_email_with_subdomain():
    assert is_valid_email("user@mail.example.com") == True

# =====================
# Negative Test Cases
# =====================
def test_missing_at_symbol():
    assert is_valid_email("userexample.com") == False

def test_forbidden_domain():
    assert is_valid_email("user@test.com") == False

# =====================
# Edge Cases
# =====================
def test_empty_string():
    assert is_valid_email("") == False

def test_at_only():
    assert is_valid_email("@") == True

def test_email_ends_with_at_test_com_case_sensitive():
    assert is_valid_email("USER@TEST.COM") == True  # Функц нь case-sensitive

def test_email_with_multiple_at_symbols():
    assert is_valid_email("user@@example.com") == True  # Функц зөвхөн нэг @ байгааг шалгадаггүй

def test_email_with_spaces():
    assert is_valid_email(" user@example.com ") == True  # Функц strip хийхгүй

def test_email_ends_with_similar_domain():
    assert is_valid_email("user@mytest.com") == True  # зөв domain биш тул True
