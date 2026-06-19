from private_guard import PrivateGuard, PrivacySettings

def test_private_guard_ad_free():
    settings = PrivacySettings(ad_free=True, tracking_free=True)
    private_guard = PrivateGuard(settings)
    assert private_guard.verify_ad_free() == True

def test_private_guard_tracking_free():
    settings = PrivacySettings(ad_free=True, tracking_free=True)
    private_guard = PrivateGuard(settings)
    assert private_guard.verify_tracking_free() == True

def test_private_guard_run_ad_free():
    settings = PrivacySettings(ad_free=True, tracking_free=True)
    private_guard = PrivateGuard(settings)
    assert private_guard.run() == "Private guard: ad-free and tracking-free functionality verified"

def test_private_guard_run_not_ad_free():
    settings = PrivacySettings(ad_free=False, tracking_free=True)
    private_guard = PrivateGuard(settings)
    assert private_guard.run() == "Private guard: functionality not verified"

def test_private_guard_run_not_tracking_free():
    settings = PrivacySettings(ad_free=True, tracking_free=False)
    private_guard = PrivateGuard(settings)
    assert private_guard.run() == "Private guard: functionality not verified"
