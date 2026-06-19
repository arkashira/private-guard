from private_guard import PrivateGuard, PrivacySettings

def test_verify_ad_free() -> None:
    settings = PrivacySettings(ad_free=True, tracking_free=True)
    private_guard = PrivateGuard(settings)
    assert private_guard.verify_ad_free() is True

def test_verify_ad_free_disabled() -> None:
    settings = PrivacySettings(ad_free=False, tracking_free=True)
    private_guard = PrivateGuard(settings)
    assert private_guard.verify_ad_free() is False

def test_verify_tracking_free() -> None:
    settings = PrivacySettings(ad_free=True, tracking_free=True)
    private_guard = PrivateGuard(settings)
    assert private_guard.verify_tracking_free() is True

def test_verify_tracking_free_disabled() -> None:
    settings = PrivacySettings(ad_free=True, tracking_free=False)
    private_guard = PrivateGuard(settings)
    assert private_guard.verify_tracking_free() is False

def test_run_ad_free_enabled() -> None:
    settings = PrivacySettings(ad_free=True, tracking_free=True)
    private_guard = PrivateGuard(settings)
    try:
        private_guard.run()
    except ValueError as e:
        assert False, f"Unexpected error: {e}"

def test_run_ad_free_disabled() -> None:
    settings = PrivacySettings(ad_free=False, tracking_free=True)
    private_guard = PrivateGuard(settings)
    try:
        private_guard.run()
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Ad-free functionality not enabled"

def test_run_tracking_free_enabled() -> None:
    settings = PrivacySettings(ad_free=True, tracking_free=True)
    private_guard = PrivateGuard(settings)
    try:
        private_guard.run()
    except ValueError as e:
        assert False, f"Unexpected error: {e}"

def test_run_tracking_free_disabled() -> None:
    settings = PrivacySettings(ad_free=True, tracking_free=False)
    private_guard = PrivateGuard(settings)
    try:
        private_guard.run()
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Tracking-free functionality not enabled"
